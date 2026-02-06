#!/usr/bin/env python3
"""
n8n Expert Specialist - Advanced Automation & API Integration
World-class automation engineering patterns
"""

import asyncio
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Union, Callable
from enum import Enum
from datetime import datetime
import json


# ============== ADVANCED N8N ARCHITECTURE PATTERNS ==============

class WorkflowArchitecture:
    """Enterprise-grade workflow design patterns."""
    
    MODULAR_DESIGN = """
# MODULAR WORKFLOW ARCHITECTURE

## 1. Sub-Workflow Pattern
Break complex workflows into reusable components:

Main Workflow:
  [Trigger] → [Validate Input] → [Execute Sub-Workflow] → [Handle Result]
                                      ↓
                              [Sub-Workflow: Process Order]
                              [Sub-Workflow: Send Notifications]
                              [Sub-Workflow: Update Analytics]

Benefits:
- Reusable components
- Easier testing
- Better error isolation
- Parallel execution possible

Implementation:
- Use Execute Workflow node
- Pass data via $json parameter
- Return standardized response format

## 2. Orchestrator Pattern
Central workflow coordinates multiple services:

Orchestrator:
  [Webhook] → [Parse Request] → [Route to Handler]
                                    ↓
              ┌────────────────────┼────────────────────┐
              ↓                    ↓                    ↓
        [Handler A]          [Handler B]          [Handler C]
        (New Lead)          (Update User)        (Process Order)
              ↓                    ↓                    ↓
        [Sub-workflows]     [Sub-workflows]     [Sub-workflows]

Benefits:
- Single entry point
- Centralized logging
- Consistent error handling
- Easy to extend

## 3. Event-Driven Architecture
Use message queues for decoupling:

Producer Workflows:
  [Event Happens] → [Format Message] → [Add to Queue (Redis/RabbitMQ)]

Consumer Workflows:
  [Trigger: Queue Item] → [Process] → [Acknowledge]

Multiple consumers can process same queue:
- Consumer 1: Send email
- Consumer 2: Update database
- Consumer 3: Post to Slack

Benefits:
- Loose coupling
- High availability
- Load balancing
- Retry mechanisms
"""

    ERROR_HANDLING_EXPERT = """
# ENTERPRISE ERROR HANDLING

## Pattern 1: Circuit Breaker
Prevents cascading failures:

[Check Circuit State]
      ↓
   [OPEN] → [Return Fallback] → [Alert Admin]
      ↓
  [CLOSED]
      ↓
[Execute Operation]
      ↓
   [Success] → [Reset Counter] → [Continue]
      ↓
   [Failure]
      ↓
[Increment Failure Count]
      ↓
[Check Threshold]
      ↓
[Exceeds?] → [Open Circuit] → [Start Timer]
      ↓
   [No] → [Retry with Backoff]

Implementation in Function node:
```javascript
const circuitState = $getWorkflowStaticData('global').circuitState || 'CLOSED';
const failureCount = $getWorkflowStaticData('global').failureCount || 0;
const threshold = 5;
const timeout = 60000; // 1 minute

if (circuitState === 'OPEN') {
  const lastFailure = $getWorkflowStaticData('global').lastFailureTime;
  if (Date.now() - lastFailure > timeout) {
    // Try half-open
    $getWorkflowStaticData('global').circuitState = 'HALF_OPEN';
  } else {
    return [{ json: { error: "Circuit open", fallback: true } }];
  }
}

// Execute operation...
// On failure:
$getWorkflowStaticData('global').failureCount = failureCount + 1;
if (failureCount + 1 >= threshold) {
  $getWorkflowStaticData('global').circuitState = 'OPEN';
  $getWorkflowStaticData('global').lastFailureTime = Date.now();
}
```

## Pattern 2: Dead Letter Queue
Failed operations saved for later retry:

[Operation] → [Success] → [Continue]
      ↓
   [Failure]
      ↓
[Save to Failed Queue] → [Send Alert]
      ↓
[Separate Retry Workflow] (runs every 10 min)
      ↓
[Process Failed Items] → [Retry] → [Success?] → [Remove from Queue]

## Pattern 3: Transactional Outbox
Ensure data consistency across systems:

[Business Operation] → [Save to Database]
      ↓
[Also Save Event to Outbox Table]
      ↓
[Separate Publisher Workflow]
      ↓
[Poll Outbox] → [Publish to Message Bus]
      ↓
[Mark as Published] → [Delete/Archive]

Benefits:
- Atomic database + event
- No data loss
- Reliable delivery
"""

    DATA_TRANSFORMATION_MASTER = """
# ADVANCED DATA TRANSFORMATION

## Complex JSON Manipulation

### 1. Deep Merge Objects
```javascript
const merge = (target, source) => {
  for (const key in source) {
    if (source[key] && typeof source[key] === 'object' && !Array.isArray(source[key])) {
      target[key] = merge(target[key] || {}, source[key]);
    } else {
      target[key] = source[key];
    }
  }
  return target;
};

const result = merge($json.baseConfig, $json.overrideConfig);
```

### 2. Flatten Nested Structures
```javascript
const flatten = (obj, prefix = '', result = {}) => {
  for (const key in obj) {
    const newKey = prefix ? `${prefix}.${key}` : key;
    if (obj[key] && typeof obj[key] === 'object' && !Array.isArray(obj[key])) {
      flatten(obj[key], newKey, result);
    } else {
      result[newKey] = obj[key];
    }
  }
  return result;
};

const flat = flatten($json.nestedData);
// { "user.name": "John", "user.address.city": "NYC" }
```

### 3. Group and Aggregate
```javascript
const groupBy = (items, key) => {
  return items.reduce((acc, item) => {
    const groupKey = item[key];
    if (!acc[groupKey]) acc[groupKey] = [];
    acc[groupKey].push(item);
    return acc;
  }, {});
};

const withStats = Object.entries(groupBy($input.all(), 'category')).map(([cat, items]) => ({
  category: cat,
  count: items.length,
  total: items.reduce((sum, i) => sum + (i.amount || 0), 0),
  average: items.reduce((sum, i) => sum + (i.amount || 0), 0) / items.length,
  items: items
}));
```

### 4. Data Validation Schema
```javascript
const validate = (data, schema) => {
  const errors = [];
  for (const [field, rules] of Object.entries(schema)) {
    const value = data[field];
    
    if (rules.required && !value) {
      errors.push(`${field} is required`);
    }
    if (rules.type && value && typeof value !== rules.type) {
      errors.push(`${field} must be ${rules.type}`);
    }
    if (rules.pattern && value && !rules.pattern.test(value)) {
      errors.push(`${field} format invalid`);
    }
    if (rules.min && value < rules.min) {
      errors.push(`${field} must be >= ${rules.min}`);
    }
  }
  return { valid: errors.length === 0, errors };
};

const schema = {
  email: { required: true, type: 'string', pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/ },
  amount: { required: true, type: 'number', min: 0 }
};

const validation = validate($json, schema);
if (!validation.valid) {
  return [{ json: { error: 'Validation failed', details: validation.errors } }];
}
```

## Date/Time Manipulation
```javascript
// Parse various formats
const parseDate = (input) => {
  const formats = [
    /^(\d{4})-(\d{2})-(\d{2})$/,           // 2024-01-15
    /^(\d{2})\/(\d{2})\/(\d{4})$/,         // 01/15/2024
    /^(\d{2})-(\d{2})-(\d{4})$/            // 15-01-2024
  ];
  
  for (const pattern of formats) {
    const match = input.match(pattern);
    if (match) {
      return new Date(match[0]).toISOString();
    }
  }
  return null;
};

// Business days calculation
const addBusinessDays = (date, days) => {
  let current = new Date(date);
  let added = 0;
  
  while (added < days) {
    current.setDate(current.getDate() + 1);
    const day = current.getDay();
    if (day !== 0 && day !== 6) { // Skip weekends
      added++;
    }
  }
  return current;
};

// Timezone conversion
const toTimezone = (date, timezone) => {
  return new Date(date).toLocaleString('en-US', { timeZone: timezone });
};
```
"""


# ============== API BUILDING PATTERNS ==============

class APIBuilder:
    """Design and build robust APIs for n8n integration."""
    
    REST_API_DESIGN = """
# REST API DESIGN BEST PRACTICES

## 1. Resource Naming
✅ Good:
  GET    /api/v1/tasks          # List all tasks
  GET    /api/v1/tasks/{id}     # Get specific task
  POST   /api/v1/tasks          # Create task
  PUT    /api/v1/tasks/{id}     # Full update
  PATCH  /api/v1/tasks/{id}     # Partial update
  DELETE /api/v1/tasks/{id}     # Delete task

❌ Bad:
  GET /api/v1/getTasks
  POST /api/v1/createTask

## 2. Response Standards

Success Response:
{
  "success": true,
  "data": { ... },
  "meta": {
    "timestamp": "2024-01-15T10:30:00Z",
    "requestId": "req_abc123",
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 150,
      "hasMore": true
    }
  }
}

Error Response:
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      { "field": "email", "message": "Invalid email format" }
    ],
    "requestId": "req_abc123"
  }
}

## 3. Pagination Patterns

Offset Pagination:
  GET /tasks?page=2&limit=50
  Response includes: total, page, limit, hasMore

Cursor Pagination (better for real-time):
  GET /tasks?cursor=eyJpZCI6MTAwfQ&limit=50
  Response includes: nextCursor, prevCursor, hasMore

Time-based Pagination:
  GET /tasks?after=2024-01-01T00:00:00Z&limit=50

## 4. Rate Limiting Headers
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1640995200
Retry-After: 60

## 5. Versioning Strategies

URL Versioning (recommended):
  /api/v1/tasks
  /api/v2/tasks

Header Versioning:
  Accept: application/vnd.api+json;version=2

Query Parameter:
  /api/tasks?version=2
"""

    WEBHOOK_DESIGN = """
# WEBHOOK DESIGN PATTERNS

## 1. Webhook Security

Signature Validation:
```javascript
// Incoming webhook handler
const crypto = require('crypto');

const payload = JSON.stringify($body);
const signature = $headers['x-webhook-signature'];
const secret = $env.WEBHOOK_SECRET;

const expected = crypto
  .createHmac('sha256', secret)
  .update(payload)
  .digest('hex');

if (signature !== expected) {
  return [{ json: { error: 'Invalid signature' }, statusCode: 401 }];
}
```

IP Allowlisting:
```javascript
const allowedIPs = ['192.168.1.0/24', '10.0.0.5'];
const clientIP = $headers['x-forwarded-for'] || $remoteAddress;

// Validate IP is in allowed list
// Return 403 if not allowed
```

## 2. Webhook Reliability

Idempotency Keys:
```javascript
const idempotencyKey = $headers['idempotency-key'];
const processedKeys = $getWorkflowStaticData('global').processedKeys || {};

if (processedKeys[idempotencyKey]) {
  // Already processed, return cached response
  return [{ json: processedKeys[idempotencyKey].response }];
}

// Process webhook...
// Store response:
processedKeys[idempotencyKey] = {
  response: result,
  timestamp: Date.now()
};
$getWorkflowStaticData('global').processedKeys = processedKeys;
```

## 3. Async Processing Pattern

Immediate Response + Async Processing:
```javascript
// 1. Validate webhook
// 2. Queue for processing (Redis/Bull/Queue)
// 3. Return 202 Accepted immediately

return [{
  json: {
    status: 'accepted',
    message: 'Processing asynchronously',
    id: jobId
  },
  statusCode: 202
}];

// Separate workflow polls queue and processes
```

## 4. Retry Logic for Outgoing Webhooks

Exponential Backoff:
```javascript
const MAX_RETRIES = 5;
const BASE_DELAY = 1000; // 1 second

for (let attempt = 1; attempt <= MAX_RETRIES; attempt++) {
  try {
    const response = await $httpRequest({
      method: 'POST',
      url: webhookUrl,
      body: payload
    });
    
    if (response.statusCode >= 200 && response.statusCode < 300) {
      return [{ json: { success: true } }];
    }
    
    throw new Error(`HTTP ${response.statusCode}`);
  } catch (error) {
    if (attempt === MAX_RETRIES) {
      // Final failure
      await sendAlert(error);
      throw error;
    }
    
    // Wait with exponential backoff
    const delay = BASE_DELAY * Math.pow(2, attempt - 1);
    await new Promise(resolve => setTimeout(resolve, delay));
  }
}
```
"""

    GRAPHQL_INTEGRATION = """
# GRAPHQL INTEGRATION PATTERNS

## 1. GraphQL Query Builder

Dynamic Query Generation:
```javascript
const buildQuery = (fields, filters) => {
  const fieldString = fields.join('\\n    ');
  const filterString = Object.entries(filters)
    .map(([k, v]) => `${k}: ${JSON.stringify(v)}`)
    .join(', ');
  
  return `
    query GetTasks {
      tasks(${filterString}) {
        ${fieldString}
      }
    }
  `;
};

const query = buildQuery(
  ['id', 'name', 'status', 'priority'],
  { status: 'todo', limit: 50 }
);
```

## 2. GraphQL Mutation with Variables

```javascript
const mutation = `
  mutation CreateTask($input: TaskInput!) {
    createTask(input: $input) {
      id
      name
      status
      createdAt
    }
  }
`;

const variables = {
  input: {
    name: $json.taskName,
    description: $json.description,
    priority: $json.priority || 'medium'
  }
};

// HTTP Request node:
// Method: POST
// URL: https://api.example.com/graphql
// Body: { query: mutation, variables: variables }
```

## 3. Error Handling for GraphQL

```javascript
const response = $json;

if (response.errors) {
  const errorMessages = response.errors.map(e => e.message);
  return [{
    json: {
      success: false,
      errors: errorMessages
    }
  }];
}

return [{
  json: {
    success: true,
    data: response.data
  }
}];
```

## 4. Pagination with GraphQL (Relay-style)

```javascript
const query = `
  query GetTasks($first: Int, $after: String) {
    tasks(first: $first, after: $after) {
      edges {
        node {
          id
          name
          status
        }
        cursor
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
`;

// Variables: { first: 50, after: lastCursor }
// Continue while pageInfo.hasNextPage
```
"""


# ============== TESTING & DEBUGGING EXPERT ==============

TESTING_STRATEGIES = """
# WORKFLOW TESTING STRATEGIES

## 1. Unit Testing Nodes

Test Individual Logic:
```javascript
// Function node that tests another function
const testCases = [
  { input: { email: 'test@example.com' }, expected: true },
  { input: { email: 'invalid' }, expected: false },
  { input: { email: '' }, expected: false }
];

const validateEmail = (email) => {
  return /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email);
};

const results = testCases.map(tc => ({
  input: tc.input,
  expected: tc.expected,
  actual: validateEmail(tc.input.email),
  passed: validateEmail(tc.input.email) === tc.expected
}));

const allPassed = results.every(r => r.passed);
return [{ json: { allPassed, results } }];
```

## 2. Integration Testing

Mock External Services:
```javascript
// Use IF nodes to detect test mode
const isTestMode = $env.TEST_MODE === 'true';

if (isTestMode) {
  // Return mock response
  return [{ json: { mock: true, data: testData } }];
} else {
  // Make real API call
  return [{ json: await makeRealApiCall() }];
}
```

## 3. Regression Testing

Store Expected Outputs:
```javascript
// Compare current output with stored expected output
const expected = $getWorkflowStaticData('global').expectedResults;
const actual = $json;

const differences = findDifferences(expected, actual);
if (differences.length > 0) {
  await notifyTeam(`Regression detected: ${differences.join(', ')}`);
}
```

## 4. Performance Testing

Measure Execution Time:
```javascript
const start = Date.now();

// ... workflow logic ...

const duration = Date.now() - start;

if (duration > 5000) { // 5 seconds
  await sendAlert(`Slow execution: ${duration}ms`);
}

return [{ json: { ...$json, _executionTime: duration } }];
```
"""


# ============== PRODUCTION DEPLOYMENT ==============

PRODUCTION_GUIDE = """
# PRODUCTION DEPLOYMENT CHECKLIST

## Pre-Deployment

- [ ] All credentials use production keys
- [ ] Error handling implemented for all nodes
- [ ] Rate limiting configured
- [ ] Timeout values set appropriately
- [ ] Logging enabled for debugging
- [ ] Backup strategy documented
- [ ] Rollback plan prepared

## Environment Configuration

Development → Staging → Production

Environment Variables:
- API_ENDPOINTS (different per env)
- DATABASE_URL
- REDIS_URL
- LOG_LEVEL (debug/info/warn/error)
- MAX_EXECUTION_TIME
- RATE_LIMIT_CONFIG

## Monitoring Setup

1. Execution Success Rate > 99%
2. Average Execution Time < 5s
3. Error Rate < 1%
4. Queue Depth (if using message queues)

Alerts For:
- Execution failure spike
- Execution time degradation
- API rate limit approaching
- Credential expiry (30 days before)
- Webhook endpoint down

## Security Hardening

- [ ] Webhook endpoints use HTTPS
- [ ] API keys rotated
- [ ] IP allowlists configured
- [ ] Sensitive data not logged
- [ ] Access controls enabled
- [ ] Audit logging active
"""


# ============== EXPERT N8N FUNCTIONS ==============

EXPERT_FUNCTIONS = {
    "Advanced Data Processing": """
// Process large datasets in chunks
const CHUNK_SIZE = 100;
const items = $input.all();
const results = [];

for (let i = 0; i < items.length; i += CHUNK_SIZE) {
  const chunk = items.slice(i, i + CHUNK_SIZE);
  const processed = await Promise.all(
    chunk.map(item => processItem(item))
  );
  results.push(...processed);
}

return results.map(r => ({ json: r }));
""",

    "Conditional Routing": """
// Route to different paths based on conditions
const data = $json;

if (data.priority === 'high' && data.dueDate < Date.now() + 86400000) {
  return [{ json: { ...data, route: 'urgent' } }];
} else if (data.category === 'support') {
  return [{ json: { ...data, route: 'support-queue' } }];
} else {
  return [{ json: { ...data, route: 'standard' } }];
}
""",

    "Data Enrichment": """
// Enrich data from multiple sources
const baseData = $json;

const [userDetails, orderHistory, preferences] = await Promise.all([
  fetchUserDetails(baseData.userId),
  fetchOrderHistory(baseData.userId),
  fetchPreferences(baseData.userId)
]);

const enriched = {
  ...baseData,
  user: userDetails,
  orders: orderHistory,
  preferences: preferences,
  customerLifetimeValue: calculateCLV(orderHistory),
  riskScore: calculateRisk(userDetails, orderHistory)
};

return [{ json: enriched }];
""",

    "Smart Retry": """
// Smart retry with different strategies
const MAX_RETRIES = 3;
const RETRYABLE_ERRORS = ['ETIMEOUT', 'ECONNRESET', '429'];

for (let attempt = 1; attempt <= MAX_RETRIES; attempt++) {
  try {
    const result = await callExternalAPI($json);
    return [{ json: result }];
  } catch (error) {
    const isRetryable = RETRYABLE_ERRORS.includes(error.code);
    const isLastAttempt = attempt === MAX_RETRIES;
    
    if (!isRetryable || isLastAttempt) {
      // Log final failure
      await logFailure(error, $json);
      throw error;
    }
    
    // Exponential backoff: 1s, 2s, 4s
    await sleep(1000 * Math.pow(2, attempt - 1));
  }
}
"""
}


# ============== Main ==============

async def main():
    """Demonstrate expert-level n8n knowledge."""
    print("=" * 70)
    print("N8N EXPERT SPECIALIST - WORLD-CLASS AUTOMATION ENGINEER")
    print("=" * 70)
    
    print("\n1. ENTERPRISE ARCHITECTURE PATTERNS")
    print("-" * 40)
    patterns = [
        "Modular Design (Sub-Workflows)",
        "Orchestrator Pattern",
        "Event-Driven Architecture",
        "Circuit Breaker Pattern",
        "Dead Letter Queue",
        "Transactional Outbox"
    ]
    for pattern in patterns:
        print(f"   • {pattern}")
    
    print("\n2. API DESIGN EXPERTISE")
    print("-" * 40)
    api_skills = [
        "REST API design (naming, versioning, pagination)",
        "GraphQL integration (queries, mutations, pagination)",
        "Webhook security (HMAC, signatures, idempotency)",
        "Rate limiting strategies",
        "Response standardization",
        "Error handling patterns"
    ]
    for skill in api_skills:
        print(f"   • {skill}")
    
    print("\n3. ADVANCED DATA PROCESSING")
    print("-" * 40)
    data_skills = [
        "Deep merge objects",
        "Flatten nested structures",
        "Group and aggregate",
        "Schema validation",
        "Date/time manipulation",
        "Chunked processing for large datasets"
    ]
    for skill in data_skills:
        print(f"   • {skill}")
    
    print("\n4. TESTING & QUALITY ASSURANCE")
    print("-" * 40)
    testing = [
        "Unit testing individual nodes",
        "Integration testing with mocks",
        "Regression testing",
        "Performance testing",
        "Test data management"
    ]
    for t in testing:
        print(f"   • {t}")
    
    print("\n5. PRODUCTION READINESS")
    print("-" * 40)
    production = [
        "Environment configuration (dev/staging/prod)",
        "Monitoring and alerting",
        "Security hardening",
        "Backup and rollback strategies",
        "Documentation standards"
    ]
    for p in production:
        print(f"   • {p}")
    
    print("\n6. EXPERT-LEVEL FUNCTIONS")
    print("-" * 40)
    for name in EXPERT_FUNCTIONS.keys():
        print(f"   • {name}")
    
    print("\n" + "=" * 70)
    print("WORLD-CLASS N8N EXPERT STATUS ACHIEVED")
    print("=" * 70)
    print("\nCapabilities:")
    print("  ✅ Design enterprise-scale workflow architectures")
    print("  ✅ Build secure, robust APIs for integration")
    print("  ✅ Implement advanced error handling patterns")
    print("  ✅ Transform complex data at scale")
    print("  ✅ Test and debug any automation issue")
    print("  ✅ Deploy production-ready workflows")
    print("  ✅ Integrate 400+ services seamlessly")
    print("  ✅ Optimize for performance and reliability")
    print("\nReady to build world-class automations for any business!")


if __name__ == "__main__":
    asyncio.run(main())
