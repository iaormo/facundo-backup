# 🎣 Phishing Response Playbook

**When to use:** You received a suspicious email, message, or link  
**Goal:** Determine if it's malicious, contain any exposure, prevent recurrence

---

## Step 1: STOP — Don't Click Anything

✅ DO:
- Screenshot the message (for evidence)
- Note the sender address/display name
- Check the timestamp
- Document what you were doing when it arrived

❌ DON'T:
- Click links
- Download attachments
- Reply to the message
- Forward it to others (spreads the bait)

---

## Step 2: Quick Triage (30 seconds)

### Red Flags Checklist

| Indicator | Suspicious? |
|-----------|-------------|
| Urgency / fear / threats | 🚩 |
| Unexpected attachment | 🚩 |
| Spelling/grammar errors | 🚩 |
| Mismatched sender (display vs actual) | 🚩 |
| Requests for passwords/2FA/credentials | 🚩🚩🚩 |
| Generic greeting ("Dear Customer") | 🚩 |
| Hover shows weird URL | 🚩 |
| Asks to "verify account" or "confirm details" | 🚩 |

**If 2+ red flags:** Treat as malicious until proven otherwise.

---

## Step 3: Verify Through Another Channel

If the message claims to be from:
- **Bank** → Call the number on your card, NOT in the email
- **Boss/colleague** → Call/message them directly (different channel)
- **Service (Amazon, PayPal, etc.)** → Log in directly via official app/site
- **IT/Security** → Contact them via official Slack/Teams, not by replying

---

## Step 4: Safe Inspection Techniques

### Check Links Without Clicking

**Option A: URL Extractors**
- Right-click → "Copy Link Address" → Paste in notepad
- Use URL expanders (e.g., `https://urlscan.io`)

**Option B: Sandbox View**
- Screenshot the link preview
- Use online sandbox to visit: `https://www.virustotal.com/gui/home/url`

### Inspect Attachments Safely

**Option A: Don't Open It**
- If you weren't expecting it, don't open it
- Contact sender via other channel to confirm

**Option B: Sandbox Analysis**
- Upload to: `https://www.virustotal.com`
- Check file hash reputation

---

## Step 5: If You Clicked/Opened Something

### Immediate Containment

1. **Disconnect from network** (WiFi off / unplug ethernet)
2. **Don't enter credentials** if a fake login page loaded
3. **If you DID enter credentials:**
   - Change that password IMMEDIATELY from another device
   - Revoke sessions if possible
   - Enable MFA if not already on
   - Check for unauthorized activity

4. **Run antivirus scan** on affected device
5. **Check browser extensions** — remove anything unknown
6. **Clear browser cache/cookies** for good measure

---

## Step 6: Report & Document

### Where to Report

| Type | Where |
|------|-------|
| Work email | Forward to security@company.com or IT |
| Personal email | Report as phishing in Gmail/Outlook |
| SMS phishing | Forward to 7726 (SPAM) |
| Financial fraud | Report to your bank + FTC (reportfraud.ftc.gov) |
| Business email compromise | FBI IC3 (ic3.gov) |

### Document for Yourself

```
Date/Time: 
Sender: 
Subject: 
What you did: (clicked link / opened attachment / nothing)
Impact: (credentials entered? device compromised?)
Actions taken: 
```

---

## Step 7: Prevent Recurrence

- Add sender to block list
- Review email rules/filters (attackers often create forwarding rules)
- Check for unauthorized app permissions
- Enable enhanced phishing protection in browser

---

## Quick Reference: Phishing Types

| Type | What It Looks Like | Example |
|------|-------------------|---------|
| **Spear phishing** | Personalized, uses your info | "Hey Ian, here's the invoice you asked about" |
| **Whaling** | Targets executives/big fish | Fake board meeting invite |
| **Vishing** | Voice phishing | "This is your bank's fraud department..." |
| **Smishing** | SMS phishing | "Your package couldn't be delivered..." |
| **QR phishing** | Malicious QR codes | Fake parking payment QR |
| **Clone phishing** | Resends real email with malicious attachment | "Resending: Q4 Report" |

---

## Escalation Triggers

🚨 **Get Facundo involved immediately if:**
- Customer data may have been accessed
- You entered credentials on a fake site
- Your device is behaving strangely after clicking
- The phishing targeted work systems specifically
- Multiple people received similar messages (possible campaign)

---

*Remember: When in doubt, throw it out. Real organizations won't punish you for verifying.*
