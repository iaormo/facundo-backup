#!/usr/bin/env python3
"""
Phase 2: Software Architecture
Clean Architecture, Design Patterns, Testing
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from typing import List, Dict, Any, Optional, Type, Callable
import json
import unittest
from unittest.mock import Mock, patch, AsyncMock
import asyncio


# ============== SOLID Principles ==============

# S - Single Responsibility Principle
# Each class has one reason to change

class NotificationService(ABC):
    """Abstract base for notifications."""
    @abstractmethod
    async def send(self, message: str, recipient: str) -> bool: ...


class DiscordNotificationService(NotificationService):
    """Discord-specific implementation."""
    async def send(self, message: str, recipient: str) -> bool:
        print(f"[Discord] To {recipient}: {message}")
        return True


class EmailNotificationService(NotificationService):
    """Email-specific implementation."""
    async def send(self, message: str, recipient: str) -> bool:
        print(f"[Email] To {recipient}: {message}")
        return True


# O - Open/Closed Principle
# Open for extension, closed for modification

class TaskFormatter(ABC):
    """Abstract formatter - extend without modifying."""
    @abstractmethod
    def format(self, task: Dict) -> str: ...


class MarkdownFormatter(TaskFormatter):
    def format(self, task: Dict) -> str:
        return f"**{task['name']}** - {task['status']}"


class JSONFormatter(TaskFormatter):
    def format(self, task: Dict) -> str:
        return json.dumps(task, indent=2)


class PlainTextFormatter(TaskFormatter):
    def format(self, task: Dict) -> str:
        return f"{task['name']}: {task['status']}"


# L - Liskov Substitution Principle
# Child classes can substitute parent classes

class TaskRepository(ABC):
    """Base repository - any subclass must be substitutable."""
    @abstractmethod
    async def save(self, task: Dict) -> str: ...
    
    @abstractmethod
    async def get(self, task_id: str) -> Optional[Dict]: ...


class InMemoryTaskRepository(TaskRepository):
    """In-memory implementation."""
    def __init__(self):
        self._tasks: Dict[str, Dict] = {}
        self._counter = 0
    
    async def save(self, task: Dict) -> str:
        self._counter += 1
        task_id = f"task_{self._counter}"
        self._tasks[task_id] = {**task, "id": task_id}
        return task_id
    
    async def get(self, task_id: str) -> Optional[Dict]:
        return self._tasks.get(task_id)


class NotionTaskRepository(TaskRepository):
    """Notion API implementation - substitutable for InMemory."""
    def __init__(self, token: str):
        self.token = token
    
    async def save(self, task: Dict) -> str:
        # Would call Notion API
        return f"notion_{task['name'][:10]}"
    
    async def get(self, task_id: str) -> Optional[Dict]:
        # Would call Notion API
        return {"id": task_id, "name": "Sample"}


# I - Interface Segregation Principle
# Split large interfaces into smaller ones

class Readable(ABC):
    @abstractmethod
    async def read(self, id: str) -> Any: ...


class Writable(ABC):
    @abstractmethod
    async def write(self, data: Any) -> str: ...


class Deletable(ABC):
    @abstractmethod
    async def delete(self, id: str) -> bool: ...


# Repository implements only what it needs
class ReadOnlyRepository(Readable):
    async def read(self, id: str) -> Any:
        return {"id": id}


class FullRepository(Readable, Writable, Deletable):
    async def read(self, id: str) -> Any:
        return {"id": id}
    
    async def write(self, data: Any) -> str:
        return "new_id"
    
    async def delete(self, id: str) -> bool:
        return True


# D - Dependency Inversion Principle
# Depend on abstractions, not concretions

class TaskManager:
    """High-level module depends on abstraction (TaskRepository)."""
    
    def __init__(self, repository: TaskRepository, notifier: NotificationService):
        self._repo = repository
        self._notifier = notifier
    
    async def create_task(self, name: str, assignee: str) -> str:
        task = {"name": name, "status": "todo", "created": datetime.now().isoformat()}
        task_id = await self._repo.save(task)
        await self._notifier.send(f"New task created: {name}", assignee)
        return task_id


# ============== Design Patterns ==============

# Factory Pattern
class NotificationFactory:
    """Factory for creating notification services."""
    
    _services: Dict[str, Type[NotificationService]] = {
        "discord": DiscordNotificationService,
        "email": EmailNotificationService
    }
    
    @classmethod
    def create(cls, service_type: str) -> NotificationService:
        service_class = cls._services.get(service_type)
        if not service_class:
            raise ValueError(f"Unknown service type: {service_type}")
        return service_class()
    
    @classmethod
    def register(cls, name: str, service_class: Type[NotificationService]):
        cls._services[name] = service_class


# Builder Pattern
@dataclass
class TaskConfig:
    name: str
    priority: str = "medium"
    due_date: Optional[datetime] = None
    labels: List[str] = None
    assignee: Optional[str] = None


class TaskBuilder:
    """Builder for complex task creation."""
    
    def __init__(self, name: str):
        self._config = TaskConfig(name=name, labels=[])
    
    def high_priority(self):
        self._config.priority = "high"
        return self
    
    def low_priority(self):
        self._config.priority = "low"
        return self
    
    def due(self, date: datetime):
        self._config.due_date = date
        return self
    
    def with_label(self, label: str):
        self._config.labels.append(label)
        return self
    
    def assign_to(self, person: str):
        self._config.assignee = person
        return self
    
    def build(self) -> TaskConfig:
        return self._config


# Strategy Pattern
class PricingStrategy(ABC):
    """Strategy for calculating prices."""
    @abstractmethod
    def calculate(self, base_price: float) -> float: ...


class StandardPricing(PricingStrategy):
    def calculate(self, base_price: float) -> float:
        return base_price


class DiscountPricing(PricingStrategy):
    def __init__(self, discount_percent: float):
        self.discount = discount_percent
    
    def calculate(self, base_price: float) -> float:
        return base_price * (1 - self.discount / 100)


class BundlePricing(PricingStrategy):
    def calculate(self, base_price: float) -> float:
        return base_price * 0.9  # 10% bundle discount


class QuoteCalculator:
    """Uses strategy pattern for flexible pricing."""
    
    def __init__(self, strategy: PricingStrategy):
        self._strategy = strategy
    
    def get_price(self, base_price: float) -> float:
        return self._strategy.calculate(base_price)
    
    def set_strategy(self, strategy: PricingStrategy):
        self._strategy = strategy


# Observer Pattern
class Event:
    TASK_CREATED = "task_created"
    TASK_COMPLETED = "task_completed"


class EventManager:
    """Observer pattern implementation."""
    
    def __init__(self):
        self._listeners: Dict[str, List[Callable]] = {}
    
    def subscribe(self, event: str, callback: Callable):
        if event not in self._listeners:
            self._listeners[event] = []
        self._listeners[event].append(callback)
    
    def unsubscribe(self, event: str, callback: Callable):
        if event in self._listeners:
            self._listeners[event].remove(callback)
    
    async def emit(self, event: str, data: Any = None):
        if event in self._listeners:
            for callback in self._listeners[event]:
                if asyncio.iscoroutinefunction(callback):
                    await callback(data)
                else:
                    callback(data)


# Command Pattern
class Command(ABC):
    """Abstract command."""
    @abstractmethod
    async def execute(self) -> Any: ...
    
    @abstractmethod
    async def undo(self) -> Any: ...


class CreateTaskCommand(Command):
    """Command to create a task."""
    
    def __init__(self, manager: TaskManager, task_name: str, assignee: str):
        self._manager = manager
        self._task_name = task_name
        self._assignee = assignee
        self._task_id: Optional[str] = None
    
    async def execute(self) -> str:
        self._task_id = await self._manager.create_task(self._task_name, self._assignee)
        return self._task_id
    
    async def undo(self) -> bool:
        # Would delete the task
        print(f"Undoing creation of task {self._task_id}")
        return True


class CommandInvoker:
    """Invoker for commands with history."""
    
    def __init__(self):
        self._history: List[Command] = []
    
    async def execute(self, command: Command) -> Any:
        result = await command.execute()
        self._history.append(command)
        return result
    
    async def undo_last(self) -> bool:
        if self._history:
            command = self._history.pop()
            return await command.undo()
        return False


# ============== Testing ==============

class TestTaskManager(unittest.IsolatedAsyncioTestCase):
    """Unit tests demonstrating TDD."""
    
    async def test_create_task(self):
        """Test task creation."""
        # Arrange
        mock_repo = Mock(spec=TaskRepository)
        mock_repo.save = AsyncMock(return_value="task_123")
        
        mock_notifier = Mock(spec=NotificationService)
        mock_notifier.send = AsyncMock(return_value=True)
        
        manager = TaskManager(mock_repo, mock_notifier)
        
        # Act
        task_id = await manager.create_task("Test Task", "papi")
        
        # Assert
        self.assertEqual(task_id, "task_123")
        mock_repo.save.assert_called_once()
        mock_notifier.send.assert_called_once()
    
    async def test_task_builder(self):
        """Test builder pattern."""
        task = (TaskBuilder("DTI Registration")
                .high_priority()
                .with_label("Legal")
                .with_label("Hayahaya")
                .assign_to("papi")
                .build())
        
        self.assertEqual(task.name, "DTI Registration")
        self.assertEqual(task.priority, "high")
        self.assertEqual(task.labels, ["Legal", "Hayahaya"])
        self.assertEqual(task.assignee, "papi")
    
    def test_pricing_strategies(self):
        """Test strategy pattern."""
        base_price = 1000
        
        standard = QuoteCalculator(StandardPricing())
        self.assertEqual(standard.get_price(base_price), 1000)
        
        discount = QuoteCalculator(DiscountPricing(20))
        self.assertEqual(discount.get_price(base_price), 800)
        
        bundle = QuoteCalculator(BundlePricing())
        self.assertEqual(bundle.get_price(base_price), 900)
    
    async def test_event_manager(self):
        """Test observer pattern."""
        events = EventManager()
        received = []
        
        async def handler(data):
            received.append(data)
        
        events.subscribe(Event.TASK_CREATED, handler)
        await events.emit(Event.TASK_CREATED, {"name": "Test"})
        
        self.assertEqual(len(received), 1)
        self.assertEqual(received[0]["name"], "Test")


# ============== Main ==============

async def main():
    """Demonstrate Phase 2 concepts."""
    print("=" * 60)
    print("PHASE 2: SOFTWARE ARCHITECTURE & DESIGN PATTERNS")
    print("=" * 60)
    
    # 1. SOLID Principles
    print("\n1. SOLID PRINCIPLES")
    
    # Dependency Injection (DIP)
    repo = InMemoryTaskRepository()
    notifier = DiscordNotificationService()
    manager = TaskManager(repo, notifier)
    
    task_id = await manager.create_task("ScalePlus Website Fix", "papi")
    print(f"   Created task: {task_id}")
    
    # 2. Factory Pattern
    print("\n2. FACTORY PATTERN")
    discord_service = NotificationFactory.create("discord")
    email_service = NotificationFactory.create("email")
    await discord_service.send("Hello", "papi")
    await email_service.send("Hello", "papi@example.com")
    
    # 3. Builder Pattern
    print("\n3. BUILDER PATTERN")
    task_config = (TaskBuilder("Camping Preparation")
                   .high_priority()
                   .with_label("Family")
                   .with_label("Hayahaya")
                   .due(datetime(2026, 2, 11))
                   .assign_to("papi")
                   .build())
    print(f"   Task: {task_config.name}")
    print(f"   Priority: {task_config.priority}")
    print(f"   Labels: {task_config.labels}")
    
    # 4. Strategy Pattern
    print("\n4. STRATEGY PATTERN")
    base_price = 4995  # ScalePlus Growth System
    
    calculator = QuoteCalculator(StandardPricing())
    print(f"   Standard: {calculator.get_price(base_price):,.0f} PHP")
    
    calculator.set_strategy(DiscountPricing(10))  # 10% off
    print(f"   With 10% discount: {calculator.get_price(base_price):,.0f} PHP")
    
    calculator.set_strategy(BundlePricing())  # Bundle with website
    print(f"   Bundle price: {calculator.get_price(base_price):,.0f} PHP")
    
    # 5. Observer Pattern
    print("\n5. OBSERVER PATTERN")
    events = EventManager()
    
    async def log_handler(data):
        print(f"   [LOG] Task event: {data}")
    
    async def notify_handler(data):
        print(f"   [NOTIFY] Sending notification for: {data.get('name')}")
    
    events.subscribe(Event.TASK_CREATED, log_handler)
    events.subscribe(Event.TASK_CREATED, notify_handler)
    
    await events.emit(Event.TASK_CREATED, {"name": "DTI Registration", "priority": "high"})
    
    # 6. Command Pattern
    print("\n6. COMMAND PATTERN")
    invoker = CommandInvoker()
    
    cmd1 = CreateTaskCommand(manager, "Fix Cloudflare Redirect", "papi")
    cmd2 = CreateTaskCommand(manager, "Update Pricing Page", "papi")
    
    id1 = await invoker.execute(cmd1)
    id2 = await invoker.execute(cmd2)
    print(f"   Executed commands: {id1}, {id2}")
    
    await invoker.undo_last()  # Undo last command
    print("   Undid last command")
    
    # 7. Formatter Strategy (OCP)
    print("\n7. OPEN/CLOSED PRINCIPLE")
    task_data = {"name": "Camping Trip", "status": "to_do", "priority": "high"}
    
    formatters = [MarkdownFormatter(), JSONFormatter(), PlainTextFormatter()]
    for formatter in formatters:
        print(f"   {formatter.__class__.__name__}: {formatter.format(task_data)[:50]}...")
    
    print("\n" + "=" * 60)
    print("PHASE 2 CONCEPTS DEMONSTRATED:")
    print("=" * 60)
    concepts = [
        "SOLID Principles (all 5)",
        "Factory Pattern",
        "Builder Pattern",
        "Strategy Pattern",
        "Observer Pattern",
        "Command Pattern with Undo",
        "Abstract Base Classes (ABC)",
        "Dependency Injection",
        "Interface Segregation",
        "Unit Testing with AsyncMock"
    ]
    for i, concept in enumerate(concepts, 1):
        print(f"  {i:2}. {concept}")
    
    # Tests defined (run separately with: python3 -m unittest phase2_architecture)
    print("\n" + "=" * 60)
    print("UNIT TESTS AVAILABLE:")
    print("=" * 60)
    print("  Run with: python3 -m unittest python_mastery.phase2_architecture")
    print("  - test_create_task: Repository and DI testing")
    print("  - test_task_builder: Builder pattern validation")
    print("  - test_pricing_strategies: Strategy pattern testing")
    print("  - test_event_manager: Observer pattern async testing")
    
    print("\n" + "=" * 60)
    print("PHASE 2 COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
