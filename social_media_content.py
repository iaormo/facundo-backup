#!/usr/bin/env python3
"""
Social Media Content Mastery for Ian (Papi)
Daily encouraging posts based on his life and values
"""

import asyncio
from datetime import datetime


# ============== DAILY SOCIAL MEDIA POSTS ==============

SOCIAL_POSTS = {
    "fatherhood": [
        "Your kids don't need a perfect dad. They need a present dad. Show up today. 💪",
        "The days are long but the years are short. One more bedtime story, one more hug. 🏠",
        "Fatherhood isn't about having all the answers. It's about walking with them while they find theirs. 👣",
        "Your children are watching how you treat their mother. Show them what love looks like. ❤️",
        "The greatest inheritance you can leave your children is your time and your character. 🌟",
    ],
    
    "entrepreneurship": [
        "Started from zero, building something meaningful. Every small step counts. 🚀",
        "Your 1-3 PM work window is sacred. Protect it like your future depends on it. Because it does. ⏰",
        "Automation isn't about replacing humans. It's about freeing humans to do what matters. 🤖",
        "Small business owners: You're not just building a company. You're building a legacy. 💼",
        "The best time to start was yesterday. The second best time is your 1 PM work window today. 📈",
    ],
    
    "faith": [
        "Sunday is not the end of the week. It's the beginning of everything that matters. ✝️",
        "Leading worship isn't about performance. It's about pointing people to the One worth worshipping. 🎵",
        "Your ministry to one high schooler might change their eternity. Never underestimate small faithful steps. 🙏",
        "Faith isn't the absence of doubt. It's the presence of trust despite the doubt. 🕊️",
        "Serve your church not because you have to, but because you get to. Privilege, not burden. ⛪",
    ],
    
    "marriage": [
        "Behind every dad building a business is a wife holding down the home. Tag your partner in crime. 💑",
        "Homeschooling together. Building together. Serving together. That's the dream. 🏠",
        "Marriage isn't 50/50. It's 100/100. Both showing up fully, even when it's hard. 💍",
        "Date your wife. Even if it's just coffee at home after the kids sleep. Keep choosing each other. ☕",
        "The best gift you can give your children is a marriage they want to emulate. 👨‍👩‍👧‍👦",
    ],
    
    "homestead": [
        "Charlotte Mason, task cards, and three kids. Homeschooling isn't for the faint of heart. But neither are you. 📚",
        "8 AM to 5 PM with your kids? That's not just homeschooling. That's discipleship. 🎓",
        "Your wife is a full-time teacher and full-time mom. No helper. Just pure dedication. Superwoman wears pajamas. 👩‍🏫",
        "Sibling relationships matter more than perfect curriculum. Character over credentials. ❤️",
        "The goal isn't perfect kids. It's kids who love Jesus, love learning, and love each other. 🌱",
    ],
    
    "filipino_pride": [
        "Filipino entrepreneurs building from the islands to the world. Represent. 🇵🇭",
        "Late night hustle (8 PM Manila) while the family sleeps. This is how legacies are built. 🌙",
        "Supporting local SMEs with automation. Lifting up the Philippines, one business at a time. 💙",
        "From Dauin to wherever God leads. Filipino grit meets global vision. 🌏",
        "We're not just building businesses. We're building hope for Filipino families. 💪",
    ],
    
    "work_life": [
        "Sleep 5 AM to 12 noon. Work 1 PM to 3 PM. Family the rest. Boundaries are beautiful. 🛏️",
        "Sunday is for church. No exceptions. Your soul needs rest more than your business needs you. ⛪",
        "Remote work from a campsite with Starlink? The future is now. Balance is possible. ⛺",
        "You don't need more hours. You need focused hours. 1-3 PM. Make them count. ⏳",
        "Work hard 5 days. Rest hard 1 day. Worship hard 1 day. That's the rhythm. 🔄",
    ],
    
    "encouragement": [
        "You don't have to be perfect. You just have to be faithful. Today is enough. ✨",
        "Someone needs to hear this: You're doing better than you think you are. Keep going. 🌟",
        "Discouraged? Remember why you started. The vision is still worth it. 🔥",
        "Your consistency today is creating your breakthrough tomorrow. Don't quit. 💪",
        "Every dad building a business while raising kids is fighting a battle no one sees. I see you. 👊",
    ],
    
    "leadership": [
        "Leading ushers at 5 PM service. Every role matters when you're serving the King. 👑",
        "High School Blast every Saturday. Investing in the next generation of leaders. 🎓",
        "The best leaders aren't those who know everything. They're those who serve everyone. 🙌",
        "Ministry isn't about platform. It's about people. Serve the one in front of you. 🤝",
        "Your kids are your first ministry. Your church is your extended ministry. Both matter. ✝️",
    ],
    
    "morning_motivation": [
        "Good morning. Your family needs you. Your business needs you. But first, you need Jesus. 🙏",
        "New day. New mercies. Same faithful God. Let's go. ☀️",
        "The morning devotional isn't checking a box. It's filling your tank. Don't skip it. 📖",
        "Another day to be a better dad, a better husband, a better man. Let's get it. 💯",
        "You woke up. That's grace. Now use it wisely. 🌅",
    ]
}


# ============== POSTING STRATEGY ==============

POSTING_STRATEGY = """
# SOCIAL MEDIA POSTING STRATEGY FOR IAN

## Daily Posting Schedule

**Monday:** Entrepreneurship / Work-Life Balance
**Tuesday:** Fatherhood / Family
**Wednesday:** Faith / Ministry
**Thursday:** Marriage / Partnership
**Friday:** Filipino Pride / Local Business
**Saturday:** Homeschool / Education
**Sunday:** Faith / Worship (morning only)

## Post Format

- **Length:** 1-3 sentences max
- **Tone:** Authentic, vulnerable, encouraging
- **Style:** Short, punchy, emotionally engaging
- **Hashtags:** None (your preference)
- **Emojis:** Minimal, meaningful

## Engagement Tips

- Post when your audience is active (test different times)
- Respond to comments within 1-2 hours
- Share real moments, not just polished thoughts
- Let your personality shine through
- Be consistent - daily presence builds trust

## Topics to Rotate

1. Behind-the-scenes of ScalePlus
2. Homeschool wins and struggles
3. Marriage moments with Heidi
4. Kids' milestones (with permission)
5. Ministry reflections
6. Filipino business journey
7. Remote work setups
8. Faith in the marketplace
9. Work-life boundaries
10. Early morning thoughts
"""


# ============== SAMPLE WEEKS ==============

SAMPLE_WEEK_1 = """
# SAMPLE WEEK 1

**Monday:** "Started from zero, building something meaningful. Every small step counts. 🚀"

**Tuesday:** "Your kids don't need a perfect dad. They need a present dad. Show up today. 💪"

**Wednesday:** "Sunday is not the end of the week. It's the beginning of everything that matters. ✝️"

**Thursday:** "Behind every dad building a business is a wife holding down the home. 💑"

**Friday:** "Filipino entrepreneurs building from the islands to the world. Represent. 🇵🇭"

**Saturday:** "Charlotte Mason, task cards, and three kids. Homeschooling isn't for the faint of heart. 📚"

**Sunday:** "Good morning. Your family needs you. Your business needs you. But first, you need Jesus. 🙏"
"""


# ============== Main ==============

async def main():
    print("=" * 70)
    print("SOCIAL MEDIA CONTENT MASTERY FOR IAN")
    print("=" * 70)
    
    print("\nCONTENT PILLARS:")
    print("-" * 40)
    for category in SOCIAL_POSTS.keys():
        print(f"  • {category.replace('_', ' ').title()}")
    
    print(f"\nTOTAL POSTS IN LIBRARY: {sum(len(posts) for posts in SOCIAL_POSTS.values())}")
    
    print("\nPOSTING SCHEDULE:")
    print("-" * 40)
    print("  Monday: Entrepreneurship")
    print("  Tuesday: Fatherhood")
    print("  Wednesday: Faith")
    print("  Thursday: Marriage")
    print("  Friday: Filipino Pride")
    print("  Saturday: Homeschool")
    print("  Sunday: Faith/Worship")
    
    print("\nSAMPLE POSTS:")
    print("-" * 40)
    for category, posts in list(SOCIAL_POSTS.items())[:3]:
        print(f"\n{category.replace('_', ' ').title()}:")
        print(f'  "{posts[0]}"')
    
    print("\n" + "=" * 70)
    print("READY TO POST DAILY ENCOURAGEMENT")
    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())
