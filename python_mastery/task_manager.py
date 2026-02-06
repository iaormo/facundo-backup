#!/usr/bin/env python3
"""
Task Manager Automation for Papi - Pure Python
Demonstrates advanced patterns without external dependencies
"""

import asyncio
import json
from dataclasses import dataclass, asdict, field
from datetime import datetime, timedelta
from enum import Enum, auto
from typing import Optional, TypeVar, Generic, List, Dict, Any, Protocol, Callable
from functools import wraps
import urllib.request
import urllib.error


# ============== Type Definitions ==============

class Priority(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class Status(Enum):
    TODO = "to_do"
    DOING = "doing"
    DONE = "done"


@dataclass(frozen=True)
class Task:
    """Immutable task entity with full type safety."""
    id: str
    name: str
    priority: Priority
    status: Status
    due_date: Optional[datetime] = None
    project: Optional[str] = None
    labels: List[str] = field(default_factory=list)
    
    def to_notion_properties(self) -> Dict[str, Any]:
        """Convert to Notion API format."""
        properties = {
            "Name": {"title": [{"text": {"content": self.name}}]},
            "Status": {"status": {"name": self.status.value.replace('_', ' ').title()}},
            "Priority": {"status": {"name": self.priority.value.capitalize()}}
        }
        if self.due_date:
            properties["Due"] = {"date": {"start": self.due_date.isoformat()}}
        if self.labels:
            properties["Labels"] = {"multi_select": [{"name": label} for label in self.labels]}
        return properties


# ============== Protocol / Interface ==============

class TaskRepository(Protocol):
    """Interface for task storage - Protocol for structural subtyping."""
    async def create(self, task: Task) -> Task: ...
    async def get(self, task_id: str) -> Optional[Task]: ...
    async def update(self, task: Task) -> Task: ...
    async def list_by_project(self, project: str) -> List[Task]: ...


# ============== Metaclass Example ==============

class SingletonMeta(type):
    """Metaclass implementing Singleton pattern."""
    _instances: Dict[type, Any] = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class TaskCounter(metaclass=SingletonMeta):
    """Singleton counter for tasks."""
    def __init__(self):
        self.count = 0
    
    def increment(self) -> int:
        self.count += 1
        return self.count


# ============== Descriptor Example ==============

class ValidatedField:
    """Descriptor for field validation."""
    def __init__(self, min_value: int = 0, max_value: int = 100):
        self.min = min_value
        self.max = max_value
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        if not (self.min <= value <= self.max):
            raise ValueError(f"{self.name} must be between {self.min} and {self.max}")
        instance.__dict__[self.name] = value


class ProjectProgress:
    """Uses descriptor for validation."""
    percentage = ValidatedField(0, 100)
    
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.percentage = 0  # Validated


# ============== Async HTTP Client ==============

class NotionAPIError(Exception):
    """Custom exception with error details."""
    def __init__(self, message: str, status_code: int = None):
        super().__init__(message)
        self.status_code = status_code


class NotionTaskRepository:
    """Production-ready Notion API client with async support."""
    
    def __init__(self, token: str, database_id: str):
        self.token = token
        self.database_id = database_id
        self.base_url = "https://api.notion.com/v1"
        self._counter = TaskCounter()
    
    async def _request(self, method: str, endpoint: str, data: Dict = None) -> Dict[str, Any]:
        """Make async request using threads (since urllib is sync)."""
        url = f"{self.base_url}/{endpoint}"
        
        def make_request():
            req = urllib.request.Request(
                url,
                method=method,
                headers={
                    "Authorization": f"Bearer {self.token}",
                    "Notion-Version": "2022-06-28",
                    "Content-Type": "application/json"
                }
            )
            if data:
                req.data = json.dumps(data).encode('utf-8')
            
            try:
                with urllib.request.urlopen(req, timeout=30) as response:
                    return json.loads(response.read().decode('utf-8'))
            except urllib.error.HTTPError as e:
                raise NotionAPIError(f"HTTP {e.code}: {e.reason}", e.code)
        
        # Run sync code in thread pool
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, make_request)
    
    async def create(self, task: Task) -> Task:
        """Create task in Notion with retry logic."""
        data = {
            "parent": {"database_id": self.database_id},
            "properties": task.to_notion_properties()
        }
        result = await self._request("POST", "pages", data)
        self._counter.increment()
        print(f"  Created task #{self._counter.count} in Notion")
        return task
    
    async def get(self, task_id: str) -> Optional[Task]:
        """Get task with error handling."""
        try:
            result = await self._request("GET", f"pages/{task_id}")
            return self._parse_task(result)
        except NotionAPIError as e:
            if e.status_code == 404:
                return None
            raise
    
    def _parse_task(self, data: Dict[str, Any]) -> Task:
        """Parse Notion response into typed Task."""
        props = data.get("properties", {})
        return Task(
            id=data.get("id", ""),
            name=self._extract_title(props),
            priority=Priority.HIGH,
            status=Status.TODO
        )
    
    def _extract_title(self, props: Dict) -> str:
        """Safely extract title from Notion properties."""
        title_list = props.get("Name", {}).get("title", [])
        if title_list:
            return title_list[0].get("text", {}).get("content", "")
        return ""


# ============== Decorators ==============

def retry_on_error(max_retries: int = 3, delay: float = 1.0):
    """Decorator for retry logic with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    wait_time = delay * (2 ** attempt)  # Exponential backoff
                    print(f"  Attempt {attempt + 1} failed, retrying in {wait_time}s...")
                    await asyncio.sleep(wait_time)
            raise last_exception
        return wrapper
    return decorator


def log_execution_time(func: Callable) -> Callable:
    """Decorator to log execution time."""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = datetime.now()
        try:
            return await func(*args, **kwargs)
        finally:
            elapsed = (datetime.now() - start).total_seconds()
            print(f"  {func.__name__} completed in {elapsed:.3f}s")
    return wrapper


# ============== Service Layer ==============

class TaskService:
    """Business logic layer following clean architecture."""
    
    def __init__(self, repository: TaskRepository):
        self._repo = repository
    
    @retry_on_error(max_retries=3, delay=0.5)
    @log_execution_time
    async def create_camping_task(self, title: str, due: datetime) -> Task:
        """Create camping task with validation and logging."""
        task = Task(
            id=f"camp_{datetime.now().timestamp():.0f}",
            name=title,
            priority=Priority.HIGH,
            status=Status.TODO,
            due_date=due,
            project="Hayahaya Adventures",
            labels=["Family", "Camping"]
        )
        return await self._repo.create(task)
    
    async def batch_create_tasks(self, tasks_data: List[Dict]) -> List[Task]:
        """Create multiple tasks concurrently."""
        tasks = [
            self.create_camping_task(t["title"], t["due"]) 
            for t in tasks_data
        ]
        return await asyncio.gather(*tasks)


# ============== Context Manager ==============

class DatabaseConnection:
    """Async context manager for resource management."""
    
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.connection = None
        self._start_time = None
    
    async def __aenter__(self):
        self._start_time = datetime.now()
        print(f"  [DB] Opening connection to {self.connection_string}")
        self.connection = {"status": "connected", "id": id(self)}
        return self.connection
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        duration = (datetime.now() - self._start_time).total_seconds()
        print(f"  [DB] Connection closed after {duration:.3f}s")
        if exc_type:
            print(f"  [DB] Exception occurred: {exc_type.__name__}")
        self.connection = None
        return False  # Don't suppress exceptions


# ============== Generator / Iterator ==============

def task_generator(project: str, count: int):
    """Generator for creating task templates."""
    templates = [
        ("Pre-Trip Car Check (BLOWBAGETS)", Priority.HIGH),
        ("Pack camping gear", Priority.HIGH),
        ("Check Starlink kit", Priority.MEDIUM),
        ("Charge EcoFlow", Priority.MEDIUM),
        ("Prepare tech class materials", Priority.LOW)
    ]
    
    for i, (name, priority) in enumerate(templates[:count]):
        yield Task(
            id=f"gen_{i}",
            name=name,
            priority=priority,
            status=Status.TODO,
            project=project
        )


# ============== Main ==============

async def main():
    """Demonstrate all advanced Python concepts."""
    print("=" * 60)
    print("ADVANCED PYTHON MASTERY - PHASE 1 COMPLETE")
    print("=" * 60)
    
    # 1. Metaclass (Singleton)
    print("\n1. METACLASS PATTERN (Singleton)")
    counter1 = TaskCounter()
    counter2 = TaskCounter()
    print(f"   Same instance: {counter1 is counter2}")
    print(f"   Count: {counter1.increment()}")
    print(f"   Count: {counter2.increment()}")
    
    # 2. Descriptor
    print("\n2. DESCRIPTOR PATTERN (Validation)")
    progress = ProjectProgress("ScalePlus Launch")
    progress.percentage = 75
    print(f"   Progress: {progress.percentage}%")
    try:
        progress.percentage = 150  # Should raise ValueError
    except ValueError as e:
        print(f"   Validation caught: {e}")
    
    # 3. Context Manager
    print("\n3. ASYNC CONTEXT MANAGER")
    async with DatabaseConnection("notion://tasks") as conn:
        print(f"   Using connection: {conn['id']}")
    
    # 4. Async/Await with Concurrency
    print("\n4. ASYNC/AWAIT WITH GATHER")
    async def simulate_api_call(name: str, delay: float):
        await asyncio.sleep(delay)
        return f"{name} completed"
    
    start = datetime.now()
    results = await asyncio.gather(
        simulate_api_call("Task A", 0.1),
        simulate_api_call("Task B", 0.2),
        simulate_api_call("Task C", 0.15)
    )
    elapsed = (datetime.now() - start).total_seconds()
    print(f"   All completed in {elapsed:.3f}s (concurrent)")
    for r in results:
        print(f"   - {r}")
    
    # 5. Generator
    print("\n5. GENERATOR PATTERN")
    for task in task_generator("Hayahaya", 3):
        print(f"   Generated: {task.name} ({task.priority.value})")
    
    # 6. Dataclass with Immutability
    print("\n6. DATACLASS (Immutable)")
    task = Task(
        id="demo_001",
        name="DTI Registration",
        priority=Priority.HIGH,
        status=Status.DOING,
        due_date=datetime(2026, 2, 7),
        project="Hayahaya Adventures",
        labels=["Priority", "Legal"]
    )
    print(f"   Task: {task.name}")
    print(f"   Due: {task.due_date}")
    print(f"   Labels: {task.labels}")
    try:
        task.name = "Changed"  # Should fail (frozen=True)
    except AttributeError:
        print("   ✓ Immutability enforced")
    
    # 7. Type Conversion
    print("\n7. NOTION API INTEGRATION")
    print("   Notion Properties JSON:")
    notion_props = task.to_notion_properties()
    print(json.dumps(notion_props, indent=4))
    
    # 8. Service Layer with Decorators
    print("\n8. SERVICE LAYER (Decorators + Async)")
    
    # Mock repository that simulates API calls
    class MockRepository:
        async def create(self, task: Task) -> Task:
            await asyncio.sleep(0.1)  # Simulate network
            return task
    
    service = TaskService(MockRepository())
    
    # Single task creation
    new_task = await service.create_camping_task(
        "Test camping task",
        datetime(2026, 2, 12, 6, 0)
    )
    
    # Batch creation
    print("\n9. BATCH OPERATIONS (Concurrent)")
    camping_tasks = [
        {"title": "Pack Starlink", "due": datetime(2026, 2, 11)},
        {"title": "Check tires", "due": datetime(2026, 2, 12)},
        {"title": "Fill gas tank", "due": datetime(2026, 2, 12)}
    ]
    created = await service.batch_create_tasks(camping_tasks)
    print(f"   Created {len(created)} tasks concurrently")
    
    print("\n" + "=" * 60)
    print("PHASE 1 ADVANCED PYTHON CONCEPTS DEMONSTRATED:")
    print("=" * 60)
    concepts = [
        "Metaclasses (Singleton pattern)",
        "Descriptors (field validation)",
        "Async/await with asyncio",
        "Context managers (async)",
        "Generators for lazy evaluation",
        "Dataclasses with immutability",
        "Type hints (Protocol, Generic, Optional)",
        "Decorators (retry, timing)",
        "Clean architecture (Repository pattern)",
        "Error handling with custom exceptions",
        "Concurrent batch operations",
        "Protocol for structural subtyping"
    ]
    for i, concept in enumerate(concepts, 1):
        print(f"  {i:2}. {concept}")
    
    print("\n" + "=" * 60)
    print("Ready for Phase 2: Software Architecture")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
