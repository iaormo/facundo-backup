# Avania N8N Workflows - Final Build Package

## Credentials Configured

### OpenAI API
- **Key:** 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
- **Model:** GPT-4o-mini (as specified)
- **Use:** AI personalization for email opening lines

### Apollo API
- **Key:** B0qwKmMAtpBBHBCd5AIfA
- **Endpoint:** https://api.apollo.io/api/v1/mixed_people/api_search
- **Use:** Lead sourcing and enrichment

### Reachinbox API
- **Key:** d5ab693c-0688-4102-8e43-769ea5c57ec3
- **Use:** Email sending and tracking

### Google Sheets
- **Sheet ID:** 1_I9TSxw1CIFf24C3IbA1Q0LR-hCzKTTyBzzpnFu1dho
- **Sheet URL:** https://docs.google.com/spreadsheets/d/1_I9TSxw1CIFf24C3IbA1Q0LR-hCzKTTyBzzpnFu1dho/edit?usp=sharing

---

## How to Import Workflows

Since the n8n API has limitations for complex workflow creation, please import manually:

### Step 1: Download the 3 JSON Files
The workflow files are located at:
- `/data/workspace/clients/avania/n8n/01-lead-import-enrichment.json`
- `/data/workspace/clients/avania/n8n/02-email-sending.json`
- `/data/workspace/clients/avania/n8n/03-response-tracking.json`

### Step 2: Add Credentials in N8N

1. Go to your n8n instance: https://automationpapi.up.railway.app/
2. Click **Settings** (gear icon) → **Credentials**
3. Add these credentials:

#### OpenAI API Credential
- Click "Add Credential"
- Search: "OpenAI API"
- Name: `openai-api-credentials`
- API Key: `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`
- Save

#### Google Sheets OAuth2
- Click "Add Credential"
- Search: "Google Sheets OAuth2 API"
- Name: `google-sheets-credentials`
- You need to complete OAuth flow (see below)

### Step 3: Set Up Google Sheets Service Account

**Why needed:** The sheet needs to be accessed by a service account

1. Go to https://console.cloud.google.com/
2. Create a new project or select existing
3. Enable **Google Sheets API**
4. Go to **IAM & Admin** → **Service Accounts**
5. Click **Create Service Account**
6. Name it: `n8n-avania-integration`
7. Grant role: **Editor**
8. Create key: **JSON** format
9. Download the JSON file
10. Copy the `client_email` from the JSON (looks like: `...@...gserviceaccount.com`)
11. Share your Google Sheet with that email address (give Editor access)
12. In n8n credentials, use the JSON key contents

### Step 4: Import Workflows

1. In n8n, click **Workflows** in left sidebar
2. Click **Import from File**
3. Select `01-lead-import-enrichment.json`
4. The workflow will open - review and save
5. Repeat for files 2 and 3

### Step 5: Configure Environment Variables

Add these to your Railway environment variables:

```bash
GOOGLE_SHEETS_ID=1_I9TSxw1CIFf24C3IbA1Q0LR-hCzKTTyBzzpnFu1dho
APOLLO_API_KEY=B0qwKmMAtpBBHBCd5AIfA
OPENAI_API_KEY=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
```

In Railway:
1. Go to your project dashboard
2. Click on your n8n service
3. Go to **Variables** tab
4. Add each variable above
5. Redeploy

### Step 6: Set Up Reachinbox Webhook

1. Copy your webhook URL:
```
https://automationpapi.up.railway.app/webhook/avania-reachinbox-webhook
```

2. Log into Reachinbox dashboard
3. Go to **Settings** → **Webhooks**
4. Add new webhook:
   - URL: `https://automationpapi.up.railway.app/webhook/avania-reachinbox-webhook`
   - Events: `email.replied`, `email.opened`, `email.clicked`
5. Save

### Step 7: Activate Workflows

1. Open each workflow
2. Click the **Inactive** toggle to make it **Active**
3. For Workflow 2 (Email Sending), the schedule trigger will start automatically
4. For Workflow 3 (Response Tracking), the webhook is now listening

---

## Testing the System

### Test 1: Lead Import
1. Add a test row to your Google Sheet:
   - Status: Pending
   - Enrichment Status: Pending
   - First Name: Test
   - Last Name: User
   - Email: your-email@example.com
   - Company: Test Company
   - Team Member: Angela
   - Campaign: QMSR

2. Run Workflow 1 manually
3. Check if personalization is generated

### Test 2: Email Sending
1. Change Status to "Ready"
2. Run Workflow 2 manually
3. Check if email is sent via Reachinbox

### Test 3: Response Tracking
1. Reply to the test email
2. Check if webhook fires (view in n8n executions)
3. Check if Sheets is updated

---

## Security Note

⚠️ **API keys are sensitive!** 
- Never commit them to Git
- Never share them in public channels
- The keys provided are now stored only in this secure workspace
- After setup, delete any files containing raw keys

---

## Support

If you need help with import:
1. The workflow JSON files are complete and ready
2. Credentials must be added manually in n8n UI
3. Google Sheets requires service account setup
4. Reachinbox webhook needs to be configured

All files are saved in `/data/workspace/clients/avania/n8n/`

---

*Build completed: February 7, 2026*
