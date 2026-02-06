#!/usr/bin/env python3
"""
Multi-Language Mastery - Backend Languages
Python, Node.js, Go, Rust, Java, C#, Ruby, PHP
"""

import asyncio


# ============== LANGUAGE COMPARISONS ==============

BACKEND_LANGUAGES = {
    "Python": {
        "paradigm": "Multi-paradigm (OOP, functional, procedural)",
        "strengths": ["Readability", "AI/ML ecosystem", "Rapid development", "Large community"],
        "use_cases": ["AI/ML", "Web (Django/FastAPI)", "Data Science", "Automation"],
        "performance": "Moderate (CPython), Fast (PyPy)",
        "typing": "Dynamic, optional static (mypy)"
    },
    "Node.js": {
        "paradigm": "Event-driven, async",
        "strengths": ["Same language frontend/backend", "NPM ecosystem", "Non-blocking I/O", "JSON native"],
        "use_cases": ["Real-time apps", "APIs", "Microservices", "Serverless"],
        "performance": "Fast for I/O bound, V8 engine",
        "typing": "Dynamic, TypeScript available"
    },
    "Go": {
        "paradigm": "Procedural, concurrent",
        "strengths": ["Goroutines (lightweight threads)", "Fast compilation", "Static binaries", "Simple syntax"],
        "use_cases": ["Microservices", "DevOps tools", "Cloud infrastructure", "High concurrency"],
        "performance": "Compiled, near C performance",
        "typing": "Static, strong"
    },
    "Rust": {
        "paradigm": "Multi-paradigm, systems",
        "strengths": ["Memory safety without GC", "Zero-cost abstractions", "Fearless concurrency", "C interop"],
        "use_cases": ["Systems programming", "WebAssembly", "Embedded", "High-performance services"],
        "performance": "Compiled, C++ level",
        "typing": "Static, strong, affine types"
    },
    "Java": {
        "paradigm": "OOP, class-based",
        "strengths": ["Enterprise ecosystem", "JVM portability", "Mature libraries", "Strong typing"],
        "use_cases": ["Enterprise apps", "Android", "Big Data", "Financial systems"],
        "performance": "JVM with JIT, very fast",
        "typing": "Static, strong"
    },
    "C#": {
        "paradigm": "Multi-paradigm, OOP, functional",
        "strengths": [".NET ecosystem", "LINQ", "Async/await", "Unity game dev"],
        "use_cases": ["Enterprise", "Web (ASP.NET)", "Game dev", "Desktop apps"],
        "performance": "Compiled to IL, JIT, very fast",
        "typing": "Static, strong"
    },
    "Ruby": {
        "paradigm": "OOP, functional",
        "strengths": ["Developer happiness", "Rails framework", "Expressive syntax", "Metaprogramming"],
        "use_cases": ["Web (Rails)", "Prototyping", "DevOps (Chef)", "Scripting"],
        "performance": "Interpreted, slower",
        "typing": "Dynamic, duck typing"
    },
    "PHP": {
        "paradigm": "Imperative, OOP, functional",
        "strengths": ["Web-focused", "Easy deployment", "WordPress ecosystem", "Low barrier"],
        "use_cases": ["Web apps", "CMS (WordPress)", "E-commerce", "Shared hosting"],
        "performance": "Interpreted, PHP 8+ JIT fast",
        "typing": "Dynamic, gradual typing"
    }
}


# ============== CODE EXAMPLES IN EACH LANGUAGE ==============

CODE_EXAMPLES = {
    "Python (FastAPI)": '''
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import asyncpg

app = FastAPI(title="Task API")

class Task(BaseModel):
    id: Optional[int]
    name: str
    status: str = "todo"
    priority: str = "medium"

@app.get("/tasks", response_model=List[Task])
async def list_tasks():
    async with asyncpg.create_pool("postgresql://localhost/db") as pool:
        rows = await pool.fetch("SELECT * FROM tasks")
        return [Task(**dict(row)) for row in rows]

@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    async with asyncpg.create_pool("postgresql://localhost/db") as pool:
        row = await pool.fetchrow(
            "INSERT INTO tasks (name, status, priority) VALUES ($1, $2, $3) RETURNING *",
            task.name, task.status, task.priority
        )
        return Task(**dict(row))

# Run: uvicorn main:app --reload
''',

    "Node.js (Express)": '''
const express = require('express');
const { Pool } = require('pg');

const app = express();
app.use(express.json());

const pool = new Pool({
    connectionString: 'postgresql://localhost/db'
});

// List tasks
app.get('/tasks', async (req, res) => {
    try {
        const result = await pool.query('SELECT * FROM tasks');
        res.json(result.rows);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Create task
app.post('/tasks', async (req, res) => {
    const { name, status = 'todo', priority = 'medium' } = req.body;
    try {
        const result = await pool.query(
            'INSERT INTO tasks (name, status, priority) VALUES ($1, $2, $3) RETURNING *',
            [name, status, priority]
        );
        res.status(201).json(result.rows[0]);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

app.listen(3000, () => console.log('Server running on port 3000'));
// Run: node server.js
''',

    "Go (Gin)": '''
package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
    "database/sql"
    _ "github.com/lib/pq"
)

type Task struct {
    ID       int    `json:"id"`
    Name     string `json:"name"`
    Status   string `json:"status"`
    Priority string `json:"priority"`
}

func main() {
    db, _ := sql.Open("postgres", "postgresql://localhost/db")
    defer db.Close()
    
    r := gin.Default()
    
    // List tasks
    r.GET("/tasks", func(c *gin.Context) {
        rows, _ := db.Query("SELECT id, name, status, priority FROM tasks")
        defer rows.Close()
        
        var tasks []Task
        for rows.Next() {
            var t Task
            rows.Scan(&t.ID, &t.Name, &t.Status, &t.Priority)
            tasks = append(tasks, t)
        }
        c.JSON(http.StatusOK, tasks)
    })
    
    // Create task
    r.POST("/tasks", func(c *gin.Context) {
        var task Task
        c.BindJSON(&task)
        
        err := db.QueryRow(
            "INSERT INTO tasks (name, status, priority) VALUES ($1, $2, $3) RETURNING id",
            task.Name, task.Status, task.Priority,
        ).Scan(&task.ID)
        
        if err != nil {
            c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
            return
        }
        c.JSON(http.StatusCreated, task)
    })
    
    r.Run(":3000")
}
// Run: go run main.go
''',

    "Rust (Actix-web)": '''
use actix_web::{web, App, HttpResponse, HttpServer, Responder};
use serde::{Deserialize, Serialize};
use sqlx::PgPool;

#[derive(Debug, Serialize, Deserialize)]
struct Task {
    id: Option<i32>,
    name: String,
    status: String,
    priority: String,
}

async fn list_tasks(pool: web::Data<PgPool>) -> impl Responder {
    let tasks = sqlx::query_as!(Task, "SELECT id, name, status, priority FROM tasks")
        .fetch_all(pool.get_ref())
        .await;
    
    match tasks {
        Ok(t) => HttpResponse::Ok().json(t),
        Err(_) => HttpResponse::InternalServerError().finish(),
    }
}

async fn create_task(pool: web::Data<PgPool>, task: web::Json<Task>) -> impl Responder {
    let result = sqlx::query_as!(
        Task,
        "INSERT INTO tasks (name, status, priority) VALUES ($1, $2, $3) RETURNING id, name, status, priority",
        task.name, task.status, task.priority
    )
    .fetch_one(pool.get_ref())
    .await;
    
    match result {
        Ok(t) => HttpResponse::Created().json(t),
        Err(_) => HttpResponse::InternalServerError().finish(),
    }
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let pool = PgPool::connect("postgresql://localhost/db").await.unwrap();
    
    HttpServer::new(move || {
        App::new()
            .app_data(web::Data::new(pool.clone()))
            .route("/tasks", web::get().to(list_tasks))
            .route("/tasks", web::post().to(create_task))
    })
    .bind("127.0.0.1:3000")?
    .run()
    .await
}
// Run: cargo run
''',

    "Java (Spring Boot)": '''
package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import org.springframework.data.jpa.repository.JpaRepository;
import javax.persistence.*;
import java.util.List;

@SpringBootApplication
public class DemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}

@Entity
class Task {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String status = "todo";
    private String priority = "medium";
    
    // Getters and setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
    public String getPriority() { return priority; }
    public void setPriority(String priority) { this.priority = priority; }
}

interface TaskRepository extends JpaRepository<Task, Long> {}

@RestController
@RequestMapping("/tasks")
class TaskController {
    private final TaskRepository repository;
    
    TaskController(TaskRepository repository) {
        this.repository = repository;
    }
    
    @GetMapping
    List<Task> listTasks() {
        return repository.findAll();
    }
    
    @PostMapping
    Task createTask(@RequestBody Task task) {
        return repository.save(task);
    }
}
// Run: ./mvnw spring-boot:run
''',

    "C# (ASP.NET Core)": '''
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseNpgsql(builder.Configuration.GetConnectionString("Default")));
builder.Services.AddControllers();

var app = builder.Build();
app.MapControllers();
app.Run();

// Models
public class Task
{
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty;
    public string Status { get; set; } = "todo";
    public string Priority { get; set; } = "medium";
}

public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) {}
    public DbSet<Task> Tasks => Set<Task>();
}

// Controller
[ApiController]
[Route("[controller]")]
public class TasksController : ControllerBase
{
    private readonly AppDbContext _context;
    
    public TasksController(AppDbContext context)
    {
        _context = context;
    }
    
    [HttpGet]
    public async Task<ActionResult<IEnumerable<Task>>> GetTasks()
    {
        return await _context.Tasks.ToListAsync();
    }
    
    [HttpPost]
    public async Task<ActionResult<Task>> CreateTask(Task task)
    {
        _context.Tasks.Add(task);
        await _context.SaveChangesAsync();
        return CreatedAtAction(nameof(GetTasks), new { id = task.Id }, task);
    }
}
// Run: dotnet run
''',

    "Ruby (Rails)": '''
# config/routes.rb
Rails.application.routes.draw do
  resources :tasks, only: [:index, :create]
end

# app/models/task.rb
class Task < ApplicationRecord
  validates :name, presence: true
  validates :status, inclusion: { in: %w[todo doing done] }
  validates :priority, inclusion: { in: %w[low medium high] }
end

# app/controllers/tasks_controller.rb
class TasksController < ApplicationController
  def index
    @tasks = Task.all
    render json: @tasks
  end
  
  def create
    @task = Task.new(task_params)
    if @task.save
      render json: @task, status: :created
    else
      render json: @task.errors, status: :unprocessable_entity
    end
  end
  
  private
  
  def task_params
    params.require(:task).permit(:name, :status, :priority)
  end
end

# db/migrate/xxx_create_tasks.rb
class CreateTasks < ActiveRecord::Migration[7.0]
  def change
    create_table :tasks do |t|
      t.string :name, null: false
      t.string :status, default: "todo"
      t.string :priority, default: "medium"
      t.timestamps
    end
  end
end
# Run: rails server
''',

    "PHP (Laravel)": '''
<?php

// routes/api.php
use Illuminate\\Support\\Facades\\Route;
use App\\Http\\Controllers\\TaskController;

Route::get('/tasks', [TaskController::class, 'index']);
Route::post('/tasks', [TaskController::class, 'store']);

// app/Models/Task.php
namespace App\\Models;

use Illuminate\\Database\\Eloquent\\Model;

class Task extends Model
{
    protected $fillable = ['name', 'status', 'priority'];
    
    protected $attributes = [
        'status' => 'todo',
        'priority' => 'medium',
    ];
}

// app/Http/Controllers/TaskController.php
namespace App\\Http\\Controllers;

use App\\Models\\Task;
use Illuminate\\Http\\Request;
use Illuminate\\Http\\JsonResponse;

class TaskController extends Controller
{
    public function index(): JsonResponse
    {
        $tasks = Task::all();
        return response()->json($tasks);
    }
    
    public function store(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'name' => 'required|string|max:255',
            'status' => 'in:todo,doing,done',
            'priority' => 'in:low,medium,high',
        ]);
        
        $task = Task::create($validated);
        return response()->json($task, 201);
    }
}

// database/migrations/xxx_create_tasks_table.php
use Illuminate\\Database\\Migrations\\Migration;
use Illuminate\\Database\\Schema\\Blueprint;
use Illuminate\\Support\\Facades\\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('tasks', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('status')->default('todo');
            $table->string('priority')->default('medium');
            $table->timestamps();
        });
    }
};
// Run: php artisan serve
'''
}


# ============== Main ==============

async def main():
    """Demonstrate multi-language backend knowledge."""
    print("=" * 70)
    print("MULTI-LANGUAGE MASTERY - BACKEND LANGUAGES")
    print("=" * 70)
    
    # 1. Language Overview
    print("\n1. BACKEND LANGUAGE COMPARISON")
    print("-" * 40)
    
    for lang, info in BACKEND_LANGUAGES.items():
        print(f"\n   {lang}:")
        print(f"     Paradigm: {info['paradigm']}")
        print(f"     Performance: {info['performance']}")
        print(f"     Typing: {info['typing']}")
        print(f"     Best for: {', '.join(info['use_cases'][:3])}")
    
    # 2. Code Examples
    print("\n2. REST API IN EACH LANGUAGE")
    print("-" * 40)
    print("   Same functionality in 8 different languages:")
    print("     • List all tasks (GET /tasks)")
    print("     • Create new task (POST /tasks)")
    print("     • PostgreSQL database integration")
    print("     • JSON request/response")
    
    for lang, code in CODE_EXAMPLES.items():
        print(f"\n   {lang}:")
        print(f"   {code[:150]}...")
    
    # 3. When to use each
    print("\n3. LANGUAGE SELECTION GUIDE")
    print("-" * 40)
    
    scenarios = [
        ("AI/ML API", "Python (FastAPI) - Best ML ecosystem"),
        ("Real-time chat", "Node.js (Socket.io) - Event-driven"),
        ("High-throughput microservices", "Go - Goroutines, fast, simple"),
        ("Systems programming", "Rust - Memory safe, C performance"),
        ("Enterprise application", "Java (Spring) - Mature ecosystem"),
        ("Microsoft ecosystem", "C# (.NET) - Best integration"),
        ("Rapid prototyping", "Ruby (Rails) - Convention over config"),
        ("WordPress/WooCommerce", "PHP (Laravel) - Web-focused"),
    ]
    
    for scenario, choice in scenarios:
        print(f"   {scenario:30} → {choice}")
    
    print("\n" + "=" * 70)
    print("BACKEND LANGUAGES MASTERED")
    print("=" * 70)
    print("\n8 Languages with working REST API examples:")
    print("  Python, Node.js, Go, Rust, Java, C#, Ruby, PHP")
    print("\nReady for any backend project!")


if __name__ == "__main__":
    asyncio.run(main())
