# Avania Outbound Tracking — Google Sheets Template

## Sheet 1: Lead Database

**Columns (A-Z):**

| Column | Header | Data Type | Notes |
|--------|--------|-----------|-------|
| A | Lead ID | Text | AUTO-001, AUTO-002, etc. |
| B | Team Member | Dropdown | Angela / Sam / Catriona / Jasmine / Jeannine |
| C | Campaign | Dropdown | QMSR / AI-Device / Strategic / General BD / ISO13485 |
| D | Status | Dropdown | New / Enriching / Ready / Sending / Sent / Responded / Meeting Booked / Closed / Unsubscribed |
| E | First Name | Text | |
| F | Last Name | Text | |
| G | Email | Text | |
| H | Company | Text | |
| I | Title | Text | |
| J | Industry | Text | Medical Devices / Biotechnology / Digital Health |
| K | Company Size | Number | Employee count |
| L | Funding Stage | Text | Seed / Series A / B / C / D / Public |
| M | Location | Text | City, State / Country |
| N | Company Website | URL | |
| O | LinkedIn URL | URL | |
| P | Enrichment Status | Dropdown | Pending / Complete / Failed |
| Q | Personalization Hook | Dropdown | Funding / FDA / Therapeutic / LinkedIn / Challenge / None |
| R | Personalized Opening Line | Text | AI-generated opening |
| S | Email 1 Status | Dropdown | Pending / Sent / Delivered / Bounced |
| T | Email 1 Date | Date | |
| U | Email 2 Status | Dropdown | Pending / Sent / Delivered / Bounced |
| V | Email 2 Date | Date | |
| W | Email 3 Status | Dropdown | Pending / Sent / Delivered / Bounced |
| X | Email 3 Date | Date | |
| Y | Response Status | Dropdown | No Response / Replied / Meeting Booked / Unsubscribed / Bounced |
| Z | Response Date | Date | |
| AA | Response Category | Dropdown | Interested / Not Now / Wrong Person / OOO / Unsubscribe / Negative |
| AB | Meeting Status | Dropdown | N/A / Pending / Scheduled / Completed / No Show / Cancelled |
| AC | Meeting Date | Date/Time | |
| AD | Meeting Notes | Text | |
| AE | Owner (Avania) | Text | Which Avania team member owns follow-up |
| AF | Created Date | Date | Auto-populated |
| AG | Last Updated | Date/Time | Auto-populated |
| AH | Notes | Text | Freeform notes |

---

## Sheet 2: Campaign Performance Dashboard

**Structure:**

| Metric | Angela | Sam | Catriona | Jasmine | Jeannine | TOTAL |
|--------|--------|-----|----------|---------|----------|-------|
| **Leads** |
| Leads Added | Formula | Formula | Formula | Formula | Formula | =SUM(B2:F2) |
| Enriched | Formula | Formula | Formula | Formula | Formula | =SUM(B3:F3) |
| Enrichment Rate | =B3/B2 | =C3/C2 | =D3/D2 | =E3/E2 | =F3/F2 | =G3/G2 |
| **Emails** |
| Emails Sent | Formula | Formula | Formula | Formula | Formula | =SUM(B6:F6) |
| Delivered | Formula | Formula | Formula | Formula | Formula | =SUM(B7:F7) |
| Delivery Rate | =B7/B6 | =C7/C6 | =D7/D6 | =E7/E6 | =F7/F6 | =G7/G6 |
| Opened | Formula | Formula | Formula | Formula | Formula | =SUM(B10:F10) |
| Open Rate | =B10/B7 | =C10/C7 | =D10/D7 | =E10/E7 | =F10/F7 | =G10/G7 |
| **Responses** |
| Replied | Formula | Formula | Formula | Formula | Formula | =SUM(B13:F13) |
| Response Rate | =B13/B10 | =C13/C10 | =D13/D10 | =E13/E10 | =F13/F10 | =G13/G10 |
| Interested | Formula | Formula | Formula | Formula | Formula | =SUM(B15:F15) |
| Not Now | Formula | Formula | Formula | Formula | Formula | =SUM(B16:F16) |
| Wrong Person | Formula | Formula | Formula | Formula | Formula | =SUM(B17:F17) |
| **Meetings** |
| Meetings Booked | Formula | Formula | Formula | Formula | Formula | =SUM(B19:F19) |
| Meeting Rate | =B19/B13 | =C19/C13 | =D19/D13 | =E19/E13 | =F19/F13 | =G19/G13 |
| Meetings Completed | Formula | Formula | Formula | Formula | Formula | =SUM(B21:F21) |
| **A/B Tests** |
| Subject Line Winner | Text | Text | Text | Text | Text | |
| Opening Line Winner | Text | Text | Text | Text | Text | |
| CTA Winner | Text | Text | Text | Text | Text | |

---

## Sheet 3: Weekly Activity Log

**Columns:**

| Week Starting | Team Member | Leads Added | Emails Sent | Opens | Replies | Meetings Booked | Notes |
|--------------|-------------|-------------|-------------|-------|---------|-----------------|-------|
| 2026-02-10 | Angela | | | | | | |
| 2026-02-10 | Sam | | | | | | |
| 2026-02-10 | Catriona | | | | | | |
| 2026-02-10 | Jasmine | | | | | | |
| 2026-02-10 | Jeannine | | | | | | |

---

## Sheet 4: A/B Test Results

**Structure:**

| Test ID | Team Member | Element Tested | Variant A | Variant B | Variant C | Winner | Sample Size | Confidence |
|---------|-------------|----------------|-----------|-----------|-----------|--------|-------------|------------|
| AB-001 | Angela | Subject Line | "QMSR is live..." | "Feb 2 changed..." | | | 200 | |
| AB-002 | Sam | Opening Hook | Funding | Therapeutic | Challenge | | 300 | |

---

## Sheet 5: Suppression List

**Columns:**

| Email | Company | Reason | Date Added | Added By |
|-------|---------|--------|------------|----------|
| | | Unsubscribe / Bounced / Competitor / Requested No Contact | | |

---

## Google Sheets Setup Instructions

### Step 1: Create the Sheet
1. Go to Google Sheets
2. Create new spreadsheet: "Avania Outbound Campaign Tracker"
3. Create 5 tabs: Lead Database, Performance Dashboard, Weekly Log, A/B Tests, Suppression List

### Step 2: Set Up Data Validation (Dropdowns)

**For Status Column (Lead Database):**
```
New, Enriching, Ready, Sending, Sent, Responded, Meeting Booked, Closed, Unsubscribed
```

**For Team Member Column:**
```
Angela, Sam, Catriona, Jasmine, Jeannine
```

**For Campaign Column:**
```
QMSR, AI-Device, Strategic, General BD, ISO13485, Breakthrough
```

**For Personalization Hook:**
```
Funding, FDA, Therapeutic, LinkedIn, Challenge, None
```

**For Response Category:**
```
Interested, Not Now, Wrong Person, OOO, Unsubscribe, Negative
```

### Step 3: Add Formulas

**Auto-Numbering Lead IDs:**
```
="AUTO-"&TEXT(ROW(A2),"000")
```

**Performance Dashboard Formulas:**
Use COUNTIFS to calculate metrics:
```
=COUNTIFS('Lead Database'!B:B, "Angela", 'Lead Database'!D:D, "Enriched")
```

### Step 4: Share Access

**Share with:**
- Ian (papi) - Editor
- Each Avania team member - Viewer (or Editor if they need to update)
- Automation service account - Editor (for n8n integration)

### Step 5: Connect to n8n

**Google Sheets Credentials:**
1. Google Cloud Console → APIs & Services → Credentials
2. Create Service Account
3. Download JSON key
4. Share Sheet with service account email
5. Use in n8n Google Sheets node

---

## Automation Formulas

### Lead Database Auto-Population

**Created Date:**
```
=IF(A2="","",TODAY())
```

**Last Updated:**
Use Google Apps Script to auto-update on edit:
```javascript
function onEdit(e) {
  var sheet = e.source.getActiveSheet();
  var row = e.range.getRow();
  var col = e.range.getColumn();
  
  if (sheet.getName() == "Lead Database" && row > 1) {
    sheet.getRange(row, 33).setValue(new Date()); // Column AG
  }
}
```

---

## Conditional Formatting Rules

### Lead Database Sheet:

1. **Status = "Meeting Booked"** → Green background
2. **Status = "Unsubscribed"** → Red background
3. **Status = "Responded"** → Yellow background
4. **Response Category = "Interested"** → Light green text
5. **Enrichment Status = "Failed"** → Red text
6. **Email 1 Status = "Bounced"** → Red background

### Performance Dashboard:

1. **Open Rate > 30%** → Green
2. **Open Rate 20-30%** → Yellow
3. **Open Rate < 20%** → Red
4. **Response Rate > 5%** → Green
5. **Meeting Rate > 2%** → Green

---

*Template created: February 6, 2026*
