# 🎯 Threat Reference Guide

**Purpose:** Quick reference for common attack types and defenses  
**Use with:** Playbooks for response procedures

---

## 🔴 P0 Threats (Most Likely + Most Impact)

### Phishing / Business Email Compromise (BEC)

**What:** Fake emails/messages tricking you into giving up credentials, money, or access  
**How it works:** 
- Mass phishing (spray and pray)
- Spear phishing (targeted, uses your info)
- BEC (impersonates CEO/vendor for wire fraud)

**Red Flags:**
- Urgency, fear, threats
- Unexpected attachments/links
- Mismatched sender addresses
- Requests to "verify account" or change payment details

**Defense:**
- MFA on everything
- Verify unusual requests via second channel
- Email security (DMARC/SPF/DKIM)
- Security awareness training

**Recovery:** See [phishing-response.md](./playbooks/phishing-response.md)

---

### Credential Stuffing / Password Spraying

**What:** Using leaked passwords from breaches to access your accounts  
**How it works:**
- Attackers buy breach databases (billions of credentials)
- Automated tools try email/password combos across sites
- Password spraying: common passwords against many accounts

**Red Flags:**
- Unexpected login notifications
- Account locked due to failed attempts
- Activity from unknown locations

**Defense:**
- Unique password per site (password manager)
- MFA (stops this even with correct password)
- Login alerts enabled
- Breach monitoring (HaveIBeenPwned alerts)

---

## 🟡 P1 Threats (Moderate Likelihood / High Impact)

### Ransomware

**What:** Malware encrypts your files, demands payment for decryption  
**How it works:**
- Phishing attachment or malicious download
- Exploits unpatched vulnerabilities
- Spreads across network shares

**Impact:**
- Data encrypted and potentially stolen
- Business operations halted
- Recovery costs (average $1.85M in 2023)

**Defense:**
- Backups (3-2-1 rule, offline/air-gapped)
- Patch management
- EDR (Endpoint Detection & Response)
- Network segmentation
- Email filtering

**Recovery:**
- DON'T PAY (no guarantee of decryption, marks you as target)
- Isolate infected systems
- Restore from clean backups
- Report to FBI (IC3.gov)

---

### Supply Chain Attacks

**What:** Attacking you by compromising your vendors/software  
**Examples:**
- SolarWinds (compromised update server)
- 3CX (compromised software build)
- Compromised npm/pip packages

**Defense:**
- Vendor security assessments
- Software bill of materials (SBOM)
- Dependency scanning
- Network segmentation (limit vendor access)
- Anomaly detection on vendor connections

---

### Cloud Misconfiguration

**What:** Exposing data due to wrong cloud settings  
**Common mistakes:**
- Public S3 buckets with private data
- Overly permissive IAM roles
- Default passwords on cloud resources
- Unencrypted databases

**Defense:**
- Infrastructure as Code (IaC) with security policies
- Cloud security posture management (CSPM)
- Regular audits
- Principle of least privilege

---

## 🟢 P2 Threats (Lower Likelihood)

### Advanced Persistent Threats (APT)

**What:** Sophisticated, long-term targeted attacks (usually nation-state or organized crime)  
**Characteristics:**
- Highly customized malware
- Living-off-the-land techniques (uses legitimate tools)
- Months-long dwell time
- Targets specific high-value data

**Defense:**
- Assume breach mentality
- Defense in depth
- Behavioral detection
- Threat hunting
- Incident response readiness

---

### Insider Threats

**What:** Malicious or negligent actions by employees/contractors  
**Types:**
- Malicious insider (steals data, sabotages)
- Negligent insider (falls for phishing, misconfigures)
- Compromised insider (credentials stolen)

**Defense:**
- Least privilege access
- Monitoring and logging
- Data loss prevention (DLP)
- Background checks
- Security culture/awareness

---

## 📱 Emerging Threats (2024-2025)

### AI-Powered Attacks

- **Deepfake voice/video:** Impersonating executives for wire fraud
- **AI-generated phishing:** Perfect grammar, highly personalized
- **Automated vulnerability discovery:** AI finding exploits faster

**Defense:**
- Verify unusual requests via trusted channel
- Out-of-band verification for financial transactions
- Deepfake detection tools (emerging)

---

### QR Code Phishing (Quishing)

**What:** Malicious QR codes in public places or emails  
**Examples:**
- Fake parking payment QR codes
- Email: "Scan to verify your account"
- Stickers placed over legitimate QR codes

**Defense:**
- Don't scan random QR codes
- Verify URL after scanning (before entering data)
- Use built-in camera preview to see URL first

---

### MFA Bypass Techniques

| Technique | How It Works | Defense |
|-----------|--------------|---------|
| **MFA fatigue** | Bombard user with push notifications until they approve | Number matching, hardware keys |
| **Adversary-in-the-middle (AiTM)** | Proxy that captures session cookies | Phishing-resistant MFA (FIDO2) |
| **SIM swap** | Take over phone number to get SMS codes | Avoid SMS MFA, carrier PIN |
| **Push bombing** | Same as MFA fatigue | Limit push notifications, hardware keys |

---

## 🛡️ Defense Strategies

### Defense in Depth

```
┌─────────────────────────────────────┐
│  Perimeter (firewall, WAF)         │
├─────────────────────────────────────┤
│  Network (segmentation, IDS)       │
├─────────────────────────────────────┤
│  Endpoint (EDR, antivirus)         │
├─────────────────────────────────────┤
│  Application (input validation)    │
├─────────────────────────────────────┤
│  Data (encryption, DLP)            │
├─────────────────────────────────────┤
│  Identity (MFA, least privilege)   │
└─────────────────────────────────────┘
```

### Zero Trust Principles

1. **Never trust, always verify** — Every request authenticated
2. **Least privilege** — Minimum access needed
3. **Assume breach** — Monitor everything
4. **Verify explicitly** — Continuous validation

### Security Mindset

> **"Prevention is ideal, but detection is a must."**

Assume you will be targeted. Build to detect and respond, not just prevent.

---

*Know your enemy, papi. Then build walls they can't climb.*
