# Avania Lead Generation System - N8N Workflows

## Deliverables

### Workflow Files (JSON)

| File | Purpose | Trigger |
|------|---------|---------|
| `01-lead-import-enrichment.json` | Import leads, AI personalization, update Sheets | Manual or Schedule |
| `02-email-sending.json` | Send emails via Reachinbox, 5-day follow-ups | Every 4 hours |
| `03-response-tracking.json` | Webhook receiver, track replies, Slack alerts | Reachinbox Webhook |

### Documentation

- `SETUP_GUIDE.md` - Complete installation and configuration guide

---

## Workflow 1: Lead Import & Enrichment

**What it does:**
1. Reads leads from Google Sheets (Status = "Pending")
2. Filters for enrichment
3. Calls OpenAI to generate personalized opening lines
4. Parses AI output to extract hook type and best opening line
5. Updates Sheets with enriched data (Status = "Ready")

**Optional Apollo Integration:**
- Can search Apollo API directly and add leads to Sheets
- Currently commented out - enable if you want direct API import

**Environment Variables:**
- `GOOGLE_SHEETS_ID`
- `OPENAI_API_KEY`

---

## Workflow 2: Email Sending

**What it does:**
1. Runs every 4 hours (Schedule Trigger)
2. Reads leads from Sheets (Status = "Ready", Email 1 not sent)
3. Limits batch to 25 emails per run (rate limiting)
4. Builds personalized email using team member template
5. Sends via Reachinbox API
6. Updates Sheets (Status = "Sent", Email 1 Status = "Sent")
7. Also checks for 5-day follow-ups and sends those

**Email Templates Included:**
- Angela Johnson (QMSR focus)
- Catriona Boyd (Quality/QMSR focus)
- Sam Engelman (AI/ML devices focus)
- Jasmine Saba (Strategic partnerships)
- Jeannine Umpleby (General BD)

**Follow-up Templates:**
- Automatic 5-day follow-up for non-responders
- Shorter, reference original email

**Hardcoded Values:**
- Reachinbox API Key: `d5ab693c-0688-4102-8e43-769ea5c57ec3`

---

## Workflow 3: Response Tracking

**What it does:**
1. Receives webhook from Reachinbox when someone replies
2. Parses webhook payload to extract email, subject, body
3. Categorizes response: Interested / Not Now / Wrong Person / OOO / Unsubscribe
4. Finds matching lead in Google Sheets by email
5. Updates Sheets with Response Status, Category, Date
6. Sends Slack notification with response preview
7. Extra alert for "Interested" responses (hot lead)

**Webhook URL Pattern:**
```
https://your-n8n-domain.com/webhook/avania-reachinbox-webhook
```

**Response Categorization Logic:**
- **Interested**: Keywords like "interested", "yes", "schedule", "meeting", "call"
- **Not Now**: "not now", "not interested", "timing", "later"
- **Wrong Person**: "wrong person", "not the right", "contact"
- **Unsubscribe**: "unsubscribe", "remove", "stop"
- **OOO**: "out of office", "ooo", "vacation"
- **Other**: Everything else

---

## Installation Steps

### 1. Prepare Google Sheets

Create sheet with tabs:
- Lead Database
- Performance Dashboard
- Weekly Log
- A/B Tests
- Suppression List

Add headers to Lead Database tab (see SETUP_GUIDE.md for full list)

### 2. Set Up Credentials in N8N

- Google Sheets OAuth2
- OpenAI API
- Slack API (optional)

### 3. Import Workflows

1. Open n8n Editor
2. Workflow menu → Import from File
3. Import all 3 JSON files
4. Activate each workflow

### 4. Configure Environment Variables

Create `.env` file with:
```
GOOGLE_SHEETS_ID=your_sheet_id
OPENAI_API_KEY=sk-...
APOLLO_API_KEY=optional
REACHINBOX_API_KEY=d5ab693c-0688-4102-8e43-769ea5c57ec3
SLACK_CHANNEL_ID=optional
SLACK_BOT_TOKEN=optional
GOOGLE_SHEETS_URL=full_sheet_url
```

### 5. Configure Reachinbox Webhook

1. Get webhook URL from Workflow 3 (after activation)
2. Add to Reachinbox dashboard: Settings → Webhooks
3. Subscribe to events: email.replied, email.opened, email.clicked

### 6. Test

1. Add 2-3 test leads to Sheets
2. Run Workflow 1 manually
3. Verify personalization generated
4. Run Workflow 2 manually
5. Reply to test email
6. Verify webhook fires and Sheets updates

---

## Daily Usage

### Adding Leads

1. Export leads from Apollo to CSV
2. Import to Google Sheets Lead Database
3. Set columns:
   - Status: `Pending`
   - Enrichment Status: `Pending`
   - Team Member: (Angela/Sam/Catriona/Jasmine/Jeannine)
   - Campaign: (QMSR/AI-Device/Strategic/General BD)
4. Run Workflow 1 or wait for schedule

### Monitoring

- Check Google Sheets for new responses
- Check Slack for real-time notifications
- Check n8n executions for errors
- Review Reachinbox dashboard for deliverability

---

## Customization Points

### Change Email Templates

Edit JavaScript in "Build Email Content" node:
- Subject lines
- Body text
- Signature format
- CAN-SPAM footer

### Adjust Send Schedule

In Workflow 2:
- Change Schedule Trigger from "every 4 hours"
- Options: Every hour, Every day at specific time, etc.

### Change Follow-up Timing

In Workflow 2, "Filter 5-Day Followup" node:
- Current: 5 days after first email
- Modify: `$now.minus({ days: 5 })` to different number

### Add More Follow-ups

Duplicate the follow-up logic:
1. Add filter for 10 days
2. Check Email 2 Status = "Sent"
3. Check Email 3 Status is empty
4. Build Email 3 template
5. Send and update Sheets

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Emails not sending | Check Sheets has "Ready" leads, verify Reachinbox API key |
| AI personalization fails | Check OpenAI API key, verify credit balance |
| Webhook not firing | Verify URL in Reachinbox, check webhook is POST |
| Slack not working | Verify bot in channel, check token permissions |
| Sheets not updating | Verify service account has edit access, check column names |

---

## File Locations

```
/data/workspace/clients/avania/n8n/
├── 01-lead-import-enrichment.json
├── 02-email-sending.json
├── 03-response-tracking.json
└── SETUP_GUIDE.md
```

---

*System ready for deployment*
