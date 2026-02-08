# Avania Apollo Lead Criteria by Team Member

## Overview
Each Avania team member targets different personas. The system searches Apollo for each criteria set, tags leads by team member, and stores in GoHighLevel.

---

## Angela Johnson - Strategic Regulatory

**Role:** Global MedTech Executive, Regulatory Affairs  
**Campaign:** Strategic Regulatory

### Apollo Search Criteria
| Filter | Value |
|--------|-------|
| **Job Titles** | VP Regulatory Affairs, SVP Regulatory Affairs, Chief Regulatory Officer, VP Quality Assurance, Director Regulatory Affairs, VP Quality |
| **Locations** | United States, Canada |
| **Company Size** | 51-200, 201-500, 501-1000 employees |
| **Keywords** | medtech, medical device, cardiovascular, neurology, AI device, digital health, breakthrough device |
| **Revenue** | $10M+ (q_revenue_gte: 10000000) |
| **Email Status** | Verified only |
| **Results** | 20 leads per run |

### Target Profile
- C-suite and VP-level regulatory leaders
- Mid to large medtech companies ($10M+ revenue)
- Companies with complex regulatory needs (Breakthrough, AI devices)
- Series B-D funded companies

### Email Hook
QMSR compliance, Breakthrough Device strategy, AI/SaMD regulatory pathways

---

## Sam Engelman - Digital Health/AI

**Role:** Director, Regulatory Affairs  
**Campaign:** AI/ML Devices

### Apollo Search Criteria
| Filter | Value |
|--------|-------|
| **Job Titles** | VP Engineering, CTO, Director Regulatory Affairs, VP Product, Head of Data Science, VP R&D |
| **Locations** | United States, Canada, United Kingdom |
| **Company Size** | 11-50, 51-200, 201-500 employees |
| **Keywords** | digital health, AI medical device, SaMD, ECG, cardiac monitoring, diagnostic algorithm, wearable, machine learning |
| **Email Status** | Verified only |
| **Results** | 20 leads per run |

### Target Profile
- Technical leaders (CTOs, VP Engineering, Data Science heads)
- AI/ML-enabled device companies
- Digital health startups and scale-ups
- Companies with software components

### Email Hook
PCCP (Predetermined Change Control Procedures), AI device regulatory strategy, SaMD 510(k) pathways

---

## Catriona Boyd - Quality/QMSR

**Role:** Director, Quality Services  
**Campaign:** QMSR Compliance

### Apollo Search Criteria
| Filter | Value |
|--------|-------|
| **Job Titles** | VP Quality Assurance, Director Quality, Quality Manager, VP QA/RA, COO, VP Operations |
| **Locations** | United States, Canada |
| **Company Size** | 11-50, 51-200, 201-500 employees |
| **Keywords** | FDA, ISO 13485, quality management, medical device manufacturer, QMS |
| **Email Status** | Verified only |
| **Results** | 20 leads per run |

### Target Profile
- Quality leaders and managers
- Companies building or optimizing QMS
- Canadian companies entering US market
- Companies facing FDA inspections

### Email Hook
QMSR transition (urgent - took effect Feb 2), ISO 13485 certification, FDA inspection readiness

---

## Jasmine Saba - Strategic Partnerships

**Role:** SVP Strategic Relationships  
**Campaign:** Strategic Partnerships

### Apollo Search Criteria
| Filter | Value |
|--------|-------|
| **Job Titles** | CEO, COO, Chief Strategy Officer, CFO, VP Strategic Planning, VP Business Development |
| **Locations** | United States, Canada, United Kingdom, Germany |
| **Company Size** | 51-200, 201-500, 501-1000, 1001-5000 employees |
| **Keywords** | medtech, medical device, clinical trials, global expansion |
| **Funding** | $20M+ total funding (q_funding_total_gte: 20000000) |
| **Email Status** | Verified only |
| **Results** | 15 leads per run |

### Target Profile
- C-suite executives
- Growth-stage companies (Series C-E)
- Companies planning M&A or IPO
- Global expansion candidates

### Email Hook
Strategic CRO partnerships, investor readiness, global market expansion

---

## Jeannine Umpleby - Business Development

**Role:** Director, Business Development  
**Campaign:** Full-Service CRO

### Apollo Search Criteria
| Filter | Value |
|--------|-------|
| **Job Titles** | VP Regulatory Affairs, VP Clinical Operations, Director RA, Director QA, COO, Head of Clinical |
| **Locations** | United States, Canada, United Kingdom |
| **Company Size** | 11-50, 51-200, 201-500 employees |
| **Keywords** | clinical trial, regulatory consulting, 510(k), PMA, CRO |
| **Email Status** | Verified only |
| **Results** | 20 leads per run |

### Target Profile
- Decision makers in regulatory, clinical, quality
- Companies evaluating CRO partners
- Startups needing end-to-end support
- Companies with upcoming submissions

### Email Hook
Integrated CRO services (regulatory + clinical + quality), QMSR transition, full-service value proposition

---

## Lead Tagging System

Each lead is tagged in GoHighLevel custom fields:

| Field | Description |
|-------|-------------|
| `team_member` | Angela / Sam / Catriona / Jasmine / Jeannine |
| `campaign` | Strategic Regulatory / AI/ML Devices / QMSR Compliance / Strategic Partnerships / Full-Service CRO |
| `lead_id` | Unique ID (e.g., AV-A-1234567890-0 for Angela leads) |
| `source` | Apollo |
| `status` | Ready → Sent → Responded |

---

## De-duplication

The system automatically removes duplicates by email address across all five searches. If a contact matches multiple criteria, they are tagged by the first team member's search that found them.

---

## Total Lead Volume

Per run:
- Angela: 20 leads
- Sam: 20 leads
- Catriona: 20 leads
- Jasmine: 15 leads
- Jeannine: 20 leads
- **Total: ~95 leads per run** (after de-duplication: ~75-85 unique)

Recommended frequency: Run once daily or twice weekly to avoid overwhelming the system.

---

## Reachinbox Configuration

**From Email:** `team@avaniaclinical.com` (Avania workspace email)

All emails send from the main Avania workspace, not individual team member emails. The signature in the email body shows the specific team member's name and title.

---

*Criteria extracted from Avania campaign documentation*
