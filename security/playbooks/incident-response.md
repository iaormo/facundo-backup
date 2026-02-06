# 🚨 Incident Response Playbook

**When to use:** You suspect compromise, breach, or active attack  
**Goal:** Contain damage, preserve evidence, recover, learn

---

## Phase 1: DETECT — Confirm the Incident

### Suspicious Indicators

| Type | Signs |
|------|-------|
| **Account** | Unknown logins, password changes you didn't make, 2FA prompts |
| **Device** | Slow performance, unexpected popups, unknown programs |
| **Financial** | Unauthorized transactions, new accounts opened |
| **Email** | Messages you didn't send, auto-forwarding rules, missing emails |
| **Network** | Unknown devices on WiFi, unusual traffic |
| **Behavioral** | Colleagues asking about "weird messages from you" |

### Quick Triage Questions

1. What makes you think there's an incident?
2. When did you first notice?
3. What systems/accounts might be affected?
4. Have you clicked anything suspicious recently?
5. Is customer data potentially involved?

**If customer data may be breached → Escalate immediately**

---

## Phase 2: CONTAIN — Stop the Bleeding

### Immediate Actions (Do in order)

#### 1. Isolate Affected Systems

**If specific device is compromised:**
- Disconnect from internet (WiFi off / unplug)
- Don't shut down yet (preserves memory evidence)
- Take photos of screen if anything suspicious is visible

**If account is compromised:**
- Sign out of all sessions (if you can still access)
- Change password from a clean device
- Check for: forwarding rules, app passwords, authorized apps

#### 2. Protect Critical Assets

- **Move money** if banking credentials may be exposed
- **Backup critical data** from clean systems
- **Alert your team** if work systems affected
- **Document everything** — timestamps, actions taken

#### 3. Preserve Evidence

Before cleaning anything:
- Screenshot suspicious activity
- Note exact times of events
- Save suspicious emails/messages (don't open attachments)
- List all potentially affected accounts

---

## Phase 3: ERADICATE — Remove the Threat

### For Compromised Accounts

1. **Change passwords** — unique, strong, from clean device
2. **Enable/re-enable MFA** — remove any unknown MFA methods
3. **Review and revoke** app permissions/OAuth tokens
4. **Check account activity** logs for unauthorized access
5. **Set up alerts** for new logins

### For Compromised Devices

1. **Boot from external media** or safe mode
2. **Run full antivirus scan** (Malwarebytes, Windows Defender)
3. **Check startup items** and scheduled tasks
4. **Review browser extensions** — remove unknown ones
5. **Consider wipe and rebuild** if rootkit suspected

### For Network Compromise

1. **Change WiFi passwords**
2. **Check connected devices** on router admin panel
3. **Update router firmware**
4. **Disable remote management** if enabled
5. **Consider factory reset** of router

---

## Phase 4: RECOVER — Restore Operations

### Verification Checklist

- [ ] Threat fully removed (confirmed by scan/clean boot)
- [ ] All passwords changed (use password manager)
- [ ] MFA enabled everywhere possible
- [ ] Backups verified clean and accessible
- [ ] No unauthorized forwarding rules or delegates
- [ ] No suspicious scheduled tasks or startup items
- [ ] Bank/credit accounts monitored for fraud

### Gradual Restoration

1. **Start with least critical systems**
2. **Monitor closely** for recurring compromise
3. **Update everything** — OS, apps, firmware
4. **Re-enable services** one by one

---

## Phase 5: LEARN — Post-Incident Review

### Document the Incident

```
INCIDENT REPORT
===============
Date/Time Detected: 
Date/Time Contained: 
Systems Affected: 
Accounts Affected: 
Data Potentially Exposed: 
Initial Vector: (phishing / credential stuffing / malware / unknown)
Actions Taken: 
Lessons Learned: 
Prevention Measures: 
```

### Key Questions

1. How did they get in?
2. What could have prevented this?
3. What detection failed?
4. What worked well in response?
5. What will we do differently?

---

## Communication Templates

### If Customer Data Breached

**Required:** Legal counsel, regulatory notification (72h for GDPR), customer notification

```
We are writing to inform you of a security incident that may have affected your personal information. 
On [DATE], we discovered unauthorized access to [SYSTEM]. 
The information involved may have included [DATA TYPES].
We have taken immediate action to secure our systems and are working with cybersecurity experts.
```

### If Team/Colleagues Affected

```
Heads up — my [email/account] was compromised. 
Please disregard any suspicious messages from me sent between [TIME] and [TIME].
I've secured the account and changed passwords.
```

---

## When to Call for Help

### External Resources

| Situation | Who to Call |
|-----------|-------------|
| Financial fraud | Bank + FTC (reportfraud.ftc.gov) |
| Identity theft | IdentityTheft.gov |
| Business compromise | FBI IC3 (ic3.gov) |
| Cyber insurance claim | Your insurance provider |
| Legal/Regulatory | Attorney specializing in data privacy |
| Technical incident response | Retainer with IR firm |

### Get Facundo Involved

🚨 Escalate to me if:
- Customer data is involved
- Multiple systems compromised
- Ransomware present
- Active attacker still in environment
- Regulatory notification required
- You need forensics/preservation

---

## Common Incident Types

| Type | Typical Vector | Immediate Action |
|------|---------------|------------------|
| **Account Takeover** | Phishing, credential stuffing | Change pwd, revoke sessions, check forwarding |
| **Ransomware** | Phishing, RDP, unpatched systems | Isolate, don't pay, restore from backup |
| **BEC (Business Email Compromise)** | Spear phishing, compromised vendor | Verify wire transfers verbally, alert bank |
| **Cryptojacking** | Malicious website, infected software | Kill processes, scan, check browser extensions |
| **Supply Chain** | Compromised software update | Isolate, assess blast radius, vendor notification |

---

## Remember

> **"Detection is better than prevention. Containment is better than cleanup."**

Speed matters. Document everything. Learn from it.

---

*Stay calm, papi. We'll get through it.*
