#!/usr/bin/env python3
"""
Expert Ads Specialist & Strategist
Meta, Google, LinkedIn advertising mastery
"""

import asyncio
from typing import Dict, List


# ============== ADS FUNDAMENTALS ==============

ADS_FUNDAMENTALS = """
# ADVERTISING FUNDAMENTALS

## The Advertising Equation

PROFIT = (Revenue per Customer × Customers Acquired) - Ad Spend

Or simplified:
ROAS = Revenue / Ad Spend
Target ROAS: 3:1 or higher (spend 1, make 3)

## Key Metrics

CPM (Cost Per 1000 Impressions): Brand awareness
CPC (Cost Per Click): Traffic generation
CPL (Cost Per Lead): Lead generation
CPA (Cost Per Acquisition): Sales
ROAS (Return on Ad Spend): Overall profitability

## The Ad Lifecycle

1. LEARNING PHASE
   - Algorithm figures out who responds
   - Don't make changes for 3-7 days
   - Need 50+ conversions to exit

2. SCALING PHASE
   - Increase budget 20-30% every 3-5 days
   - Monitor frequency (don't burn out audience)
   - Test new creatives

3. OPTIMIZATION PHASE
   - Cut underperforming ads
   - Test new audiences
   - Refresh creatives

## Campaign Structure Best Practices

CAMPAIGN → AD SET → AD

Campaign: Objective (Traffic, Leads, Sales)
Ad Set: Targeting (Who sees it)
Ad: Creative (What they see)

Single-ad-set-per-campaign approach:
- Better optimization
- Clearer data
- Easier to manage
"""


# ============== META ADS (FACEBOOK/INSTAGRAM) ==============

META_ADS_MASTERY = {
    "Campaign Objectives": {
        "AWARENESS": "Reach, Brand Awareness, Video Views",
        "CONSIDERATION": "Traffic, Engagement, App Installs, Video Views, Lead Generation, Messages",
        "CONVERSION": "Conversions, Catalog Sales, Store Traffic"
    },
    
    "Ad Formats": {
        "Single Image": "Best for: Simple message, quick offers",
        "Carousel": "Best for: Multiple products, storytelling, features",
        "Video": "Best for: Engagement, education, storytelling",
        "Collection": "Best for: E-commerce, product catalogs",
        "Stories/Reels": "Best for: Mobile-first, younger audience"
    },
    
    "Targeting Options": {
        "Core Audiences": "Demographics, interests, behaviors",
        "Custom Audiences": "Website visitors, email list, app users",
        "Lookalike Audiences": "Similar to your best customers",
        "Retargeting": "People who interacted but didn't convert"
    },
    
    "ScalePlus Strategy": {
        "Campaign 1 - Awareness": {
            "objective": "Video Views",
            "audience": "Business owners, entrepreneurs (broad)",
            "budget": "200 PHP/day",
            "creative": "60-second educational video about automation",
            "goal": "Build awareness and engagement"
        },
        "Campaign 2 - Consideration": {
            "objective": "Lead Generation",
            "audience": "Engaged video viewers (retargeting)",
            "budget": "500 PHP/day",
            "creative": "Carousel: 5 tasks you can automate",
            "offer": "Free automation audit",
            "goal": "Capture leads"
        },
        "Campaign 3 - Conversion": {
            "objective": "Conversions",
            "audience": "Lookalike of customers",
            "budget": "800 PHP/day",
            "creative": "Testimonial video with CTA",
            "goal": "Book discovery calls"
        }
    },
    
    "Hayahaya Strategy": {
        "Campaign 1 - Awareness": {
            "objective": "Video Views",
            "audience": "Camping, hiking, travel interests",
            "budget": "300 PHP/day",
            "creative": "Beautiful adventure reel (15-30s)",
            "goal": "Build brand awareness"
        },
        "Campaign 2 - Consideration": {
            "objective": "Lead Generation",
            "audience": "Video viewers, website visitors",
            "budget": "400 PHP/day",
            "creative": "Carousel: Top camping spots",
            "offer": "Free camping checklist + 20% off",
            "goal": "Capture emails"
        },
        "Campaign 3 - Conversion": {
            "objective": "Conversions",
            "audience": "Engaged users, lookalikes",
            "budget": "600 PHP/day",
            "creative": "Customer testimonial + availability",
            "goal": "Book rentals"
        }
    },
    
    "Creative Best Practices": {
        "Video": [
            "Hook in first 3 seconds",
            "Add captions (85% watch without sound)",
            "Vertical format for Stories/Reels",
            "15-30 seconds optimal length",
            "Clear CTA at end"
        ],
        "Images": [
            "Minimal text (use headline instead)",
            "High contrast",
            "Faces perform well",
            "Show the outcome/benefit",
            "Brand colors consistent"
        ],
        "Copy": [
            "Headline: Clear benefit or question",
            "Body: Problem → Solution → CTA",
            "Keep it short and scannable",
            "Use numbers and specifics",
            "Test different angles"
        ]
    }
}


# ============== GOOGLE ADS ==============

GOOGLE_ADS_MASTERY = {
    "Campaign Types": {
        "Search": "Text ads on Google search results",
        "Display": "Banner ads on websites",
        "Video": "YouTube ads",
        "Shopping": "Product listings",
        "Performance Max": "AI-driven across all Google properties"
    },
    
    "Search Ads - Best Practices": {
        "Keyword Match Types": {
            "Broad Match": "Automation services (loose match)",
            "Phrase Match": '"automation services" (close variants)',
            "Exact Match": "[automation services Philippines] (exact only)"
        },
        "Ad Extensions": [
            "Sitelinks (link to specific pages)",
            "Callouts (additional benefits)",
            "Structured snippets (categories)",
            "Call extensions (phone number)",
            "Location extensions (address)"
        ],
        "Quality Score Factors": [
            "Expected CTR",
            "Ad relevance",
            "Landing page experience"
        ]
    },
    
    "ScalePlus Keywords": {
        "High Intent": [
            "business automation Philippines",
            "AI automation services",
            "website development for SMEs",
            "chatbot for customer service",
            "automate my business"
        ],
        "Medium Intent": [
            "business process automation",
            "customer service automation",
            "SME digital transformation"
        ],
        "Low Intent (Informational)": [
            "what is business automation",
            "benefits of automation",
            "automation tools for business"
        ]
    },
    
    "Hayahaya Keywords": {
        "High Intent": [
            "camping gear rental Manila",
            "glamping setup Philippines",
            "Jimny rental for camping",
            "Starlink rental Philippines",
            "camping equipment rental"
        ],
        "Medium Intent": [
            "weekend camping near Manila",
            "glamping spots Philippines",
            "camping gear for rent"
        ],
        "Location-Based": [
            "camping gear rental Quezon City",
            "glamping near Tagaytay",
            "camping equipment Makati"
        ]
    },
    
    "Ad Copy Formulas": {
        "Problem-Solution": {
            "Headline 1": "Stop Doing Manual Tasks",
            "Headline 2": "Automate Your Business Today",
            "Headline 3": "Save 10+ Hours Per Week",
            "Description": "ScalePlus helps Filipino SMEs automate customer service, bookings, and admin tasks. Free 15-min audit."
        },
        "Benefit-Focused": {
            "Headline 1": "24/7 Customer Service",
            "Headline 2": "Without 24/7 Payroll",
            "Headline 3": "AI Automation for SMEs",
            "Description": "Handle inquiries automatically. Setup in 1 week. Trusted by 50+ Filipino businesses. Book free audit."
        }
    }
}


# ============== LINKEDIN ADS ==============

LINKEDIN_ADS_MASTERY = {
    "Best For": [
        "B2B lead generation",
        "Professional services",
        "High-value deals",
        "Thought leadership",
        "Recruiting"
    ],
    
    "Ad Formats": {
        "Sponsored Content": "Native posts in feed (single image, video, carousel)",
        "Sponsored Messaging": "Direct messages (Conversation Ads, Message Ads)",
        "Lead Gen Forms": "Pre-filled forms for easy conversion",
        "Dynamic Ads": "Personalized ads (Follower, Spotlight, Job Ads)",
        "Text Ads": "Simple text ads on sidebar"
    },
    
    "Targeting Options": {
        "Company": "Size, industry, name, growth rate",
        "Demographics": "Job title, seniority, function",
        "Education": "Schools, degrees, fields",
        "Interests": "Groups joined, skills, interests"
    },
    
    "ScalePlus Strategy": {
        "Audience": {
            "Job Titles": "Owner, CEO, Founder, Managing Director",
            "Company Size": "11-50, 51-200 employees",
            "Location": "Philippines",
            "Industries": "Retail, Services, Food & Beverage, Real Estate"
        },
        "Campaign 1 - Thought Leadership": {
            "objective": "Website visits",
            "format": "Sponsored Content - Single image",
            "content": "Educational post about automation trends",
            "budget": "500 PHP/day",
            "goal": "Build authority and drive traffic"
        },
        "Campaign 2 - Lead Generation": {
            "objective": "Lead generation",
            "format": "Lead Gen Form",
            "offer": "Free Automation Audit",
            "budget": "1000 PHP/day",
            "goal": "Capture qualified leads"
        },
        "Campaign 3 - Retargeting": {
            "objective": "Website conversions",
            "format": "Sponsored Content - Video",
            "audience": "Website visitors",
            "budget": "800 PHP/day",
            "goal": "Convert interested prospects"
        }
    },
    
    "Messaging Ads Best Practices": [
        "Personalize with {{first_name}}",
        "Keep it conversational",
        "Offer clear value",
        "Include CTA button",
        "Follow up if no response in 3 days"
    ]
}


# ============== AD COPY MASTERY ==============

AD_COPY_TEMPLATES = {
    "PAS (Problem-Agitate-Solution)": {
        "template": """
Problem: Are you [experiencing pain]?
Agitate: Every day you [continue pain], you [negative consequence].
Solution: [Your solution] helps you [desired outcome] without [objection].
CTA: [Clear action]
""",
        "example_scaleplus": """
Problem: Are you drowning in customer inquiries?
Agitate: Every hour you spend answering the same questions is an hour not growing your business. Your competitors are automating and getting ahead.
Solution: ScalePlus AI automation handles 80% of inquiries instantly, giving you 10 hours back per week without hiring more staff.
CTA: Book your free 15-minute automation audit
"""
    },
    
    "Before-After-Bridge": {
        "template": """
Before: [Current painful situation]
After: [Ideal future situation]
Bridge: [How you get there]
CTA: [Action]
""",
        "example_hayahaya": """
Before: Want to camp but don't want to buy 50K worth of gear you'll use twice
After: Weekend adventure with premium equipment, no storage hassles
Bridge: Hayahaya delivers everything you need - tent, Starlink, power - directly to your campsite
CTA: Check availability and get 20% off your first booking
"""
    },
    
    "AIDA (Attention-Interest-Desire-Action)": {
        "template": """
Attention: [Hook to stop the scroll]
Interest: [Why should they care]
Desire: [Paint the picture of success]
Action: [What to do now]
""",
        "example": """
Attention: Finally, 24/7 customer service without hiring a night shift
Interest: Our AI chatbots handle 80% of inquiries automatically, in Tagalog and English
Desire: Imagine waking up to find all overnight questions answered, appointments booked, and leads qualified - while you slept
Action: Get your free automation audit (only 3 spots this month)
"""
    }
}


# ============== OPTIMIZATION PLAYBOOK ==============

OPTIMIZATION_PLAYBOOK = """
# ADS OPTIMIZATION PLAYBOOK

## Weekly Optimization Checklist

### MONDAY: Review Weekend Performance
- [ ] Check spend vs. budget
- [ ] Review weekend CPA/CPL
- [ ] Note any anomalies
- [ ] Check frequency (retargeting)

### WEDNESDAY: Creative Review
- [ ] Check CTR by creative
- [ ] Pause CTR < 1% (after 3 days)
- [ ] Scale CTR > 3%
- [ ] Upload new creative variations

### FRIDAY: Audience Analysis
- [ ] Check performance by age
- [ ] Check performance by placement
- [ ] Check performance by device
- [ ] Note insights for next week

### WEEKLY: Budget Scaling
- [ ] If ROAS > 3: Increase budget 20%
- [ ] If ROAS 2-3: Keep stable, optimize
- [ ] If ROAS < 2: Cut or fix

## Troubleshooting Guide

### High CPM (Cost Per 1000 Impressions)
Causes:
- Too narrow audience
- Competitive auction
- Low relevance score
Fixes:
- Broaden audience slightly
- Test new creative
- Improve ad relevance

### High CPC (Cost Per Click)
Causes:
- Weak creative/headline
- Wrong audience
- Low relevance
Fixes:
- Test new hooks in first 3 seconds
- Refine targeting
- Improve ad-audience match

### Low Conversion Rate
Causes:
- Landing page mismatch
- Weak offer
- Technical issues
Fixes:
- Align landing page with ad
- Strengthen offer/incentive
- Check tracking is working

### Ad Fatigue (Frequency > 3)
Causes:
- Audience seen ad too many times
- Creative is stale
Fixes:
- Refresh creative
- Expand audience
- Exclude recent converters

## A/B Testing Framework

### What to Test (Priority Order)
1. Headline/Hook (biggest impact)
2. Offer/Incentive
3. Image/Video creative
4. Call-to-action
5. Targeting

### Test Structure
- Test one variable at a time
- Run for 3-7 days minimum
- Need 100+ conversions for significance
- Winner: Lower CPA or higher ROAS

### Test Ideas for ScalePlus
- Headline: "Save Time" vs "Save Money" vs "Reduce Stress"
- Offer: Free Audit vs ROI Calculator vs Case Study
- Creative: Testimonial vs Demo vs Educational
- CTA: "Book Audit" vs "See How It Works" vs "Get Started"

### Test Ideas for Hayahaya
- Hook: Beautiful scenery vs Happy people vs Gear close-up
- Offer: 20% off vs Free delivery vs Extra day free
- Angle: Adventure vs Relaxation vs Instagram-worthy
- CTA: "Book Now" vs "Check Availability" vs "Plan Your Trip"
"""


# ============== Main ==============

async def main():
    """Demonstrate ads specialist expertise."""
    print("=" * 70)
    print("EXPERT ADS SPECIALIST & STRATEGIST")
    print("=" * 70)
    
    print("\n1. PLATFORM MASTERY")
    print("-" * 40)
    print("   Meta (Facebook/Instagram):")
    print("     • Campaign objectives: Awareness → Consideration → Conversion")
    print("     • Ad formats: Image, Video, Carousel, Collection")
    print("     • Targeting: Core, Custom, Lookalike, Retargeting")
    print("\n   Google Ads:")
    print("     • Search: Text ads on keywords")
    print("     • Display: Banner ads on websites")
    print("     • YouTube: Video ads")
    print("     • Shopping: Product listings")
    print("\n   LinkedIn Ads:")
    print("     • Best for: B2B, professional services")
    print("     • Formats: Sponsored Content, Messaging, Lead Gen Forms")
    print("     • Targeting: Job title, company, seniority")
    
    print("\n2. SCALEPLUS.IO AD STRATEGY")
    print("-" * 40)
    print("   Campaign 1: Awareness (200 PHP/day)")
    print("     Video views → Build awareness")
    print("   Campaign 2: Consideration (500 PHP/day)")
    print("     Lead gen → Free automation audit")
    print("   Campaign 3: Conversion (800 PHP/day)")
    print("     Conversions → Book discovery calls")
    
    print("\n3. HAYAHAYA ADVENTURES STRATEGY")
    print("-" * 40)
    print("   Campaign 1: Awareness (300 PHP/day)")
    print("     Video views → Adventure reels")
    print("   Campaign 2: Consideration (400 PHP/day)")
    print("     Lead gen → Free checklist + 20% off")
    print("   Campaign 3: Conversion (600 PHP/day)")
    print("     Conversions → Book rentals")
    
    print("\n4. AD COPY MASTERY")
    print("-" * 40)
    print("   PAS (Problem-Agitate-Solution)")
    print("   Before-After-Bridge")
    print("   AIDA (Attention-Interest-Desire-Action)")
    print("   All with real examples for your businesses")
    
    print("\n5. OPTIMIZATION SYSTEM")
    print("-" * 40)
    print("   Weekly checklist: Mon/Wed/Fri tasks")
    print("   Troubleshooting: CPM, CPC, conversion issues")
    print("   A/B testing framework")
    print("   Budget scaling rules")
    
    print("\n" + "=" * 70)
    print("ADS SPECIALIST MASTERY COMPLETE")
    print("=" * 70)
    print("\nCapabilities:")
    print("  ✅ Create high-performing Meta ad campaigns")
    print("  ✅ Build profitable Google Ads accounts")
    print("  ✅ Execute LinkedIn B2B lead generation")
    print("  ✅ Write compelling ad copy")
    print("  ✅ Optimize for ROAS and CPA targets")
    print("  ✅ Scale winning campaigns profitably")
    print("\nReady to drive qualified leads at scale!")


if __name__ == "__main__":
    asyncio.run(main())
