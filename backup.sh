#!/bin/bash
# Facundo Daily Backup Script
# Syncs OpenClaw workspace, config, sessions, and skills to GitHub

set -e

BACKUP_DIR="/Users/ianjamesormo/facundo-backup"
OPENCLAW_DIR="/Users/ianjamesormo/.openclaw"
WORKSPACE="$OPENCLAW_DIR/workspace"
DATE=$(date '+%Y-%m-%d %H:%M')

cd "$BACKUP_DIR"

# Pull latest first
git pull --rebase origin master 2>/dev/null || true

# --- Sync workspace files ---
for f in AGENTS.md SOUL.md IDENTITY.md TOOLS.md USER.md BOOTSTRAP.md HEARTBEAT.md MEMORY.md; do
  [ -f "$WORKSPACE/$f" ] && cp "$WORKSPACE/$f" "$BACKUP_DIR/$f"
done

# --- Sync memory folder ---
mkdir -p "$BACKUP_DIR/memory"
[ -d "$WORKSPACE/memory" ] && cp -R "$WORKSPACE/memory/"* "$BACKUP_DIR/memory/" 2>/dev/null || true

# --- Sync skills ---
mkdir -p "$BACKUP_DIR/skills"
[ -d "$WORKSPACE/skills" ] && cp -R "$WORKSPACE/skills/"* "$BACKUP_DIR/skills/" 2>/dev/null || true

# --- Sync config (redacted) ---
mkdir -p "$BACKUP_DIR/configs"
if [ -f "$OPENCLAW_DIR/openclaw.json" ]; then
  python3 -c "
import json, sys
with open('$OPENCLAW_DIR/openclaw.json') as f:
    c = json.load(f)
def redact(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ('apiKey','token','api_key') and isinstance(v, str) and len(v) > 10:
                o[k] = v[:8] + '...[REDACTED]'
            elif isinstance(v, (dict, list)):
                redact(v)
    elif isinstance(o, list):
        for i in o: redact(i)
redact(c)
if 'skills' in c and 'entries' in c['skills']:
    for n, e in c['skills']['entries'].items():
        for k in list(e.keys()):
            if any(s in k.lower() for s in ('key','token','secret')) and isinstance(e[k], str) and len(e[k]) > 10:
                e[k] = e[k][:8] + '...[REDACTED]'
with open('$BACKUP_DIR/configs/openclaw.json', 'w') as f:
    json.dump(c, f, indent=2)
"
fi

# --- Sync sessions ---
mkdir -p "$BACKUP_DIR/sessions"
cp "$OPENCLAW_DIR/agents/main/sessions/"*.jsonl "$BACKUP_DIR/sessions/" 2>/dev/null || true
cp "$OPENCLAW_DIR/agents/main/sessions/sessions.json" "$BACKUP_DIR/sessions/" 2>/dev/null || true

# --- Sync agent models/auth ---
mkdir -p "$BACKUP_DIR/agent"
cp "$OPENCLAW_DIR/agents/main/agent/"*.json "$BACKUP_DIR/agent/" 2>/dev/null || true

# --- Commit and push ---
cd "$BACKUP_DIR"
git add -A
if git diff --cached --quiet; then
  echo "[$DATE] No changes to backup"
else
  git commit -m "backup: daily sync — $DATE"
  git push origin master
  echo "[$DATE] Backup pushed to GitHub"
fi
