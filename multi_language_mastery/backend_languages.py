#!/usr/bin/env python3
"""
Multi-Language Programming Mastery
Go, Rust, Node.js/TypeScript, Java - Backend Expertise
"""

import asyncio
from typing import Dict, List


# ============== Go (Golang) ==============

GO_EXAMPLES = """
// Go - Systems programming, microservices, high performance

// ============================================
// Basic Structure
// ============================================

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "log"
    "net/http"
    "time"
    
    "github.com/gin-gonic/gin"
    "github.com/jackc/pgx/v5/pgxpool"
)

// Task model
type Task struct {
    ID          string    `json:"id"`
    Name        string    `json:"name"`
    Status      string    `json:"status"`
    Priority    string    `json:"priority"`
    CreatedAt   time.Time `json:"created_at"`
}

// TaskRepository interface
type TaskRepository interface {
    Create(ctx context.Context, task *Task) error
    GetByID(ctx context.Context, id string) (*Task, error)
    List(ctx context.Context, status string) ([]Task, error)
    Update(ctx context.Context, task *Task) error
    Delete(ctx context.Context, id string) error
}

// Postgres implementation
type PostgresTaskRepository struct {
    db *pgxpool.Pool
}

func NewPostgresTaskRepository(db *pgxpool.Pool) *PostgresTaskRepository {
    return &PostgresTaskRepository{db: db}
}

func (r *PostgresTaskRepository) Create(ctx context.Context, task *Task) error {
    query := `
        INSERT INTO tasks (id, name, status, priority, created_at)
        VALUES ($1, $2, $3, $4, $5)
    `
    _, err := r.db.Exec(ctx, query, task.ID, task.Name, task.Status, task.Priority, task.CreatedAt)
    return err
}

func (r *PostgresTaskRepository) GetByID(ctx context.Context, id string) (*Task, error) {
    query := `SELECT id, name, status, priority, created_at FROM tasks WHERE id = $1`
    
    task := &Task{}
    err := r.db.QueryRow(ctx, query, id).Scan(
        &task.ID, &task.Name, &task.Status, &task.Priority, &task.CreatedAt,
    )
    if err != nil {
        return nil, err
    }
    return task, nil
}

// ============================================
// HTTP Server with Gin
// ============================================

type TaskHandler struct {
    repo TaskRepository
}

func NewTaskHandler(repo TaskRepository) *TaskHandler {
    return &TaskHandler{repo: repo}
}

func (h *TaskHandler) CreateTask(c *gin.Context) {
    var task Task
    if err := c.ShouldBindJSON(&task); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    
    task.ID = generateID()
    task.CreatedAt = time.Now()
    task.Status = "todo"
    
    ctx, cancel := context.WithTimeout(c.Request.Context(), 5*time.Second)
    defer cancel()
    
    if err := h.repo.Create(ctx, &task); err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
        return
    }
    
    c.JSON(http.StatusCreated, task)
}

func (h *TaskHandler) GetTask(c *gin.Context) {
    id := c.Param("id")
    
    ctx, cancel := context.WithTimeout(c.Request.Context(), 5*time.Second)
    defer cancel()
    
    task, err := h.repo.GetByID(ctx, id)
    if err != nil {
        c.JSON(http.StatusNotFound, gin.H{"error": "Task not found"})
        return
    }
    
    c.JSON(http.StatusOK, task)
}

// ============================================
// Goroutines and Channels (Concurrency)
// ============================================

// Worker pool pattern
func workerPool(jobs <-chan Task, results chan<- error, workerID int) {
    for job := range jobs {
        fmt.Printf("Worker %d processing task %s\\n", workerID, job.ID)
        // Process task
        time.Sleep(100 * time.Millisecond)
        results <- nil
    }
}

func processTasksConcurrently(tasks []Task, numWorkers int) {
    jobs := make(chan Task, len(tasks))
    results := make(chan error, len(tasks))
    
    // Start workers
    for w := 1; w <= numWorkers; w++ {
        go workerPool(jobs, results, w)
    }
    
    // Send jobs
    for _, task := range tasks {
        jobs <- task
    }
    close(jobs)
    
    // Collect results
    for i := 0; i < len(tasks); i++ {
        <-results
    }
}

// ============================================
// Graceful Shutdown
// ============================================

func main() {
    // Database connection
    dbpool, err := pgxpool.New(context.Background(), "postgres://user:pass@localhost/mydb")
    if err != nil {
        log.Fatal(err)
    }
    defer dbpool.Close()
    
    // Repository and handler
    repo := NewPostgresTaskRepository(dbpool)
    handler := NewTaskHandler(repo)
    
    // Router
    r := gin.Default()
    
    // Routes
    r.GET("/health", func(c *gin.Context) {
        c.JSON(http.StatusOK, gin.H{"status": "healthy"})
    })
    
    api := r.Group("/api/v1")
    {
        api.POST("/tasks", handler.CreateTask)
        api.GET("/tasks/:id", handler.GetTask)
    }
    
    // Start server with graceful shutdown
    srv := &http.Server{
        Addr:    ":8080",
        Handler: r,
    }
    
    go func() {
        if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
            log.Fatalf("Server error: %v", err)
        }
    }()
    
    // Wait for interrupt signal
    quit := make(chan os.Signal, 1)
    signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
    <-quit
    
    log.Println("Shutting down server...")
    
    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()
    
    if err := srv.Shutdown(ctx); err != nil {
        log.Fatal("Server forced to shutdown:", err)
    }
    
    log.Println("Server exited")
}
"""


# ============== Rust ==============

RUST_EXAMPLES = """
// Rust - Systems programming, safety, performance

// ============================================
// Basic Structure
// ============================================

use std::collections::HashMap;
use std::sync::Arc;
use tokio::sync::RwLock;
use serde::{Deserialize, Serialize};
use actix_web::{web, App, HttpResponse, HttpServer, Responder};
use sqlx::PgPool;

// ============================================
// Data Models
// ============================================

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Task {
    pub id: String,
    pub name: String,
    pub status: TaskStatus,
    pub priority: Priority,
    pub created_at: chrono::DateTime<chrono::Utc>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "lowercase")]
pub enum TaskStatus {
    Todo,
    Doing,
    Done,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "lowercase")]
pub enum Priority {
    Low,
    Medium,
    High,
}

// ============================================
// Repository Pattern
// ============================================

#[derive(Clone)]
pub struct TaskRepository {
    db: PgPool,
}

impl TaskRepository {
    pub fn new(db: PgPool) -> Self {
        Self { db }
    }
    
    pub async fn create(&self, task: &Task) -> Result<(), sqlx::Error> {
        sqlx::query(
            "INSERT INTO tasks (id, name, status, priority, created_at)
             VALUES ($1, $2, $3, $4, $5)"
        )
        .bind(&task.id)
        .bind(&task.name)
        .bind(&task.status)
        .bind(&task.priority)
        .bind(&task.created_at)
        .execute(&self.db)
        .await?;
        
        Ok(())
    }
    
    pub async fn find_by_id(&self, id: &str) -> Result<Option<Task>, sqlx::Error> {
        let task = sqlx::query_as::<_, Task>(
            "SELECT id, name, status, priority, created_at FROM tasks WHERE id = $1"
        )
        .bind(id)
        .fetch_optional(&self.db)
        .await?;
        
        Ok(task)
    }
    
    pub async fn list_by_status(&self, status: &TaskStatus) -> Result<Vec<Task>, sqlx::Error> {
        let tasks = sqlx::query_as::<_, Task>(
            "SELECT id, name, status, priority, created_at 
             FROM tasks WHERE status = $1
             ORDER BY created_at DESC"
        )
        .bind(status)
        .fetch_all(&self.db)
        .await?;
        
        Ok(tasks)
    }
}

// ============================================
// HTTP Handlers (Actix-web)
// ============================================

pub async fn create_task(
    repo: web::Data<TaskRepository>,
    body: web::Json<CreateTaskRequest>,
) -> impl Responder {
    let task = Task {
        id: uuid::Uuid::new_v4().to_string(),
        name: body.name.clone(),
        status: TaskStatus::Todo,
        priority: body.priority.clone(),
        created_at: chrono::Utc::now(),
    };
    
    match repo.create(&task).await {
        Ok(_) => HttpResponse::Created().json(task),
        Err(e) => HttpResponse::InternalServerError().json(json!({
            "error": e.to_string()
        })),
    }
}

pub async fn get_task(
    repo: web::Data<TaskRepository>,
    path: web::Path<String>,
) -> impl Responder {
    let id = path.into_inner();
    
    match repo.find_by_id(&id).await {
        Ok(Some(task)) => HttpResponse::Ok().json(task),
        Ok(None) => HttpResponse::NotFound().json(json!({"error": "Task not found"})),
        Err(e) => HttpResponse::InternalServerError().json(json!({
            "error": e.to_string()
        })),
    }
}

#[derive(Deserialize)]
pub struct CreateTaskRequest {
    name: String,
    priority: Priority,
}

// ============================================
// Main Application
// ============================================

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    // Load configuration
    let database_url = std::env::var("DATABASE_URL")
        .expect("DATABASE_URL must be set");
    
    // Create connection pool
    let pool = PgPool::connect(&database_url)
        .await
        .expect("Failed to create pool");
    
    // Run migrations
    sqlx::migrate!("./migrations")
        .run(&pool)
        .await
        .expect("Failed to run migrations");
    
    let repo = TaskRepository::new(pool);
    let repo_data = web::Data::new(repo);
    
    println!("Starting server on port 8080");
    
    HttpServer::new(move || {
        App::new()
            .app_data(repo_data.clone())
            .route("/health", web::get().to(health_check))
            .service(
                web::scope("/api/v1")
                    .route("/tasks", web::post().to(create_task))
                    .route("/tasks/{id}", web::get().to(get_task))
            )
    })
    .bind("0.0.0.0:8080")?
    .run()
    .await
}

async fn health_check() -> impl Responder {
    HttpResponse::Ok().json(json!({"status": "healthy"}))
}

// ============================================
// Concurrency with Tokio
// ============================================

use tokio::task;
use tokio::sync::mpsc;

async fn process_tasks_parallel(tasks: Vec<Task>) -> Vec<Result<(), Error>> {
    let mut handles = vec![];
    
    for task in tasks {
        let handle = task::spawn(async move {
            // Process task asynchronously
            process_task(task).await
        });
        handles.push(handle);
    }
    
    let mut results = vec![];
    for handle in handles {
        results.push(handle.await.unwrap());
    }
    
    results
}

// Channel-based worker pool
async fn worker_pool_example() {
    let (tx, mut rx) = mpsc::channel::<Task>(100);
    
    // Spawn workers
    let worker_handles: Vec<_> = (0..4)
        .map(|id| {
            let rx = rx.clone();
            task::spawn(async move {
                worker(id, rx).await;
            })
        })
        .collect();
    
    // Send tasks
    for i in 0..20 {
        let task = Task {
            id: format!("task-{}", i),
            name: format!("Task {}", i),
            status: TaskStatus::Todo,
            priority: Priority::Medium,
            created_at: chrono::Utc::now(),
        };
        tx.send(task).await.unwrap();
    }
    
    drop(tx); // Close channel
    
    // Wait for workers
    for handle in worker_handles {
        handle.await.unwrap();
    }
}

async fn worker(id: usize, mut rx: mpsc::Receiver<Task>) {
    while let Some(task) = rx.recv().await {
        println!("Worker {} processing {}", id, task.id);
        // Process task
        tokio::time::sleep(tokio::time::Duration::from_millis(100)).await;
    }
}
"""


# ============== Node.js/TypeScript ==============

NODEJS_EXAMPLES = """
// Node.js with TypeScript - Enterprise backend development

// ============================================
// Project Structure
// ============================================
/*
src/
  config/         # Configuration management
  controllers/    # HTTP request handlers
  services/       # Business logic
  repositories/   # Data access layer
  models/         # Domain models/interfaces
  middleware/     # Express middleware
  utils/          # Helper functions
  types/          # TypeScript type definitions
  app.ts          # Application setup
  server.ts       # Server entry point
tests/
  unit/
  integration/
*/

// ============================================
// Domain Models
// ============================================

// src/types/task.ts
export enum TaskStatus {
  TODO = 'todo',
  DOING = 'doing',
  DONE = 'done'
}

export enum Priority {
  LOW = 'low',
  MEDIUM = 'medium',
  HIGH = 'high'
}

export interface Task {
  id: string;
  name: string;
  description?: string;
  status: TaskStatus;
  priority: Priority;
  userId: string;
  dueDate?: Date;
  createdAt: Date;
  updatedAt?: Date;
}

export interface CreateTaskDTO {
  name: string;
  description?: string;
  priority: Priority;
  dueDate?: Date;
}

// ============================================
// Repository Pattern with Prisma
// ============================================

// src/repositories/task.repository.ts
import { PrismaClient, Task as PrismaTask } from '@prisma/client';
import { Task, CreateTaskDTO, TaskStatus } from '../types/task';

export interface ITaskRepository {
  create(data: CreateTaskDTO, userId: string): Promise<Task>;
  findById(id: string): Promise<Task | null>;
  findByUserId(userId: string, filters?: TaskFilters): Promise<Task[]>;
  update(id: string, data: Partial<Task>): Promise<Task>;
  delete(id: string): Promise<void>;
}

export interface TaskFilters {
  status?: TaskStatus;
  priority?: Priority;
  dueBefore?: Date;
  dueAfter?: Date;
}

export class TaskRepository implements ITaskRepository {
  constructor(private prisma: PrismaClient) {}

  async create(data: CreateTaskDTO, userId: string): Promise<Task> {
    const task = await this.prisma.task.create({
      data: {
        ...data,
        userId,
        status: TaskStatus.TODO,
      },
    });
    return this.mapToDomain(task);
  }

  async findById(id: string): Promise<Task | null> {
    const task = await this.prisma.task.findUnique({
      where: { id },
    });
    return task ? this.mapToDomain(task) : null;
  }

  async findByUserId(userId: string, filters?: TaskFilters): Promise<Task[]> {
    const where: any = { userId };
    
    if (filters?.status) where.status = filters.status;
    if (filters?.priority) where.priority = filters.priority;
    if (filters?.dueBefore || filters?.dueAfter) {
      where.dueDate = {};
      if (filters.dueBefore) where.dueDate.lte = filters.dueBefore;
      if (filters.dueAfter) where.dueDate.gte = filters.dueAfter;
    }

    const tasks = await this.prisma.task.findMany({
      where,
      orderBy: [
        { priority: 'desc' },
        { createdAt: 'desc' },
      ],
    });
    
    return tasks.map(this.mapToDomain);
  }

  async update(id: string, data: Partial<Task>): Promise<Task> {
    const task = await this.prisma.task.update({
      where: { id },
      data: {
        ...data,
        updatedAt: new Date(),
      },
    });
    return this.mapToDomain(task);
  }

  async delete(id: string): Promise<void> {
    await this.prisma.task.delete({
      where: { id },
    });
  }

  private mapToDomain(prismaTask: PrismaTask): Task {
    return {
      id: prismaTask.id,
      name: prismaTask.name,
      description: prismaTask.description ?? undefined,
      status: prismaTask.status as TaskStatus,
      priority: prismaTask.priority as Priority,
      userId: prismaTask.userId,
      dueDate: prismaTask.dueDate ?? undefined,
      createdAt: prismaTask.createdAt,
      updatedAt: prismaTask.updatedAt ?? undefined,
    };
  }
}

// ============================================
// Service Layer
// ============================================

// src/services/task.service.ts
import { ITaskRepository } from '../repositories/task.repository';
import { Task, CreateTaskDTO, TaskStatus } from '../types/task';
import { EventEmitter } from 'events';

export class TaskService {
  private events = new EventEmitter();

  constructor(private taskRepo: ITaskRepository) {}

  async createTask(userId: string, data: CreateTaskDTO): Promise<Task> {
    // Validate business rules
    if (data.dueDate && data.dueDate < new Date()) {
      throw new Error('Due date cannot be in the past');
    }

    const task = await this.taskRepo.create(data, userId);
    
    // Emit event for side effects
    this.events.emit('task:created', { task, userId });
    
    return task;
  }

  async completeTask(taskId: string, userId: string): Promise<Task> {
    const task = await this.taskRepo.findById(taskId);
    
    if (!task) {
      throw new Error('Task not found');
    }
    
    if (task.userId !== userId) {
      throw new Error('Not authorized to complete this task');
    }

    const updated = await this.taskRepo.update(taskId, {
      status: TaskStatus.DONE,
    });

    this.events.emit('task:completed', { task: updated, userId });
    
    return updated;
  }

  onTaskCreated(handler: (data: { task: Task; userId: string }) => void): void {
    this.events.on('task:created', handler);
  }
}

// ============================================
// Express Controllers
// ============================================

// src/controllers/task.controller.ts
import { Request, Response, NextFunction } from 'express';
import { TaskService } from '../services/task.service';
import { CreateTaskDTO } from '../types/task';

export class TaskController {
  constructor(private taskService: TaskService) {}

  create = async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    try {
      const userId = req.user!.id; // From auth middleware
      const taskData: CreateTaskDTO = req.body;
      
      const task = await this.taskService.createTask(userId, taskData);
      
      res.status(201).json({
        success: true,
        data: task,
      });
    } catch (error) {
      next(error);
    }
  };

  getById = async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    try {
      const { id } = req.params;
      const userId = req.user!.id;
      
      // Implementation...
      
      res.json({
        success: true,
        data: { id },
      });
    } catch (error) {
      next(error);
    }
  };
}

// ============================================
// Express App Setup
// ============================================

// src/app.ts
import express from 'express';
import cors from 'cors';
import helmet from 'helmet';
import compression from 'compression';
import { PrismaClient } from '@prisma/client';

import { TaskRepository } from './repositories/task.repository';
import { TaskService } from './services/task.service';
import { TaskController } from './controllers/task.controller';
import { errorHandler } from './middleware/error.handler';
import { authMiddleware } from './middleware/auth.middleware';

export function createApp(): express.Application {
  const app = express();
  
  // Middleware
  app.use(helmet());
  app.use(cors({
    origin: process.env.FRONTEND_URL || 'http://localhost:3000',
    credentials: true,
  }));
  app.use(compression());
  app.use(express.json());
  app.use(express.urlencoded({ extended: true }));
  
  // Database
  const prisma = new PrismaClient();
  
  // Dependency injection
  const taskRepo = new TaskRepository(prisma);
  const taskService = new TaskService(taskRepo);
  const taskController = new TaskController(taskService);
  
  // Routes
  app.get('/health', (req, res) => {
    res.json({ status: 'healthy', timestamp: new Date().toISOString() });
  });
  
  app.use('/api/v1/tasks', authMiddleware, createTaskRouter(taskController));
  
  // Error handling
  app.use(errorHandler);
  
  return app;
}

// ============================================
// Server Entry
// ============================================

// src/server.ts
import { createApp } from './app';

const PORT = process.env.PORT || 3000;

const app = createApp();

const server = app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Graceful shutdown
process.on('SIGTERM', () => {
  console.log('SIGTERM received, shutting down gracefully');
  server.close(() => {
    console.log('Server closed');
    process.exit(0);
  });
});
"""


# ============== Main ==============

async def main():
    """Demonstrate multi-language backend expertise."""
    print("=" * 70)
    print("MULTI-LANGUAGE BACKEND MASTERY")
    print("=" * 70)
    
    languages = {
        "Go": {
            "strengths": ["High performance", "Easy concurrency", "Fast compilation", "Static binaries"],
            "best_for": ["Microservices", "Cloud-native apps", "CLI tools", "High-throughput APIs"],
            "frameworks": ["Gin", "Echo", "Fiber", "Standard library"],
            "paradigm": "Procedural with OOP features"
        },
        "Rust": {
            "strengths": ["Memory safety", "Zero-cost abstractions", "Fearless concurrency", "Performance"],
            "best_for": ["Systems programming", "WebAssembly", "High-performance services", "Security-critical apps"],
            "frameworks": ["Actix-web", "Axum", "Rocket", "Tide"],
            "paradigm": "Multi-paradigm (functional, OOP, procedural)"
        },
        "Node.js/TypeScript": {
            "strengths": ["Same language as frontend", "Massive ecosystem", "Async I/O", "Fast development"],
            "best_for": ["Real-time apps", "APIs", "Microservices", "Serverless"],
            "frameworks": ["Express", "NestJS", "Fastify", "Koa"],
            "paradigm": "Event-driven, async/await"
        }
    }
    
    for lang, info in languages.items():
        print(f"\n{lang.upper()}")
        print("-" * 40)
        print(f"  Strengths: {', '.join(info['strengths'][:2])}")
        print(f"  Best for: {', '.join(info['best_for'][:2])}")
        print(f"  Frameworks: {', '.join(info['frameworks'][:2])}")
    
    print("\n" + "=" * 70)
    print("CONCEPTS DEMONSTRATED:")
    print("=" * 70)
    concepts = [
        "Go: Goroutines and Channels",
        "Go: Gin HTTP framework",
        "Go: PostgreSQL with pgx",
        "Go: Graceful shutdown",
        "Rust: Ownership and Borrowing",
        "Rust: Actix-web framework",
        "Rust: SQLx for type-safe SQL",
        "Rust: Async/await with Tokio",
        "Node.js: TypeScript types",
        "Node.js: Prisma ORM",
        "Node.js: Repository pattern",
        "Node.js: Express with DI",
        "All: Clean architecture",
        "All: Repository pattern",
        "All: Service layer"
    ]
    for i, concept in enumerate(concepts, 1):
        print(f"  {i:2}. {concept}")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    asyncio.run(main())
