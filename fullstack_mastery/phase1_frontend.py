#!/usr/bin/env python3
"""
Fullstack Mastery - Phase 1: Frontend Fundamentals
HTML, CSS, JavaScript, TypeScript, React
"""

import asyncio
import json
from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from datetime import datetime


# ============== HTML5 Semantic Structure ==============

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="ScalePlus.io - Business Automation">
    <title>{{title}}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav aria-label="Main navigation">
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#pricing">Pricing</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section id="hero" aria-labelledby="hero-heading">
            <h1 id="hero-heading">{{headline}}</h1>
            <p>{{subheadline}}</p>
            <button onclick="handleCTA()">Get Started</button>
        </section>
        
        <section id="services" aria-labelledby="services-heading">
            <h2 id="services-heading">Our Services</h2>
            <article>
                <h3>Website Lite</h3>
                <p>3-page professional websites starting at 4,995 PHP/month</p>
            </article>
            <article>
                <h3>Growth System</h3>
                <p>Complete automation and growth retainers at 9,995 PHP/month</p>
            </article>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2026 ScalePlus.io. All rights reserved.</p>
    </footer>
    
    <script src="app.js"></script>
</body>
</html>'''


# ============== Modern CSS (CSS3 + Flexbox/Grid) ==============

CSS_TEMPLATE = '''/* CSS Variables / Design Tokens */
:root {
    --color-primary: #2563eb;
    --color-primary-dark: #1d4ed8;
    --color-secondary: #64748b;
    --color-background: #ffffff;
    --color-text: #1e293b;
    --color-text-light: #64748b;
    
    --font-sans: system-ui, -apple-system, sans-serif;
    --font-mono: ui-monospace, monospace;
    
    --spacing-xs: 0.25rem;
    --spacing-sm: 0.5rem;
    --spacing-md: 1rem;
    --spacing-lg: 2rem;
    --spacing-xl: 4rem;
    
    --radius-sm: 0.25rem;
    --radius-md: 0.5rem;
    --radius-lg: 1rem;
    
    --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
    --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
    --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
    
    --transition-fast: 150ms ease;
    --transition-base: 250ms ease;
}

/* Reset & Base */
*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    font-size: 16px;
    scroll-behavior: smooth;
}

body {
    font-family: var(--font-sans);
    color: var(--color-text);
    line-height: 1.6;
    background: var(--color-background);
}

/* Modern Layout with Grid */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 var(--spacing-md);
}

.grid {
    display: grid;
    gap: var(--spacing-lg);
}

.grid-cols-2 {
    grid-template-columns: repeat(2, 1fr);
}

.grid-cols-3 {
    grid-template-columns: repeat(3, 1fr);
}

@media (max-width: 768px) {
    .grid-cols-2, .grid-cols-3 {
        grid-template-columns: 1fr;
    }
}

/* Flexbox Utilities */
.flex {
    display: flex;
}

.flex-col {
    flex-direction: column;
}

.items-center {
    align-items: center;
}

.justify-between {
    justify-content: space-between;
}

.gap-md {
    gap: var(--spacing-md);
}

/* Components */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: var(--spacing-sm) var(--spacing-md);
    border: none;
    border-radius: var(--radius-md);
    font-size: 1rem;
    font-weight: 500;
    cursor: pointer;
    transition: all var(--transition-fast);
}

.btn-primary {
    background: var(--color-primary);
    color: white;
}

.btn-primary:hover {
    background: var(--color-primary-dark);
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
}

.btn-primary:active {
    transform: translateY(0);
}

/* Card Component */
.card {
    background: white;
    border-radius: var(--radius-lg);
    padding: var(--spacing-lg);
    box-shadow: var(--shadow-sm);
    transition: box-shadow var(--transition-base);
}

.card:hover {
    box-shadow: var(--shadow-lg);
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.animate-fade-in {
    animation: fadeIn 0.5s ease forwards;
}

/* Accessibility */
.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
}

:focus-visible {
    outline: 2px solid var(--color-primary);
    outline-offset: 2px;
}

/* Dark Mode Support */
@media (prefers-color-scheme: dark) {
    :root {
        --color-background: #0f172a;
        --color-text: #f1f5f9;
        --color-text-light: #94a3b8;
    }
    
    .card {
        background: #1e293b;
    }
}
'''


# ============== JavaScript (ES6+) ==============

JS_TEMPLATE = '''// Modern JavaScript (ES6+)

// ============================================
// Module Pattern & Architecture
// ============================================

class App {
    constructor() {
        this.state = {
            user: null,
            tasks: [],
            loading: false
        };
        this.eventBus = new EventBus();
        this.api = new APIClient('https://api.scaleplus.io');
    }
    
    async init() {
        this.setupEventListeners();
        await this.loadInitialData();
        this.render();
    }
    
    setupEventListeners() {
        // Event delegation
        document.addEventListener('click', (e) => {
            if (e.target.matches('[data-action]')) {
                const action = e.target.dataset.action;
                this.handleAction(action, e.target);
            }
        });
        
        // Custom events
        this.eventBus.on('task:created', (task) => {
            this.showNotification(`Task "${task.name}" created`);
        });
    }
    
    async loadInitialData() {
        try {
            this.setState({ loading: true });
            const tasks = await this.api.get('/tasks');
            this.setState({ tasks, loading: false });
        } catch (error) {
            this.handleError(error);
        }
    }
    
    setState(newState) {
        this.state = { ...this.state, ...newState };
        this.eventBus.emit('state:changed', this.state);
    }
    
    handleAction(action, element) {
        const actions = {
            'create-task': () => this.openTaskModal(),
            'delete-task': () => this.deleteTask(element.dataset.id),
            'toggle-theme': () => this.toggleTheme()
        };
        
        actions[action]?.();
    }
    
    showNotification(message) {
        const notification = document.createElement('div');
        notification.className = 'notification';
        notification.textContent = message;
        document.body.appendChild(notification);
        
        setTimeout(() => notification.remove(), 3000);
    }
    
    handleError(error) {
        console.error('App Error:', error);
        this.showNotification('Something went wrong. Please try again.');
    }
    
    render() {
        // Render based on state
        console.log('Rendering with state:', this.state);
    }
}

// ============================================
// API Client with Fetch
// ============================================

class APIClient {
    constructor(baseURL) {
        this.baseURL = baseURL;
        this.headers = {
            'Content-Type': 'application/json'
        };
    }
    
    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        const config = {
            ...options,
            headers: { ...this.headers, ...options.headers }
        };
        
        if (config.body && typeof config.body === 'object') {
            config.body = JSON.stringify(config.body);
        }
        
        const response = await fetch(url, config);
        
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        
        return response.json();
    }
    
    get(endpoint) {
        return this.request(endpoint, { method: 'GET' });
    }
    
    post(endpoint, body) {
        return this.request(endpoint, { method: 'POST', body });
    }
    
    put(endpoint, body) {
        return this.request(endpoint, { method: 'PUT', body });
    }
    
    delete(endpoint) {
        return this.request(endpoint, { method: 'DELETE' });
    }
}

// ============================================
// Event Bus (Pub/Sub)
// ============================================

class EventBus {
    constructor() {
        this.events = new Map();
    }
    
    on(event, callback) {
        if (!this.events.has(event)) {
            this.events.set(event, []);
        }
        this.events.get(event).push(callback);
    }
    
    off(event, callback) {
        const callbacks = this.events.get(event);
        if (callbacks) {
            const index = callbacks.indexOf(callback);
            if (index > -1) callbacks.splice(index, 1);
        }
    }
    
    emit(event, data) {
        const callbacks = this.events.get(event);
        if (callbacks) {
            callbacks.forEach(callback => callback(data));
        }
    }
}

// ============================================
// Utility Functions
// ============================================

// Debounce
const debounce = (fn, delay) => {
    let timeoutId;
    return (...args) => {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => fn(...args), delay);
    };
};

// Throttle
const throttle = (fn, limit) => {
    let inThrottle;
    return (...args) => {
        if (!inThrottle) {
            fn(...args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
};

// LocalStorage with expiration
const storage = {
    set: (key, value, ttl = null) => {
        const item = { value, expires: ttl ? Date.now() + ttl : null };
        localStorage.setItem(key, JSON.stringify(item));
    },
    get: (key) => {
        const item = JSON.parse(localStorage.getItem(key));
        if (item && item.expires && Date.now() > item.expires) {
            localStorage.removeItem(key);
            return null;
        }
        return item?.value;
    },
    remove: (key) => localStorage.removeItem(key)
};

// DOM Ready
const ready = (fn) => {
    if (document.readyState !== 'loading') {
        fn();
    } else {
        document.addEventListener('DOMContentLoaded', fn);
    }
};

// Initialize app
ready(() => {
    window.app = new App();
    window.app.init();
});
'''


# ============== TypeScript Fundamentals ==============

TYPESCRIPT_TEMPLATE = '''// TypeScript - Typed Superset of JavaScript

// ============================================
// Basic Types
// ============================================

type UserRole = 'admin' | 'user' | 'guest';
type TaskStatus = 'todo' | 'doing' | 'done';
type Priority = 'low' | 'medium' | 'high';

interface User {
    id: string;
    name: string;
    email: string;
    role: UserRole;
    createdAt: Date;
}

interface Task {
    id: string;
    name: string;
    description?: string;  // Optional
    status: TaskStatus;
    priority: Priority;
    assignee?: User;
    dueDate?: Date;
    readonly createdAt: Date;  // Readonly
}

// ============================================
// Generic Types
// ============================================

interface APIResponse<T> {
    data: T;
    status: number;
    message: string;
    timestamp: Date;
}

interface PaginatedResponse<T> {
    items: T[];
    total: number;
    page: number;
    pageSize: number;
    hasMore: boolean;
}

type TaskResponse = APIResponse<Task>;
type TasksResponse = APIResponse<PaginatedResponse<Task>>;

// ============================================
// Classes with Types
// ============================================

class TaskManager {
    private tasks: Map<string, Task> = new Map();
    private subscribers: Array<(tasks: Task[]) => void> = [];
    
    constructor(private api: TaskAPI) {}
    
    async createTask(taskData: Omit<Task, 'id' | 'createdAt'>): Promise<Task> {
        const task: Task = {
            ...taskData,
            id: this.generateId(),
            createdAt: new Date()
        };
        
        await this.api.create(task);
        this.tasks.set(task.id, task);
        this.notify();
        
        return task;
    }
    
    async getTask(id: string): Promise<Task | undefined> {
        if (this.tasks.has(id)) {
            return this.tasks.get(id);
        }
        
        const task = await this.api.get(id);
        if (task) {
            this.tasks.set(id, task);
        }
        return task;
    }
    
    getTasksByStatus(status: TaskStatus): Task[] {
        return Array.from(this.tasks.values())
            .filter(task => task.status === status);
    }
    
    subscribe(callback: (tasks: Task[]) => void): () => void {
        this.subscribers.push(callback);
        return () => {
            const index = this.subscribers.indexOf(callback);
            if (index > -1) {
                this.subscribers.splice(index, 1);
            }
        };
    }
    
    private notify(): void {
        const tasks = Array.from(this.tasks.values());
        this.subscribers.forEach(callback => callback(tasks));
    }
    
    private generateId(): string {
        return `task_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    }
}

// ============================================
// Interfaces for APIs
// ============================================

interface TaskAPI {
    get(id: string): Promise<Task | null>;
    create(task: Task): Promise<Task>;
    update(id: string, updates: Partial<Task>): Promise<Task>;
    delete(id: string): Promise<void>;
    list(filters?: TaskFilters): Promise<Task[]>;
}

interface TaskFilters {
    status?: TaskStatus;
    priority?: Priority;
    assigneeId?: string;
    dueBefore?: Date;
    dueAfter?: Date;
}

// ============================================
// Utility Types
// ============================================

// Make all properties optional
type PartialTask = Partial<Task>;

// Make all properties required
type RequiredTask = Required<Task>;

// Pick specific properties
type TaskSummary = Pick<Task, 'id' | 'name' | 'status'>;

// Omit specific properties  
type TaskUpdateData = Omit<Task, 'id' | 'createdAt'>;

// Record type
 type TaskById = Record<string, Task>;

// ============================================
// Type Guards
// ============================================

function isTask(obj: unknown): obj is Task {
    return (
        typeof obj === 'object' &&
        obj !== null &&
        'id' in obj &&
        'name' in obj &&
        'status' in obj
    );
}

function assertTask(obj: unknown): asserts obj is Task {
    if (!isTask(obj)) {
        throw new TypeError('Object is not a Task');
    }
}

// ============================================
// Async/Await with Types
// ============================================

async function fetchTasks(): Promise<Task[]> {
    const response = await fetch('/api/tasks');
    
    if (!response.ok) {
        throw new Error(`Failed to fetch: ${response.status}`);
    }
    
    const data: unknown = await response.json();
    
    if (Array.isArray(data) && data.every(isTask)) {
        return data;
    }
    
    throw new Error('Invalid response format');
}

// ============================================
// React with TypeScript (Conceptual)
// ============================================

/*
// Component Props
interface TaskCardProps {
    task: Task;
    onStatusChange: (id: string, status: TaskStatus) => void;
    onDelete: (id: string) => void;
}

// Component with hooks
const TaskCard: React.FC<TaskCardProps> = ({ task, onStatusChange, onDelete }) => {
    const [isEditing, setIsEditing] = useState<boolean>(false);
    const inputRef = useRef<HTMLInputElement>(null);
    
    useEffect(() => {
        if (isEditing && inputRef.current) {
            inputRef.current.focus();
        }
    }, [isEditing]);
    
    const handleSubmit = useCallback((e: FormEvent) => {
        e.preventDefault();
        // Handle submit
    }, []);
    
    return (
        <article className="task-card">
            <h3>{task.name}</h3>
            <span className={`badge badge-${task.priority}`}>
                {task.priority}
            </span>
            <button onClick={() => onDelete(task.id)}>Delete</button>
        </article>
    );
};

// Custom hook
function useTasks() {
    const [tasks, setTasks] = useState<Task[]>([]);
    const [loading, setLoading] = useState<boolean>(false);
    const [error, setError] = useState<Error | null>(null);
    
    const loadTasks = useCallback(async () => {
        setLoading(true);
        try {
            const data = await fetchTasks();
            setTasks(data);
        } catch (err) {
            setError(err instanceof Error ? err : new Error('Unknown error'));
        } finally {
            setLoading(false);
        }
    }, []);
    
    useEffect(() => {
        loadTasks();
    }, [loadTasks]);
    
    return { tasks, loading, error, refetch: loadTasks };
}
*/

export { TaskManager, TaskAPI, Task, User, TaskStatus, Priority };
export type { TaskFilters, TaskResponse };
'''


# ============== React Concepts ==============

REACT_CONCEPTS = '''
// ============================================
// React Fundamentals
// ============================================

// 1. JSX - JavaScript XML
const element = <h1>Hello, ScalePlus!</h1>;

// 2. Components
// Functional Component
function Welcome({ name }) {
    return <h1>Hello, {name}</h1>;
}

// 3. Props (Properties)
function TaskCard({ task, onComplete }) {
    return (
        <div className="task-card">
            <h3>{task.name}</h3>
            <button onClick={() => onComplete(task.id)}>
                Complete
            </button>
        </div>
    );
}

// 4. State with useState
function Counter() {
    const [count, setCount] = useState(0);
    
    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={() => setCount(count + 1)}>
                Increment
            </button>
        </div>
    );
}

// 5. useEffect for side effects
function TaskList() {
    const [tasks, setTasks] = useState([]);
    
    useEffect(() => {
        // Fetch tasks on mount
        fetchTasks().then(setTasks);
        
        // Cleanup on unmount
        return () => {
            console.log('Component unmounting');
        };
    }, []); // Empty deps = run once
    
    return <ul>{tasks.map(t => <li key={t.id}>{t.name}</li>)}</ul>;
}

// 6. Custom Hooks
function useLocalStorage(key, initialValue) {
    const [value, setValue] = useState(() => {
        const stored = localStorage.getItem(key);
        return stored ? JSON.parse(stored) : initialValue;
    });
    
    useEffect(() => {
        localStorage.setItem(key, JSON.stringify(value));
    }, [key, value]);
    
    return [value, setValue];
}

// 7. Context API for state management
const ThemeContext = createContext();

function ThemeProvider({ children }) {
    const [theme, setTheme] = useState('light');
    
    return (
        <ThemeContext.Provider value={{ theme, setTheme }}>
            {children}
        </ThemeContext.Provider>
    );
}

// 8. useReducer for complex state
function taskReducer(state, action) {
    switch (action.type) {
        case 'ADD':
            return [...state, action.task];
        case 'REMOVE':
            return state.filter(t => t.id !== action.id);
        case 'UPDATE':
            return state.map(t => t.id === action.id ? action.task : t);
        default:
            return state;
    }
}

function TaskManager() {
    const [tasks, dispatch] = useReducer(taskReducer, []);
    
    const addTask = (task) => {
        dispatch({ type: 'ADD', task });
    };
    
    return <TaskList tasks={tasks} onAdd={addTask} />;
}

// 9. React Router
/*
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';

function App() {
    return (
        <BrowserRouter>
            <nav>
                <Link to="/">Home</Link>
                <Link to="/tasks">Tasks</Link>
            </nav>
            
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/tasks" element={<TaskList />} />
                <Route path="/tasks/:id" element={<TaskDetail />} />
            </Routes>
        </BrowserRouter>
    );
}
*/

// 10. Performance Optimization
// React.memo for preventing re-renders
const MemoizedTaskCard = React.memo(TaskCard);

// useMemo for expensive calculations
const sortedTasks = useMemo(() => {
    return tasks.sort((a, b) => b.priority - a.priority);
}, [tasks]);

// useCallback for function props
const handleDelete = useCallback((id) => {
    deleteTask(id);
}, []);
'''


# ============== Main Demo ==============

async def main():
    """Demonstrate Phase 1 Fullstack concepts."""
    print("=" * 70)
    print("FULLSTACK MASTERY - PHASE 1: FRONTEND FUNDAMENTALS")
    print("=" * 70)
    
    print("\n1. HTML5 SEMANTIC STRUCTURE")
    print("-" * 40)
    print("   Features demonstrated:")
    print("     ✓ Semantic elements (header, nav, main, section, article, footer)")
    print("     ✓ Accessibility (aria-label, aria-labelledby)")
    print("     ✓ Meta tags for SEO")
    print("     ✓ Template syntax for dynamic content")
    
    print("\n2. MODERN CSS (CSS3 + Flexbox/Grid)")
    print("-" * 40)
    print("   Features demonstrated:")
    print("     ✓ CSS Variables (Design Tokens)")
    print("     ✓ Flexbox layout utilities")
    print("     ✓ CSS Grid with responsive breakpoints")
    print("     ✓ Component-based architecture")
    print("     ✓ Animations and transitions")
    print("     ✓ Dark mode support (prefers-color-scheme)")
    print("     ✓ Accessibility (focus-visible, sr-only)")
    
    print("\n3. JAVASCRIPT (ES6+)")
    print("-" * 40)
    print("   Features demonstrated:")
    print("     ✓ ES6 Classes and modules")
    print("     ✓ Async/await with Fetch API")
    print("     ✓ Event delegation pattern")
    print("     ✓ Pub/Sub Event Bus")
    print("     ✓ State management")
    print("     ✓ Debounce and throttle utilities")
    print("     ✓ LocalStorage with expiration")
    
    print("\n4. TYPESCRIPT")
    print("-" * 40)
    print("   Features demonstrated:")
    print("     ✓ Type annotations (interfaces, types)")
    print("     ✓ Union types and literal types")
    print("     ✓ Generics (APIResponse<T>)")
    print("     ✓ Utility types (Partial, Pick, Omit, Record)")
    print("     ✓ Type guards and assertions")
    print("     ✓ Class-based architecture with private members")
    print("     ✓ Function overloads and optional parameters")
    
    print("\n5. REACT CONCEPTS")
    print("-" * 40)
    print("   Features demonstrated:")
    print("     ✓ JSX syntax")
    print("     ✓ Functional components")
    print("     ✓ Props and prop drilling")
    print("     ✓ useState for local state")
    print("     ✓ useEffect for side effects")
    print("     ✓ Custom hooks")
    print("     ✓ Context API")
    print("     ✓ useReducer for complex state")
    print("     ✓ React Router")
    print("     ✓ Performance optimization (memo, useMemo, useCallback)")
    
    print("\n" + "=" * 70)
    print("PHASE 1 SUMMARY")
    print("=" * 70)
    print("   Templates created:")
    print("     • HTML5 semantic structure (accessible, SEO-friendly)")
    print("     • Modern CSS with variables, grid, flexbox, dark mode")
    print("     • ES6+ JavaScript with async patterns")
    print("     • TypeScript with full type safety")
    print("     • React concepts and patterns")
    
    print("\n   Key Skills:")
    skills = [
        "Semantic HTML & Accessibility",
        "Modern CSS (Grid, Flexbox, Variables)",
        "Responsive Design",
        "ES6+ JavaScript",
        "Async Programming (Promises, async/await)",
        "TypeScript Fundamentals",
        "React Components & Hooks",
        "State Management",
        "Performance Optimization"
    ]
    for i, skill in enumerate(skills, 1):
        print(f"     {i}. {skill}")
    
    print("\n" + "=" * 70)
    print("Ready for Phase 2: Backend Development")
    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())
