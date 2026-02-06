#!/usr/bin/env python3
"""
Fullstack Mastery - Phase 2: Backend Development
FastAPI, Databases, Auth, API Design
"""

import asyncio
import json
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional, TypeVar, Generic
from enum import Enum
import hashlib
import secrets
import re


# ============== REST API Design ==============

class HTTPStatus(Enum):
    """HTTP Status Codes"""
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_ERROR = 500


@dataclass
class APIResponse:
    """Standard API response format."""
    success: bool
    data: Any = None
    message: str = ""
    errors: List[str] = None
    meta: Dict = None
    
    def to_dict(self) -> Dict:
        return {
            "success": self.success,
            "data": self.data,
            "message": self.message,
            "errors": self.errors or [],
            "meta": self.meta or {}
        }


class RESTResource:
    """Base class for REST resources."""
    
    def __init__(self, name: str):
        self.name = name
        self.routes = []
    
    def index(self) -> APIResponse:
        """GET /resource"""
        raise NotImplementedError
    
    def show(self, id: str) -> APIResponse:
        """GET /resource/:id"""
        raise NotImplementedError
    
    def create(self, data: Dict) -> APIResponse:
        """POST /resource"""
        raise NotImplementedError
    
    def update(self, id: str, data: Dict) -> APIResponse:
        """PUT /resource/:id"""
        raise NotImplementedError
    
    def destroy(self, id: str) -> APIResponse:
        """DELETE /resource/:id"""
        raise NotImplementedError


# ============== FastAPI-Style Framework ==============

class Route:
    def __init__(self, path: str, method: str, handler, middleware=None):
        self.path = path
        self.method = method
        self.handler = handler
        self.middleware = middleware or []


class FastAPIClone:
    """FastAPI-style framework implementation."""
    
    def __init__(self):
        self.routes: List[Route] = []
        self.middlewares: List[callable] = []
        self.exception_handlers: Dict[type, callable] = {}
    
    def get(self, path: str):
        def decorator(func):
            self.routes.append(Route(path, "GET", func))
            return func
        return decorator
    
    def post(self, path: str):
        def decorator(func):
            self.routes.append(Route(path, "POST", func))
            return func
        return decorator
    
    def put(self, path: str):
        def decorator(func):
            self.routes.append(Route(path, "PUT", func))
            return func
        return decorator
    
    def delete(self, path: str):
        def decorator(func):
            self.routes.append(Route(path, "DELETE", func))
            return func
        return decorator
    
    def add_middleware(self, middleware_class):
        self.middlewares.append(middleware_class)
    
    def exception_handler(self, exc_class):
        def decorator(func):
            self.exception_handlers[exc_class] = func
            return func
        return decorator
    
    async def handle_request(self, method: str, path: str, body=None, headers=None):
        """Process incoming request."""
        for route in self.routes:
            if route.method == method and self._match_path(route.path, path):
                try:
                    # Run middleware
                    context = {"headers": headers or {}}
                    for middleware in self.middlewares:
                        context = await middleware.process(context)
                    
                    # Extract path params
                    params = self._extract_params(route.path, path)
                    
                    # Call handler
                    if body:
                        result = await route.handler(body, **params)
                    else:
                        result = await route.handler(**params)
                    
                    return result
                    
                except Exception as e:
                    handler = self.exception_handlers.get(type(e))
                    if handler:
                        return handler(e)
                    raise
        
        return APIResponse(False, None, "Not found", [], {"status": 404})
    
    def _match_path(self, route_path: str, request_path: str) -> bool:
        """Check if route matches request path."""
        route_parts = route_path.split('/')
        request_parts = request_path.split('/')
        
        if len(route_parts) != len(request_parts):
            return False
        
        for route_part, request_part in zip(route_parts, request_parts):
            if route_part.startswith('{') and route_part.endswith('}'):
                continue  # Path parameter
            if route_part != request_part:
                return False
        
        return True
    
    def _extract_params(self, route_path: str, request_path: str) -> Dict:
        """Extract path parameters."""
        params = {}
        route_parts = route_path.split('/')
        request_parts = request_path.split('/')
        
        for route_part, request_part in zip(route_parts, request_parts):
            if route_part.startswith('{') and route_part.endswith('}'):
                param_name = route_part[1:-1]
                params[param_name] = request_part
        
        return params


# ============== Application Instance ==============

app = FastAPIClone()

# Mock database
db = {
    "tasks": {},
    "users": {},
    "sessions": {}
}


# ============== API Endpoints ==============

@app.get("/health")
async def health_check():
    return APIResponse(True, {
        "status": "healthy",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat()
    })


@app.get("/tasks")
async def list_tasks():
    """List all tasks with pagination support."""
    tasks = list(db["tasks"].values())
    return APIResponse(True, tasks, meta={"count": len(tasks)})


@app.post("/tasks")
async def create_task(body: Dict):
    """Create new task with validation."""
    # Validation
    required = ['name']
    missing = [f for f in required if f not in body]
    if missing:
        return APIResponse(False, None, "Validation failed", 
                         [f"Missing field: {f}" for f in missing])
    
    task_id = secrets.token_hex(8)
    task = {
        "id": task_id,
        "name": body["name"],
        "description": body.get("description", ""),
        "status": body.get("status", "todo"),
        "priority": body.get("priority", "medium"),
        "created_at": datetime.now().isoformat(),
        "updated_at": None
    }
    
    db["tasks"][task_id] = task
    return APIResponse(True, task, "Task created", meta={"status": 201})


@app.get("/tasks/{task_id}")
async def get_task(task_id: str):
    """Get task by ID."""
    task = db["tasks"].get(task_id)
    if not task:
        return APIResponse(False, None, "Task not found", [], {"status": 404})
    return APIResponse(True, task)


@app.put("/tasks/{task_id}")
async def update_task(body: Dict, task_id: str):
    """Update task."""
    if task_id not in db["tasks"]:
        return APIResponse(False, None, "Task not found", [], {"status": 404})
    
    task = db["tasks"][task_id]
    allowed_fields = ['name', 'description', 'status', 'priority']
    
    for field in allowed_fields:
        if field in body:
            task[field] = body[field]
    
    task["updated_at"] = datetime.now().isoformat()
    return APIResponse(True, task, "Task updated")


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    """Delete task."""
    if task_id not in db["tasks"]:
        return APIResponse(False, None, "Task not found", [], {"status": 404})
    
    del db["tasks"][task_id]
    return APIResponse(True, None, "Task deleted", meta={"status": 204})


# ============== Authentication & Authorization ==============

class AuthManager:
    """JWT-style authentication manager."""
    
    def __init__(self, secret: str):
        self.secret = secret
        self.users = db["users"]
        self.sessions = db["sessions"]
    
    def hash_password(self, password: str) -> str:
        """Hash password with salt."""
        salt = secrets.token_hex(16)
        pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode(), 
                                       salt.encode(), 100000)
        return salt + pwdhash.hex()
    
    def verify_password(self, password: str, hashed: str) -> bool:
        """Verify password against hash."""
        salt = hashed[:32]
        stored_hash = hashed[32:]
        pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode(),
                                       salt.encode(), 100000)
        return pwdhash.hex() == stored_hash
    
    def generate_token(self, user_id: str) -> str:
        """Generate simple token (simplified JWT)."""
        header = json.dumps({"alg": "HS256", "typ": "JWT"})
        payload = json.dumps({
            "sub": user_id,
            "iat": datetime.now().timestamp(),
            "exp": (datetime.now() + timedelta(hours=24)).timestamp()
        })
        
        token = f"{self._b64encode(header)}.{self._b64encode(payload)}"
        signature = hashlib.sha256(f"{token}.{self.secret}".encode()).hexdigest()
        
        full_token = f"{token}.{signature}"
        self.sessions[full_token] = {"user_id": user_id, "created": datetime.now()}
        return full_token
    
    def verify_token(self, token: str) -> Optional[Dict]:
        """Verify and decode token."""
        if token not in self.sessions:
            return None
        
        session = self.sessions[token]
        # Check expiration
        if datetime.now() - session["created"] > timedelta(hours=24):
            del self.sessions[token]
            return None
        
        return session
    
    def _b64encode(self, data: str) -> str:
        import base64
        return base64.urlsafe_b64encode(data.encode()).decode().rstrip('=')


# ============== Database Design ==============

class DatabaseSchema:
    """Database schema design examples."""
    
    # SQL Schema
    SQL_SCHEMA = """
    -- Users table
    CREATE TABLE users (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        email VARCHAR(255) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL,
        name VARCHAR(100) NOT NULL,
        role VARCHAR(20) DEFAULT 'user',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    -- Tasks table
    CREATE TABLE tasks (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        user_id UUID REFERENCES users(id) ON DELETE CASCADE,
        name VARCHAR(200) NOT NULL,
        description TEXT,
        status VARCHAR(20) DEFAULT 'todo',
        priority VARCHAR(20) DEFAULT 'medium',
        due_date TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    -- Indexes for performance
    CREATE INDEX idx_tasks_user_id ON tasks(user_id);
    CREATE INDEX idx_tasks_status ON tasks(status);
    CREATE INDEX idx_tasks_due_date ON tasks(due_date);
    
    -- Full-text search
    CREATE INDEX idx_tasks_search ON tasks USING gin(to_tsvector('english', name || ' ' || COALESCE(description, '')));
    """
    
    # MongoDB Schema (NoSQL)
    MONGODB_SCHEMA = {
        "users": {
            "_id": "ObjectId",
            "email": "string (unique)",
            "password_hash": "string",
            "profile": {
                "name": "string",
                "avatar": "string"
            },
            "preferences": {
                "theme": "string",
                "notifications": "boolean"
            },
            "created_at": "ISODate"
        },
        "tasks": {
            "_id": "ObjectId",
            "user_id": "ObjectId (ref)",
            "name": "string",
            "description": "string",
            "status": "string (enum)",
            "priority": "string (enum)",
            "tags": ["string"],
            "metadata": {
                "source": "string",
                "client": "string"
            },
            "due_date": "ISODate",
            "created_at": "ISODate"
        }
    }


# ============== GraphQL Concepts ==============

GRAPHQL_SCHEMA = """
type Task {
    id: ID!
    name: String!
    description: String
    status: TaskStatus!
    priority: Priority!
    assignee: User
    dueDate: String
    createdAt: String!
}

type User {
    id: ID!
    email: String!
    name: String!
    tasks(status: TaskStatus): [Task!]!
}

enum TaskStatus {
    TODO
    DOING
    DONE
}

enum Priority {
    LOW
    MEDIUM
    HIGH
}

type Query {
    tasks(
        status: TaskStatus
        priority: Priority
        limit: Int = 20
        offset: Int = 0
    ): [Task!]!
    
    task(id: ID!): Task
    
    me: User
}

type Mutation {
    createTask(
        name: String!
        description: String
        priority: Priority = MEDIUM
        dueDate: String
    ): Task!
    
    updateTask(
        id: ID!
        name: String
        description: String
        status: TaskStatus
        priority: Priority
    ): Task!
    
    deleteTask(id: ID!): Boolean!
}

type Subscription {
    taskCreated: Task!
    taskUpdated(id: ID!): Task!
}
"""


# ============== WebSocket Concepts ==============

class WebSocketManager:
    """WebSocket connection manager for real-time features."""
    
    def __init__(self):
        self.connections: Dict[str, Any] = {}
        self.rooms: Dict[str, set] = {}
    
    async def connect(self, client_id: str, websocket):
        """Handle new connection."""
        self.connections[client_id] = websocket
        print(f"Client {client_id} connected")
    
    async def disconnect(self, client_id: str):
        """Handle disconnection."""
        if client_id in self.connections:
            del self.connections[client_id]
        
        # Remove from all rooms
        for room in self.rooms.values():
            room.discard(client_id)
        
        print(f"Client {client_id} disconnected")
    
    async def join_room(self, client_id: str, room: str):
        """Add client to room."""
        if room not in self.rooms:
            self.rooms[room] = set()
        self.rooms[room].add(client_id)
    
    async def leave_room(self, client_id: str, room: str):
        """Remove client from room."""
        if room in self.rooms:
            self.rooms[room].discard(client_id)
    
    async def broadcast(self, message: Dict, room: str = None):
        """Broadcast message to clients."""
        if room:
            targets = self.rooms.get(room, set())
        else:
            targets = set(self.connections.keys())
        
        for client_id in targets:
            if client_id in self.connections:
                # Would send via websocket
                print(f"Sending to {client_id}: {message}")


# ============== API Versioning ==============

class APIVersioning:
    """API versioning strategies."""
    
    # Strategy 1: URL Path
    # /api/v1/tasks
    # /api/v2/tasks
    
    # Strategy 2: Header
    # Accept: application/vnd.api+json;version=2
    
    # Strategy 3: Query Parameter
    # /api/tasks?version=2
    
    VERSIONS = {
        "v1": {
            "endpoints": ["/tasks", "/users"],
            "deprecated": True,
            "sunset_date": "2026-12-31"
        },
        "v2": {
            "endpoints": ["/tasks", "/users", "/projects"],
            "deprecated": False
        }
    }


# ============== Rate Limiting ==============

class RateLimiter:
    """Token bucket rate limiter."""
    
    def __init__(self, rate: int = 100, per: int = 60):
        self.rate = rate  # requests per window
        self.per = per    # window in seconds
        self.buckets: Dict[str, Dict] = {}
    
    def is_allowed(self, key: str) -> bool:
        """Check if request is allowed."""
        now = datetime.now()
        
        if key not in self.buckets:
            self.buckets[key] = {
                "tokens": self.rate,
                "last_update": now
            }
        
        bucket = self.buckets[key]
        
        # Add tokens based on time passed
        time_passed = (now - bucket["last_update"]).total_seconds()
        tokens_to_add = time_passed * (self.rate / self.per)
        bucket["tokens"] = min(self.rate, bucket["tokens"] + tokens_to_add)
        bucket["last_update"] = now
        
        # Check and consume token
        if bucket["tokens"] >= 1:
            bucket["tokens"] -= 1
            return True
        
        return False
    
    def get_retry_after(self, key: str) -> int:
        """Get seconds until next request allowed."""
        if key not in self.buckets:
            return 0
        
        bucket = self.buckets[key]
        if bucket["tokens"] >= 1:
            return 0
        
        # Time to generate 1 token
        return int(self.per / self.rate)


# ============== Main ==============

async def main():
    """Demonstrate Phase 2 backend concepts."""
    print("=" * 70)
    print("FULLSTACK MASTERY - PHASE 2: BACKEND DEVELOPMENT")
    print("=" * 70)
    
    # 1. API Design
    print("\n1. REST API DESIGN")
    print("-" * 40)
    
    # Test endpoints
    print("   Testing API endpoints:")
    
    # Create task
    response = await app.handle_request("POST", "/tasks", 
                                       {"name": "DTI Registration", "priority": "high"})
    print(f"   POST /tasks → success={response.success}")
    task_id = response.data["id"] if response.data else None
    
    # Get task
    if task_id:
        response = await app.handle_request("GET", f"/tasks/{task_id}")
        print(f"   GET /tasks/{task_id[:8]}... → success={response.success}")
    
    # List tasks
    response = await app.handle_request("GET", "/tasks")
    print(f"   GET /tasks → count={response.meta.get('count', 0)}")
    
    # 2. Authentication
    print("\n2. AUTHENTICATION & AUTHORIZATION")
    print("-" * 40)
    
    auth = AuthManager(secret="scaleplus-secret-key")
    
    # Hash password
    password_hash = auth.hash_password("papi-secure-password")
    print(f"   Password hashed: {password_hash[:20]}...")
    
    # Verify password
    is_valid = auth.verify_password("papi-secure-password", password_hash)
    print(f"   Password valid: {is_valid}")
    
    # Generate token
    token = auth.generate_token("user_123")
    print(f"   Token generated: {token[:40]}...")
    
    # Verify token
    session = auth.verify_token(token)
    print(f"   Token valid: {session is not None}")
    
    # 3. Database Design
    print("\n3. DATABASE DESIGN")
    print("-" * 40)
    print("   SQL Schema includes:")
    print("     • Users table with UUID primary keys")
    print("     • Tasks table with foreign key relationships")
    print("     • Indexes for query performance")
    print("     • Full-text search with GIN index")
    print("   MongoDB Schema includes:")
    print("     • Embedded documents for preferences")
    print("     • Arrays for tags")
    print("     • Flexible metadata field")
    
    # 4. GraphQL
    print("\n4. GRAPHQL API DESIGN")
    print("-" * 40)
    print("   Schema includes:")
    print("     • Types: Task, User with relationships")
    print("     • Enums: TaskStatus, Priority")
    print("     • Queries: tasks, task, me")
    print("     • Mutations: createTask, updateTask, deleteTask")
    print("     • Subscriptions: taskCreated, taskUpdated")
    
    # 5. WebSockets
    print("\n5. WEBSOCKET REAL-TIME")
    print("-" * 40)
    
    ws_manager = WebSocketManager()
    await ws_manager.connect("client_1", None)
    await ws_manager.join_room("client_1", "tasks")
    await ws_manager.broadcast({"type": "task_created", "data": {}}, room="tasks")
    await ws_manager.disconnect("client_1")
    
    print("   WebSocket manager features:")
    print("     • Connection management")
    print("     • Room-based messaging")
    print("     • Broadcast capabilities")
    
    # 6. Rate Limiting
    print("\n6. RATE LIMITING (Token Bucket)")
    print("-" * 40)
    
    limiter = RateLimiter(rate=5, per=60)  # 5 requests per minute
    
    for i in range(7):
        allowed = limiter.is_allowed("user_123")
        status = "ALLOWED" if allowed else "BLOCKED"
        print(f"   Request {i+1}: {status}")
    
    retry_after = limiter.get_retry_after("user_123")
    print(f"   Retry after: {retry_after}s")
    
    print("\n" + "=" * 70)
    print("PHASE 2 CONCEPTS DEMONSTRATED:")
    print("=" * 70)
    concepts = [
        "REST API Design (RESTful principles)",
        "FastAPI-style framework from scratch",
        "CRUD operations with validation",
        "Standard API response format",
        "JWT Authentication",
        "Password hashing (PBKDF2)",
        "SQL Database Design",
        "NoSQL (MongoDB) Schema Design",
        "Indexing strategies",
        "GraphQL Schema Design",
        "WebSocket Real-time Communication",
        "Room-based messaging",
        "API Versioning strategies",
        "Token Bucket Rate Limiting"
    ]
    for i, concept in enumerate(concepts, 1):
        print(f"  {i:2}. {concept}")
    
    print("\n" + "=" * 70)
    print("PHASE 2 COMPLETE")
    print("=" * 70)
    print("\nReady for Phase 3: DevOps & System Design")


if __name__ == "__main__":
    asyncio.run(main())
