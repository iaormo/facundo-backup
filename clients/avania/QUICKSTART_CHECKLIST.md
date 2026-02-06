# Avania Outbound System — Quick Start Checklist

**Project:** Automated outbound lead generation for 5 Avania team members  
**Stack:** Apollo → Web Enrichment → AI Personalization → Reachinbox → Google Sheets  
**Goal:** 50+ meetings booked per quarter

---

## PHASE 1: ACCESS & ACCOUNTS (Days 1-3)

### Apollo.io Setup
- [ ] Create Apollo account OR confirm existing account access
- [ ] Verify data export permissions (need CSV export)
- [ ] Test API access if available
- [ ] Create 5 separate lead lists (one per team member)

### Email Infrastructure (Reachinbox)
- [ ] Create Reachinbox account
- [ ] Set up 5 email accounts:
  - [ ] angela.johnson@avaniaclinical.com
  - [ ] sam.engelman@avaniaclinical.com
  - [ ] catriona.boyd@avaniaclinical.com
  - [ ] jasmine.saba@avaniaclinical.com
  - [ ] jeannine.umpleby@avaniaclinical.com
- [ ] Configure SPF, DKIM, DMARC records
- [ ] Start warmup process (2-3 weeks minimum)

### Google Sheets
- [ ] Create "Avania Outbound Campaign Tracker" sheet
- [ ] Create 5 tabs as per template
- [ ] Set up data validation dropdowns
- [ ] Add conditional formatting
- [ ] Share with team members

### n8n Automation
- [ ] Confirm n8n instance (OpenClaw node or external)
- [ ] Install required nodes: Google Sheets, HTTP Request, OpenAI
- [ ] Set up credential storage securely
- [ ] Test connectivity to all services

---

## PHASE 2: DATA & ENRICHMENT (Days 4-7)

### Lead Sourcing
- [ ] Export first batch from Apollo (50 leads per team member = 250 total)
- [ ] Upload to Google Sheets Lead Database
- [ ] Verify data quality (emails, titles, companies)

### Enrichment Setup
- [ ] Configure web scraping workflow in n8n
- [ ] Test enrichment on 10 sample leads
- [ ] Verify data accuracy:
  - [ ] Company descriptions
  - [ ] Recent funding news
  - [ ] LinkedIn activity
  - [ ] Therapeutic area identification
- [ ] Refine enrichment logic based on test results

### Personalization Engine
- [ ] Create OpenAI prompt templates
- [ ] Test personalization on enriched leads (20 samples)
- [ ] Review opening lines with Avania team
- [ ] Adjust tone/voice as needed
- [ ] Set up quality scoring (reject low-confidence personalizations)

---

## PHASE 3: INTEGRATION & TESTING (Days 8-10)

### Workflow Integration
- [ ] Build n8n workflow: Apollo → Enrichment → Personalization → Sheets
- [ ] Build n8n workflow: Sheets → Reachinbox (sending)
- [ ] Build n8n workflow: Reachinbox → Sheets (response tracking)
- [ ] Set up Slack notifications for responses

### End-to-End Testing
- [ ] Test complete flow with 5 test leads (one per team member)
- [ ] Verify emails send correctly
- [ ] Verify tracking updates in Sheets
- [ ] Test response handling workflow
- [ ] Check deliverability (inbox placement)

### Email Template Finalization
- [ ] Load final email templates into Reachinbox
- [ ] Configure sequences (Email 1 → 5 days → Email 2 → 10 days → Email 3)
- [ ] Set up unsubscribe handling
- [ ] Add CAN-SPAM compliant footers

---

## PHASE 4: SOFT LAUNCH (Days 11-14)

### Initial Send
- [ ] Load 100 leads (20 per team member)
- [ ] Start with 5 emails/day per account (25 total/day)
- [ ] Monitor deliverability closely
- [ ] Check for bounces, spam complaints
- [ ] Track open rates, response rates

### Daily Monitoring (First Week)
- [ ] Morning: Check overnight sends/deliveries
- [ ] Afternoon: Review responses, handoff to team members
- [ ] End of day: Update Sheets, note any issues

### Quick Wins
- [ ] Identify any immediate responses
- [ ] Fast-track interested prospects to team
- [ ] Document what's working

---

## PHASE 5: SCALE & OPTIMIZE (Week 3+)

### Volume Ramp
- [ ] Week 3: 10 emails/day per account (50/day)
- [ ] Week 4: 20 emails/day per account (100/day)
- [ ] Week 5+: 30-50 emails/day per account (150-250/day)

### A/B Testing
- [ ] Week 3: Launch subject line tests
- [ ] Week 5: Analyze results, implement winner
- [ ] Week 6: Launch opening line tests
- [ ] Ongoing: Continuous optimization

### List Refresh
- [ ] Weekly: Export new leads from Apollo
- [ ] Weekly: Remove unsubscribed/bounced contacts
- [ ] Monthly: Refresh stale leads (not opened after 3 emails)

---

## DAILY OPERATIONS CHECKLIST

### Morning (15 min)
- [ ] Check Sheets for new responses
- [ ] Review overnight email delivery stats
- [ ] Check spam/bounce rates
- [ ] Hand off interested responses to Avania team

### Afternoon (15 min)
- [ ] Load new leads if quota available
- [ ] Review any failed enrichments
- [ ] Check Reachinbox for delivery issues
- [ ] Update team on day's activity

### Weekly (30 min)
- [ ] Review performance dashboard
- [ ] Identify top-performing variants
- [ ] Plan next week's A/B tests
- [ ] Refresh lead lists

### Monthly (1 hour)
- [ ] Full performance review
- [ ] ROI calculation (meetings → clients)
- [ ] Strategy adjustment
- [ ] Report to Avania leadership

---

## TROUBLESHOOTING GUIDE

### High Bounce Rate (>5%)
**Cause:** Poor email list quality, outdated data  
**Fix:** 
- Pause sending
- Verify email validity with verification tool
- Remove bounced contacts
- Review Apollo filters

### Low Open Rate (<20%)
**Cause:** Poor subject lines, deliverability issues, wrong audience  
**Fix:**
- Test new subject line variants
- Check spam folder placement
- Review audience targeting
- Verify warmup completed

### Low Response Rate (<2%)
**Cause:** Weak opening lines, wrong audience, poor timing  
**Fix:**
- Test new personalization hooks
- Review ICP criteria
- Adjust send times
- A/B test email length

### Emails Going to Spam
**Cause:** Domain reputation, content triggers, authentication issues  
**Fix:**
- Check SPF/DKIM/DMARC setup
- Review email content for spam words
- Increase warmup period
- Check IP/domain reputation

### Enrichment Failures
**Cause:** API limits, missing data, scraping blocks  
**Fix:**
- Check API rate limits
- Use backup enrichment sources
- Add retry logic
- Manual review for key accounts

---

## KEY CONTACTS & ACCESS

| Service | Login URL | Username/Access | Notes |
|---------|-----------|-----------------|-------|
| Apollo | https://apollo.io | TBD | Lead sourcing |
| Reachinbox | https://reachinbox.ai | TBD | Email sending |
| Google Sheets | Google Drive | Shared link | Tracking |
| n8n | OpenClaw node | papi admin | Automation |
| OpenAI | https://platform.openai.com | API key | Personalization |

---

## SUCCESS METRICS (30-60-90 Day Targets)

### 30 Days
- [ ] System fully operational
- [ ] 500+ leads enriched and contacted
- [ ] >20% open rate
- [ ] >3% response rate
- [ ] 5+ meetings booked

### 60 Days
- [ ] 1,500+ leads contacted
- [ ] >25% open rate
- [ ] >5% response rate
- [ ] 20+ meetings booked
- [ ] 2+ new clients signed

### 90 Days
- [ ] 2,500+ leads contacted
- [ ] >30% open rate
- [ ] >5% response rate
- [ ] 50+ meetings booked
- [ ] 5+ new clients signed
- [ ] ROI positive

---

## DECISION LOG

| Date | Decision | Reason | Impact |
|------|----------|--------|--------|
| | | | |

---

*Checklist created: February 6, 2026*  
*Next Review: Upon completion of Phase 1*
