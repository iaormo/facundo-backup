# 🔐 Account Recovery Playbook

**When to use:** You're locked out, lost access, or account compromised  
**Goal:** Regain access safely and secure the account

---

## Scenario A: Forgotten Password

### Recovery Steps

1. **Use official password reset**
   - Go directly to official website (type URL, don't click links)
   - Use "Forgot password" → check email/SMS for reset link
   - **Check spam folder** if reset email doesn't arrive

2. **If reset email missing:**
   - Verify you're checking the right email account
   - Check for email forwarding rules (compromise indicator)
   - Try alternative recovery methods (backup email, phone)

3. **After regaining access:**
   - Change password immediately (unique, strong)
   - Enable MFA if not already on
   - Review recent account activity
   - Check authorized apps/devices

---

## Scenario B: Account Hacked (Attacker Changed Password)

### Immediate Actions

1. **Try account recovery flow**
   - "Forgot password" → use backup email/phone if set up
   - Answer security questions (if configured)

2. **If recovery options compromised:**
   - Contact platform support directly
   - Prepare proof of ownership: gov ID, payment methods, creation date
   - Check if account is posting/sending messages without you

3. **While locked out:**
   - Alert contacts that your account is compromised
   - Monitor for impersonation attempts
   - Check other accounts (credential reuse risk)

4. **After regaining access:**
   - Change password (new, unique)
   - Check and update recovery email/phone
   - Remove unauthorized MFA methods
   - Revoke all app permissions
   - Review and end all active sessions
   - Check for: forwarding rules, authorized apps, payment methods

---

## Scenario C: MFA Lockout (Lost Phone/Authenticator)

### Recovery Options (in order)

1. **Backup codes**
   - Hopefully you saved these when setting up MFA
   - Use one code to log in → disable old MFA → set up new MFA

2. **Alternative MFA methods**
   - Try backup phone number
   - Try hardware security key if configured
   - Try alternate authenticator if you have multiple

3. **Platform recovery**
   - Contact platform support
   - Identity verification required (ID, recent activity, etc.)
   - May take 24-72 hours

### Prevention (Do This Now)

- [ ] Save backup codes in password manager
- [ ] Set up multiple MFA methods if available
- [ ] Use hardware key as backup (YubiKey)
- [ ] Print backup codes, store in physical safe

---

## Scenario D: Social Engineering / SIM Swap

### Signs of SIM Swap
- No cell service suddenly
- Password reset SMS not arriving
- Account notifications about phone number changes

### Immediate Response

1. **Contact carrier immediately**
   - Report suspected SIM swap
   - Request account lock/freeze
   - Verify and restore your number

2. **Secure financial accounts**
   - Call banks (use numbers on cards, not online)
   - Freeze credit (Experian, Equifax, TransUnion)
   - Change online banking passwords from clean device

3. **Check all accounts**
   - Email, banking, crypto, social media
   - Look for unauthorized changes

4. **After stabilizing:**
   - Remove SMS 2FA from all accounts
   - Switch to authenticator apps or hardware keys
   - File police report if financial loss

---

## Account Recovery Checklist

### Post-Recovery Security Hardening

- [ ] Password changed (unique, 20+ chars)
- [ ] MFA enabled/re-enabled with multiple methods
- [ ] Backup codes generated and stored safely
- [ ] Recovery email/phone verified and current
- [ ] All sessions signed out/revoked
- [ ] Authorized apps reviewed (remove unknown)
- [ ] Email forwarding rules checked
- [ ] Recent activity reviewed
- [ ] Security alerts enabled
- [ ] Account login notifications on

---

## Platform-Specific Recovery Links

| Platform | Recovery URL |
|----------|--------------|
| Google | https://myaccount.google.com/signinoptions/recoveryoptions |
| Microsoft | https://account.live.com/password/reset |
| Apple ID | https://iforgot.apple.com |
| GitHub | https://github.com/password_reset |
| AWS | https://signin.aws.amazon.com/resetpassword |
| Cloudflare | Contact support with domain proof |

---

## Red Flags During Recovery

🚨 **Stop and verify if:**
- Someone contacts you claiming to be "support" unsolicited
- You're asked for passwords or MFA codes
- Links in "recovery" emails go to weird URLs
- You're pressured to act "immediately" or lose access
- Recovery site looks slightly off (wrong logo, typos)

**Real support never asks for your password or MFA codes.**

---

*Stay secure, papi. Keep those backup codes safe.*
