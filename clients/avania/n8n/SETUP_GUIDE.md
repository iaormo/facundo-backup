# Avania N8N Workflows - Setup Guide

## Overview

Three interconnected workflows for automated lead generation:

1. **Lead Import & Enrichment** - Imports leads from Apollo/CSV, enriches with AI personalization
2. **Email Sending** - Scheduled sending via Reachinbox with follow-up sequences
3. **Response Tracking** - Webhook receiver for replies, updates Sheets, Slack notifications

---

## Prerequisites

### Required Accounts

1. **n8n Instance**
   - Self-hosted (Docker) OR n8n.cloud
   - Version 1.0+ recommended

2. **Google Cloud Console**
   - Google Sheets API enabled
   - Service account with Sheets access
   - Download service account JSON key

3. **OpenAI**
   - API key from platform.openai.com
   - GPT-4o-mini access (or GPT-3.5-turbo as fallback)

4. **Reachinbox**
   - Account with API access
   - API Key: `d5ab693c-0688-4102-8e43-769ea5c57ec3`
   - Email accounts warmed up and connected

5. **Apollo** (Optional - can use CSV import instead)
   - API key for direct integration
   - Or export leads manually to CSV

6. **Slack** (Optional - for notifications)
   - Slack app with bot token
   - Channel ID for notifications

---

## Environment Variables

Create a `.env` file in your n8n environment:

```bash
# Google Sheets
GOOGLE_SHEETS_ID=your_google_sheet_id_here

# OpenAI
OPENAI_API_KEY=sk-your_openai_key_here

# Apollo (optional)
APOLLO_API_KEY=your_apollo_api_key_here

# Reachinbox (provided)
REACHINBOX_API_KEY=d5ab693c-0688-4102-8e43-769ea5c57ec3

# Slack (optional)
SLACK_CHANNEL_ID=C1234567890
SLACK_BOT_TOKEN=xoxb-your-token-here

# Sheet URL (for Slack links)
GOOGLE_SHEETS_URL=https://docs.google.com/spreadsheets/d/YOUR_ID/edit
```

---

## Google Sheets Setup

### 1. Create the Sheet

1. Go to [Google Sheets](https://sheets.google.com)
2. Create new spreadsheet: "Avania Outbound Campaign Tracker"
3. Create tabs:
   - Lead Database
   - Performance Dashboard
   - Weekly Log
   - A/B Tests
   - Suppression List

### 2. Share with Service Account

1. Get service account email from JSON key (ends with `@...gserviceaccount.com`)
2. Share sheet with that email (Editor access)
3. Copy the Sheet ID from URL: `https://docs.google.com/spreadsheets/d/SHEET_ID/edit`

### 3. Lead Database Headers

Row 1 must contain these headers:

```
Lead ID | Team Member | Campaign | Status | First Name | Last Name | Email | Company | Title | Industry | Company Size | Funding Stage | Location | Company Website | LinkedIn URL | Enrichment Status | Personalization Hook | Personalized Opening Line | Email 1 Status | Email 1 Date | Email 2 Status | Email 2 Date | Email 3 Status | Email 3 Date | Response Status | Response Date | Response Category | Meeting Status | Meeting Date | Meeting Notes | Owner (Avania) | Created Date | Last Updated | Notes
```

---

## N8N Credentials Setup

### 1. Google Sheets OAuth2

1. In n8n: Settings → Credentials → Add Credential
2. Search: "Google Sheets OAuth2 API"
3. Configure:
   - Client ID: From Google Cloud Console
   - Client Secret: From Google Cloud Console
   - Scopes: `https://www.googleapis.com/auth/spreadsheets`
4. Complete OAuth flow

### 2. OpenAI API

1. Add Credential → "OpenAI API"
2. API Key: Your OpenAI key

### 3. Slack API (Optional)

1. Add Credential → "Slack API"
2. Access Token: Your bot token

---

## Workflow Import

### Method 1: JSON Import

1. Open n8n Editor
2. Workflow menu (⋮) → Import from File
3. Import each workflow:
   - `01-lead-import-enrichment.json`
   - `02-email-sending.json`
   - `03-response-tracking.json`

### Method 2: Copy-Paste JSON

1. Open workflow JSON file
2. Copy entire content
3. n8n Editor → Workflow menu → Import from JSON
4. Paste and save

---

## Workflow Configuration

### Workflow 1: Lead Import & Enrichment

**Trigger Options:**
- Manual: Click "Execute Workflow" to run on demand
- Schedule: Add Schedule Trigger node for automated runs

**Nodes to Configure:**

1. **Read New Leads**
   - Credential: Select your Google Sheets OAuth2
   - Document ID: `={{ $env.GOOGLE_SHEETS_ID }}`
   - Sheet Name: `Lead Database`

2. **AI Personalization**
   - Credential: Select OpenAI API
   - Model: `gpt-4o-mini` (or `gpt-3.5-turbo`)

3. **Update Lead Database**
   - Credential: Google Sheets OAuth2
   - Same Document ID

### Workflow 2: Email Sending

**Schedule:**
- Runs every 4 hours by default
- Adjust in Schedule Trigger node as needed

**Nodes to Configure:**

1. **Read Ready Leads**
   - Same Google Sheets config

2. **Send via Reachinbox**
   - API key is hardcoded: `d5ab693c-0688-4102-8e43-769ea5c57ec3`
   - Verify this matches your account

3. **Send Follow-up**
   - Same API key

**Email Templates:**
- Edit in "Build Email Content" node JavaScript code
- Customize subject lines and body text per team member
- Include CAN-SPAM compliant footer

### Workflow 3: Response Tracking

**Webhook URL:**
- Copy webhook URL after activating workflow
- Example: `https://your-n8n.com/webhook/avania-reachinbox-webhook`
- Configure this URL in Reachinbox webhook settings

**Nodes to Configure:**

1. **Slack Notification** (optional)
   - Credential: Select Slack API
   - Channel ID: Set via environment variable or hardcode

2. **Hot Lead Alert** (optional)
   - Same Slack config
   - Only fires for "Interested" responses

---

## Reachinbox Webhook Setup

1. Log into Reachinbox dashboard
2. Go to Settings → Webhooks
3. Add webhook:
   - URL: Your n8n webhook URL (from Workflow 3)
   - Events: `email.replied`, `email.opened`, `email.clicked`
4. Save and test

---

## Testing

### Test Lead Import

1. Add 2-3 test rows to Google Sheets with:
   - Status: `Pending`
   - Enrichment Status: `Pending`
   - Valid email addresses you control

2. Run Workflow 1 manually
3. Check Sheets for updated status and personalization

### Test Email Sending

1. Verify test leads show Status: `Ready`
2. Run Workflow 2 manually
3. Check email delivery in Reachinbox
4. Verify Sheets updates to Status: `Sent`

### Test Response Tracking

1. Reply to test email from your inbox
2. Check if webhook fires (n8n execution log)
3. Verify Sheets updates Response Status
4. Check Slack notification (if configured)

---

## Daily Operations

### Adding New Leads

**Option A: Apollo CSV Import**
1. Export leads from Apollo as CSV
2. Import to Google Sheets (match column headers)
3. Set Status: `Pending`, Enrichment Status: `Pending`
4. Run Workflow 1

**Option B: Apollo API (in workflow)**
1. Uncomment "Apollo Search" node in Workflow 1
2. Configure search parameters in node
3. Run to auto-import

### Monitoring

1. **Google Sheets**: Check daily for new responses
2. **n8n Executions**: Review for errors
3. **Reachinbox Dashboard**: Monitor deliverability
4. **Slack**: Get real-time notifications

### Troubleshooting

**No emails sending:**
- Check Sheets has leads with Status: `Ready`
- Verify Reachinbox API key
- Check n8n execution logs for errors

**Personalization failing:**
- Verify OpenAI API key
- Check OpenAI credit balance
- Review "Parse AI Output" node for errors

**Responses not tracking:**
- Verify webhook URL in Reachinbox
- Check webhook is POST method
- Test webhook with curl or Postman

**Slack not notifying:**
- Verify bot is in channel
- Check bot permissions
- Test with simple message node

---

## Security Notes

1. **API Keys**: Store in n8n credentials, never in workflow JSON
2. **Environment Variables**: Use for sensitive config
3. **Google Sheets**: Service account only needs Sheets access
4. **Webhook**: Use HTTPS, consider adding auth token
5. **Logs**: Redact PII in execution logs if needed

---

## Customization

### Add More Team Members

1. Add to "Build Email Content" node switch statement
2. Create email template for new team member
3. Update fromEmail format if needed

### Change Email Templates

1. Edit JavaScript code in "Build Email Content" node
2. Keep personalization: `${openingLine}` at start
3. Update subject lines
4. Add CAN-SPAM footer

### Adjust Follow-up Timing

In "Filter 5-Day Followup" node:
- Current: 5 days after Email 1
- Change: Modify the `$now.minus({ days: 5 })` line

### Add Third Follow-up

1. Duplicate "Filter 5-Day Followup" node
2. Change to 10 days
3. Add "Email 3 Status" check
4. Build new email template

---

## Support

- **n8n Docs**: docs.n8n.io
- **OpenAI Docs**: platform.openai.com/docs
- **Reachinbox Support**: support@reachinbox.io
- **Avania Project**: Contact papi

---

*Setup Guide created: February 7, 2026*
