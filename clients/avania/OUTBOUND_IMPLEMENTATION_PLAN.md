# Avania Outbound Automation System — Implementation Plan

**Client:** Avania Clinical  
**Objective:** Automated outbound lead generation using Apollo + web enrichment + personalized outreach via Reachinbox  
**Tracking:** Google Sheets pipeline  
**Date:** February 6, 2026

---

## SYSTEM ARCHITECTURE OVERVIEW

```
┌─────────────────────────────────────────────────────────────────┐
│                    LEAD GENERATION FLOW                         │
└─────────────────────────────────────────────────────────────────┘

Apollo (Lead Sourcing)
    ↓
Web Enrichment (Company/Person Research)
    ↓
AI Personalization Engine (Opening Lines + Email Variants)
    ↓
Reachinbox (Email Sending + Warmup)
    ↓
Google Sheets (Tracking + CRM)
    ↓
Response Handling → Handoff to Avania Team Members
```

---

## PHASE 1: TECH STACK SETUP

### 1.1 Apollo Configuration

**Apollo Account:** TBD (need Avania to provide or create)

**Search Criteria by Team Member:**

#### Angela Johnson — Strategic Regulatory
**Accounts:**
- Industry: Medical Devices, Biotechnology
- Keywords: "medtech", "cardiovascular", "neurology", "AI device", "digital health", "breakthrough device"
- Size: 50-500 employees
- Funding: Series B-D, $10M-$500M valuation
- Geography: US, Canada

**People:**
- Titles: CEO, COO, Chief Strategy Officer, VP Regulatory Affairs, VP Quality
- Seniority: VP+, C-suite, Director (at smaller companies)

**Apollo Filters:**
```
Industries: Medical Devices, Biotechnology, Computer Software (medical)
Company Size: 50-500 employees
Funding Stage: Series B, C, D, Venture
Job Titles: VP Regulatory Affairs, Chief Strategy Officer, COO, CEO, VP Quality
Location: United States, Canada
```

---

#### Sam Engelman — Digital Health/AI
**Accounts:**
- Industry: Medical Devices, Computer Software
- Keywords: "digital health", "AI medical device", "SaMD", "ECG", "cardiac monitoring", "diagnostic algorithm", "wearable"
- Size: 11-200 employees
- Funding: Seed-Series C
- Geography: US, Canada, UK, EU

**People:**
- Titles: VP Engineering, CTO, Director Regulatory Affairs, VP Product, Head of Data Science
- Seniority: VP, Director, Head

**Apollo Filters:**
```
Industries: Medical Devices, Computer Software
Company Size: 11-200 employees
Funding Stage: Seed, Series A, B, C
Job Titles: VP Engineering, CTO, Director Regulatory Affairs, VP Product, Head of Data Science
Technologies: Machine Learning, AI, Healthcare Software
Location: United States, Canada, UK, EU
```

---

#### Catriona Boyd — Quality/QMSR
**Accounts:**
- Industry: Medical Devices
- Keywords: "FDA", "ISO 13485", "quality management", "medical device manufacturer"
- Size: 11-500 employees
- Geography: US (primary), Canada (secondary)

**People:**
- Titles: VP Quality Assurance, Director Quality, Quality Manager, COO
- Seniority: VP, Director, Manager

**Apollo Filters:**
```
Industries: Medical Devices, Biotechnology
Company Size: 11-500 employees
Job Titles: VP Quality Assurance, Director Quality, Quality Manager, Director QA/RA
Location: United States, Canada
Signals: Recently funded, Hiring (quality roles)
```

---

#### Jasmine Saba — Strategic Partnerships
**Accounts:**
- Industry: Medical Devices, Biotechnology
- Keywords: "growth stage", "venture funded", "clinical trials", "global expansion"
- Size: 100-1000 employees
- Funding: Series C-E, IPO preparation
- Geography: US, Canada, EU

**People:**
- Titles: CEO, COO, Chief Strategy Officer, CFO, VP Business Development
- Seniority: C-suite, VP+

**Apollo Filters:**
```
Industries: Medical Devices, Biotechnology
Company Size: 100-1000 employees
Funding Stage: Series C, D, E, Pre-IPO
Job Titles: CEO, COO, Chief Strategy Officer, CFO, VP Strategic Planning
Location: United States, Canada, EU
```

---

#### Jeannine Umpleby — Business Development
**Accounts:**
- Industry: Medical Devices
- Keywords: "CRO", "clinical trial", "regulatory consulting", "510(k)", "PMA"
- Size: 11-500 employees
- Geography: US (primary), Canada, EU

**People:**
- Titles: VP Regulatory Affairs, VP Clinical Operations, Director RA, Director QA, COO
- Seniority: VP, Director, Head

**Apollo Filters:**
```
Industries: Medical Devices, Biotechnology
Company Size: 11-500 employees
Job Titles: VP Regulatory Affairs, VP Clinical Operations, Director RA, Director QA, COO
Location: United States, Canada, EU
```

---

### 1.2 Apollo List Structure

**Naming Convention:**
```
Avania_[TeamMember]_[Segment]_[Date]

Examples:
- Avania_Angela_StrategicRegulatory_2026-02-06
- Avania_Sam_DigitalHealth_2026-02-06
- Avania_Catriona_QMSR_2026-02-06
```

**Initial Volume Targets:**
- Angela: 100-150 leads/week
- Sam: 150-200 leads/week
- Catriona: 100-150 leads/week
- Jasmine: 75-100 leads/week (higher touch, lower volume)
- Jeannine: 150-200 leads/week

---

## PHASE 2: WEB ENRICHMENT SETUP

### 2.1 Enrichment Data Points

**For Each Lead, Enrich:**

**Company Level:**
- Website URL
- Company description (from website/LinkedIn)
- Recent funding announcements (Crunchbase, PitchBook)
- Recent news/press releases
- Product/device focus
- Therapeutic area
- Geographic markets they serve
- Regulatory milestones (FDA clearances, CE marks)
- Clinical trial activity (ClinicalTrials.gov)

**Person Level:**
- LinkedIn profile summary
- Recent LinkedIn posts/activity
- Job tenure (how long at company)
- Previous companies
- Educational background
- Mutual connections (if any)

### 2.2 Enrichment Tools Options

**Option A: n8n + APIs (Recommended)**
- n8n workflow triggered by new Apollo leads
- API calls to: LinkedIn (scraping), company website, Crunchbase, news APIs
- Output: Structured enrichment data

**Option B: Clay + n8n**
- Use Clay for enrichment (waterfall enrichment)
- n8n for workflow orchestration
- More user-friendly, slightly more expensive

**Option C: PhantomBuster**
- LinkedIn profile scraping
- Company website scraping
- Less flexible but easier setup

---

## PHASE 3: AI PERSONALIZATION ENGINE

### 3.1 Personalization Logic

**Trigger:** Enrichment data received

**Process:**
1. Analyze company + person data
2. Identify personalization hooks:
   - Recent funding → "Congrats on the Series B..."
   - FDA clearance → "Saw your recent FDA 510(k) for [device]..."
   - Therapeutic area → "Your work in [cardiovascular/neurology]..."
   - LinkedIn activity → "Saw your post about [topic]..."
   - Mutual challenge → "Most [AI device] companies I talk to..."

3. Generate 3 personalized opening line variants
4. Select best match based on confidence score

### 3.2 Opening Line Templates by Hook Type

**Funding Hook:**
- "Congrats on {{company}}'s recent {{funding_round}}—growing from {{previous_stage}} to {{current_stage}} typically brings new regulatory complexity..."

**FDA Clearance Hook:**
- "Saw {{company}} secured FDA 510(k) for {{device_name}} last {{month}}—congrats. Most companies at this stage start thinking about {{next_challenge}}..."

**Therapeutic Area Hook:**
- "Your work in {{therapeutic_area}} caught my attention—I've been supporting {{similar_companies}} with {{specific_challenge}}..."

**LinkedIn Activity Hook:**
- "Saw your recent post about {{topic}}—{{insightful_comment}}. It resonates with what we're seeing across {{segment}}..."

**Challenge-Based Hook:**
- "Most {{company_type}} companies I talk to are dealing with {{common_challenge}} right now—is that on your radar at {{company}}?"

---

### 3.3 n8n Personalization Workflow

```
[Apollo Lead Export] 
    → [Web Enrichment Node]
        → [Data Parsing Node]
            → [OpenAI Prompt Node] 
                → [Quality Check Node]
                    → [Output to Sheets]
```

**OpenAI Prompt Structure:**
```
Given this lead data:
- Company: {{company_name}}
- Industry: {{industry}}
- Description: {{company_description}}
- Recent News: {{recent_news}}
- Person: {{first_name}} {{last_name}}
- Title: {{job_title}}
- LinkedIn Summary: {{linkedin_summary}}
- Recent Posts: {{recent_posts}}

Generate 3 personalized opening lines for an email about {{campaign_topic}}.

Opening lines should:
1. Be 1-2 sentences max
2. Reference specific, relevant details from the data
3. Sound natural and conversational
4. Lead into the value proposition naturally

Output format:
Option 1: [opening line]
Option 2: [opening line]
Option 3: [opening line]
Reasoning: [why these work]
```

---

## PHASE 4: REACHINBOX SETUP

### 4.1 Account Structure

**Email Domain Strategy:**
Option 1: Use @avaniaclinical.com (main domain) — simpler, less risky
Option 2: Use variations for each team member:
- angela.johnson@avaniaclinical.com
- sam.engelman@avaniaclinical.com
- catriona.boyd@avaniaclinical.com
- jasmine.saba@avaniaclinical.com
- jeannine.umpleby@avaniaclinical.com

**Recommendation:** Use Option 2 for authenticity—emails come from the actual person

### 4.2 Warmup Configuration

**Per Account:**
- Warmup duration: 2-3 weeks minimum before cold outreach
- Daily warmup emails: 10-20
- Ramp to cold: Start with 5-10 cold emails/day, scale to 30-50/day
- Total daily volume (warmup + cold): 40-60 emails/account

### 4.3 Sending Schedule

**Optimal Send Times (US Eastern):**
- Tuesday-Thursday primary
- 8:00-10:00 AM (prospect local time)

**Per Account Daily Limits:**
- Angela: 30-50 emails/day
- Sam: 40-60 emails/day
- Catriona: 30-50 emails/day
- Jasmine: 20-30 emails/day (higher touch)
- Jeannine: 40-60 emails/day

---

## PHASE 5: GOOGLE SHEETS TRACKING

### 5.1 Master Tracking Sheet Structure

**Sheet 1: Lead Database**
| Column | Description |
|--------|-------------|
| Lead ID | Unique identifier |
| Team Member | Assigned Avania person |
| Campaign | QMSR / AI-Device / Strategic / etc. |
| First Name | |
| Last Name | |
| Email | |
| Company | |
| Title | |
| Industry | |
| Company Size | |
| Funding Stage | |
| Location | |
| Enrichment Status | Complete / Pending / Failed |
| Personalization Hook Type | Funding / FDA / Therapeutic / LinkedIn / Challenge |
| Personalized Opening Line | |
| Email 1 Status | Sent / Delivered / Bounced |
| Email 1 Date | |
| Email 2 Status | |
| Email 2 Date | |
| Email 3 Status | |
| Email 3 Date | |
| Response Status | No Response / Replied / Meeting Booked / Unsubscribed |
| Response Date | |
| Response Category | Interested / Not Now / Wrong Person / OOO |
| Meeting Status | Pending / Scheduled / Completed / No Show |
| Meeting Date | |
| Notes | |
| Last Updated | |

**Sheet 2: Campaign Performance**
| Metric | Angela | Sam | Catriona | Jasmine | Jeannine | Total |
|--------|--------|-----|----------|---------|----------|-------|
| Leads Added | | | | | | |
| Enriched | | | | | | |
| Emails Sent | | | | | | |
| Delivered | | | | | | |
| Opened | | | | | | |
| Open Rate | | | | | | |
| Replied | | | | | | |
| Response Rate | | | | | | |
| Meetings Booked | | | | | | |
| Meeting Rate | | | | | | |

**Sheet 3: Weekly Activity Log**
| Week | Team Member | Leads Added | Emails Sent | Responses | Meetings Booked |
|------|-------------|-------------|-------------|-----------|-----------------|

---

### 5.2 Automation: Sheets ↔ n8n

**Inbound (Apollo → Sheets):**
- Apollo list export (CSV) → Upload to Google Drive → n8n watches folder → Parses CSV → Adds to Lead Database sheet

**Outbound (Sheets → Reachinbox):**
- n8n polls Sheets for "Ready to Send" status
- Pulls lead data + personalized opening line
- Sends to Reachinbox API
- Updates Sheets with "Sent" status + timestamp

**Response Tracking (Reachinbox → Sheets):**
- Reachinbox webhook on reply → n8n receives → Updates Sheets with reply status
- Slack/email notification to assigned team member

---

## PHASE 6: RESPONSE HANDLING WORKFLOW

### 6.1 Response Categories & Actions

| Response Type | Action | Next Step |
|--------------|--------|-----------|
| **Interested / Positive** | Handoff to assigned team member | Calendar booking link + personal outreach |
| **Not Now / Timing** | Move to nurture sequence | Add to "Check Back in 90 Days" list |
| **Wrong Person** | Ask for referral | Update contact info + find right person |
| **Unsubscribe / Negative** | Remove from sequence | Flag in CRM, no further outreach |
| **Out of Office** | Pause sequence | Resume after return date |
| **Bounced** | Flag for verification | Try alternative contact method |

### 6.2 Handoff to Avania Team

**Notification Trigger:** Positive response received

**Notification Includes:**
- Lead contact info
- Company details
- Campaign context
- Email thread history
- Suggested next steps

**Notification Method:**
- Slack DM to assigned team member
- Email alert
- Dashboard update

---

## PHASE 7: A/B TESTING FRAMEWORK

### 7.1 Testable Elements

**Subject Lines:**
- Variable: Length (short vs. long), Question vs. Statement, Personalization vs. Generic
- Test: 2-3 variants per campaign
- Sample size: 100 emails per variant minimum

**Opening Lines:**
- Variable: Hook type (funding vs. therapeutic vs. challenge-based)
- Test: Rotate variants evenly
- Sample size: 100 emails per variant

**CTA:**
- Variable: "30-minute call" vs. "strategy session" vs. "quick conversation"
- Test: Same email body, different CTA
- Sample size: 150 emails per variant

**Email Length:**
- Variable: 80-100 words vs. 120-150 words
- Test: Especially for Sam (technical) vs. Jasmine (executive)
- Sample size: 200 emails per variant

### 7.2 Testing Schedule

**Week 1-2:** Baseline (use current templates, establish benchmarks)
**Week 3-4:** Subject line test
**Week 5-6:** Opening line test
**Week 7-8:** CTA test
**Week 9-10:** Email length test
**Ongoing:** Continuous optimization

---

## PHASE 8: COMPLIANCE & BEST PRACTICES

### 8.1 CAN-SPAM Compliance

**Required:**
- Physical mailing address in email footer
- Clear unsubscribe link
- Accurate "From" name and email
- Subject lines not misleading

**Best Practices:**
- Honor unsubscribes within 48 hours
- Maintain suppression list
- Warm up domains properly
- Monitor bounce rates (<5%)
- Monitor spam complaints (<0.1%)

### 8.2 Deliverability Monitoring

**Daily Checks:**
- Bounce rate per account
- Spam complaint rate
- Domain reputation (Google Postmaster Tools)
- IP reputation

**Weekly Checks:**
- Inbox placement tests
- Blacklist checks
- Email authentication (SPF, DKIM, DMARC)

---

## IMPLEMENTATION TIMELINE

### Week 1: Foundation
- [ ] Apollo account setup + list creation
- [ ] Reachinbox account setup + email account creation
- [ ] Google Sheets template creation
- [ ] n8n workflow scaffolding

### Week 2: Enrichment & Personalization
- [ ] Web enrichment tool selection + setup
- [ ] AI personalization prompt development
- [ ] Test enrichment on 50 sample leads
- [ ] Refine personalization outputs

### Week 3: Integration & Testing
- [ ] Connect Apollo → n8n → Sheets
- [ ] Connect Sheets → Reachinbox
- [ ] End-to-end test with 20 leads
- [ ] Fix integration issues

### Week 4: Warmup & Soft Launch
- [ ] Begin email warmup (all 5 accounts)
- [ ] Load first 100 leads per team member
- [ ] Soft launch (5-10 emails/day per account)
- [ ] Monitor deliverability + responses

### Week 5: Scale
- [ ] Ramp to full volume (30-50 emails/day per account)
- [ ] Launch all 5 campaigns simultaneously
- [ ] Begin A/B testing
- [ ] Weekly performance reviews

### Week 6+: Optimize
- [ ] Analyze performance data
- [ ] Implement winning variants
- [ ] Refresh lead lists
- [ ] Continuous optimization

---

## TECH STACK SUMMARY

| Function | Tool | Cost Estimate |
|----------|------|---------------|
| Lead Sourcing | Apollo.io | ~$100-200/mo |
| Workflow Automation | n8n (self-hosted) | ~$50/mo hosting |
| Web Enrichment | n8n + APIs / Clay | ~$100-300/mo |
| AI Personalization | OpenAI API | ~$50-100/mo |
| Email Sending | Reachinbox | ~$100-200/mo |
| Tracking | Google Sheets | Free |
| Notifications | Slack | Free |
| **Total** | | **~$400-850/mo** |

---

## SUCCESS METRICS

### Targets by Month 3:

| Metric | Target |
|--------|--------|
| Total Leads Added | 2,500+ |
| Enrichment Rate | >90% |
| Email Delivery Rate | >95% |
| Open Rate | >25% |
| Response Rate | >5% |
| Meeting Booked Rate | >2% |
| Total Meetings Booked | 50+ |

### ROI Calculation:
- Average Avania engagement value: $50K-200K
- Close rate from meeting to client: ~20-30%
- Target: 2-3 new clients per quarter from outbound

---

## NEXT STEPS

**Immediate Actions Needed:**

1. **Apollo Access:** Confirm Apollo account credentials or create new account
2. **Domain/Email Setup:** Confirm email addresses for each of the 5 team members
3. **Reachinbox Access:** Set up Reachinbox account + connect email accounts
4. **n8n Instance:** Confirm n8n hosting (OpenClaw node or external)
5. **Sheet Template:** Create Google Sheet with proper structure + sharing permissions
6. **Lead List Priority:** Which campaign launches first? (Recommendation: Catriona QMSR - hottest market)

---

*Implementation plan created: February 6, 2026*  
*Status: Ready for execution*
