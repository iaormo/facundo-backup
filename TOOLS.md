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

**Timezone:** Asia/Manila (PHT, UTC+8). ALWAYS use this timezone when creating events. When a user says "March 25 at 10am", that means March 25 at 10:00 AM PHT.

**CRITICAL — Date Handling:** When creating calendar events via AppleScript, always set the date string explicitly with the correct day of week and use `date "DayOfWeek, Month Day, Year at HH:MM:SS AM/PM"` format. Do NOT use ISO 8601 or UTC dates — AppleScript will misinterpret them and add events on the wrong day. Example: `date "Tuesday, March 25, 2026 at 10:00:00 AM"`.

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

**AppleScript Add Event Template:**
```applescript
tell application "Calendar"
  tell calendar "ianjames.ormo@gmail.com"
    make new event with properties {summary:"EVENT NAME", start date:date "Tuesday, March 25, 2026 at 10:00:00 AM", end date:date "Tuesday, March 25, 2026 at 10:30:00 AM"}
  end tell
end tell
```

**Permissions:** Other users in group chats can also request to add events to the calendar.

## Email (himalaya CLI)

**Account:** ian@scaleplus.io (Google Workspace)
**Binary:** /opt/homebrew/bin/himalaya
**Config:** ~/.config/himalaya/config.toml

**Send:** `printf 'From: Ian James Ormo <ian@scaleplus.io>\nTo: EMAIL\nSubject: SUBJECT\n\nBODY' | /opt/homebrew/bin/himalaya message send`
**Read inbox:** `/opt/homebrew/bin/himalaya envelope list --page-size 10`
**Read message:** `/opt/homebrew/bin/himalaya message read MESSAGE_ID`

Always confirm with user before sending. See `skills/email/SKILL.md` for full usage.
