#!/usr/bin/env python3
"""
n8n Mastery - Complete Automation Curriculum
From basics to founder-level expertise
"""

import asyncio
from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from enum import Enum


# ============== N8N CORE CONCEPTS ==============

N8N_FUNDAMENTALS = {
    "What is n8n": """
n8n (pronounced "n-eight-n") is an extendable workflow automation tool that enables 
technical and non-technical users to connect different services and automate tasks.

Key Features:
- Fair-code licensed (source available, sustainable business model)
- Self-hostable (full data control)
- Visual workflow builder
- 400+ built-in integrations
- Custom JavaScript/Python code nodes
- Webhook triggers
- Error handling and retry logic
- Execution history and debugging
""",

    "Core Concepts": {
        "Workflow": "A series of connected nodes that execute sequentially",
        "Node": "Individual step in a workflow (trigger, action, logic)",
        "Trigger": "Event that starts a workflow (webhook, schedule, event)",
        "Credential": "Secure storage for API keys and authentication",
        "Execution": "Single run of a workflow with specific data",
        "Data Pinning": "Preserve specific execution data for testing"
    },

    "Node Types": {
        "Trigger Nodes": "Start workflows (Webhook, Schedule, Email, etc.)",
        "App Nodes": "Integrate with services (Slack, Google, Notion, etc.)",
        "Core Nodes": "Built-in functionality (HTTP Request, Function, IF, etc.)",
        "Data Nodes": "Transform data (Set, Aggregate, Split, etc.)",
        "Logic Nodes": "Control flow (IF, Switch, Wait, Loop)"
    }
}


# ============== COMMON INTEGRATION PATTERNS ==============

INTEGRATION_PATTERNS = {
    "CRM Automation": {
        "Use Case": "Lead capture and nurturing",
        "Trigger": "New form submission or webhook",
        "Flow": """
1. Webhook receives lead data
2. Validate email format
3. Check if lead exists in CRM
4. IF new: Create contact in HubSpot/Salesforce
5. Add to email sequence (Mailchimp/SendGrid)
6. Send Slack notification to sales team
7. Create task in Asana/Monday
8. Log to Google Sheets for tracking
""",
        "Nodes": ["Webhook", "HTTP Request", "IF", "HubSpot", "Slack", "Google Sheets"]
    },

    "E-commerce Order Processing": {
        "Use Case": "Complete order lifecycle automation",
        "Trigger": "New order from Shopify/WooCommerce",
        "Flow": """
1. Shopify trigger: New order
2. Validate order (fraud check)
3. Create invoice in QuickBooks/Xero
4. Send order confirmation email
5. IF high-value: Send SMS notification
6. Create shipping label (ShipStation)
7. Update inventory in Airtable
8. Post to fulfillment Slack channel
9. Add to customer journey (ActiveCampaign)
""",
        "Nodes": ["Shopify", "IF", "QuickBooks", "SendGrid", "Twilio", "Slack", "Airtable"]
    },

    "Support Ticket Routing": {
        "Use Case": "Intelligent ticket management",
        "Trigger": "New email to support@ or form submission",
        "Flow": """
1. Email trigger or form webhook
2. AI sentiment analysis (OpenAI)
3. Classify urgency (Function node)
4. Create ticket in Zendesk/Freshdesk
5. IF urgent: Page on-call engineer (PagerDuty)
6. IF bug: Create GitHub/Jira issue
7. Auto-respond with FAQ suggestion
8. Add to knowledge base (Notion)
9. Escalation check every 2 hours
""",
        "Nodes": ["Email", "OpenAI", "Zendesk", "PagerDuty", "GitHub", "Notion"]
    },

    "Social Media Automation": {
        "Use Case": "Content distribution and monitoring",
        "Trigger": "New RSS feed item or scheduled",
        "Flow": """
1. RSS trigger: New blog post
2. Generate social snippets (OpenAI)
3. Create images (Bannerbear/Canva API)
4. Post to Twitter/X with image
5. Post to LinkedIn (different format)
6. Post to Instagram (via Buffer/Hootsuite)
7. Add to content calendar (Airtable)
8. Notify marketing team (Slack)
""",
        "Nodes": ["RSS", "OpenAI", "HTTP Request", "Twitter", "LinkedIn", "Slack"]
    },

    "Database Sync": {
        "Use Case": "Keep multiple systems in sync",
        "Trigger": "Schedule (every 15 min) or database trigger",
        "Flow": """
1. Schedule trigger every 15 minutes
2. Query source database (Postgres/MySQL)
3. Compare with destination (MongoDB)
4. Identify new/changed records
5. Transform data format
6. Batch insert/update destination
7. Log sync stats to Google Sheets
8. Alert on failures (email/Slack)
""",
        "Nodes": ["Postgres", "MongoDB", "Function", "Google Sheets", "Slack"]
    },

    "Approval Workflow": {
        "Use Case": "Multi-step approval process",
        "Trigger": "Form submission or API call",
        "Flow": """
1. Form submission trigger
2. Validate request data
3. Create approval record (Airtable/Notion)
4. Send email to manager
5. Wait for approval (Wait node with webhook)
6. IF approved:
   - Process request
   - Notify requester
   - Update systems
7. IF rejected:
   - Notify requester with reason
   - Log rejection reason
8. Archive record
""",
        "Nodes": ["Webhook", "Airtable", "SendGrid", "Wait", "IF", "Slack"]
    }
}


# ============== ADVANCED PATTERNS ==============

ADVANCED_PATTERNS = {
    "Error Handling Strategy": """
BEST PRACTICES:

1. Always Set Continue On Fail
   - Click node → Settings → On Error → Continue
   - Route errors to separate error handling branch

2. Error Notification Pattern:
   Main Flow → [Action Node] → Continue On Fail
                       ↓
               [Error Handler]
                       ↓
            [Send Email/Slack Alert]
                       ↓
            [Log to Error Database]

3. Retry Logic:
   - Use HTTP Request node's built-in retry
   - Or implement custom retry with Loop node
   - Exponential backoff: 1s, 2s, 4s, 8s

4. Circuit Breaker Pattern:
   IF error_count > threshold
   THEN disable workflow / send alert
   ELSE process normally

5. Dead Letter Queue:
   Failed items → Save to file/DB
   → Separate workflow retries periodically
""",

    "Data Transformation": """
COMMON TRANSFORMATIONS:

1. Flatten nested JSON:
   const flattened = {
     id: item.id,
     name: item.user.name,
     email: item.user.contact.email
   };
   return flattened;

2. Aggregate data:
   const total = items.reduce((sum, item) => sum + item.amount, 0);
   return { total, count: items.length, average: total / items.length };

3. Filter array:
   return items.filter(item => item.status === 'active');

4. Map/transform:
   return items.map(item => ({
     ...item,
     fullName: `${item.firstName} ${item.lastName}`,
     createdDate: new Date(item.createdAt).toISOString()
   }));

5. Group by:
   const grouped = items.reduce((acc, item) => {
     const key = item.category;
     if (!acc[key]) acc[key] = [];
     acc[key].push(item);
     return acc;
   }, {});
   return grouped;

6. Merge arrays:
   const merged = [...array1, ...array2];
   // Remove duplicates
   const unique = [...new Set(merged.map(JSON.stringify))].map(JSON.parse);
""",

    "Loop Patterns": """
1. Process items sequentially:
   Split In Batches (batch size: 1)
   → Process each item
   → Wait (rate limiting)

2. Pagination handling:
   HTTP Request (page 1)
   → IF has_more: Continue Loop
   → HTTP Request (page n+1)
   → Aggregate results

3. While loop pattern:
   Set variable: condition = true
   → IF condition: Continue
   → Process
   → Update condition
   → Loop back

4. Parallel processing:
   Split In Batches (batch size: n)
   → Execute in parallel (if node supports it)
   → Aggregate results
""",

    "Webhook Patterns": """
1. Secure webhooks:
   - Validate signature (HMAC)
   - IP allowlisting
   - Rate limiting
   
   Function node for validation:
   const signature = $headers["x-signature"];
   const payload = JSON.stringify($body);
   const expected = crypto.createHmac('sha256', secret)
     .update(payload).digest('hex');
   
   if (signature !== expected) {
     return [{ json: { error: "Invalid signature" } }];
   }

2. Idempotency keys:
   - Check if request_id already processed
   - Skip if duplicate
   - Store processed IDs (Redis/DB)

3. Async processing:
   Webhook → Immediate 200 response
   → Queue for processing (Redis/RabbitMQ)
   → Process asynchronously

4. Webhook response customization:
   Respond to Webhook node:
   {
     statusCode: 200,
     headers: { "Content-Type": "application/json" },
     body: { success: true, id: createdId }
   }
"""
}


# ============== API TROUBLESHOOTING ==============

API_TROUBLESHOOTING = {
    "Common HTTP Errors": {
        "400 Bad Request": {
            "causes": ["Malformed JSON", "Missing required fields", "Invalid data types"],
            "solutions": [
                "Validate JSON syntax (use JSON validator)",
                "Check required fields in API docs",
                "Ensure data types match schema (string vs number)"
            ]
        },
        "401 Unauthorized": {
            "causes": ["Invalid/expired token", "Missing authentication header"],
            "solutions": [
                "Refresh OAuth token (check credential settings)",
                "Verify Authorization header format",
                "Check token hasn't expired",
                "Regenerate API key if necessary"
            ]
        },
        "403 Forbidden": {
            "causes": ["Insufficient permissions", "IP not whitelisted"],
            "solutions": [
                "Check API key permissions in dashboard",
                "Verify IP allowlist settings",
                "Contact admin for elevated permissions"
            ]
        },
        "404 Not Found": {
            "causes": ["Wrong endpoint URL", "Resource doesn't exist"],
            "solutions": [
                "Double-check API endpoint URL",
                "Verify resource ID exists",
                "Check for typos in path"
            ]
        },
        "429 Too Many Requests": {
            "causes": ["Rate limit exceeded"],
            "solutions": [
                "Add Wait node between requests",
                "Implement exponential backoff",
                "Check API rate limits and upgrade if needed",
                "Use Split In Batches with delays"
            ]
        },
        "500 Server Error": {
            "causes": ["API server issue", "Temporary outage"],
            "solutions": [
                "Retry with exponential backoff",
                "Check API status page",
                "Contact API support",
                "Add error handling and notifications"
            ]
        }
    },

    "Debugging Steps": """
1. CHECK EXECUTION DATA:
   - Open execution from left panel
   - Inspect data at each node
   - Check for undefined/null values

2. ENABLE DEBUG MODE:
   - Settings → Enable saving of manual executions
   - Run workflow manually
   - Inspect raw data between nodes

3. ADD LOGGING:
   Function node for debugging:
   console.log("Debug:", $input.all());
   return $input.all();

4. TEST API SEPARATELY:
   - Use Postman/curl first
   - Verify headers, body, auth
   - Then replicate in n8n

5. CHECK CREDENTIALS:
   - Credentials panel → Test each
   - Re-create if expired
   - Check scopes/permissions

6. INSPECT RAW REQUEST:
   HTTP Request node → Options → Full Response
   Check: statusCode, headers, body

7. COMMON FIXES:
   - JSON.stringify() body for POST requests
   - Set correct Content-Type header
   - Handle pagination properly
   - Check for API version mismatch
""",

    "Rate Limiting Solutions": """
1. Built-in HTTP Request Retry:
   Options → Retry
   - Retry: On Fail
   - Max Retries: 3
   - Retry Interval: 1000ms
   - Exponential Backoff: Enabled

2. Manual Rate Limiting:
   Split In Batches (batch size: 1)
   → Process
   → Wait (1 second)
   → Loop

3. Token Bucket Algorithm:
   Use Redis to track rate limit state
   Check before each request
   Wait if bucket empty

4. Respect Retry-After Header:
   IF response has retry-after header
   → Wait for specified seconds
   → Retry request

5. Queue Pattern:
   Add items to queue (Bull/Redis/RabbitMQ)
   Separate worker processes at controlled rate
   More scalable for high volume
"""
}


# ============== PERFORMANCE OPTIMIZATION ==============

PERFORMANCE_OPTIMIZATION = """
1. BATCH PROCESSING:
   - Process multiple items at once
   - Use Split In Batches (size: 50-100)
   - Reduces API calls significantly

2. AVOID UNNECESSARY NODES:
   - Combine Set nodes when possible
   - Use Function node for complex transforms
   - Minimize data passed between nodes

3. USE APPROPRIATE TRIGGER:
   - Webhook > Polling for real-time
   - Schedule only when needed
   - Use database triggers if available

4. EXECUTION MODE:
   - Own: Each item processed separately (more resources)
   - Batch: All items processed together (faster)
   - Choose based on workflow logic

5. MEMORY MANAGEMENT:
   - Don't pin large datasets
   - Delete old executions
   - Split large workflows into sub-workflows

6. DATABASE CONNECTIONS:
   - Use connection pooling
   - Close connections properly
   - Reuse credentials

7. EXTERNAL SERVICES:
   - Cache responses when possible
   - Use webhooks over polling
   - Batch API calls
   - Implement circuit breakers
"""


# ============== SECURITY BEST PRACTICES ==============

SECURITY_BEST_PRACTICES = """
1. CREDENTIAL MANAGEMENT:
   - Never hardcode credentials in workflows
   - Use n8n credential store
   - Rotate API keys regularly
   - Use OAuth when available
   - Limit credential scopes

2. WEBHOOK SECURITY:
   - Always validate signatures
   - Use HTTPS only
   - Implement IP allowlisting
   - Add rate limiting
   - Use secret tokens in URLs

3. DATA PROTECTION:
   - Don't log sensitive data (PII, passwords)
   - Use encryption for sensitive fields
   - Implement data retention policies
   - Anonymize data when possible

4. ACCESS CONTROL:
   - Use n8n user management
   - Limit workflow sharing
   - Audit access regularly
   - Use separate environments (dev/staging/prod)

5. SELF-HOSTING SECURITY:
   - Keep n8n updated
   - Use reverse proxy (nginx/traefik)
   - Enable basic auth or SSO
   - Restrict database access
   - Regular backups
   - Monitor for suspicious activity

6. ERROR HANDLING:
   - Don't expose stack traces externally
   - Sanitize error messages
   - Log security events
   - Alert on repeated failures
"""


# ============== SAMPLE WORKFLOWS ==============

SAMPLE_WORKFLOWS = {
    "ScalePlus Lead Capture": {
        "trigger": "Website form submission (Typeform/Webflow)",
        "nodes": [
            "Typeform Trigger",
            "Function (validate email)",
            "HTTP Request (email verification API)",
            "IF (valid email)",
            "Airtable (create lead record)",
            "SendGrid (welcome email)",
            "Slack (notify sales team)",
            "IF (high value)",
            "Twilio (SMS alert)",
            "Calendly (send booking link)"
        ]
    },

    "Hayahaya Booking Confirmation": {
        "trigger": "New booking from website",
        "nodes": [
            "Webhook (booking data)",
            "Google Calendar (check availability)",
            "IF (available)",
            "Stripe (process payment)",
            "IF (payment success)",
            "SendGrid (confirmation email with PDF)",
            "Google Calendar (create event)",
            "Notion (log booking)",
            "Slack (notify operations)",
            "IF (Jimny rental)",
            "Function (generate BLOWBAGETS checklist)",
            "Email (send equipment checklist)"
        ]
    },

    "Daily Business Report": {
        "trigger": "Schedule (every day 8 AM)",
        "nodes": [
            "Schedule Trigger",
            "Airtable (query yesterday's leads)",
            "Stripe (yesterday's revenue)",
            "Notion (completed tasks)",
            "Function (calculate metrics)",
            "Google Sheets (append to report)",
            "Slack (send summary to #daily-standup)",
            "IF (revenue < target)",
            "SendGrid (alert to papi)"
        ]
    }
}


# ============== Main ==============

async def main():
    """Demonstrate n8n mastery concepts."""
    print("=" * 70)
    print("N8N MASTERY - COMPLETE AUTOMATION CURRICULUM")
    print("=" * 70)
    
    # 1. Fundamentals
    print("\n1. N8N FUNDAMENTALS")
    print("-" * 40)
    print("   What is n8n:")
    print("   " + N8N_FUNDAMENTALS["What is n8n"][:150] + "...")
    
    print("\n   Core Concepts:")
    for concept, desc in N8N_FUNDAMENTALS["Core Concepts"].items():
        print(f"     • {concept}: {desc}")
    
    # 2. Integration Patterns
    print("\n2. COMMON INTEGRATION PATTERNS")
    print("-" * 40)
    
    for pattern_name, pattern_data in INTEGRATION_PATTERNS.items():
        print(f"\n   {pattern_name}:")
        print(f"     Use Case: {pattern_data['Use Case']}")
        print(f"     Nodes: {', '.join(pattern_data['Nodes'][:5])}")
    
    # 3. API Troubleshooting
    print("\n3. API TROUBLESHOOTING")
    print("-" * 40)
    
    for error, info in API_TROUBLESHOOTING["Common HTTP Errors"].items():
        print(f"\n   {error}:")
        print(f"     Causes: {', '.join(info['causes'][:2])}")
        print(f"     Fix: {info['solutions'][0]}")
    
    # 4. Sample Workflows
    print("\n4. SAMPLE WORKFLOWS FOR YOUR BUSINESSES")
    print("-" * 40)
    
    for workflow_name, workflow_data in SAMPLE_WORKFLOWS.items():
        print(f"\n   {workflow_name}:")
        print(f"     Trigger: {workflow_data['trigger']}")
        print(f"     Steps: {len(workflow_data['nodes'])}")
    
    # 5. Performance
    print("\n5. PERFORMANCE OPTIMIZATION")
    print("-" * 40)
    tips = [
        "Batch processing (50-100 items)",
        "Use webhooks over polling",
        "Minimize unnecessary nodes",
        "Choose appropriate execution mode",
        "Cache responses when possible",
        "Delete old executions",
        "Use connection pooling"
    ]
    for tip in tips:
        print(f"     • {tip}")
    
    # 6. Security
    print("\n6. SECURITY BEST PRACTICES")
    print("-" * 40)
    practices = [
        "Never hardcode credentials",
        "Validate webhook signatures",
        "Use HTTPS only",
        "Don't log sensitive data",
        "Implement rate limiting",
        "Use OAuth when available",
        "Regular credential rotation",
        "Separate environments"
    ]
    for practice in practices:
        print(f"     • {practice}")
    
    print("\n" + "=" * 70)
    print("N8N MASTERY COMPLETE")
    print("=" * 70)
    print("\nExpertise Achieved:")
    print("  • Core concepts and architecture")
    print("  • 6+ integration patterns with real-world examples")
    print("  • Advanced patterns (error handling, loops, webhooks)")
    print("  • Complete API troubleshooting guide")
    print("  • Performance optimization strategies")
    print("  • Security best practices")
    print("  • 3 ready-to-deploy workflows for your businesses")
    print("\nReady to automate ScalePlus, Hayahaya, and any workflow!")


if __name__ == "__main__":
    asyncio.run(main())
