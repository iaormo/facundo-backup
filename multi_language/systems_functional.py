#!/usr/bin/env python3
"""
Multi-Language Mastery - Frontend & Systems Languages
JavaScript, TypeScript, C, C++, Haskell, Scala, and more
"""

import asyncio


# ============== FRONTEND LANGUAGES ==============

FRONTEND_LANGUAGES = {
    "JavaScript": {
        "dominant": True,
        "paradigm": "Multi-paradigm",
        "strengths": ["Universal browser support", "Async nature", "Massive ecosystem"],
        "versions": ["ES5", "ES6+", "ES2023"],
        "runtime": "V8, SpiderMonkey, JavaScriptCore"
    },
    "TypeScript": {
        "dominant": True,
        "paradigm": "Typed superset of JavaScript",
        "strengths": ["Static typing", "IDE support", "Better maintainability"],
        "versions": ["4.x", "5.x"],
        "runtime": "Compiles to JavaScript"
    },
    "WebAssembly": {
        "dominant": False,
        "paradigm": "Binary instruction format",
        "strengths": ["Near-native performance", "Language agnostic", "Secure sandbox"],
        "use_cases": ["Gaming", "Video editing", "CAD", "Compression"],
        "runtime": "Browser VM"
    }
}


# ============== SYSTEMS LANGUAGES ==============

SYSTEMS_LANGUAGES = {
    "C": {
        "level": "Low",
        "paradigm": "Procedural",
        "strengths": ["Maximum performance", "Hardware control", "Universal portability"],
        "use_cases": ["OS kernels", "Embedded systems", "Drivers", "Databases"],
        "memory": "Manual (malloc/free)"
    },
    "C++": {
        "level": "Low/Mid",
        "paradigm": "Multi-paradigm (OOP, generic, procedural)",
        "strengths": ["Zero-cost abstractions", "STL", "RAII", "Backward compatible with C"],
        "use_cases": ["Game engines", "High-frequency trading", "Browsers", "CAD"],
        "memory": "Manual + Smart pointers"
    },
    "Rust": {
        "level": "Low/Mid",
        "paradigm": "Multi-paradigm with ownership",
        "strengths": ["Memory safety without GC", "Zero-cost abstractions", "Fearless concurrency"],
        "use_cases": ["Systems", "WebAssembly", "Embedded", "CLI tools"],
        "memory": "Ownership + Borrow checker"
    },
    "Go": {
        "level": "Mid",
        "paradigm": "Procedural, concurrent",
        "strengths": ["Goroutines", "Fast compile", "Static binaries", "Simple"],
        "use_cases": ["Cloud infrastructure", "Microservices", "DevOps tools"],
        "memory": "Garbage collected"
    },
    "Zig": {
        "level": "Low",
        "paradigm": "Procedural",
        "strengths": ["C interop", "Comptime", "Explicit control", "Cross-compilation"],
        "use_cases": ["Systems programming", "Embedded", "Game dev"],
        "memory": "Manual with safety features"
    }
}


# ============== FUNCTIONAL LANGUAGES ==============

FUNCTIONAL_LANGUAGES = {
    "Haskell": {
        "paradigm": "Pure functional, lazy",
        "strengths": ["Type safety", "Immutability by default", "Elegant abstractions"],
        "use_cases": ["Financial systems", "Compilers", "Formal verification"],
        "features": ["Monads", "Type classes", "Lazy evaluation", "GHC"]
    },
    "Scala": {
        "paradigm": "Object-functional",
        "strengths": ["JVM ecosystem", "Concise syntax", "Pattern matching"],
        "use_cases": ["Big Data (Spark)", "Distributed systems", "Web"],
        "features": ["Case classes", "Implicits", "Traits", "Akka"]
    },
    "Elixir": {
        "paradigm": "Functional, concurrent",
        "strengths": ["Erlang VM (BEAM)", "Fault tolerance", "Hot code reloading"],
        "use_cases": ["Real-time apps", "Chat systems", "IoT"],
        "features": ["Phoenix framework", "OTP", "Pattern matching", "Processes"]
    },
    "Clojure": {
        "paradigm": "Lisp, functional",
        "strengths": ["JVM/CLR/JS", "Immutable data", "Macros"],
        "use_cases": ["Data processing", "Web", "Financial"],
        "features": ["REPL-driven", "STM", "Protocols", "Multimethods"]
    },
    "F#": {
        "paradigm": "Functional, OOP",
        "strengths": [".NET ecosystem", "Type inference", "Units of measure"],
        "use_cases": ["Financial", "Data science", "Web"],
        "features": ["Computation expressions", "Active patterns", "Type providers"]
    }
}


# ============== LANGUAGE FEATURES COMPARISON ==============

FEATURES = {
    "Memory Management": {
        "Manual (C/C++)": "Full control, error prone",
        "Garbage Collection (Java, Go, JS)": "Automatic, pauses possible",
        "Ownership (Rust)": "Compile-time safety, zero-cost",
        "Reference Counting (Swift, Python)": "Deterministic, cycle issues"
    },
    "Type Systems": {
        "Static (Java, C#, Go)": "Compile-time checking, performance",
        "Dynamic (Python, Ruby, JS)": "Flexibility, runtime errors",
        "Gradual (TypeScript, Python+mypy)": "Optional static types",
        "Inferred (Haskell, Rust, Scala)": "Type safety without verbosity"
    },
    "Concurrency Models": {
        "Threads (Java, C++)": "OS threads, heavy",
        "Goroutines (Go)": "Lightweight threads, CSP",
        "Async/Await (JS, Python, Rust)": "Non-blocking, event loop",
        "Actors (Erlang/Elixir, Akka)": "Message passing, fault tolerant",
        "STM (Haskell, Clojure)": "Software transactional memory"
    }
}


# ============== CODE EXAMPLES ==============

CODE_EXAMPLES = {
    "C (Systems)": '''
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Task structure
typedef struct {
    int id;
    char* name;
    char* status;
    char* priority;
} Task;

// Create task
Task* create_task(int id, const char* name, const char* status, const char* priority) {
    Task* task = malloc(sizeof(Task));
    task->id = id;
    task->name = strdup(name);
    task->status = strdup(status);
    task->priority = strdup(priority);
    return task;
}

// Free task
void free_task(Task* task) {
    free(task->name);
    free(task->status);
    free(task->priority);
    free(task);
}

int main() {
    Task* task = create_task(1, "DTI Registration", "doing", "high");
    printf("Task: %s (%s)\\n", task->name, task->priority);
    free_task(task);
    return 0;
}
// Compile: gcc -o task task.c && ./task
''',

    "C++ (Modern)": '''
#include <iostream>
#include <string>
#include <vector>
#include <memory>

class Task {
private:
    int id;
    std::string name;
    std::string status;
    std::string priority;

public:
    Task(int id, std::string name, std::string status = "todo", std::string priority = "medium")
        : id(id), name(std::move(name)), status(std::move(status)), priority(std::move(priority)) {}
    
    // Rule of 5
    ~Task() = default;
    Task(const Task&) = default;
    Task(Task&&) = default;
    Task& operator=(const Task&) = default;
    Task& operator=(Task&&) = default;
    
    void display() const {
        std::cout << "Task[" << id << "]: " << name 
                  << " (" << status << ", " << priority << ")\\n";
    }
};

int main() {
    auto task = std::make_unique<Task>(1, "DTI Registration", "doing", "high");
    task->display();
    
    std::vector<Task> tasks;
    tasks.emplace_back(2, "Setup Starlink", "todo", "medium");
    
    return 0;
}
// Compile: g++ -std=c++17 -o task task.cpp && ./task
''',

    "Haskell (Functional)": '''
module Main where

-- Define Task type
data Task = Task {
    taskId :: Int,
    taskName :: String,
    taskStatus :: Status,
    taskPriority :: Priority
} deriving (Show, Eq)

data Status = Todo | Doing | Done deriving (Show, Eq)
data Priority = Low | Medium | High deriving (Show, Eq, Ord)

-- Create a task
createTask :: Int -> String -> Status -> Priority -> Task
createTask id name status priority = Task id name status priority

-- Filter high priority tasks
highPriority :: [Task] -> [Task]
highPriority = filter (\\t -> taskPriority t == High)

-- Sort by priority
sortByPriority :: [Task] -> [Task]
sortByPriority = sortBy (\\a b -> compare (taskPriority b) (taskPriority a))

-- Pure function example
calculateRevenue :: Int -> Int -> Int
calculateRevenue price quantity = price * quantity

main :: IO ()
main = do
    let task = createTask 1 "DTI Registration" Doing High
    print task
    
    let tasks = [
            createTask 2 "Setup Website" Todo Medium,
            createTask 3 "Launch Campaign" Todo High,
            createTask 4 "Review Code" Doing Low
          ]
    
    putStrLn "High priority tasks:"
    mapM_ print (highPriority tasks)
-- Run: ghc task.hs && ./task
''',

    "Elixir (Concurrent)": '''
defmodule Task do
  defstruct [:id, :name, :status, :priority]
  
  @type t :: %__MODULE__{
    id: integer(),
    name: String.t(),
    status: String.t(),
    priority: String.t()
  }
end

defmodule TaskManager do
  use GenServer
  
  # Client API
  def start_link(_) do
    GenServer.start_link(__MODULE__, [], name: __MODULE__)
  end
  
  def create_task(name, status \\\\ "todo", priority \\\\ "medium") do
    GenServer.call(__MODULE__, {:create, name, status, priority})
  end
  
  def list_tasks do
    GenServer.call(__MODULE__, :list)
  end
  
  # Server callbacks
  @impl true
  def init(_) do
    {:ok, %{tasks: [], next_id: 1}}
  end
  
  @impl true
  def handle_call({:create, name, status, priority}, _from, state) do
    task = %Task{
      id: state.next_id,
      name: name,
      status: status,
      priority: priority
    }
    
    new_state = %{
      state |
      tasks: [task | state.tasks],
      next_id: state.next_id + 1
    }
    
    {:reply, task, new_state}
  end
  
  @impl true
  def handle_call(:list, _from, state) do
    {:reply, state.tasks, state}
  end
end

# Usage
# TaskManager.start_link([])
# TaskManager.create_task("DTI Registration", "doing", "high")
# Run: iex task.ex
''',

    "Scala (JVM)": '''
package com.scaleplus

// Case class (immutable)
case class Task(
  id: Int,
  name: String,
  status: String = "todo",
  priority: String = "medium"
)

object TaskManager {
  // Immutable list
  private var tasks: List[Task] = Nil
  private var nextId: Int = 1
  
  def createTask(name: String, status: String = "todo", priority: String = "medium"): Task = {
    val task = Task(nextId, name, status, priority)
    tasks = task :: tasks
    nextId += 1
    task
  }
  
  def listTasks(): List[Task] = tasks
  
  def highPriorityTasks(): List[Task] = 
    tasks.filter(_.priority == "high")
  
  // Pattern matching
  def taskSummary(task: Task): String = task match {
    case Task(_, name, "done", _) => s"✓ $name"
    case Task(_, name, "doing", "high") => s"⚡ $name (urgent)"
    case Task(_, name, _, _) => s"○ $name"
  }
}

// Main
object Main extends App {
  import TaskManager._
  
  val task1 = createTask("DTI Registration", "doing", "high")
  val task2 = createTask("Setup Website")
  
  println(s"Created: ${task1.name}")
  println(s"High priority: ${highPriorityTasks().map(_.name)}")
}
// Run: scala task.scala
'''
}


# ============== Main ==============

async def main():
    """Demonstrate systems and functional language knowledge."""
    print("=" * 70)
    print("MULTI-LANGUAGE MASTERY - SYSTEMS & FUNCTIONAL LANGUAGES")
    print("=" * 70)
    
    # 1. Systems Languages
    print("\n1. SYSTEMS PROGRAMMING LANGUAGES")
    print("-" * 40)
    
    for lang, info in SYSTEMS_LANGUAGES.items():
        print(f"\n   {lang}:")
        print(f"     Level: {info['level']}")
        print(f"     Paradigm: {info['paradigm']}")
        print(f"     Memory: {info['memory']}")
        print(f"     Best for: {', '.join(info['use_cases'][:2])}")
    
    # 2. Functional Languages
    print("\n2. FUNCTIONAL PROGRAMMING LANGUAGES")
    print("-" * 40)
    
    for lang, info in FUNCTIONAL_LANGUAGES.items():
        print(f"\n   {lang}:")
        print(f"     Paradigm: {info['paradigm']}")
        print(f"     Features: {', '.join(info['features'][:2])}")
        print(f"     Best for: {', '.join(info['use_cases'][:2])}")
    
    # 3. Feature Comparison
    print("\n3. LANGUAGE FEATURE COMPARISON")
    print("-" * 40)
    
    for category, features in FEATURES.items():
        print(f"\n   {category}:")
        for model, desc in features.items():
            print(f"     • {model}: {desc}")
    
    # 4. Code Examples
    print("\n4. CODE EXAMPLES")
    print("-" * 40)
    
    for lang, code in CODE_EXAMPLES.items():
        print(f"\n   {lang}:")
        print(f"   {code[:100]}...")
    
    # 5. Language Selection
    print("\n5. DOMAIN-SPECIFIC LANGUAGE SELECTION")
    print("-" * 40)
    
    selections = [
        ("OS Kernel/Device Driver", "C or Rust"),
        ("Game Engine", "C++ (Unreal) or Rust (Bevy)"),
        ("High-Frequency Trading", "C++ or Rust"),
        ("Financial Systems", "Haskell or F#"),
        ("Distributed Systems", "Elixir/Erlang or Scala/Akka"),
        ("Big Data Processing", "Scala (Spark)"),
        ("WebAssembly Module", "Rust or C/C++"),
        ("Embedded Systems", "C, C++, Rust, or Zig"),
        ("Real-time Chat", "Elixir (Phoenix)"),
        ("Compiler/Parser", "Haskell, Rust, or C++"),
    ]
    
    for domain, choice in selections:
        print(f"   {domain:35} → {choice}")
    
    print("\n" + "=" * 70)
    print("SYSTEMS & FUNCTIONAL LANGUAGES MASTERED")
    print("=" * 70)
    print("\nLanguages covered:")
    print("  Systems: C, C++, Rust, Go, Zig")
    print("  Functional: Haskell, Scala, Elixir, Clojure, F#")
    print("  Frontend: JavaScript, TypeScript, WebAssembly")
    print("\nReady for any programming challenge!")


if __name__ == "__main__":
    asyncio.run(main())
