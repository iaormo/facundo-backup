#!/usr/bin/env python3
"""
Phase 4: Production Systems
FastAPI, Databases, Docker, Deployment
"""

import asyncio
import json
import sqlite3
from abc import ABC, abstractmethod
from collections import defaultdict
from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum
from typing import List, Dict, Any, Optional, TypeVar, Generic
from contextlib import asynccontextmanager
import urllib.request
import urllib.error


# ============== FastAPI-style Web Framework (from scratch) ==============

class HTTPMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


@dataclass
class Request:
    """HTTP Request object."""
    method: str
    path: str
    headers: Dict[str, str]
    body: Optional[str] = None
    query_params: Dict[str, str] = None
    path_params: Dict[str, str] = None


@dataclass
class Response:
    """HTTP Response object."""
    status_code: int
    body: Any
    headers: Dict[str, str] = None
    
    def __post_init__(self):
        if self.headers is None:
            self.headers = {"Content-Type": "application/json"}


class Route:
    """Route handler registration."""
    
    def __init__(self, path: str, method: str, handler):
        self.path = path
        self.method = method
        self.handler = handler
        self.param_names = self._extract_params(path)
    
    def _extract_params(self, path: str) -> List[str]:
        """Extract {param} from path."""
        import re
        return re.findall(r'{(\w+)}', path)
    
    def match(self, path: str, method: str) -> Optional[Dict[str, str]]:
        """Check if route matches path, return path params if so."""
        if method != self.method:
            return None
        
        # Convert route pattern to regex
        pattern = self.path
        for param in self.param_names:
            pattern = pattern.replace(f"{{{param}}}", f"(?P<{param}>[^/]+)")
        pattern = f"^{pattern}$"
        
        import re
        match = re.match(pattern, path)
        if match:
            return match.groupdict()
        return None


class FastAPIClone:
    """Minimal FastAPI-style framework."""
    
    def __init__(self):
        self.routes: List[Route] = []
        self.middlewares: List[callable] = []
    
    def get(self, path: str):
        """Decorator for GET routes."""
        def decorator(handler):
            self.routes.append(Route(path, "GET", handler))
            return handler
        return decorator
    
    def post(self, path: str):
        """Decorator for POST routes."""
        def decorator(handler):
            self.routes.append(Route(path, "POST", handler))
            return handler
        return decorator
    
    def put(self, path: str):
        """Decorator for PUT routes."""
        def decorator(handler):
            self.routes.append(Route(path, "PUT", handler))
            return handler
        return decorator
    
    def delete(self, path: str):
        """Decorator for DELETE routes."""
        def decorator(handler):
            self.routes.append(Route(path, "DELETE", handler))
            return handler
        return decorator
    
    async def handle(self, request: Request) -> Response:
        """Handle incoming request."""
        # Find matching route
        for route in self.routes:
            path_params = route.match(request.path, request.method)
            if path_params is not None:
                request.path_params = path_params
                try:
                    result = await route.handler(request)
                    if isinstance(result, Response):
                        return result
                    return Response(200, result)
                except Exception as e:
                    return Response(500, {"error": str(e)})
        
        return Response(404, {"error": "Not found"})


# ============== Application Instance ==============

app = FastAPIClone()

# Sample data store
tasks_db: Dict[str, Dict] = {}


# ============== API Endpoints ==============

@app.get("/health")
async def health_check(request: Request):
    """Health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }


@app.get("/tasks")
async def list_tasks(request: Request):
    """List all tasks."""
    return {
        "tasks": list(tasks_db.values()),
        "count": len(tasks_db)
    }


@app.post("/tasks")
async def create_task(request: Request):
    """Create new task."""
    if not request.body:
        return Response(400, {"error": "Body required"})
    
    try:
        data = json.loads(request.body)
        task_id = f"task_{len(tasks_db) + 1}"
        task = {
            "id": task_id,
            "name": data.get("name"),
            "status": data.get("status", "todo"),
            "priority": data.get("priority", "medium"),
            "created_at": datetime.now().isoformat()
        }
        tasks_db[task_id] = task
        return Response(201, task)
    except json.JSONDecodeError:
        return Response(400, {"error": "Invalid JSON"})


@app.get("/tasks/{task_id}")
async def get_task(request: Request):
    """Get task by ID."""
    task_id = request.path_params.get("task_id")
    task = tasks_db.get(task_id)
    if task:
        return task
    return Response(404, {"error": "Task not found"})


@app.put("/tasks/{task_id}")
async def update_task(request: Request):
    """Update task."""
    task_id = request.path_params.get("task_id")
    if task_id not in tasks_db:
        return Response(404, {"error": "Task not found"})
    
    try:
        data = json.loads(request.body) if request.body else {}
        tasks_db[task_id].update(data)
        tasks_db[task_id]["updated_at"] = datetime.now().isoformat()
        return tasks_db[task_id]
    except json.JSONDecodeError:
        return Response(400, {"error": "Invalid JSON"})


@app.delete("/tasks/{task_id}")
async def delete_task(request: Request):
    """Delete task."""
    task_id = request.path_params.get("task_id")
    if task_id in tasks_db:
        del tasks_db[task_id]
        return Response(204, None)
    return Response(404, {"error": "Task not found"})


# ============== Database Layer ==============

class Database(ABC):
    """Abstract database interface."""
    
    @abstractmethod
    async def connect(self): ...
    
    @abstractmethod
    async def execute(self, query: str, params: tuple = None): ...
    
    @abstractmethod
    async def fetch(self, query: str, params: tuple = None) -> List[Dict]: ...


class SQLiteDatabase(Database):
    """SQLite implementation."""
    
    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self.connection = None
    
    async def connect(self):
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row
    
    async def execute(self, query: str, params: tuple = None):
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.connection.commit()
        return cursor.lastrowid
    
    async def fetch(self, query: str, params: tuple = None) -> List[Dict]:
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    
    async def close(self):
        if self.connection:
            self.connection.close()


class ConnectionPool:
    """Database connection pool."""
    
    def __init__(self, db_class, max_connections: int = 10):
        self.db_class = db_class
        self.max_connections = max_connections
        self.pool: asyncio.Queue = asyncio.Queue(maxsize=max_connections)
        self._initialized = False
    
    async def initialize(self):
        """Initialize pool with connections."""
        for _ in range(self.max_connections):
            db = self.db_class()
            await db.connect()
            await self.pool.put(db)
        self._initialized = True
    
    @asynccontextmanager
    async def acquire(self):
        """Acquire connection from pool."""
        db = await self.pool.get()
        try:
            yield db
        finally:
            await self.pool.put(db)


# ============== Caching ==============

class Cache(ABC):
    """Abstract cache interface."""
    
    @abstractmethod
    async def get(self, key: str) -> Optional[Any]: ...
    
    @abstractmethod
    async def set(self, key: str, value: Any, ttl: int = 3600): ...
    
    @abstractmethod
    async def delete(self, key: str): ...


class InMemoryCache(Cache):
    """In-memory cache with TTL."""
    
    def __init__(self):
        self._data: Dict[str, Any] = {}
        self._expires: Dict[str, datetime] = {}
    
    async def get(self, key: str) -> Optional[Any]:
        if key in self._expires:
            if datetime.now() > self._expires[key]:
                del self._data[key]
                del self._expires[key]
                return None
        return self._data.get(key)
    
    async def set(self, key: str, value: Any, ttl: int = 3600):
        self._data[key] = value
        self._expires[key] = datetime.now() + __import__('datetime').timedelta(seconds=ttl)
    
    async def delete(self, key: str):
        self._data.pop(key, None)
        self._expires.pop(key, None)


# ============== Authentication ==============

class Authenticator(ABC):
    """Abstract authentication."""
    
    @abstractmethod
    async def authenticate(self, token: str) -> Optional[Dict]: ...


class JWTAuthenticator(Authenticator):
    """JWT token authentication (simplified)."""
    
    def __init__(self, secret: str):
        self.secret = secret
        self._tokens: Dict[str, Dict] = {}
    
    def generate_token(self, user_id: str, data: Dict) -> str:
        """Generate simple token."""
        import hashlib
        token = hashlib.sha256(f"{user_id}:{self.secret}:{datetime.now()}".encode()).hexdigest()
        self._tokens[token] = {"user_id": user_id, **data}
        return token
    
    async def authenticate(self, token: str) -> Optional[Dict]:
        return self._tokens.get(token)


# ============== Rate Limiting ==============

class RateLimiter:
    """Simple rate limiter."""
    
    def __init__(self, max_requests: int = 100, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window = window_seconds
        self._requests: Dict[str, List[datetime]] = {}
    
    async def is_allowed(self, key: str) -> bool:
        """Check if request is allowed."""
        now = datetime.now()
        window_start = now - __import__('datetime').timedelta(seconds=self.window)
        
        # Clean old requests
        if key in self._requests:
            self._requests[key] = [t for t in self._requests[key] if t > window_start]
        else:
            self._requests[key] = []
        
        # Check limit
        if len(self._requests[key]) >= self.max_requests:
            return False
        
        # Record request
        self._requests[key].append(now)
        return True


# ============== Background Tasks ==============

class TaskQueue:
    """Async task queue."""
    
    def __init__(self):
        self._queue: asyncio.Queue = asyncio.Queue()
        self._workers: List[asyncio.Task] = []
        self._running = False
    
    async def start(self, num_workers: int = 3):
        """Start worker tasks."""
        self._running = True
        for i in range(num_workers):
            worker = asyncio.create_task(self._worker(f"worker-{i}"))
            self._workers.append(worker)
    
    async def stop(self):
        """Stop all workers."""
        self._running = False
        for worker in self._workers:
            worker.cancel()
        await asyncio.gather(*self._workers, return_exceptions=True)
    
    async def _worker(self, name: str):
        """Worker coroutine."""
        while self._running:
            try:
                task = await asyncio.wait_for(self._queue.get(), timeout=1.0)
                await self._process_task(task)
                self._queue.task_done()
            except asyncio.TimeoutError:
                continue
            except Exception as e:
                print(f"Worker {name} error: {e}")
    
    async def _process_task(self, task: Dict):
        """Process a task."""
        task_type = task.get("type")
        if task_type == "send_notification":
            print(f"  [Worker] Sending notification: {task.get('message')}")
        elif task_type == "sync_notion":
            print(f"  [Worker] Syncing with Notion")
        await asyncio.sleep(0.1)  # Simulate work
    
    async def add_task(self, task: Dict):
        """Add task to queue."""
        await self._queue.put(task)


# ============== Docker Concepts ==============

DOCKERFILE_EXAMPLE = """
# Multi-stage build for production
FROM python:3.11-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.11-slim

WORKDIR /app

# Copy only necessary artifacts
COPY --from=builder /root/.local /root/.local
COPY ./app ./app

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
"""

DOCKER_COMPOSE = """
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/app
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis
    
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=app
    volumes:
      - postgres_data:/var/lib/postgresql/data
    
  redis:
    image: redis:7-alpine
    
  worker:
    build: .
    command: celery -A app.tasks worker --loglevel=info
    depends_on:
      - redis
      - db

volumes:
  postgres_data:
"""

# ============== Monitoring ==============

class MetricsCollector:
    """Collect application metrics."""
    
    def __init__(self):
        self._counters: Dict[str, int] = defaultdict(int)
        self._gauges: Dict[str, float] = {}
        self._histograms: Dict[str, List[float]] = defaultdict(list)
    
    def increment(self, name: str, value: int = 1):
        """Increment counter."""
        self._counters[name] += value
    
    def gauge(self, name: str, value: float):
        """Set gauge value."""
        self._gauges[name] = value
    
    def histogram(self, name: str, value: float):
        """Record histogram value."""
        self._histograms[name].append(value)
    
    def get_metrics(self) -> Dict:
        """Get all metrics."""
        return {
            "counters": dict(self._counters),
            "gauges": self._gauges,
            "histograms": {k: {"count": len(v), "avg": sum(v)/len(v) if v else 0} 
                          for k, v in self._histograms.items()}
        }


# ============== Main ==============

async def main():
    """Demonstrate Phase 4 production concepts."""
    print("=" * 70)
    print("PHASE 4: PRODUCTION SYSTEMS")
    print("=" * 70)
    
    # 1. Web Framework
    print("\n1. FASTAPI-STYLE WEB FRAMEWORK")
    print("-" * 40)
    
    # Test API endpoints
    print("   Testing API endpoints:")
    
    # Health check
    req = Request("GET", "/health", {})
    resp = await app.handle(req)
    print(f"   GET /health → {resp.status_code}: {resp.body}")
    
    # Create task
    req = Request("POST", "/tasks", {}, 
                  body=json.dumps({"name": "DTI Registration", "priority": "high"}))
    resp = await app.handle(req)
    print(f"   POST /tasks → {resp.status_code}: {resp.body}")
    
    # Get task
    req = Request("GET", "/tasks/task_1", {})
    resp = await app.handle(req)
    print(f"   GET /tasks/task_1 → {resp.status_code}: {resp.body}")
    
    # 2. Database Layer
    print("\n2. DATABASE LAYER (SQLite)")
    print("-" * 40)
    
    db = SQLiteDatabase()
    await db.connect()
    
    # Create table
    await db.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            status TEXT DEFAULT 'todo',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Insert
    task_id = await db.execute(
        "INSERT INTO tasks (name, status) VALUES (?, ?)",
        ("ScalePlus Website", "doing")
    )
    print(f"   Inserted task with ID: {task_id}")
    
    # Query
    tasks = await db.fetch("SELECT * FROM tasks")
    print(f"   Tasks in database: {len(tasks)}")
    
    await db.close()
    
    # 3. Connection Pool
    print("\n3. CONNECTION POOLING")
    print("-" * 40)
    
    pool = ConnectionPool(SQLiteDatabase, max_connections=3)
    await pool.initialize()
    
    async with pool.acquire() as conn:
        await conn.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER)")
        print("   Acquired connection from pool")
    
    print("   Connection returned to pool")
    
    # 4. Caching
    print("\n4. CACHING LAYER")
    print("-" * 40)
    
    cache = InMemoryCache()
    await cache.set("task:1", {"name": "DTI Registration"}, ttl=60)
    cached = await cache.get("task:1")
    print(f"   Cached task: {cached}")
    
    # 5. Authentication
    print("\n5. JWT AUTHENTICATION")
    print("-" * 40)
    
    auth = JWTAuthenticator(secret="papi-secret-key")
    token = auth.generate_token("user_123", {"role": "admin", "name": "papi"})
    print(f"   Generated token: {token[:20]}...")
    
    user = await auth.authenticate(token)
    print(f"   Authenticated user: {user}")
    
    # 6. Rate Limiting
    print("\n6. RATE LIMITING")
    print("-" * 40)
    
    limiter = RateLimiter(max_requests=3, window_seconds=60)
    
    for i in range(5):
        allowed = await limiter.is_allowed("user_123")
        print(f"   Request {i+1}: {'ALLOWED' if allowed else 'BLOCKED'}")
    
    # 7. Background Tasks
    print("\n7. BACKGROUND TASK QUEUE")
    print("-" * 40)
    
    queue = TaskQueue()
    await queue.start(num_workers=2)
    
    await queue.add_task({"type": "send_notification", "message": "Task created"})
    await queue.add_task({"type": "sync_notion"})
    await queue.add_task({"type": "send_notification", "message": "Reminder"})
    
    await asyncio.sleep(0.5)  # Let workers process
    await queue.stop()
    
    print("   Tasks processed by workers")
    
    # 8. Docker
    print("\n8. DOCKER CONFIGURATION")
    print("-" * 40)
    print("   Dockerfile (multi-stage build):")
    print("   " + DOCKERFILE_EXAMPLE[:200] + "...")
    
    # 9. Monitoring
    print("\n9. METRICS COLLECTION")
    print("-" * 40)
    
    metrics = MetricsCollector()
    metrics.increment("tasks_created", 5)
    metrics.increment("api_requests", 100)
    metrics.gauge("active_users", 10)
    metrics.histogram("response_time", 0.045)
    metrics.histogram("response_time", 0.123)
    metrics.histogram("response_time", 0.089)
    
    all_metrics = metrics.get_metrics()
    print(f"   Counters: {all_metrics['counters']}")
    print(f"   Gauges: {all_metrics['gauges']}")
    print(f"   Response time avg: {all_metrics['histograms']['response_time']['avg']:.3f}s")
    
    print("\n" + "=" * 70)
    print("PHASE 4 CONCEPTS DEMONSTRATED:")
    print("=" * 70)
    concepts = [
        "FastAPI-style Web Framework (from scratch)",
        "REST API Design (GET/POST/PUT/DELETE)",
        "Path Parameters & Request Handling",
        "Database Layer (SQLite)",
        "Connection Pooling",
        "In-Memory Caching with TTL",
        "JWT Authentication",
        "Rate Limiting",
        "Background Task Queue",
        "Async Workers",
        "Dockerfile (Multi-stage)",
        "Docker Compose",
        "Metrics Collection",
        "Production Patterns"
    ]
    for i, concept in enumerate(concepts, 1):
        print(f"  {i:2}. {concept}")
    
    print("\n" + "=" * 70)
    print("PHASE 4 COMPLETE")
    print("=" * 70)
    print("\nNext: Phase 5 - Specialized AI (NLP, Computer Vision, RAG)")


if __name__ == "__main__":
    asyncio.run(main())
