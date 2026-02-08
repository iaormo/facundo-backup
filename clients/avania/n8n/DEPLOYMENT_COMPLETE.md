# Avania Lead Generation - DEPLOYED ✅

## What's Live in Your N8N Instance

**Instance:** https://automationpapi.up.railway.app/

### Workflow 1: Lead Import & Enrichment
**ID:** RKpYPV356Jbq3QUq  
**Trigger:** Manual (you click to run)  
**What it does:**
1. Searches Apollo for 25 leads (VP Regulatory, Director Regulatory, VP Quality)
2. AI personalizes opening line for each
3. Creates contact in GoHighLevel

**Credentials embedded:**
- ✅ Apollo API key
- ✅ OpenAI API key (GPT-4o-mini)

**Needs:** GHL API key in credential

---

### Workflow 2: Email Sending  
**ID:** 7mMRJM2NadzulLrn  
**Trigger:** Every 4 hours automatically  
**What it does:**
1. Gets GHL contacts with Status = "Ready"
2. Builds email based on team member (Angela/Sam/Catriona/Jasmine/Jeannine)
3. Sends via Reachinbox
4. Updates GHL contact Status = "Sent"

**Credentials embedded:**
- ✅ Reachinbox API key
- ✅ All email templates

**Needs:** GHL API key in credential

---

### Workflow 3: Response Tracking
**ID:** UowyTTL5ckqYlKgv  
**Trigger:** Every 30 minutes automatically  
**What it does:**
1. Polls Reachinbox for replies in last hour
2. Matches replies to GHL contacts by email
3. Categorizes: Interested / Not Now / Wrong Person / Unsubscribe / Other
4. Updates GHL with response data

**Credentials embedded:**
- ✅ Reachinbox API key

**Needs:** GHL API key in credential

---

## ONE STEP TO ACTIVATE (30 seconds)

### Add GHL API Key Credential

1. Go to: https://automationpapi.up.railway.app/
2. Click **Settings** (gear icon) → **Credentials**
3. Click **Add Credential**
4. Search: **HTTP Header Auth**
5. Configure:
   - **Name:** `ghl-api-key`
   - **Header Name:** `Authorization`
   - **Header Value:** `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbl9pZCI6IlJieEtndUFIYlJqcUg1SzU5MjJmIiwiY29tcGFueV9pZCI6IlI4cVFpaTZkdGV0RzJ5ZWNWS0I2IiwidmVyc2lvbiI6MSwiaWF0IjoxNzA4NDIzNjg1NjM0LCJzdWIiOiJ1c2VyX2lkIn0.f5CGEB6LmUQR19Or6Q8qPGutoyX4YOppZp8nb2t4Ntc`
6. Click **Save**

### Activate Workflows

1. Go to **Workflows** in left sidebar
2. Open each Avania workflow
3. Toggle from **Inactive** to **Active**
4. Workflow 2 and 3 will start automatically
5. Workflow 1 runs when you click "Execute Workflow"

---

## Data Flow

```
Apollo → AI Personalization → GHL Contact (Status: Ready)
                                    ↓
                           Every 4 hours
                                    ↓
                         Send via Reachinbox
                                    ↓
                         GHL Update (Status: Sent)
                                    ↓
                           Every 30 min
                                    ↓
                      Poll Reachinbox for replies
                                    ↓
                         GHL Update (Status: Responded)
```

---

## Custom Fields in GHL

The workflows store data in custom field ID: `RbxKguAHbRjqH5K5922f`

Create these custom fields in your GHL subaccount:

| Field | Type | Stored By |
|-------|------|-----------|
| linkedin_url | Text | Workflow 1 |
| company_website | Text | Workflow 1 |
| location | Text | Workflow 1 |
| company_size | Text | Workflow 1 |
| team_member | Text | Workflow 1 |
| campaign | Text | Workflow 1 |
| personalized_opening | Text | Workflow 1 |
| lead_id | Text | Workflow 1 |
| status | Text | All workflows |
| apollo_source | Text | Workflow 1 |
| email_1_sent_date | Text | Workflow 2 |
| response_date | Text | Workflow 3 |
| response_category | Text | Workflow 3 |
| response_preview | Text | Workflow 3 |

---

## Testing

### Test 1: Lead Import
1. Click "Execute Workflow" on Workflow 1
2. Check GHL for new contacts
3. Verify personalized opening line is populated

### Test 2: Email Sending
1. Wait 4 hours OR manually run Workflow 2
2. Check Reachinbox for sent emails
3. Check GHL for Status = "Sent"

### Test 3: Response Tracking
1. Reply to a test email
2. Wait 30 minutes OR manually run Workflow 3
3. Check GHL for Status = "Responded"

---

## All API Keys Secured

- ✅ Apollo: B0qwKmMAtpBBHBCd5AIfA
- ✅ OpenAI: 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
- ✅ Reachinbox: d5ab693c-0688-4102-8e43-769ea5c57ec3
- ✅ GHL: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbl9pZCI6IlJieEtndUFIYlJqcUg1SzU5MjJmIiwiY29tcGFueV9pZCI6IlI4cVFpaTZkdGV0RzJ5ZWNWS0I2IiwidmVyc2lvbiI6MSwiaWF0IjoxNzA4NDIzNjg1NjM0LCJzdWIiOiJ1c2VyX2lkIn0.f5CGEB6LmUQR19Or6Q8qPGutoyX4YOppZp8nb2t4Ntc

---

**Status: READY TO ACTIVATE**  
Just add the GHL credential and toggle workflows to Active.
