# Gateway Timeout Prevention & Update Monitoring

**Created:** 2026-02-07  
**Purpose:** Prevent cron/gateway timeouts and ensure update awareness

---

## Gateway Timeout Prevention

### Root Causes Identified

1. **Gateway not running**
   - In containerized environments, systemd is unavailable
   - Gateway must run in foreground mode

2. **Multiple state directories**
   - Conflicting paths: ~/.openclaw vs /data/.openclaw
   - Causes session history splits and connectivity issues

3. **Missing PATH in service config**
   - Gateway daemon needs minimal PATH set
   - Fixed via `openclaw doctor --fix`

### Prevention Measures (Active)

| Measure | Status | Details |
|---------|--------|---------|
| `commands.restart: true` | ✅ Set | Allows automatic restarts from tools |
| State directory | ✅ Fixed | /data/.openclaw (single source) |
| Service PATH | ✅ Fixed | Configured via doctor --fix |
| Loopback binding | ✅ Active | 127.0.0.1:18789 (secure) |

### When Gateway Times Out

**Symptoms:**
```
gateway timeout after 60000ms
Gateway target: ws://127.0.0.1:18789
```

**Recovery Steps:**
1. Check status: `openclaw gateway status`
2. Kill any stuck processes: `pkill -f "openclaw.*gateway"`
3. Restart in foreground: `openclaw gateway run` (for containers)
4. Verify: `openclaw status` should show "Gateway: reachable"

**For Container Environments:**
```bash
# Run gateway continuously (no systemd)
openclaw gateway run

# Or background it with logging
openclaw gateway run > /tmp/openclaw/gateway.log 2>&1 &
```

---

## Update Monitoring

### Cron Job Configured

**Job ID:** c8746d53-64a4-441e-85aa-03026c76b978  
**Schedule:** Every 6 hours (UTC)  
**Channel:** #bot-log (1469265244483358800)

**What it does:**
- Runs `openclaw status`
- Checks for available updates
- Posts to Discord only when update is available
- Includes: version, git commits behind, update instructions

### Manual Update Check

```bash
openclaw status
# Look for: "Update: available · git main · behind X"

# To update:
openclaw update
```

---

## Cron Job Best Practices (From Fixes)

### Discord Delivery Format

**Wrong:**
```json
"delivery": {
  "to": "1469265197263880359"
}
```

**Correct:**
```json
"delivery": {
  "to": "channel:1469265197263880359"
}
```

### Required Fields for Delivery

```json
{
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "prompt text here"
  },
  "delivery": {
    "mode": "announce",
    "channel": "discord",
    "to": "channel:CHANNEL_ID"
  }
}
```

---

## Quick Commands Reference

| Task | Command |
|------|---------|
| Check status | `openclaw status` |
| Check gateway | `openclaw gateway status` |
| Fix issues | `openclaw doctor --fix` |
| List cron jobs | `openclaw cron list` |
| Update OpenClaw | `openclaw update` |
| View logs | `openclaw logs --follow` |

---

## Monitoring Checklist

- [ ] Gateway reachable (check every 6h via update cron)
- [ ] No duplicate cron jobs (audit monthly)
- [ ] Discord delivery format correct (channel: prefix)
- [ ] State directory permissions (chmod 700)
- [ ] Update availability (automated via cron)

---

_Maintained by Facundo. Last updated: 2026-02-07_
