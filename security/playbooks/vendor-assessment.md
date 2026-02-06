# 🏢 Vendor Security Assessment

**When to use:** Evaluating new tools, services, or vendors  
**Goal:** Understand security posture before trusting with data

---

## Quick Triage (5 Minutes)

### Public Security Info

| Check | Where to Look | What You Want |
|-------|---------------|---------------|
| **Security page** | `/security` or Trust Center | SOC 2, ISO 27001, GDPR compliance |
| **Status page** | `status.company.com` | Uptime, incident history |
| **Bug bounty** | HackerOne, Bugcrowd | Active security program |
| **Data handling** | Privacy policy | Data retention, deletion, location |
| **Breaches** | HaveIBeenPwned, news | Past incidents, response quality |

### Dealbreakers 🚩

- No HTTPS/TLS encryption
- No MFA available
- No way to delete your data
- Stores passwords in plaintext (ask!)
- Recent major breach with poor response
- Based in high-risk jurisdiction (unless you understand the risk)

---

## Detailed Assessment Questions

### 1. Authentication & Access

- [ ] MFA supported? (TOTP/hardware keys, not just SMS)
- [ ] SSO/SAML available? (Okta, Azure AD, etc.)
- [ ] Role-based access control?
- [ ] Session management (timeout, concurrent limits)?
- [ ] API key management and rotation?

### 2. Data Protection

- [ ] Encryption at rest? (AES-256)
- [ ] Encryption in transit? (TLS 1.2+)
- [ ] Data residency options? (EU, US, etc.)
- [ ] Backup frequency and retention?
- [ ] Data deletion guarantees?

### 3. Compliance & Certifications

| Certification | What It Means | When It Matters |
|---------------|---------------|-----------------|
| **SOC 2 Type II** | Security controls audited | Handling customer data |
| **ISO 27001** | Information security management | Enterprise vendors |
| **GDPR** | EU data protection compliance | EU customers |
| **HIPAA** | Healthcare data protection | Medical/health data |
| **PCI DSS** | Payment card security | Handling credit cards |

### 4. Incident Response

- [ ] Published incident response plan?
- [ ] Notification SLA for breaches? (24-72h typical)
- [ ] Past incidents documented?
- [ ] Third-party penetration testing?

### 5. Business Continuity

- [ ] Uptime SLA? (99.9% = 8.7h downtime/year)
- [ ] Data export/portability?
- [ ] What happens if they go out of business?

---

## Self-Service Assessment Tools

### Website Security Scan

```bash
# Check SSL/TLS configuration
https://www.ssllabs.com/ssltest/analyze.html?d=example.com

# Check security headers
https://securityheaders.com/?q=example.com

# Check DNS security
https://mxtoolbox.com/SuperTool.aspx
```

### Company Intelligence

- https://www.crunchbase.com (funding, leadership)
- https://news.ycombinator.com (developer sentiment)
- https://www.g2.com (reviews, often mention security)

---

## Risk Classification

| Sensitivity | Examples | Assessment Level |
|-------------|----------|------------------|
| **Low** | Public website, analytics | Quick triage |
| **Medium** | CRM, email marketing, support | Detailed questionnaire |
| **High** | Production database, payments | Security review call, SOC 2 review |
| **Critical** | Core infrastructure, customer PII | Legal review, DPA, possible audit |

---

## Vendor Security Questionnaire Template

```
SECURITY QUESTIONNAIRE
For: [Vendor Name]
Date: [Date]
Assessed by: [Your Name]

1. DATA HANDLING
   - What data will you access/store/process?
   - Where is data physically stored?
   - Who has access to our data?
   - Data retention period?
   - Deletion procedure upon contract end?

2. SECURITY CONTROLS
   - Encryption at rest: [ ] Yes [ ] No - Algorithm: ____
   - Encryption in transit: [ ] TLS 1.2 [ ] TLS 1.3
   - MFA available: [ ] Yes [ ] No - Types: ____
   - Penetration testing frequency: ____
   - Vulnerability disclosure program: [ ] Yes [ ] No

3. COMPLIANCE
   - Certifications: SOC2 [ ] ISO27001 [ ] GDPR [ ] Other: ____
   - Last audit date: ____
   - Audit report available under NDA: [ ] Yes [ ] No

4. INCIDENT RESPONSE
   - Breach notification SLA: ____ hours
   - Incident response plan documented: [ ] Yes [ ] No
   - Cyber insurance: [ ] Yes [ ] No

5. BUSINESS CONTINUITY
   - Uptime SLA: ____%
   - RTO (Recovery Time Objective): ____
   - RPO (Recovery Point Objective): ____
   - Data export format: ____

RISK ASSESSMENT: [ ] Low [ ] Medium [ ] High
APPROVED FOR USE: [ ] Yes [ ] Yes with conditions [ ] No
CONDITIONS: ___________________________________
```

---

## Ongoing Monitoring

Once approved, set calendar reminders to:

- **Quarterly:** Check for new breaches or security incidents
- **Annually:** Re-review certifications, reassess risk
- **On breach news:** Immediate impact assessment

---

*Better to assess before you trust, papi. Trust but verify.*
