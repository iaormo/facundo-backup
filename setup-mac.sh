#!/bin/bash
# OpenClaw Local Setup Script for Papi's Mac
# Replicates Facundo to local Mac securely
# WARNING: Only run on trusted personal machines

set -e  # Exit on error

echo "==============================================="
echo "  FACUNDO LOCAL SETUP - MAC INSTALLATION"
echo "==============================================="
echo ""
echo "⚠️  SECURITY NOTICE:"
echo "   - This script will prompt for API tokens"
echo "   - Tokens will be stored in OpenClaw's secure config"
echo "   - Never share tokens or this script with anyone"
echo "   - Only run on YOUR personal Mac"
echo ""
read -p "Continue? (yes/no): " CONFIRM

if [ "$CONFIRM" != "yes" ]; then
    echo "Setup cancelled."
    exit 0
fi

echo ""
echo "Step 1: Creating workspace directory..."
mkdir -p ~/facundo
cd ~/facundo

echo ""
echo "Step 2: Cloning workspace from GitHub..."
if [ -d ".git" ]; then
    echo "   Workspace already exists, pulling latest..."
    git pull origin master
else
    git clone https://github.com/iaormo/facundo-backup.git .
fi

echo ""
echo "Step 3: Verifying OpenClaw installation..."
if ! command -v openclaw &> /dev/null; then
    echo "❌ OpenClaw CLI not found!"
    echo "   Install it first: npm install -g openclaw"
    exit 1
fi
echo "   ✅ OpenClaw found: $(openclaw --version)"

echo ""
echo "Step 4: Initializing OpenClaw workspace..."
openclaw setup --yes 2>/dev/null || true

echo ""
echo "==============================================="
echo "  CHANNEL SETUP (Secure Token Input)"
echo "==============================================="
echo ""
echo "You'll now be prompted for API tokens."
echo "Get them from your Notion or respective dashboards."
echo ""

# Discord Setup
echo "--- Discord Setup ---"
read -p "Set up Discord bot? (yes/no): " SETUP_DISCORD
if [ "$SETUP_DISCORD" = "yes" ]; then
    echo "   Get your token from: https://discord.com/developers/applications"
    echo "   (Input will be hidden for security)"
    read -s -p "   Enter Discord Bot Token: " DISCORD_TOKEN
    echo ""
    
    if [ -n "$DISCORD_TOKEN" ]; then
        openclaw config set discord.botToken "$DISCORD_TOKEN"
        echo "   ✅ Discord token configured"
        
        read -p "   Enter your Discord Server ID: " DISCORD_GUILD
        if [ -n "$DISCORD_GUILD" ]; then
            openclaw config set discord.guildId "$DISCORD_GUILD"
            echo "   ✅ Discord server configured"
        fi
    fi
    
    # Clear variable
    unset DISCORD_TOKEN
fi

# OpenAI Setup
echo ""
echo "--- OpenAI Setup (for AI features) ---"
read -p "Set up OpenAI? (yes/no): " SETUP_OPENAI
if [ "$SETUP_OPENAI" = "yes" ]; then
    echo "   Get your key from: https://platform.openai.com/api-keys"
    read -s -p "   Enter OpenAI API Key: " OPENAI_KEY
    echo ""
    
    if [ -n "$OPENAI_KEY" ]; then
        openclaw config set openai.apiKey "$OPENAI_KEY"
        echo "   ✅ OpenAI configured"
    fi
    
    unset OPENAI_KEY
fi

# Notion Setup
echo ""
echo "--- Notion Setup (optional) ---"
read -p "Set up Notion integration? (yes/no): " SETUP_NOTION
if [ "$SETUP_NOTION" = "yes" ]; then
    echo "   Get your token from: https://www.notion.so/my-integrations"
    read -s -p "   Enter Notion API Token: " NOTION_TOKEN
    echo ""
    
    if [ -n "$NOTION_TOKEN" ]; then
        openclaw config set notion.apiKey "$NOTION_TOKEN"
        echo "   ✅ Notion configured"
    fi
    
    unset NOTION_TOKEN
fi

echo ""
echo "==============================================="
echo "  VERIFICATION"
echo "==============================================="

echo ""
echo "Step 5: Checking workspace files..."
REQUIRED_FILES=("SOUL.md" "USER.md" "TOOLS.md" "AGENTS.md")
for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "   ✅ $file"
    else
        echo "   ⚠️  $file not found"
    fi
done

echo ""
echo "Step 6: Listing mastery files..."
MASTERY_COUNT=$(ls -1 *_mastery.py 2>/dev/null | wc -l)
echo "   Found $MASTERY_COUNT mastery modules:"
ls -1 *_mastery.py 2>/dev/null | head -10 | sed 's/^/   - /'

echo ""
echo "Step 7: Testing OpenClaw..."
openclaw status 2>/dev/null && echo "   ✅ OpenClaw status: OK" || echo "   ⚠️  OpenClaw gateway not running (run: openclaw gateway start)"

echo ""
echo "==============================================="
echo "  SETUP COMPLETE!"
echo "==============================================="
echo ""
echo "📁 Workspace location: ~/facundo"
echo ""
echo "🚀 Next steps:"
echo "   1. cd ~/facundo"
echo "   2. openclaw gateway start"
echo "   3. openclaw dashboard  (to open web UI)"
echo "   4. Test: openclaw agent --local --message 'Hello from Mac'"
echo ""
echo "🔐 Security reminders:"
echo "   - Tokens are stored in OpenClaw's encrypted config"
echo "   - Never commit tokens to GitHub"
echo "   - Run 'openclaw config' to review/modify settings"
echo ""
echo "💡 To recreate cron jobs, see: cron-jobs-setup.md"
echo ""
echo "✅ Facundo is now on your Mac!"
