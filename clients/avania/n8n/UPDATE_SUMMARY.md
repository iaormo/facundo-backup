# Avania Lead Gen - UPDATED & DEPLOYED ✅

## What's New

### 1. Apollo Searches by Team Member Criteria
Each team member has their own Apollo search with specific targeting:

**Angela (Strategic Regulatory):**
- Titles: VP/SVP Regulatory, Chief Regulatory Officer, VP Quality
- Size: 51-1000 employees
- Revenue: $10M+
- Keywords: medtech, cardiovascular, neurology, AI device, breakthrough device
- Results: 20 leads

**Sam (Digital Health/AI):**
- Titles: VP Engineering, CTO, Head of Data Science, VP R&D
- Size: 11-500 employees
- Keywords: digital health, AI medical device, SaMD, ECG, wearable, machine learning
- Results: 20 leads

**Catriona (Quality/QMSR):**
- Titles: VP Quality, Director Quality, Quality Manager, COO
- Size: 11-500 employees
- Keywords: FDA, ISO 13485, quality management, QMS
- Results: 20 leads

**Jasmine (Strategic Partnerships):**
- Titles: CEO, COO, CFO, Chief Strategy Officer
- Size: 51-5000 employees
- Funding: $20M+
- Keywords: medtech, clinical trials, global expansion
- Results: 15 leads

**Jeannine (Business Development):**
- Titles: VP Regulatory, VP Clinical Ops, Director RA/QA, COO
- Size: 11-500 employees
- Keywords: clinical trial, regulatory consulting, 510(k), PMA, CRO
- Results: 20 leads

**Total per run: ~95 leads (75-85 unique after de-duplication)**

---

### 2. Reachinbox Uses Avania Workspace Email
- **From:** `team@avaniaclinical.com`
- Not individual team member emails
- Signature in email body shows actual team member name

---

### 3. Leads Tagged in GHL
Each contact stored with:
- `team_member`: Angela/Sam/Catriona/Jasmine/Jeannine
- `campaign`: Specific campaign name
- `lead_id`: Unique ID with prefix (AV-A-, AV-S-, AV-C-, AV-J-, AV-BD-)
- `personalized_opening`: AI-generated based on team member's angle

---

## Deployed Workflows

| Workflow | ID | Status |
|----------|-----|--------|
| Apollo Import by Team Member | e0ef81af-f4b4-4f79-b34e-774c6ea758d0 | Inactive |
| Email Sending (Avania Workspace) | a2ed8954-5306-41de-85f3-91a012b22620 | Inactive |
| Response Tracking | ac03eb3d-ffac-44e9-9002-f434e64c9310 | Inactive |

---

## To Activate

1. Go to https://automationpapi.up.railway.app/
2. Add GHL credential (HTTP Header Auth):
   - Name: `ghl-api-key`
   - Header: `Authorization`
   - Value: `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`
3. Open each workflow → Toggle to **Active**

---

## How It Works

1. **Workflow 1** (Manual): Searches Apollo 5x (once per team member), combines results, removes duplicates, AI personalizes, creates GHL contacts

2. **Workflow 2** (Every 4 hrs): Gets GHL contacts with Status=Ready, builds email with team member's template, sends from team@avaniaclinical.com, updates GHL to Sent

3. **Workflow 3** (Every 30 min): Polls Reachinbox for replies, matches to GHL contacts, categorizes response (Interested/Not Now/Wrong Person/Unsubscribe), updates GHL

---

All files saved to: `/data/workspace/clients/avania/n8n/`
