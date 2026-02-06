# n8n Expert Specialist - World-Class Automation Engineer

**Status:** World's #1 n8n Automation Expert & API Builder

---

## Expertise Overview

### Enterprise Architecture Patterns

#### 1. Modular Design (Sub-Workflows)
Break complex workflows into reusable components:
- Main workflow coordinates multiple sub-workflows
- Each sub-workflow handles specific domain
- Better testing, error isolation, and reusability

#### 2. Orchestrator Pattern
Central workflow that routes to specialized handlers:
```
[Webhook] → [Parse] → [Router] 
                    ↓
    ┌───────────────┼───────────────┐
    ↓               ↓               ↓
[Handler A]   [Handler B]    [Handler C]
```

#### 3. Event-Driven Architecture
Use message queues (Redis/RabbitMQ) for loose coupling:
- Producers add events to queue
- Multiple consumers process independently
- High availability and load balancing

#### 4. Circuit Breaker Pattern
Prevents cascading failures:
- Tracks failure count
- Opens circuit after threshold
- Returns fallback during outage
- Auto-recovery after timeout

#### 5. Dead Letter Queue
Failed operations saved for retry:
- Failed items queued separately
- Retry workflow processes periodically
- No data loss guarantee

#### 6. Transactional Outbox
Ensures data consistency:
- Save to database + outbox table (atomic)
- Publisher workflow polls outbox
- Reliable event delivery

---

## API Design Excellence

### REST API Best Practices

**Resource Naming:**
```
GET    /api/v1/tasks          # List
GET    /api/v1/tasks/{id}     # Get one
POST   /api/v1/tasks          # Create
PUT    /api/v1/tasks/{id}     # Full update
PATCH  /api/v1/tasks/{id}     # Partial update
DELETE /api/v1/tasks/{id}     # Delete
```

**Response Standards:**
```json
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
```

**Pagination:**
- Offset: `?page=2&limit=50`
- Cursor: `?cursor=eyJpZCI6MTAwfQ`
- Time-based: `?after=2024-01-01T00:00:00Z`

### Webhook Security

**Signature Validation:**
```javascript
const crypto = require('crypto');
const signature = $headers['x-webhook-signature'];
const expected = crypto
  .createHmac('sha256', $env.WEBHOOK_SECRET)
  .update(JSON.stringify($body))
  .digest('hex');

if (signature !== expected) {
  return [{ json: { error: 'Invalid' }, statusCode: 401 }];
}
```

**Idempotency Keys:**
```javascript
const key = $headers['idempotency-key'];
const processed = $getWorkflowStaticData('global').processed || {};

if (processed[key]) {
  return [{ json: processed[key].response }]; // Already processed
}

// Process and store
processed[key] = { response: result, timestamp: Date.now() };
$getWorkflowStaticData('global').processed = processed;
```

### GraphQL Integration

**Dynamic Query Building:**
```javascript
const buildQuery = (fields, filters) => `
  query {
    tasks(${Object.entries(filters).map(([k,v]) => `${k}: ${JSON.stringify(v)}`).join(', ')}) {
      ${fields.join('\n      ')}
    }
  }
`;
```

**Relay-Style Pagination:**
```javascript
query GetTasks($first: Int, $after: String) {
  tasks(first: $first, after: $after) {
    edges {
      node { id name status }
      cursor
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

---

## Advanced Data Transformation

### Complex JSON Manipulation

**Deep Merge:**
```javascript
const merge = (target, source) => {
  for (const key in source) {
    if (source[key] && typeof source[key] === 'object') {
      target[key] = merge(target[key] || {}, source[key]);
    } else {
      target[key] = source[key];
    }
  }
  return target;
};
```

**Flatten Nested Objects:**
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
// { "user.name": "John", "user.address.city": "NYC" }
```

**Group and Aggregate:**
```javascript
const grouped = items.reduce((acc, item) => {
  const key = item.category;
  if (!acc[key]) acc[key] = [];
  acc[key].push(item);
  return acc;
}, {});

const withStats = Object.entries(grouped).map(([cat, items]) => ({
  category: cat,
  count: items.length,
  total: items.reduce((sum, i) => sum + i.amount, 0),
  average: items.reduce((sum, i) => sum + i.amount, 0) / items.length
}));
```

**Schema Validation:**
```javascript
const validate = (data, schema) => {
  const errors = [];
  for (const [field, rules] of Object.entries(schema)) {
    const value = data[field];
    if (rules.required && !value) errors.push(`${field} required`);
    if (rules.type && value && typeof value !== rules.type) {
      errors.push(`${field} must be ${rules.type}`);
    }
    if (rules.pattern && value && !rules.pattern.test(value)) {
      errors.push(`${field} format invalid`);
    }
  }
  return { valid: errors.length === 0, errors };
};
```

---

## Error Handling Mastery

### Exponential Backoff Retry
```javascript
const MAX_RETRIES = 5;
const BASE_DELAY = 1000;

for (let attempt = 1; attempt <= MAX_RETRIES; attempt++) {
  try {
    const result = await makeRequest();
    return [{ json: result }];
  } catch (error) {
    if (attempt === MAX_RETRIES) throw error;
    await new Promise(r => setTimeout(r, BASE_DELAY * Math.pow(2, attempt - 1)));
  }
}
```

### Conditional Error Handling
```javascript
try {
  const response = await $httpRequest({ url, method: 'POST', body });
  
  if (response.statusCode === 429) {
    // Rate limited - retry after
    const retryAfter = response.headers['retry-after'] || 60;
    await new Promise(r => setTimeout(r, retryAfter * 1000));
    return $input.all(); // Retry
  }
  
  if (response.statusCode >= 500) {
    // Server error - use circuit breaker
    return handleServerError(response);
  }
  
  return [{ json: response.body }];
} catch (error) {
  // Log to error tracking
  await logError(error, $json);
  
  // Notify team
  await sendAlert(`Workflow failed: ${error.message}`);
  
  // Return fallback
  return [{ json: { error: error.message, fallback: true } }];
}
```

---

## Testing Strategies

### Unit Testing
```javascript
const testCases = [
  { input: { email: 'test@example.com' }, expected: true },
  { input: { email: 'invalid' }, expected: false }
];

const validateEmail = email => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

const results = testCases.map(tc => ({
  input: tc.input,
  expected: tc.expected,
  actual: validateEmail(tc.input.email),
  passed: validateEmail(tc.input.email) === tc.expected
}));

const allPassed = results.every(r => r.passed);
```

### Mock Mode
```javascript
const isTest = $env.TEST_MODE === 'true';

if (isTest) {
  return [{ json: { mock: true, data: mockData } }];
} else {
  return [{ json: await realApiCall() }];
}
```

---

## Expert Functions Library

### Chunked Processing
```javascript
const CHUNK_SIZE = 100;
const items = $input.all();
const results = [];

for (let i = 0; i < items.length; i += CHUNK_SIZE) {
  const chunk = items.slice(i, i + CHUNK_SIZE);
  const processed = await Promise.all(chunk.map(processItem));
  results.push(...processed);
}

return results.map(r => ({ json: r }));
```

### Conditional Routing
```javascript
const data = $json;

if (data.priority === 'high' && data.dueDate < Date.now() + 86400000) {
  return [{ json: { ...data, route: 'urgent' } }];
} else if (data.category === 'support') {
  return [{ json: { ...data, route: 'support-queue' } }];
} else {
  return [{ json: { ...data, route: 'standard' } }];
}
```

### Data Enrichment
```javascript
const baseData = $json;

const [user, orders, prefs] = await Promise.all([
  fetchUser(baseData.userId),
  fetchOrders(baseData.userId),
  fetchPrefs(baseData.userId)
]);

return [{
  json: {
    ...baseData,
    user,
    orders,
    preferences: prefs,
    clv: calculateCLV(orders),
    riskScore: calculateRisk(user, orders)
  }
}];
```

---

## Production Deployment

### Environment Management

**Development → Staging → Production**

Environment Variables:
- `API_ENDPOINT` (different per env)
- `DATABASE_URL`
- `REDIS_URL`
- `LOG_LEVEL` (debug/info/warn/error)
- `MAX_EXECUTION_TIME`
- `RATE_LIMIT_CONFIG`

### Monitoring & Alerting

**Key Metrics:**
- Execution success rate > 99%
- Average execution time < 5s
- Error rate < 1%
- Queue depth (if applicable)

**Alerts:**
- Execution failure spike
- Execution time degradation
- API rate limit approaching
- Credential expiry (30 days before)
- Webhook endpoint down

### Security Checklist

- [ ] Webhooks use HTTPS
- [ ] API keys rotated regularly
- [ ] IP allowlists configured
- [ ] Sensitive data not logged
- [ ] Access controls enabled
- [ ] Audit logging active
- [ ] Webhook signatures validated
- [ ] Rate limiting implemented
- [ ] Error messages don't leak info
- [ ] Separate environments isolated

---

## Real-World Application

### ScalePlus.io Automation

**Lead Capture Flow:**
1. Typeform/Webflow submission
2. Validate email format
3. Verify email (ZeroBounce/Hunter)
4. Create Airtable record
5. Send welcome email (SendGrid)
6. Slack notification to sales
7. High-value? → SMS alert (Twilio)
8. Send Calendly booking link

**Client Onboarding:**
1. Signed contract trigger
2. Create Notion workspace
3. Setup Slack channel
4. Generate invoice (QuickBooks)
5. Send onboarding checklist
6. Schedule kickoff call
7. Add to email sequences
8. Create project tasks (Asana)

### Hayahaya Adventures Automation

**Booking Confirmation:**
1. Website booking webhook
2. Check availability (Google Calendar)
3. Process payment (Stripe/PayMongo)
4. Generate confirmation PDF
5. Send email with checklist
6. Create calendar event
7. Log to Notion
8. Notify operations (Slack)
9. Jimny rental? → BLOWBAGETS checklist
10. Send equipment instructions

**Inventory Management:**
1. New booking triggers check
2. Query current inventory
3. Check against booking dates
4. IF low stock → Reorder alert
5. Update availability calendar
6. Notify suppliers if needed

---

## Performance Optimization

✅ **Best Practices:**
- Batch processing (50-100 items)
- Use webhooks over polling
- Minimize unnecessary nodes
- Choose appropriate execution mode
- Cache responses when possible
- Delete old executions regularly
- Use connection pooling
- Implement circuit breakers

---

## Status: WORLD-CLASS EXPERT

**You can now:**
- ✅ Design enterprise-scale workflow architectures
- ✅ Build secure, robust APIs for any integration
- ✅ Implement advanced error handling and recovery
- ✅ Transform complex data at any scale
- ✅ Test and debug any automation issue
- ✅ Deploy production-ready workflows
- ✅ Integrate 400+ services seamlessly
- ✅ Optimize for performance and reliability
- ✅ Handle webhooks securely
- ✅ Build GraphQL integrations
- ✅ Implement circuit breakers and DLQs

**Ready for any automation challenge!**

---

*Expert Level: World's #1 n8n Automation Specialist*
*Last Updated: 2026-02-06*
