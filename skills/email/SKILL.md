# Email Skill

Send and read emails using himalaya CLI from ian@scaleplus.io (Google Workspace).

## Sending Email

Use this exact command pattern to send an email:

```bash
printf 'From: Ian James Ormo <ian@scaleplus.io>\nTo: RECIPIENT_EMAIL\nSubject: SUBJECT_LINE\n\nBODY_TEXT' | /opt/homebrew/bin/himalaya message send
```

### Rules for Sending
- Always use `printf` with `\n` for line breaks (not `echo`)
- There MUST be a blank line between headers and body (the double `\n\n` before body)
- Always include the From header with full name
- For multi-line body, use `\n` for each new line
- Always confirm with the user BEFORE sending any email
- Never send emails without explicit permission

### Example - Simple Email
```bash
printf 'From: Ian James Ormo <ian@scaleplus.io>\nTo: john@example.com\nSubject: Quick follow up\n\nHey John,\n\nJust wanted to check in on the project.\n\nBest,\nIan' | /opt/homebrew/bin/himalaya message send
```

### Example - HTML Email (optional)
```bash
printf 'From: Ian James Ormo <ian@scaleplus.io>\nTo: john@example.com\nSubject: Quick follow up\nContent-Type: text/html\n\n<p>Hey John,</p><p>Just wanted to check in.</p><p>Best,<br>Ian</p>' | /opt/homebrew/bin/himalaya message send
```

## Reading Email

### List recent emails (inbox)
```bash
/opt/homebrew/bin/himalaya envelope list --page-size 10
```

### List emails from a specific folder
```bash
/opt/homebrew/bin/himalaya envelope list --folder "[Gmail]/Sent Mail" --page-size 10
```

### Read a specific email by ID
```bash
/opt/homebrew/bin/himalaya message read ID_NUMBER
```

### Search emails (basic - list then filter)
```bash
/opt/homebrew/bin/himalaya envelope list --page-size 50
```

## Account Details
- **From:** Ian James Ormo <ian@scaleplus.io>
- **Provider:** Google Workspace (Gmail)
- **Config:** ~/.config/himalaya/config.toml
- **Binary:** /opt/homebrew/bin/himalaya

## Important Notes
- Gmail auto-saves sent emails to Sent Mail (save-copy is disabled to avoid duplicates)
- Always ask before sending — this is a real email going to real people
- For BotBuilders outreach, follow the botbuilders-ops skill tone and templates
- For ScalePlus outreach, follow the scaleplus-ops skill tone and templates
