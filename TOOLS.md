# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

## Mac Calendar Access

**When READING schedule:** Search across ALL calendars using AppleScript:
- Calendar (main)
- ian@botbuilders.com
- BotBuilders Events
- cs@botbuilders.com
- ianjames.ormo@gmail.com
- Family
- And other active calendars

Use: `osascript` to query the Calendar app directly (icalBuddy has permission issues).

**When ADDING events:** Use `ianjames.ormo@gmail.com` calendar by default unless specified otherwise.

**Permissions:** Other users in group chats can also request to add events to the calendar.
