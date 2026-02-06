# ✅ Security Hardening Checklist

**Purpose:** Baseline security for all accounts, devices, and services  
**Goal:** Complete this checklist for yourself, your business, and any customer-facing systems

---

## 🆔 Identity & Access Management

### Personal Accounts (Priority: P0)

- [ ] **Password Manager Setup**
  - [ ] Bitwarden, 1Password, or Proton Pass installed
  - [ ] Master password: 20+ chars, unique, memorized
  - [ ] 2FA enabled on password manager itself
  - [ ] Emergency access configured (trusted contact)

- [ ] **Critical Accounts Secured** (do these first)
  - [ ] Primary email (Gmail/Outlook/Proton) — MFA + unique password
  - [ ] Banking/financial accounts — MFA + alerts enabled
  - [ ] Password manager — MFA + backup codes saved
  - [ ] Phone/carrier account — PIN/password protection (prevent SIM swap)
  - [ ] Domain registrar — MFA + lock domain
  - [ ] Cloud admin (AWS/Azure/GCP) — MFA + root account secured

- [ ] **MFA Everywhere Possible**
  - [ ] Authenticator app preferred (Google Auth, Authy, Aegis)
  - [ ] Hardware keys for critical accounts (YubiKey)
  - [ ] SMS only as last resort (SIM swap risk)
  - [ ] Backup codes saved in password manager + physical safe

- [ ] **Password Hygiene**
  - [ ] No password reuse across accounts
  - [ ] All passwords 20+ characters (manager-generated)
  - [ ] Changed any default passwords
  - [ ] Audit and update old/reused passwords quarterly

---

## 📧 Email Security

- [ ] **Domain Security** (if you own domains)
  - [ ] SPF record configured
  - [ ] DKIM enabled
  - [ ] DMARC policy: p=quarantine or p=reject
  - [ ] DNSSEC enabled if supported

- [ ] **Account Security**
  - [ ] MFA enabled on email
  - [ ] Review and remove app passwords
  - [ ] Check forwarding rules (attackers often hide these)
  - [ ] Check delegates/granted access
  - [ ] Disable POP/IMAP if not needed

- [ ] **Email Habits**
  - [ ] Separate emails: personal, business, junk signups
  - [ ] Don't click links in emails (navigate manually)
  - [ ] Verify sender before opening attachments
  - [ ] Report phishing attempts

---

## 💻 Device Security

### All Devices

- [ ] **Full Disk Encryption**
  - [ ] Windows: BitLocker enabled
  - [ ] Mac: FileVault enabled
  - [ ] Linux: LUKS/dm-crypt configured
  - [ ] Mobile: encryption on (default on modern devices)

- [ ] **Screen Lock**
  - [ ] Auto-lock: 2-5 minutes max
  - [ ] Strong PIN/password (not pattern on Android)
  - [ ] Biometric enabled if available

- [ ] **Updates**
  - [ ] Auto-updates enabled (OS)
  - [ ] Auto-updates enabled (apps)
  - [ ] Check for updates monthly

- [ ] **Network**
  - [ ] Disable WiFi when not in use
  - [ ] Disable Bluetooth when not in use
  - [ ] Forget public WiFi networks
  - [ ] Use VPN on untrusted networks

### Computers

- [ ] **Antivirus/EDR**
  - [ ] Windows Defender or equivalent enabled
  - [ ] Real-time protection on
  - [ ] Full scan monthly

- [ ] **Firewall**
  - [ ] Host firewall enabled
  - [ ] Default deny inbound

- [ ] **Browser**
  - [ ] HTTPS-Only mode enabled
  - [ ] Privacy badger / uBlock Origin installed
  - [ ] Review and remove unknown extensions
  - [ ] Password saving disabled (use manager instead)
  - [ ] Clear cookies/cache monthly

### Mobile Devices

- [ ] **Find My Device**
  - [ ] Find My iPhone / Find My Device enabled
  - [ ] Remote wipe capability confirmed

- [ ] **App Security**
  - [ ] Only install from official stores
  - [ ] Review app permissions quarterly
  - [ ] Remove unused apps
  - [ ] Disable lock screen notifications for sensitive apps

- [ ] **Backup**
  - [ ] iCloud/Google backup encrypted
  - [ ] Local encrypted backup monthly

---

## 🌐 Network Security

### Home/Office Network

- [ ] **Router Hardening**
  - [ ] Default admin password changed
  - [ ] WPA3 encryption (or WPA2 if WPA3 unavailable)
  - [ ] Strong WiFi password (20+ chars)
  - [ ] Guest network enabled for IoT/visitors
  - [ ] Remote management disabled
  - [ ] UPnP disabled
  - [ ] Firmware updated

- [ ] **Device Inventory**
  - [ ] List of all connected devices
  - [ ] Unknown devices investigated/removed
  - [ ] IoT devices isolated on separate network if possible

- [ ] **DNS Security**
  - [ ] Using secure DNS (Cloudflare 1.1.1.1, Quad9, or NextDNS)
  - [ ] DNSSEC enabled if available
  - [ ] Consider DNS filtering (block malware/phishing)

---

## ☁️ Cloud & Online Services

- [ ] **Admin Accounts**
  - [ ] Separate admin and user accounts
  - [ ] Admin accounts never used for daily browsing
  - [ ] Admin MFA hardware-key protected

- [ ] **API Keys & Secrets**
  - [ ] No hardcoded secrets in repos
  - [ ] Secrets in environment variables or vault
  - [ ] Regular key rotation (90 days max)
  - [ ] Least privilege on all keys

- [ ] **Access Logging**
  - [ ] Login alerts enabled
  - [ ] Review access logs monthly
  - [ ] Anomaly detection if available

- [ ] **Data Classification**
  - [ ] Know where sensitive data lives
  - [ ] Encryption at rest enabled
  - [ ] Backup encryption verified

---

## 💾 Backup Strategy (3-2-1 Rule)

- [ ] **3 Copies of Data**
  - [ ] Primary (working copy)
  - [ ] Local backup
  - [ ] Offsite/cloud backup

- [ ] **2 Different Media Types**
  - [ ] Local: external drive or NAS
  - [ ] Cloud: encrypted cloud storage

- [ ] **1 Offsite**
  - [ ] Cloud backup active and syncing
  - [ ] Physical offsite backup (safe deposit box, etc.)

- [ ] **Backup Verification**
  - [ ] Test restore quarterly
  - [ ] Verify encryption passwords work
  - [ ] Check backup integrity

---

## 🏢 Business Security (If Applicable)

- [ ] **Policies**
  - [ ] Acceptable use policy documented
  - [ ] Incident response plan
  - [ ] Data classification policy
  - [ ] Remote work security guidelines

- [ ] **Employee Training**
  - [ ] Phishing awareness training
  - [ ] Password security training
  - [ ] Incident reporting procedure

- [ ] **Customer Data**
  - [ ] Encryption at rest and in transit
  - [ ] Access logging
  - [ ] Data retention policy
  - [ ] Secure deletion procedures
  - [ ] Privacy policy published

---

## 🔍 Ongoing Maintenance

### Weekly
- [ ] Review security alerts/notifications
- [ ] Check for unusual account activity

### Monthly
- [ ] Update all software
- [ ] Review account access logs
- [ ] Check backup status
- [ ] Review bank/credit statements

### Quarterly
- [ ] Password audit (change any weak/reused)
- [ ] Review and remove unused accounts
- [ ] Review app permissions
- [ ] Test backup restoration
- [ ] Review vendor access

### Annually
- [ ] Full security review
- [ ] Update incident response plan
- [ ] Review and update policies
- [ ] Consider external penetration test
- [ ] Review insurance coverage

---

## 📊 Score Your Security

| Category | Max | Your Score |
|----------|-----|------------|
| Identity & Access | 20 | __ |
| Email Security | 15 | __ |
| Device Security | 20 | __ |
| Network Security | 15 | __ |
| Cloud Services | 15 | __ |
| Backup & Recovery | 15 | __ |
| **TOTAL** | **100** | **__** |

### Scoring
- **90-100:** Excellent — Keep it up
- **70-89:** Good — Address gaps
- **50-69:** Needs work — Prioritize fixes
- **Below 50:** At risk — Immediate action needed

---

*Tick them off, papi. Every box checked is an attack vector closed.*
