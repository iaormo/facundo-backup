# 🔒 Security Framework

**Scope:** Personal + Business + Customer data protection  
**Owner:** Ian (papi) + Facundo  
**Last Updated:** 2026-02-06

## Quick Start — Security Levels

| Level | What | When |
|-------|------|------|
| 🟢 **Baseline** | Everyone, always | Default minimum |
| 🟡 **Elevated** | Sensitive accounts, customer data | Banking, email, admin access |
| 🔴 **Critical** | Infrastructure, production, secrets | Servers, databases, root keys |

---

## 🚨 Immediate Actions (Do Today)

### 1. Password Hygiene
- [ ] Use a password manager (Bitwarden, 1Password, Proton Pass)
- [ ] Unique 20+ character passwords for every account
- [ ] Audit existing passwords — change any reused ones

### 2. MFA Everything
- [ ] Enable MFA on: Email, banking, cloud admin, domain registrar, GitHub
- [ ] Use authenticator apps or hardware keys (YubiKey)
- [ ] Disable SMS 2FA where possible (SIM swap risk)

### 3. Email Security
- [ ] Enable DMARC, SPF, DKIM on all domains
- [ ] Review forwarding rules and app permissions
- [ ] Set up separate emails: personal, business, junk signups

### 4. Device Hardening
- [ ] Full disk encryption on all devices
- [ ] Auto-lock screens (2-5 min timeout)
- [ ] Disable Bluetooth/WiFi when not needed
- [ ] Keep OS and apps updated (auto-update enabled)

### 5. Backups
- [ ] 3-2-1 backup rule: 3 copies, 2 media types, 1 offsite
- [ ] Test restoration quarterly
- [ ] Encrypt backup data

---

## 🎯 Threat Priority Matrix

| Threat | Likelihood | Impact | Priority |
|--------|------------|--------|----------|
| Phishing / BEC | 🔴 High | 🔴 High | P0 |
| Credential Stuffing | 🔴 High | 🟡 Med | P0 |
| Ransomware | 🟡 Med | 🔴 High | P1 |
| Supply Chain | 🟡 Med | 🔴 High | P1 |
| Insider Threat | 🟢 Low | 🔴 High | P2 |
| APT / Targeted | 🟢 Low | 🔴 High | P2 |

---

## 📋 Playbooks

- [phishing-response.md](./playbooks/phishing-response.md) — Got a sketchy email?
- [incident-response.md](./playbooks/incident-response.md) — Think you're compromised?
- [account-recovery.md](./playbooks/account-recovery.md) — Locked out or breached?
- [vendor-assessment.md](./playbooks/vendor-assessment.md) — Evaluating new tools?

---

## 🛡️ Defense Layers

```
┌─────────────────────────────────────────┐
│  7. BACKUP & RECOVERY                   │
├─────────────────────────────────────────┤
│  6. MONITORING & DETECTION              │
├─────────────────────────────────────────┤
│  5. NETWORK SEGMENTATION                │
├─────────────────────────────────────────┤
│  4. ENDPOINT PROTECTION                 │
├─────────────────────────────────────────┤
│  3. ACCESS CONTROL (IAM + MFA)          │
├─────────────────────────────────────────┤
│  2. ASSET INVENTORY                     │
├─────────────────────────────────────────┤
│  1. AWARENESS & POLICY                  │
└─────────────────────────────────────────┘
```

---

## 📊 Security Scorecard

Track our posture over time:

| Category | Score | Last Check |
|----------|-------|------------|
| Identity & Access | ? | - |
| Email Security | ? | - |
| Device Security | ? | - |
| Network Security | ? | - |
| Data Protection | ? | - |
| Incident Readiness | ? | - |

---

## 🔄 Regular Reviews

- **Weekly:** Check security alerts, review access logs
- **Monthly:** Patch review, password audit, backup test
- **Quarterly:** Full security review, tabletop exercise
- **Annually:** Full penetration test (external), policy review

---

*Questions? Ask Facundo. Stay safe, papi.*
