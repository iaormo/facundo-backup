# Avania Lead Gen - GoHighLevel Setup Guide

## Changes Made
- ✅ Removed Google Sheets integration
- ✅ Removed webhook dependency
- ✅ Using GoHighLevel as primary CRM
- ✅ Using Reachinbox API for sending AND polling for responses

## What You Need to Do (2 minutes)

### 1. Create Custom Fields in GHL (1 minute)

Go to your GHL subaccount: **RbxKguAHbRjqH5K5922f**

Navigate to: **Settings** → **Custom Fields** → **Create Custom Fields**

Create these contact custom fields:

| Field Name | Field Type | Description |
|------------|------------|-------------|
| `linkedin_url` | Text | LinkedIn profile URL |
| `company_website` | Text | Company website |
| `location` | Text | City, State |
| `company_size` | Text | Employee count |
| `team_member` | Text | Angela/Sam/Catriona/Jasmine/Jeannine |
| `campaign` | Text | QMSR/AI-Device/Strategic/General |
| `personalized_opening` | Text | AI-generated opening line |
| `lead_id` | Text | Unique lead identifier |
| `status` | Text | Pending/Ready/Sent/Responded |
| `apollo_source` | Text | true/false |
| `email_1_sent_date` | Text | Timestamp |
| `email_2_sent_date` | Text | Timestamp |
| `reachinbox_message_id` | Text | Message ID from Reachinbox |
| `response_date` | Text | When they replied |
| `response_category` | Text | Interested/Not Now/Wrong Person/Unsubscribe/Other |
| `response_preview` | Text | First 500 chars of reply |

### 2. Get GHL API Key (30 seconds)

1. In GHL, go to **Settings** → **Business Profile**
2. Scroll to **API Key**
3. Copy the key
4. Add to your n8n environment variables as `GHL_API_KEY`

### 3. Set Up Custom Field Mapping (30 seconds)

In Workflow 1 and 2, the custom field ID is: `RbxKguAHbRjqH5K5922f`

This needs to match your actual custom field ID. To find it:

1. Go to **Settings** → **Custom Fields**
2. Click on any custom field
3. Look at the URL - you'll see the ID
4. Update the workflows if different

## How It Works

### Workflow 1: Lead Import (Runs Manually)
1. Searches Apollo for leads
2. AI personalizes opening line
3. Creates contact in GHL with all fields populated
4. Status = "Ready"

### Workflow 2: Email Sending (Runs Every 4 Hours)
1. Gets all GHL contacts with Status = "Ready"
2. Builds email based on team member
3. Sends via Reachinbox API
4. Updates GHL contact:
   - Status = "Sent"
   - email_1_sent_date = timestamp
   - reachinbox_message_id = tracking ID

### Workflow 3: Response Tracking (Runs Every 30 Minutes)
1. Polls Reachinbox API for replies in last hour
2. Matches replies to GHL contacts by email
3. Categorizes response (Interested/Not Now/etc)
4. Updates GHL contact:
   - Status = "Responded"
   - response_date = timestamp
   - response_category = category
   - response_preview = reply text
5. Sends Slack notification

## Data Stored in GHL Contacts

Each contact will have:
- **Standard fields:** Name, email, company, job title
- **Custom fields:**
  - Personal details: linkedin_url, location, company_size
  - Campaign info: team_member, campaign, personalized_opening
  - Status tracking: status, email_sent_date, response_category
  - Full message history: response_preview

## Next Steps

1. Add `GHL_API_KEY` to your n8n environment variables
2. Create the custom fields in GHL
3. Import the 3 workflows to n8n
4. Activate workflows
5. Run Workflow 1 manually to test

## Troubleshooting

**Contacts not creating:**
- Check GHL API key is correct
- Verify custom field ID matches
- Check n8n execution logs

**Emails not sending:**
- Verify contacts have Status = "Ready"
- Check Reachinbox API key
- Check email addresses are valid

**Responses not tracking:**
- Verify Workflow 3 is active
- Check Reachinbox API is returning replies
- Verify email matching logic

---

*All credentials embedded in workflow files*
*Only need GHL_API_KEY environment variable*
