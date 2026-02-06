#!/usr/bin/env python3
"""
Security Mastery & Mobile Development
Cybersecurity, Mobile Languages (Swift, Kotlin, Dart)
"""

import asyncio
import hashlib
import hmac
import base64
import secrets
from datetime import datetime


# ============== SECURITY FUNDAMENTALS ==============

SECURITY_PRINCIPLES = {
    "CIA Triad": {
        "Confidentiality": "Prevent unauthorized access to data",
        "Integrity": "Ensure data is not tampered with",
        "Availability": "Ensure systems are accessible when needed"
    },
    "Defense in Depth": "Multiple layers of security controls",
    "Least Privilege": "Minimum access necessary to perform function",
    "Zero Trust": "Never trust, always verify"
}


# ============== CRYPTOGRAPHY ==============

class Cryptography:
    """Cryptographic operations and concepts."""
    
    @staticmethod
    def hash_sha256(data: str) -> str:
        """SHA-256 hashing."""
        return hashlib.sha256(data.encode()).hexdigest()
    
    @staticmethod
    def hash_with_salt(data: str, salt: str = None) -> tuple:
        """Salted hash for passwords."""
        if salt is None:
            salt = secrets.token_hex(16)
        salted = data + salt
        return hashlib.pbkdf2_hmac('sha256', salted.encode(), 
                                    salt.encode(), 100000).hex(), salt
    
    @staticmethod
    def generate_hmac(message: str, key: str) -> str:
        """HMAC for message authentication."""
        return hmac.new(key.encode(), message.encode(), 
                       hashlib.sha256).hexdigest()
    
    CONCEPTS = {
        "Hashing": {
            "MD5": "Broken, do not use",
            "SHA-1": "Deprecated, use for legacy only",
            "SHA-256": "Current standard",
            "SHA-3": "Next-gen standard",
            "bcrypt/Argon2": "For password hashing"
        },
        "Encryption": {
            "Symmetric (AES)": "Same key for encrypt/decrypt",
            "Asymmetric (RSA)": "Public key encrypt, private key decrypt",
            "Hybrid": "Asymmetric for key exchange, symmetric for data"
        },
        "Encoding": {
            "Base64": "Not encryption, just encoding",
            "Hex": "Binary to hex string",
            "URL Encoding": "Safe for URLs"
        }
    }


# ============== WEB SECURITY ==============

WEB_SECURITY = {
    "OWASP Top 10 (2021)": {
        "A01:2021-Broken Access Control": "Improper enforcement of access policies",
        "A02:2021-Cryptographic Failures": "Weak encryption, sensitive data exposure",
        "A03:2021-Injection": "SQL, NoSQL, OS command, LDAP injection",
        "A04:2021-Insecure Design": "Missing security controls in design",
        "A05:2021-Security Misconfiguration": "Default configs, verbose errors",
        "A06:2021-Vulnerable Components": "Outdated libraries, dependencies",
        "A07:2021-ID and Auth Failures": "Weak auth, session management",
        "A08:2021-Software and Data Integrity": "CI/CD, deserialization",
        "A09:2021-Security Logging Failures": "Insufficient monitoring",
        "A10:2021-SSRF": "Server-Side Request Forgery"
    },
    
    "Common Attacks": {
        "SQL Injection": {
            "description": "Inject malicious SQL through user input",
            "prevention": "Parameterized queries, ORM, input validation",
            "example": "' OR '1'='1' --"
        },
        "XSS (Cross-Site Scripting)": {
            "description": "Inject client-side scripts into web pages",
            "prevention": "Output encoding, CSP, input validation",
            "types": ["Stored", "Reflected", "DOM-based"]
        },
        "CSRF": {
            "description": "Force user to execute unwanted actions",
            "prevention": "CSRF tokens, SameSite cookies, Referer header"
        },
        "MITM": {
            "description": "Intercept communication between parties",
            "prevention": "HTTPS, certificate pinning, HSTS"
        }
    },
    
    "Security Headers": {
        "Content-Security-Policy": "Prevent XSS by controlling resources",
        "X-Frame-Options": "Prevent clickjacking",
        "X-Content-Type-Options": "Prevent MIME sniffing",
        "Strict-Transport-Security": "Force HTTPS",
        "X-XSS-Protection": "Browser XSS filter",
        "Referrer-Policy": "Control referrer information"
    }
}


# ============== AUTHENTICATION & AUTHORIZATION ==============

AUTH_PATTERNS = {
    "Authentication Methods": {
        "Password": "Something you know",
        "SMS/Email OTP": "Something you have (weak)",
        "TOTP (Google Auth)": "Time-based one-time password",
        "Hardware Keys": "YubiKey, FIDO2/WebAuthn",
        "Biometric": "Fingerprint, FaceID",
        "Magic Links": "Email-based passwordless"
    },
    
    "OAuth 2.0 Flows": {
        "Authorization Code": "Web apps, most secure",
        "PKCE": "Mobile apps, public clients",
        "Client Credentials": "Server-to-server",
        "Device Code": "Smart TVs, CLI tools",
        "Implicit": "Deprecated, use PKCE"
    },
    
    "JWT Security": {
        "Algorithm Confusion": "Always verify algorithm",
        "None Algorithm": "Reject 'none' algorithm",
        "Weak Secrets": "Use strong HS256 secrets or RS256",
        "Token Storage": "HttpOnly cookies > localStorage",
        "Expiration": "Short-lived access tokens"
    },
    
    "Session Management": {
        "Secure Cookies": "Secure, HttpOnly, SameSite",
        "Session Timeout": "Idle and absolute timeouts",
        "Concurrent Sessions": "Limit per user",
        "Session Fixation": "Regenerate ID on auth",
        "Logout": "Invalidate server-side"
    }
}


# ============== SECURE CODING PRACTICES ==============

SECURE_CODING = """
# SECURE CODING CHECKLIST

## Input Validation
- [ ] Validate on server-side (never trust client)
- [ ] Whitelist allowed values, don't blacklist
- [ ] Validate type, length, format, range
- [ ] Sanitize special characters

## Output Encoding
- [ ] HTML encode before DOM insertion
- [ ] URL encode for URL parameters
- [ ] SQL escape or use parameterized queries
- [ ] JSON encode for JSON output

## Authentication
- [ ] Multi-factor authentication
- [ ] Strong password policies
- [ ] Account lockout after failures
- [ ] Secure password storage (bcrypt, Argon2)

## Session Management
- [ ] Secure, HttpOnly, SameSite cookies
- [ ] Short session timeouts
- [ ] Regenerate ID on privilege change
- [ ] Proper logout (server-side invalidation)

## Cryptography
- [ ] Use established libraries (don't roll your own)
- [ ] AES-256 for encryption
- [ ] SHA-256 for hashing (not passwords)
- [ ] bcrypt/Argon2 for passwords
- [ ] Secure random number generation

## Error Handling
- [ ] Generic error messages to users
- [ ] Detailed logs for developers
- [ ] Don't expose stack traces
- [ ] Fail securely (deny by default)

## Dependencies
- [ ] Keep dependencies updated
- [ ] Use Snyk/Dependabot for scanning
- [ ] Minimize dependency count
- [ ] Verify package integrity
"""


# ============== MOBILE DEVELOPMENT ==============

MOBILE_LANGUAGES = {
    "Swift (iOS)": {
        "platform": "iOS, macOS, watchOS, tvOS",
        "paradigm": "Protocol-oriented, functional, OOP",
        "strengths": ["Type safety", "Performance", "Apple ecosystem", "Modern syntax"],
        "features": ["Optionals", "Generics", "Closures", "Async/await", "SwiftUI"],
        "runtime": "Compiled, LLVM"
    },
    
    "Kotlin (Android)": {
        "platform": "Android, JVM, Native, JS",
        "paradigm": "Multi-paradigm (OOP, functional)",
        "strengths": ["Null safety", "Coroutines", "Interoperable with Java", "Concise"],
        "features": ["Extension functions", "Data classes", "Sealed classes", "Flow"],
        "runtime": "JVM, Native"
    },
    
    "Dart (Flutter)": {
        "platform": "iOS, Android, Web, Desktop",
        "paradigm": "Object-oriented",
        "strengths": ["Hot reload", "Single codebase", "Fast UI", "Growing ecosystem"],
        "features": ["Futures", "Streams", "Mixins", "Null safety"],
        "runtime": "Dart VM (dev), AOT compiled (release)"
    },
    
    "React Native (JS)": {
        "platform": "iOS, Android",
        "paradigm": "React, component-based",
        "strengths": ["JavaScript", "Native performance", "Large community", "Hot reload"],
        "features": ["JS bridge", "Native modules", "Hermes engine", "Expo"],
        "runtime": "JavaScriptCore/Hermes"
    }
}


MOBILE_CODE_EXAMPLES = {
    "Swift (iOS)": '''
import SwiftUI

// Task Model
struct Task: Identifiable, Codable {
    let id: UUID
    var name: String
    var status: TaskStatus
    var priority: Priority
    var dueDate: Date?
    
    enum TaskStatus: String, Codable, CaseIterable {
        case todo, doing, done
    }
    
    enum Priority: String, Codable, CaseIterable {
        case low, medium, high
        
        var color: Color {
            switch self {
            case .low: return .green
            case .medium: return .yellow
            case .high: return .red
            }
        }
    }
}

// ViewModel
class TaskViewModel: ObservableObject {
    @Published var tasks: [Task] = []
    
    func addTask(name: String, priority: Task.Priority) {
        let task = Task(
            id: UUID(),
            name: name,
            status: .todo,
            priority: priority,
            dueDate: nil
        )
        tasks.append(task)
    }
    
    func toggleStatus(_ task: Task) {
        if let index = tasks.firstIndex(where: { $0.id == task.id }) {
            let nextStatus: Task.TaskStatus
            switch tasks[index].status {
            case .todo: nextStatus = .doing
            case .doing: nextStatus = .done
            case .done: nextStatus = .todo
            }
            tasks[index].status = nextStatus
        }
    }
}

// SwiftUI View
struct TaskListView: View {
    @StateObject private var viewModel = TaskViewModel()
    @State private var newTaskName = ""
    
    var body: some View {
        NavigationView {
            List {
                ForEach(viewModel.tasks) { task in
                    TaskRow(task: task)
                        .onTapGesture {
                            viewModel.toggleStatus(task)
                        }
                }
            }
            .navigationTitle("Tasks")
            .toolbar {
                Button("Add") {
                    viewModel.addTask(name: "New Task", priority: .medium)
                }
            }
        }
    }
}

struct TaskRow: View {
    let task: Task
    
    var body: some View {
        HStack {
            Circle()
                .fill(task.priority.color)
                .frame(width: 12, height: 12)
            
            Text(task.name)
                .strikethrough(task.status == .done)
            
            Spacer()
            
            Text(task.status.rawValue)
                .font(.caption)
                .padding(4)
                .background(Color.gray.opacity(0.2))
                .cornerRadius(4)
        }
    }
}
''',

    "Kotlin (Android)": '''
package com.scaleplus.taskmanager

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch
import java.util.UUID
import java.time.LocalDateTime

// Data class (immutable)
data class Task(
    val id: String = UUID.randomUUID().toString(),
    val name: String,
    val status: TaskStatus = TaskStatus.TODO,
    val priority: Priority = Priority.MEDIUM,
    val dueDate: LocalDateTime? = null
) {
    enum class TaskStatus { TODO, DOING, DONE }
    enum class Priority { LOW, MEDIUM, HIGH }
}

// Repository
class TaskRepository {
    private val tasks = mutableListOf<Task>()
    
    fun getTasks(): List<Task> = tasks.toList()
    
    fun addTask(task: Task) {
        tasks.add(task)
    }
    
    fun updateTask(task: Task) {
        val index = tasks.indexOfFirst { it.id == task.id }
        if (index != -1) {
            tasks[index] = task
        }
    }
    
    fun deleteTask(id: String) {
        tasks.removeAll { it.id == id }
    }
}

// ViewModel
class TaskViewModel(private val repository: TaskRepository) : ViewModel() {
    
    private val _tasks = MutableStateFlow<List<Task>>(emptyList())
    val tasks: StateFlow<List<Task>> = _tasks
    
    init {
        loadTasks()
    }
    
    fun loadTasks() {
        viewModelScope.launch {
            _tasks.value = repository.getTasks()
        }
    }
    
    fun addTask(name: String, priority: Task.Priority = Task.Priority.MEDIUM) {
        viewModelScope.launch {
            val task = Task(name = name, priority = priority)
            repository.addTask(task)
            loadTasks()
        }
    }
    
    fun toggleTaskStatus(task: Task) {
        viewModelScope.launch {
            val newStatus = when (task.status) {
                Task.TaskStatus.TODO -> Task.TaskStatus.DOING
                Task.TaskStatus.DOING -> Task.TaskStatus.DONE
                Task.TaskStatus.DONE -> Task.TaskStatus.TODO
            }
            repository.updateTask(task.copy(status = newStatus))
            loadTasks()
        }
    }
}

// Composable UI (Jetpack Compose)
/*
@Composable
fun TaskListScreen(viewModel: TaskViewModel = viewModel()) {
    val tasks by viewModel.tasks.collectAsState()
    
    LazyColumn {
        items(tasks) { task ->
            TaskItem(
                task = task,
                onToggle = { viewModel.toggleTaskStatus(task) }
            )
        }
    }
}

@Composable
fun TaskItem(task: Task, onToggle: () -> Unit) {
    Card(
        modifier = Modifier
            .fillMaxWidth()
            .padding(8.dp)
            .clickable(onClick = onToggle)
    ) {
        Row(
            modifier = Modifier.padding(16.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            // Priority indicator
            Box(
                modifier = Modifier
                    .size(12.dp)
                    .background(
                        when (task.priority) {
                            Task.Priority.HIGH -> Color.Red
                            Task.Priority.MEDIUM -> Color.Yellow
                            Task.Priority.LOW -> Color.Green
                        },
                        CircleShape
                    )
            )
            
            Spacer(modifier = Modifier.width(16.dp))
            
            Text(
                text = task.name,
                style = MaterialTheme.typography.bodyLarge,
                textDecoration = if (task.status == Task.TaskStatus.DONE) 
                    TextDecoration.LineThrough else TextDecoration.None
            )
        }
    }
}
*/
''',

    "Dart (Flutter)": '''
import 'package:flutter/material.dart';
import 'package:uuid/uuid.dart';

// Task Model
enum TaskStatus { todo, doing, done }

enum Priority { low, medium, high }

class Task {
  final String id;
  String name;
  TaskStatus status;
  Priority priority;
  DateTime? dueDate;
  
  Task({
    String? id,
    required this.name,
    this.status = TaskStatus.todo,
    this.priority = Priority.medium,
    this.dueDate,
  }) : id = id ?? const Uuid().v4();
  
  Color get priorityColor {
    switch (priority) {
      case Priority.high:
        return Colors.red;
      case Priority.medium:
        return Colors.orange;
      case Priority.low:
        return Colors.green;
    }
  }
}

// State Management with ChangeNotifier
class TaskProvider extends ChangeNotifier {
  final List<Task> _tasks = [];
  
  List<Task> get tasks => List.unmodifiable(_tasks);
  
  List<Task> get tasksByPriority {
    return [..._tasks]..sort((a, b) => 
      b.priority.index.compareTo(a.priority.index));
  }
  
  void addTask(String name, Priority priority) {
    _tasks.add(Task(name: name, priority: priority));
    notifyListeners();
  }
  
  void toggleTaskStatus(String id) {
    final task = _tasks.firstWhere((t) => t.id == id);
    final nextStatus = TaskStatus.values[
      (task.status.index + 1) % TaskStatus.values.length
    ];
    task.status = nextStatus;
    notifyListeners();
  }
  
  void deleteTask(String id) {
    _tasks.removeWhere((t) => t.id == id);
    notifyListeners();
  }
}

// Flutter Widget
class TaskListScreen extends StatelessWidget {
  const TaskListScreen({Key? key}) : super(key: key);
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Tasks'),
        actions: [
          IconButton(
            icon: const Icon(Icons.add),
            onPressed: () => _showAddTaskDialog(context),
          ),
        ],
      ),
      body: Consumer<TaskProvider>(
        builder: (context, provider, child) {
          return ListView.builder(
            itemCount: provider.tasks.length,
            itemBuilder: (context, index) {
              final task = provider.tasks[index];
              return TaskListItem(task: task);
            },
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => _showAddTaskDialog(context),
        child: const Icon(Icons.add),
      ),
    );
  }
  
  void _showAddTaskDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (context) => const AddTaskDialog(),
    );
  }
}

class TaskListItem extends StatelessWidget {
  final Task task;
  
  const TaskListItem({Key? key, required this.task}) : super(key: key);
  
  @override
  Widget build(BuildContext context) {
    return Dismissible(
      key: Key(task.id),
      onDismissed: (_) {
        context.read<TaskProvider>().deleteTask(task.id);
      },
      child: ListTile(
        leading: CircleAvatar(
          backgroundColor: task.priorityColor,
          radius: 8,
        ),
        title: Text(
          task.name,
          style: TextStyle(
            decoration: task.status == TaskStatus.done
                ? TextDecoration.lineThrough
                : null,
          ),
        ),
        subtitle: Text(task.status.name.toUpperCase()),
        trailing: Checkbox(
          value: task.status == TaskStatus.done,
          onChanged: (_) {
            context.read<TaskProvider>().toggleTaskStatus(task.id);
          },
        ),
        onTap: () {
          context.read<TaskProvider>().toggleTaskStatus(task.id);
        },
      ),
    );
  }
}
'''
}


# ============== Main ==============

async def main():
    """Demonstrate security and mobile development knowledge."""
    print("=" * 70)
    print("SECURITY MASTERY & MOBILE DEVELOPMENT")
    print("=" * 70)
    
    # 1. Security Principles
    print("\n1. SECURITY FUNDAMENTALS")
    print("-" * 40)
    print("   CIA Triad:")
    for principle, desc in SECURITY_PRINCIPLES["CIA Triad"].items():
        print(f"     • {principle}: {desc}")
    
    # 2. Cryptography Demo
    print("\n2. CRYPTOGRAPHY")
    print("-" * 40)
    
    password = "papi-secret-password"
    hash_result = Cryptography.hash_sha256(password)
    print(f"   SHA-256 of '{password[:10]}...': {hash_result[:32]}...")
    
    salted_hash, salt = Cryptography.hash_with_salt(password)
    print(f"   PBKDF2 salted hash: {salted_hash[:32]}...")
    
    # 3. OWASP Top 10
    print("\n3. OWASP TOP 10 (2021)")
    print("-" * 40)
    for code, desc in WEB_SECURITY["OWASP Top 10 (2021)"].items():
        print(f"   {code}: {desc[:40]}...")
    
    # 4. Mobile Development
    print("\n4. MOBILE DEVELOPMENT LANGUAGES")
    print("-" * 40)
    
    for lang, info in MOBILE_LANGUAGES.items():
        print(f"\n   {lang}:")
        print(f"     Platform: {info['platform']}")
        print(f"     Strengths: {', '.join(info['strengths'][:2])}")
        print(f"     Runtime: {info['runtime']}")
    
    # 5. Mobile Platform Selection
    print("\n5. MOBILE PLATFORM SELECTION")
    print("-" * 40)
    
    selections = [
        ("Native iOS app", "Swift (SwiftUI)"),
        ("Native Android app", "Kotlin (Jetpack Compose)"),
        ("Cross-platform (single codebase)", "Flutter (Dart)"),
        ("Cross-platform (JavaScript)", "React Native"),
        ("Game development", "Unity (C#) or Unreal (C++)"),
        ("Enterprise iOS", "Swift with UIKit"),
        ("Rapid prototyping", "Flutter or React Native"),
    ]
    
    for scenario, choice in selections:
        print(f"   {scenario:35} → {choice}")
    
    # 6. Security Headers
    print("\n6. SECURITY HEADERS")
    print("-" * 40)
    for header, desc in WEB_SECURITY["Security Headers"].items():
        print(f"   {header:30} - {desc}")
    
    print("\n" + "=" * 70)
    print("SECURITY & MOBILE MASTERY COMPLETE")
    print("=" * 70)
    print("\nSecurity Coverage:")
    print("  • Cryptography (hashing, encryption, HMAC)")
    print("  • OWASP Top 10 vulnerabilities")
    print("  • Authentication & Authorization")
    print("  • Secure coding practices")
    print("\nMobile Coverage:")
    print("  • Swift (iOS) with SwiftUI")
    print("  • Kotlin (Android) with Jetpack Compose")
    print("  • Flutter (Dart) - cross-platform")
    print("  • React Native - JavaScript")
    print("\nReady for secure, full-stack, multi-platform development!")


if __name__ == "__main__":
    asyncio.run(main())
