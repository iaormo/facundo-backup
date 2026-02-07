#!/usr/bin/env python3
"""
Prompt Engineering Mastery
World-class prompt engineering for AI systems
"""

import asyncio
from typing import Dict, List, Any, Optional


# ============== CORE PRINCIPLES ==============

CORE_PRINCIPLES = """
# PROMPT ENGINEERING FUNDAMENTALS

## What is Prompt Engineering?
The art and science of crafting inputs to AI systems to produce desired outputs.
It's not about "tricking" AI—it's about clear communication.

## The Prompt Engineering Formula

QUALITY OUTPUT = Clear Instructions + Context + Examples + Constraints

## The 5 Principles of Great Prompts

### 1. CLARITY
Be specific about what you want.

❌ Bad: "Write something about marketing"
✅ Good: "Write a 500-word blog post about email marketing for B2B SaaS companies, 
         targeting marketing managers. Include 3 actionable tips and a CTA."

### 2. CONTEXT
Provide relevant background information.

❌ Bad: "Analyze this data"
✅ Good: "You're a data analyst for an e-commerce company. Analyze this Q4 sales data 
         and identify: 1) Top 3 growth opportunities, 2) Underperforming categories, 
         3) Recommendations for Q1."

### 3. CONSTRAINTS
Set boundaries and specifications.

❌ Bad: "Create a social media post"
✅ Good: "Create an Instagram post for a coffee shop:
         - Max 150 characters (for caption)
         - Tone: Friendly, energetic
         - Include emoji
         - Hashtag strategy: 5 hashtags
         - Goal: Drive morning rush visits"

### 4. EXAMPLES (Few-Shot Learning)
Show what good looks like.

Prompt: 
"Classify these customer reviews as Positive, Neutral, or Negative.

Examples:
Review: 'Amazing product, highly recommend!'
Sentiment: Positive

Review: 'It\'s okay, nothing special.'
Sentiment: Neutral

Review: 'Terrible quality, waste of money.'
Sentiment: Negative

Now classify:
Review: 'Exactly what I needed, fast shipping!'
Sentiment:"

### 5. ITERATION
Treat prompting as a conversation, not a one-shot.

Step 1: Initial prompt
Step 2: Review output
Step 3: Refine based on gaps
Step 4: Repeat until satisfied

---

## The Anatomy of a Perfect Prompt

```
[ROLE]
You are [expert role].

[CONTEXT]
[Background information and situation]

[TASK]
[Specific action to perform]

[FORMAT]
[Desired output structure]

[CONSTRAINTS]
- [Limitation 1]
- [Limitation 2]

[EXAMPLES]
[Sample input/output pairs]

[EVALUATION CRITERIA]
[What makes a good response]
```

### Example: Complete Prompt

```
ROLE:
You are a senior copywriter specializing in B2B technology marketing.

CONTEXT:
Our company, ScalePlus.io, provides AI automation services for Filipino SMEs.
We help businesses automate customer service, lead follow-up, and admin tasks.
Our target customers are business owners and operations managers.

TASK:
Write a landing page headline and subheadline that converts visitors to leads.

FORMAT:
Headline: [One powerful sentence, max 10 words]
Subheadline: [2-3 sentences explaining the value, max 30 words]

CONSTRAINTS:
- Avoid jargon like "AI" and "automation" (use "smart systems" instead)
- Focus on time savings and business growth
- Include emotional appeal (relief from overwhelm)
- Use active voice

EXAMPLES:
Good Headline: "Get 10 Hours Back Every Week"
Good Subheadline: "Stop drowning in repetitive tasks. Our smart systems handle the busywork while you focus on growing your business."

Bad Headline: "AI-Powered Automation Solutions for SMEs"
Bad Subheadline: "We provide cutting-edge technology to streamline your operations."

EVALUATION CRITERIA:
- Would a busy business owner immediately understand the benefit?
- Does it create curiosity or urgency?
- Is it memorable and shareable?
```
"""


# ============== ADVANCED TECHNIQUES ==============

ADVANCED_TECHNIQUES = {
    "Chain of Thought (CoT)": {
        "description": "Prompt the model to show its reasoning step by step",
        "when_to_use": "Complex reasoning, math problems, logical analysis",
        "example": """
Solve this problem step by step:
"A bakery sells cupcakes for 50 pesos each. 
They offer a discount: buy 5, get 1 free.
Maria wants to buy 24 cupcakes for her party.
How much will she pay?"

Show your reasoning:
Step 1: [First calculation]
Step 2: [Next calculation]
...
Final Answer: [Amount]
""",
        "benefits": ["More accurate results", "Easier to debug", "Better for complex tasks"]
    },
    
    "Few-Shot Prompting": {
        "description": "Provide examples of desired input/output pairs",
        "when_to_use": "Specific formatting, style matching, classification tasks",
        "example": """
Rewrite these product descriptions to be more compelling:

Example 1:
Original: "Blue cotton t-shirt, size M, comfortable fit"
Rewrite: "Experience all-day comfort in our premium cotton tee. 
          The perfect blue that goes with everything. Fits like it was made for you."

Example 2:
Original: "Wireless headphones, noise cancelling, 20-hour battery"
Rewrite: "Block out the world, immerse in your music. 
          20 hours of uninterrupted sound. Your sanctuary, anywhere."

Now rewrite:
Original: "Stainless steel water bottle, 1 liter, keeps drinks cold"
Rewrite:
""",
        "benefits": ["Consistent formatting", "Style matching", "Better accuracy"]
    },
    
    "Zero-Shot with Definition": {
        "description": "Define the task clearly without examples",
        "when_to_use": "Simple tasks, when examples might bias results",
        "example": """
Classify the sentiment of this review as one of:
- Very Negative
- Negative
- Neutral
- Positive
- Very Positive

Review: "The product works as described but the shipping took longer than expected."

Rules:
- "Very Negative": Major issues, would not recommend
- "Negative": Some problems, disappointed
- "Neutral": Mixed feelings or no strong opinion
- "Positive": Satisfied, meets expectations
- "Very Positive": Exceeded expectations, would highly recommend

Classification:
""",
        "benefits": ["No example bias", "Faster prompting", "Good for classification"]
    },
    
    "Role Prompting": {
        "description": "Assign a specific persona to the AI",
        "when_to_use": "Specialized knowledge, specific tone, expert perspective",
        "example": """
You are a seasoned CTO with 20 years of experience in scaling tech startups.
You've successfully led companies from seed to Series B.
You're known for pragmatic, no-nonsense advice.

A founder asks you:
"We have 50 customers and growing fast. When should we hire our first product manager?"

Respond as this CTO would:
""",
        "benefits": ["Expert perspective", "Consistent voice", "Specialized knowledge"]
    },
    
    "Step-by-Step Decomposition": {
        "description": "Break complex tasks into sequential steps",
        "when_to_use": "Multi-step processes, workflows, content creation",
        "example": """
Create a comprehensive blog post by following these steps:

Step 1: Outline
Create a detailed outline with:
- 3 main sections
- 2-3 subsections per section
- Key points for each subsection

Step 2: Introduction
Write a hook that addresses the reader's pain point
Establish credibility
Preview what's covered

Step 3: Body (for each section)
Write using the key points from outline
Include examples and data
Add transition sentences

Step 4: Conclusion
Summarize main takeaways
Include clear CTA
Add thought-provoking final sentence

Step 5: Refinement
Review for clarity and flow
Check word count (target: 1500 words)
Ensure all key points are covered

Topic: Email Marketing Best Practices for E-commerce
""",
        "benefits": ["Structured output", "Easier to review", "Comprehensive coverage"]
    },
    
    "Self-Consistency": {
        "description": "Generate multiple answers and select the best/most common",
        "when_to_use": "Critical decisions, fact-checking, when accuracy is paramount",
        "example": """
Generate 3 different answers to this question, then select the best one.

Question: "What are the main benefits of automation for small businesses?"

Answer 1: [Generate]
Answer 2: [Generate]
Answer 3: [Generate]

Now analyze:
- Which answer is most comprehensive?
- Which has the most practical examples?
- Which would resonate most with a busy business owner?

Final Answer: [Select and justify]
""",
        "benefits": ["Higher accuracy", "Multiple perspectives", "Quality selection"]
    },
    
    "Tree of Thoughts": {
        "description": "Explore multiple reasoning paths, evaluate each, choose best",
        "when_to_use": "Complex problem-solving, strategic decisions",
        "example": """
Problem: "We need to increase revenue by 20% in Q2."

Explore 3 different strategies:

Path 1: Customer Acquisition Focus
- Pros: [list]
- Cons: [list]
- Expected outcome: [describe]

Path 2: Customer Retention/Expansion Focus
- Pros: [list]
- Cons: [list]
- Expected outcome: [describe]

Path 3: Pricing Optimization
- Pros: [list]
- Cons: [list]
- Expected outcome: [describe]

Evaluate each path on:
1. Cost to implement
2. Time to results
3. Risk level
4. Potential ROI

Recommendation: [Best path with reasoning]
""",
        "benefits": ["Strategic thinking", "Risk assessment", "Better decisions"]
    }
}


# ============== SYSTEM PROMPTS ==============

SYSTEM_PROMPTS = """
# SYSTEM PROMPT MASTERY

## What are System Prompts?
Instructions that set the baseline behavior, tone, and capabilities of the AI.
They apply to the entire conversation, not just a single message.

## Elements of Powerful System Prompts

### 1. IDENTITY & ROLE
Define who the AI is:
"You are a helpful AI assistant specializing in business automation."
"You are an expert copywriter with 15 years of experience."
"You are a patient, encouraging teacher."

### 2. KNOWLEDGE BOUNDARIES
Define what the AI knows:
"You have deep expertise in: marketing automation, CRM systems, email marketing."
"You do not provide legal or medical advice."
"For technical questions, you explain concepts simply without jargon."

### 3. BEHAVIOR & TONE
Define how the AI responds:
"Be concise. Use bullet points for lists."
"Be encouraging but honest about challenges."
"Use examples to illustrate concepts."
"Ask clarifying questions when the request is ambiguous."

### 4. OUTPUT FORMAT
Define structure:
"Always provide your response in this format:
- Summary: [one sentence]
- Details: [bullet points]
- Action Items: [numbered list]"

### 5. CONSTRAINTS & RULES
Define limitations:
"Never mention competitors by name."
"Keep responses under 500 words."
"If you don't know something, say so rather than guessing."

---

## Example System Prompts

### For a Customer Support AI
```
You are a helpful customer support agent for TechFlow Solutions.

Your role:
- Answer product questions clearly and accurately
- Troubleshoot technical issues step by step
- Escalate complex problems to human agents

Tone:
- Friendly and professional
- Patient with frustrated customers
- Empathetic to their challenges

Knowledge:
- Expert in all TechFlow products
- Familiar with common integrations
- Up-to-date on latest features

Constraints:
- Never share internal company information
- Don't make promises about feature timelines
- If unsure, offer to connect with specialist

Format:
1. Acknowledge their issue
2. Provide solution or next steps
3. Offer additional help
```

### For a Creative Writing Assistant
```
You are a creative writing coach and editor.

Your expertise:
- Fiction: novels, short stories, screenplays
- Non-fiction: memoirs, essays, blog posts
- Genre specialization: sci-fi, fantasy, thriller

Your approach:
- Encourage the writer's unique voice
- Provide constructive, specific feedback
- Offer techniques, not just corrections
- Ask questions to deepen the work

Tone:
- Warm and encouraging
- Honest but kind
- Enthusiastic about good writing

Behavior:
- When editing, explain WHY you're suggesting changes
- Offer alternatives, not just corrections
- Celebrate what's working well
- Adapt to the writer's experience level

Never:
- Rewrite the entire piece (unless asked)
- Be dismissive of the writer's vision
- Focus only on grammar (also address story/structure)
```

### For a Technical Documentation Writer
```
You are a technical documentation specialist.

Your role:
- Create clear, accurate technical documentation
- Explain complex concepts simply
- Structure information for easy scanning

Writing principles:
1. Clarity over cleverness
2. Specific examples over abstract descriptions
3. Active voice preferred
4. Short sentences and paragraphs
5. Consistent terminology

Format:
- Use headers for scannability
- Include code examples
- Add "TL;DR" summaries for long sections
- Use tables for comparisons

Audience awareness:
- Assume technical background but explain domain-specific terms
- Include prerequisites at the beginning
- Provide next steps at the end
- Link to related documentation

Review checklist (apply to all output):
- [ ] Accurate and up-to-date
- [ ] Complete (covers what user needs to know)
- [ ] Clear (understandable at first read)
- [ ] Concise (no unnecessary words)
```

---

## Dynamic System Prompts

Adjust based on context:

```
IF user asks about pricing:
  "You are a sales consultant. Be consultative, not pushy. 
   Ask about their needs before discussing price."

IF user reports a bug:
  "You are a technical support engineer. Prioritize understanding 
   the issue. Ask for reproduction steps."

IF user is frustrated:
  "You are a customer success manager. Focus on de-escalation 
   and finding a solution."
```
"""


# ============== PROMPT OPTIMIZATION ==============

PROMPT_OPTIMIZATION = """
# PROMPT OPTIMIZATION TECHNIQUES

## The Iterative Refinement Process

### Step 1: Baseline
Write your initial prompt and get output.

### Step 2: Evaluate
Ask:
- Did it follow instructions?
- Is the format correct?
- Is the tone appropriate?
- Is it complete?
- Are there errors?

### Step 3: Refine
Add specificity where the model failed.

### Step 4: Test
Run again with refined prompt.

### Step 5: Document
Save successful prompts as templates.

---

## Common Issues & Fixes

### Issue: Output too long
❌ "Write about email marketing"
✅ "Write a 200-word overview of email marketing for beginners"

### Issue: Wrong format
❌ "List the benefits"
✅ "List the benefits as a numbered list with brief descriptions"

### Issue: Too generic
❌ "Make this better"
✅ "Improve this headline by: 1) Adding specificity, 2) Creating urgency, 3) Including a benefit"

### Issue: Wrong tone
❌ "Write an email"
✅ "Write a professional but warm email to a client who missed a payment. 
    Be empathetic but firm about the need for payment."

### Issue: Hallucinations
❌ "Tell me about the latest trends"
✅ "Based on your training data up to [date], what were the major trends 
    in digital marketing in 2023? If you're unsure, say so."

---

## A/B Testing Prompts

Test variations to find what works best:

Test 1: Direct vs. Indirect
- A: "Write a blog post about..."
- B: "You are an expert blogger. Write a post about..."

Test 2: With vs. Without Examples
- A: "Rewrite this to be more persuasive"
- B: "Rewrite this to be more persuasive. Example: [before] → [after]"

Test 3: Different Framing
- A: "Explain quantum computing"
- B: "Explain quantum computing to a 10-year-old"
- C: "Explain quantum computing as if teaching a college class"

Track:
- Response quality (1-10)
- Accuracy
- Format adherence
- Time to desired output

---

## Prompt Templates Library

### Content Creation
```
TOPIC: [topic]
FORMAT: [blog post/email/social post/script]
AUDIENCE: [description]
TONE: [professional/casual/enthusiastic/etc]
LENGTH: [word count]
KEY POINTS TO INCLUDE:
- [point 1]
- [point 2]
- [point 3]
CTA: [what reader should do next]
```

### Analysis
```
CONTEXT: [background information]
DATA: [data to analyze]
ANALYSIS TYPE: [trend/correlation/comparison/etc]
OUTPUT FORMAT:
- Key findings: [bullet points]
- Implications: [paragraph]
- Recommendations: [numbered list]
```

### Coding
```
LANGUAGE: [programming language]
TASK: [what the code should do]
INPUT: [sample input]
EXPECTED OUTPUT: [sample output]
CONSTRAINTS:
- [constraint 1]
- [constraint 2]
INCLUDE:
- Comments explaining logic
- Error handling
- Edge case consideration
```

### Creative Writing
```
GENRE: [genre]
SETTING: [time/place]
CHARACTERS: [brief description]
PLOT POINT: [what happens]
TONE: [mood/atmosphere]
LENGTH: [word count]
STYLE NOTES: [similar to author X, include dialogue, etc]
```
"""


# ============== MULTI-MODAL & ADVANCED ==============

MULTIMODAL_PROMPTING = """
# MULTI-MODAL AND ADVANCED PROMPTING

## Multi-Modal Prompting

When working with images, audio, or other modalities:

### Image Analysis
```
Analyze this image and provide:
1. Main subject: [what is the focus]
2. Setting: [where is this]
3. Mood: [emotional tone]
4. Colors: [dominant colors]
5. Composition: [how elements are arranged]
6. Use cases: [where this could be used]
```

### Image Generation
```
Create an image with these specifications:

Subject: [main focus]
Style: [photorealistic/illustration/abstract/etc]
Colors: [palette or mood]
Lighting: [natural/dramatic/soft/etc]
Composition: [rule of thirds, centered, etc]
Mood: [feeling to convey]
Details to include: [specific elements]
Avoid: [unwanted elements]

Reference style: [artist or example]
```

### Audio/Video
```
Transcribe this audio and:
1. Provide full transcript
2. Identify speakers [Speaker 1, Speaker 2]
3. Note timestamps for key moments
4. Summarize main points
5. Extract action items
```

---

## Chain Prompting (Multi-Step)

Break complex tasks into connected prompts:

Step 1: Research
"Find information about [topic]. Provide 5 key facts."

Step 2: Outline
"Based on these facts, create an outline for a blog post."

Step 3: Draft
"Using this outline, write the first draft."

Step 4: Edit
"Review this draft and suggest improvements for:
- Clarity
- Engagement
- Structure
- Grammar"

Step 5: Polish
"Apply these improvements and produce the final version."

---

## Conditional Prompting

IF-THEN logic in prompts:

```
Analyze this customer feedback:

IF the feedback is positive (4-5 stars):
  - Thank them for specific praise
  - Ask for a referral or review
  - Offer loyalty reward

IF the feedback is neutral (3 stars):
  - Acknowledge their mixed experience
  - Ask what would make it 5 stars
  - Offer to make it right

IF the feedback is negative (1-2 stars):
  - Apologize sincerely
  - Take responsibility
  - Offer immediate resolution
  - Escalate to manager if appropriate

Feedback: [paste here]
```

---

## Meta-Prompting

Prompts that create prompts:

```
I need to create a prompt that will [desired outcome].

Please create an effective prompt that includes:
1. Clear role definition
2. Specific task description
3. Output format requirements
4. Any constraints
5. Example if helpful

The prompt should be optimized for [model name] and designed to [specific goal].
```

Example output:
```
"You are an expert SEO copywriter.

Create meta descriptions for web pages.

Requirements:
- Max 155 characters
- Include target keyword naturally
- Include call to action
- Enticing click-through

Format:
Page: [page title]
Keyword: [target keyword]
Meta Description: [your output]

Example:
Page: Email Marketing Services
Keyword: email marketing
Meta Description: Boost sales with expert email marketing. 
Get 10x ROI. Free strategy call. Start growing today!"
```
"""


# ============== DOMAIN-SPECIFIC PROMPTS ==============

DOMAIN_PROMPTS = {
    "Sales": {
        "Cold Email": """
Write a cold email to [prospect role] at [company type].

Context:
- Our product: [product description]
- Their likely pain point: [pain point]
- Value proposition: [value]

Structure:
1. Subject line: [intriguing but not clickbait]
2. Opening: [personalized hook]
3. Problem: [acknowledge their pain]
4. Solution: [how you help]
5. Proof: [brief credibility]
6. CTA: [low-commitment ask]
7. P.S.: [additional hook]

Tone: Professional but conversational
Length: 150 words max
        """,
        
        "Discovery Call Questions": """
Create a discovery call script for [product/service].

Opening (build rapport):
- [2-3 questions about them/business]

Discovery (understand pain):
- [3-4 questions about current challenges]
- [2-3 questions about goals]
- [2 questions about timeline/budget]

Value Demo (show solution):
- [How to transition to showing product]
- [Key features to highlight based on pain]

Objection Handling:
- Price: [response]
- Timing: [response]
- Competition: [response]

Closing:
- [How to ask for next step]
        """
    },
    
    "Marketing": {
        "Landing Page": """
Create a landing page for [product/service].

Target audience: [description]
Main benefit: [benefit]
Offer: [what they get]

Sections:
1. Hero: [headline + subhead + CTA]
2. Problem: [pain point]
3. Solution: [how it works]
4. Benefits: [3 key benefits with icons]
5. Social Proof: [testimonial]
6. FAQ: [3 common objections]
7. Final CTA: [urgency element]

Tone: [description]
        """,
        
        "Email Sequence": """
Create a 5-email nurture sequence for [audience].

Goal: [conversion goal]
Product: [description]

Email 1 (Day 0): Welcome + deliver lead magnet
Subject: [subject line]
Content: [structure]
CTA: [action]

Email 2 (Day 2): Problem agitation
Subject: [subject line]
Content: [structure]
CTA: [action]

[Continue for emails 3-5...]
        """
    },
    
    "Product": {
        "PRD (Product Requirements Doc)": """
Create a PRD for [feature name].

Overview:
- Problem Statement: [what pain this solves]
- Target User: [who benefits]
- Success Metrics: [how we measure success]

Requirements:
Functional:
- [requirement 1]
- [requirement 2]

Non-Functional:
- Performance: [requirements]
- Security: [requirements]
- Scalability: [requirements]

User Stories:
As a [user], I want [goal], so that [benefit]
[3-5 stories]

Acceptance Criteria:
- [criterion 1]
- [criterion 2]

Open Questions:
- [question 1]
- [question 2]
        """,
        
        "User Research Summary": """
Summarize these user interview notes:

[Notes pasted here]

Provide:
1. Key Insights (5-7 bullets)
2. Pain Points (ranked by frequency)
3. Desired Outcomes
4. Surprising Findings
5. Recommended Actions
6. Quotes to Share (3-5 verbatim)
        """
    },
    
    "Operations": {
        "SOP Creation": """
Create a Standard Operating Procedure for [task].

Purpose: [why this SOP exists]
Scope: [who does this / when]

Prerequisites:
- [what's needed before starting]

Procedure:
Step 1: [action]
  - Details: [specific instructions]
  - Expected outcome: [what success looks like]
  - Time estimate: [duration]

[Continue steps...]

Quality Check:
- [how to verify it was done correctly]

Troubleshooting:
Problem: [common issue]
Solution: [how to fix]

Tools/Resources:
- [tools needed]
- [reference materials]
        """
    }
}


# ============== Main ==============

async def main():
    """Demonstrate prompt engineering expertise."""
    print("=" * 70)
    print("PROMPT ENGINEERING MASTERY")
    print("=" * 70)
    
    print("\n1. CORE PRINCIPLES")
    print("-" * 40)
    print("   Formula: Clear Instructions + Context + Examples + Constraints")
    print("   5 Principles: Clarity, Context, Constraints, Examples, Iteration")
    print("   Perfect prompt anatomy: Role + Context + Task + Format + Constraints")
    
    print("\n2. ADVANCED TECHNIQUES")
    print("-" * 40)
    for technique, info in ADVANCED_TECHNIQUES.items():
        print(f"\n   {technique}:")
        print(f"     When: {info['when_to_use']}")
        print(f"     Benefits: {', '.join(info['benefits'][:2])}")
    
    print("\n3. SYSTEM PROMPTS")
    print("-" * 40)
    print("   Elements:")
    elements = ["Identity & Role", "Knowledge Boundaries", "Behavior & Tone", 
                "Output Format", "Constraints & Rules"]
    for element in elements:
        print(f"     • {element}")
    
    print("\n4. OPTIMIZATION")
    print("-" * 40)
    print("   Process: Baseline → Evaluate → Refine → Test → Document")
    print("   Common fixes for: length, format, tone, hallucinations")
    print("   A/B testing framework")
    
    print("\n5. DOMAIN-SPECIFIC PROMPTS")
    print("-" * 40)
    for domain in DOMAIN_PROMPTS.keys():
        print(f"   • {domain}")
        for template in DOMAIN_PROMPTS[domain].keys():
            print(f"     - {template}")
    
    print("\n" + "=" * 70)
    print("PROMPT ENGINEERING MASTERY COMPLETE")
    print("=" * 70)
    print("\nCapabilities:")
    print("  ✅ Write clear, effective prompts")
    print("  ✅ Apply advanced techniques (CoT, Few-shot, etc.)")
    print("  ✅ Create powerful system prompts")
    print("  ✅ Optimize prompts iteratively")
    print("  ✅ Use multi-modal prompting")
    print("  ✅ Build domain-specific prompt libraries")
    print("  ✅ Debug and fix prompt issues")
    print("\nReady to get the best possible output from any AI system!")


if __name__ == "__main__":
    asyncio.run(main())
