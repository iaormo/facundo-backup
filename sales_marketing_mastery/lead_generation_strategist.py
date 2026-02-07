#!/usr/bin/env python3
"""
World's Best Lead Generation Strategist
Complete playbook for ScalePlus.io and Hayahaya Adventures
"""

import asyncio
from typing import List, Dict, Any


# ============== LEAD GENERATION PHILOSOPHY ==============

LEAD_GEN_PHILOSOPHY = """
# WORLD-CLASS LEAD GENERATION PHILOSOPHY

## The Lead Generation Equation

QUALIFIED LEADS = (Traffic Quality × Conversion Rate) / Cost

To maximize leads:
1. Increase traffic from ideal customer sources
2. Improve conversion with better offers and UX
3. Reduce cost through optimization and targeting

## The 3-Pillar Approach

### PILLAR 1: Attract (Get them to notice you)
- Content that solves problems
- SEO for high-intent keywords
- Social media presence
- Paid advertising

### PILLAR 2: Capture (Get their contact info)
- Irresistible lead magnets
- Optimized landing pages
- Webinar registrations
- Free consultations

### PILLAR 3: Nurture (Build relationship until ready)
- Email sequences
- Retargeting ads
- Social proof
- Value-first follow-up

## Lead Quality Spectrum

COLD → WARM → HOT → CUSTOMER

Cold Leads:
- Don't know you exist
- Haven't identified their problem
- Need education first

Warm Leads:
- Aware of their problem
- Researching solutions
- Comparing options

Hot Leads:
- Ready to buy
- Evaluating specific vendors
- Need final nudge

Your goal: Move them from cold to hot systematically.

## ScalePlus.io Lead Gen Strategy

### Ideal Customer Journey:

1. DISCOVERY (Cold)
   Trigger: See LinkedIn post about automation
   Action: Read, maybe like/comment
   
2. AWARENESS (Cold → Warm)
   Trigger: Download "50 Tasks to Automate" PDF
   Action: Join email list
   
3. EDUCATION (Warm)
   Trigger: Email sequence about automation ROI
   Action: Open emails, click links
   
4. CONSIDERATION (Warm → Hot)
   Trigger: Watch case study video
   Action: Click to book audit
   
5. EVALUATION (Hot)
   Trigger: Discovery call
   Action: Discuss specific needs
   
6. DECISION (Hot → Customer)
   Trigger: Receive proposal
   Action: Sign contract

### Lead Sources Priority:

Tier 1 (Highest Quality):
- Referrals from existing clients
- LinkedIn direct outreach
- Discovery calls from content
- Partner introductions

Tier 2 (Good Quality):
- Facebook/Instagram ads
- Google Search ads
- Webinar attendees
- Event networking

Tier 3 (Lower Quality, Scale):
- SEO organic traffic
- Social media followers
- General content downloads
- Display ads

## Hayahaya Adventures Lead Gen Strategy

### Customer Journey:

1. DREAM (Cold)
   Trigger: See stunning Instagram reel
   Action: Double-tap, maybe follow
   
2. PLAN (Cold → Warm)
   Trigger: Download camping checklist
   Action: Join email list, get discount code
   
3. IMAGINE (Warm)
   Trigger: Browse gear catalog
   Action: Look at Jimny, Starlink packages
   
4. COMMIT (Warm → Hot)
   Trigger: Check availability
   Action: Select dates, see pricing
   
5. BOOK (Hot)
   Trigger: Complete booking form
   Action: Make deposit payment
   
6. EXPERIENCE (Customer)
   Trigger: Pickup/delivery
   Action: Use gear, have adventure
   
7. SHARE (Advocate)
   Trigger: Post on social media
   Action: Tag Hayahaya, refer friends

### Lead Sources Priority:

Tier 1:
- Instagram/TikTok influencer collabs
- Referrals from past customers
- Google "camping gear rental Manila"
- Facebook/Instagram ads

Tier 2:
- SEO for camping content
- Social media organic
- Partnerships with campsites
- Event presence (outdoor expos)

Tier 3:
- Display ads
- Broad social targeting
- Cold email
"""


# ============== LEAD MAGNET BLUEPRINT ==============

LEAD_MAGNET_BLUEPRINT = {
    "ScalePlus.io": {
        "The Automation ROI Calculator": {
            "type": "Interactive Tool",
            "hook": "See exactly how much time and money you'll save",
            "value_proposition": "Personalized savings report based on your business",
            "time_to_create": "4 hours",
            "conversion_rate": "15-25%",
            "follow_up": "5-day email course on automation basics",
            "promotion": "LinkedIn posts, Facebook ads to business owners"
        },
        
        "50 Tasks You Can Automate Today": {
            "type": "PDF Checklist",
            "hook": "Stop doing manual work that software can handle",
            "value_proposition": "Categorized by department (sales, support, admin)",
            "time_to_create": "2 hours",
            "conversion_rate": "25-35%",
            "follow_up": "Case studies of businesses who automated these",
            "promotion": "Blog posts, LinkedIn articles"
        },
        
        "The SME Tech Stack Guide": {
            "type": "PDF + Spreadsheet",
            "hook": "Best tools for every business function",
            "value_proposition": "Curated, tested, with pricing and alternatives",
            "time_to_create": "3 hours",
            "conversion_rate": "20-30%",
            "follow_up": "Tool-specific tutorials",
            "promotion": "SEO, Facebook groups"
        },
        
        "Customer Service Response Templates": {
            "type": "Notion Template + Video",
            "hook": "Never stare at a blank screen again",
            "value_proposition": "50+ templates for common scenarios",
            "time_to_create": "3 hours",
            "conversion_rate": "30-40%",
            "follow_up": "Training on using templates effectively",
            "promotion": "Target support managers on LinkedIn"
        },
        
        "Free 15-Minute Automation Audit": {
            "type": "Consultation",
            "hook": "I'll find 3 things you can automate right now",
            "value_proposition": "Personalized advice from expert",
            "time_to_create": "30 min (setup Calendly)",
            "conversion_rate": "5-10% (but 50%+ close rate)",
            "follow_up": "Proposal within 24 hours",
            "promotion": "All channels, highest priority"
        },
        
        "Private Facebook Group: Filipino Business Automators": {
            "type": "Community",
            "hook": "Join 500+ business owners automating their growth",
            "value_proposition": "Daily tips, Q&A, networking",
            "time_to_create": "1 hour (setup)",
            "conversion_rate": "40-50%",
            "follow_up": "Weekly live sessions, member spotlights",
            "promotion": "All channels, viral growth"
        }
    },
    
    "Hayahaya Adventures": {
        "The Ultimate Camping Checklist": {
            "type": "Interactive PDF + App",
            "hook": "Never forget essential gear again",
            "value_proposition": "Categorized checklist with weather considerations",
            "time_to_create": "2 hours",
            "conversion_rate": "35-45%",
            "follow_up": "Gear recommendations with rental links",
            "promotion": "Instagram, Facebook camping groups"
        },
        
        "Top 10 Glamping Spots Near Manila": {
            "type": "Guide + Google Maps + Videos",
            "hook": "Weekend getaways within 3 hours",
            "value_proposition": "Detailed guides with permits, costs, best seasons",
            "time_to_create": "4 hours",
            "conversion_rate": "30-40%",
            "follow_up": "Gear packages for each spot",
            "promotion": "SEO, social media, travel groups"
        },
        
        "Starlink Setup Guide for Beginners": {
            "type": "Video Course + PDF",
            "hook": "Get online anywhere in 10 minutes",
            "value_proposition": "Step-by-step with troubleshooting",
            "time_to_create": "3 hours",
            "conversion_rate": "25-35%",
            "follow_up": "Rental offer: 'Try before you buy'",
            "promotion": "YouTube, digital nomad groups"
        },
        
        "Adventure Planning Template": {
            "type": "Notion/Sheets Template",
            "hook": "Plan the perfect trip every time",
            "value_proposition": "Budget tracker, packing list, itinerary builder",
            "time_to_create": "2 hours",
            "conversion_rate": "30-40%",
            "follow_up": "Sample itineraries for different group sizes",
            "promotion": "Instagram, Pinterest"
        },
        
        "The Weekender's Guide to Camping": {
            "type": "Email Course (5 days)",
            "hook": "Learn to camp in 5 days - 1 email per day",
            "value_proposition": "Beginner-friendly, no gear needed",
            "time_to_create": "3 hours",
            "conversion_rate": "40-50%",
            "follow_up": "First booking discount (20% off)",
            "promotion": "Pop-ups, social media"
        }
    }
}


# ============== LANDING PAGE FORMULA ==============

LANDING_PAGE_FORMULA = """
# HIGH-CONVERTING LANDING PAGE FORMULA

## Headline Formula
[End Result] + [Time Period] + [Objection Handler]

Examples:
- "Get 10 Hours Back Per Week with Automation (Without Hiring)"
- "Plan Your Perfect Camping Trip in 30 Minutes (Even If You've Never Camped)"
- "24/7 Customer Service for 1/10th the Cost (Setup in 1 Week)"

## Landing Page Structure

### ABOVE THE FOLD
1. Headline (clear value proposition)
2. Subheadline (expand on the promise)
3. Hero Image/Video (show the outcome)
4. CTA Button (what they get)
5. Trust Indicator (social proof count)

### THE BODY
6. Problem Agitation (do you experience this?)
7. Solution Introduction (how this solves it)
8. Benefits (3-5 key benefits with icons)
9. Social Proof (testimonials with photos)
10. How It Works (3 simple steps)
11. FAQ (address objections)
12. Final CTA (button + urgency)

### BELOW THE FOLD
13. More Social Proof (logos, case studies)
14. Guarantee (risk reversal)
15. About/Credentials (why trust you)
16. Contact Info (reduce friction)

## ScalePlus Landing Page

HEADLINE: "Stop Doing Work That Software Can Handle"
SUBHEADLINE: "Filipino SMEs save 10+ hours/week with our AI automation. No technical skills required."

BENEFITS:
1. 24/7 Customer Service - Chatbots handle inquiries instantly
2. Save 10+ Hours/Week - Automate repetitive tasks
3. Scale Without Hiring - Handle 10x volume with same team
4. Setup in 1 Week - We handle all the technical work

SOCIAL PROOF:
"ScalePlus automated our booking system and saved us 15 hours per week. Best investment we've made." - Maria Santos, Resort Owner

CTA: "Get Your Free Automation Audit"
FORM: Name, Email, Company, Biggest Challenge

## Hayahaya Landing Page

HEADLINE: "Adventure Without the Gear Investment"
SUBHEADLINE: "Premium camping and glamping gear delivered to your destination. Starlink internet included."

BENEFITS:
1. No Gear Purchase - Rent everything you need
2. Setup in 30 Minutes - We provide instructions + support
3. Stay Connected - Starlink internet anywhere
4. Instagram-Ready - Professional glamping setup

SOCIAL PROOF:
"The Starlink was a game-changer. Posting from the middle of nowhere!" - John Reyes, Content Creator

CTA: "Check Availability & Pricing"
FORM: Name, Email, Preferred Dates, Group Size
"""


# ============== EMAIL NURTURE SEQUENCES ==============

EMAIL_SEQUENCES = {
    "ScalePlus - Automation Audit Leads": [
        {
            "day": 0,
            "subject": "Your Automation Audit is confirmed",
            "content": "Thanks for booking! Here's what to expect...",
            "cta": "Add to Calendar"
        },
        {
            "day": 1,
            "subject": "Case Study: How [Company] Saved 20 Hours/Week",
            "content": "Similar to your business, they were overwhelmed...",
            "cta": "Read Full Case Study"
        },
        {
            "day": 3,
            "subject": "The 5 Most Time-Consuming Tasks (And How to Automate Them)",
            "content": "1. Email responses... 2. Appointment scheduling...",
            "cta": "Download Free Checklist"
        },
        {
            "day": 5,
            "subject": "Quick question about your audit",
            "content": "Looking forward to our call. One quick question...",
            "cta": "Reply to This Email"
        },
        {
            "day": 7,
            "subject": "What if you never had to answer the same question twice?",
            "content": "Imagine never typing the same email response again...",
            "cta": "See How It Works"
        }
    ],
    
    "Hayahaya - Camping Checklist Download": [
        {
            "day": 0,
            "subject": "Your Camping Checklist is here!",
            "content": "Download + exclusive 20% off code inside...",
            "cta": "Download Checklist"
        },
        {
            "day": 2,
            "subject": "The #1 mistake first-time campers make",
            "content": "Don't forget the ground tarp! Here's why...",
            "cta": "See Full Gear List"
        },
        {
            "day": 4,
            "subject": "3 Glamping Spots Perfect for Beginners",
            "content": "Easy access, beautiful views, all permits handled...",
            "cta": "Check Availability"
        },
        {
            "day": 7,
            "subject": "Your 20% discount expires tomorrow",
            "content": "Don't miss out on your first booking discount...",
            "cta": "Book Now & Save"
        },
        {
            "day": 14,
            "subject": "Still planning your trip?",
            "content": "Here are some itineraries that might help...",
            "cta": "View Itineraries"
        }
    ]
}


# ============== LEAD SCORING ==============

LEAD_SCORING = """
# LEAD SCORING SYSTEM

Assign points based on behavior and profile:

## DEMOGRAPHIC SCORING

ScalePlus:
+20 points: Company size 10-50 employees
+30 points: Company size 50-200 employees
+10 points: Revenue 5M-20M PHP
+20 points: Revenue 20M+ PHP
+15 points: Job title: Owner/CEO
+10 points: Job title: Manager/Director
+20 points: Industry: E-commerce, Services, SaaS

Hayahaya:
+15 points: Age 28-40
+10 points: Metro Manila location
+20 points: Previous outdoor experience
+15 points: Group size 4-8 (sweet spot)
+10 points: Interested in Starlink

## BEHAVIORAL SCORING

+5 points: Visit pricing page
+10 points: Visit case studies/testimonials
+20 points: Download lead magnet
+30 points: Book discovery call/audit
+15 points: Open email
+25 points: Click email link
+40 points: Watch demo video
+50 points: Request proposal

## SCORE RANGES

Cold (0-25): Nurture with content
Warm (26-50): Sales outreach
Hot (51-75): Priority follow-up
Qualified (76+): Immediate sales attention

## AUTOMATION RULES

IF score > 50 AND not contacted:
  → Send to sales team
  
IF score > 75:
  → Personal email from founder
  
IF no activity 30 days:
  → Re-engagement campaign
  
IF clicked pricing AND visited 3+ times:
  → Trigger retargeting ads
"""


# ============== Main ==============

async def main():
    """Demonstrate lead generation expertise."""
    print("=" * 70)
    print("WORLD'S BEST LEAD GENERATION STRATEGIST")
    print("=" * 70)
    
    print("\n1. LEAD GENERATION PHILOSOPHY")
    print("-" * 40)
    print("   Formula: QUALIFIED LEADS = (Traffic × Conversion) / Cost")
    print("   3 Pillars: Attract → Capture → Nurture")
    print("   Journey: Cold → Warm → Hot → Customer")
    
    print("\n2. LEAD MAGNETS LIBRARY")
    print("-" * 40)
    print("   ScalePlus.io (6 lead magnets):")
    for name in LEAD_MAGNET_BLUEPRINT["ScalePlus.io"].keys():
        print(f"     • {name}")
    print("\n   Hayahaya Adventures (5 lead magnets):")
    for name in LEAD_MAGNET_BLUEPRINT["Hayahaya Adventures"].keys():
        print(f"     • {name}")
    
    print("\n3. LANDING PAGE FORMULA")
    print("-" * 40)
    print("   Structure: 16 elements from headline to final CTA")
    print("   Headline formula: [Result] + [Time] + [Objection Handler]")
    print("   Example: 'Get 10 Hours Back Per Week (Without Hiring)'")
    
    print("\n4. EMAIL NURTURE SEQUENCES")
    print("-" * 40)
    print("   ScalePlus (5 emails over 7 days)")
    print("   Hayahaya (5 emails over 14 days)")
    print("   All with specific timing, subject lines, and CTAs")
    
    print("\n5. LEAD SCORING SYSTEM")
    print("-" * 40)
    print("   Demographic scoring (company size, title, etc.)")
    print("   Behavioral scoring (pages visited, emails opened)")
    print("   Ranges: Cold (0-25) to Qualified (76+)")
    print("   Automation rules for sales handoff")
    
    print("\n" + "=" * 70)
    print("LEAD GENERATION MASTERY COMPLETE")
    print("=" * 70)
    print("\nCapabilities:")
    print("  ✅ Create irresistible lead magnets")
    print("  ✅ Design high-converting landing pages")
    print("  ✅ Build automated nurture sequences")
    print("  ✅ Score and prioritize leads")
    print("  ✅ Optimize conversion rates")
    print("  ✅ Scale lead generation profitably")
    print("\nReady to flood the pipeline with qualified leads!")


if __name__ == "__main__":
    asyncio.run(main())
