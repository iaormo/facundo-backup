<?php
/**
 * FREE COURSE: Transition to Freelancing & Remote Work
 * A complete course outline for people leaving traditional jobs
 */

class FreelancingTransitionCourse {
    
    /**
     * COURSE OVERVIEW
     */
    public function getCourseOverview() {
        return [
            'title' => 'Zero to Remote: Your Freelancing Transition Blueprint',
            'subtitle' => 'Go from employee to earning your first $500/month online',
            'duration' => '4 weeks (self-paced)',
            'format' => 'Video lessons + Worksheets + Community',
            'target_audience' => 'Employees ready to leave 9-5, beginners with no freelancing experience',
            'outcome' => 'Clear roadmap, first client strategy, and action plan',
            'price' => 'FREE (lead magnet for VA coaching program)',
        ];
    }
    
    /**
     * MODULE 1: Mindset Shift (Days 1-3)
     */
    public function module1_MindsetShift() {
        return [
            'module_number' => 1,
            'title' => 'The Freelancer Mindset',
            'duration' => '3 days',
            'objective' => 'Shift from employee thinking to business owner thinking',
            
            'lessons' => [
                [
                    'lesson' => 1.1,
                    'title' => 'Employee vs Freelancer: What Changes',
                    'video_length' => '15 min',
                    'content' => [
                        'The security myth: Jobs are not safer than clients',
                        'Income ceiling: Salary cap vs unlimited earning potential',
                        'Time ownership: Trading time for money vs trading results',
                        'Benefits reality: You can earn enough to buy your own benefits',
                        'Case study: Maria left her ₱25k office job, now earns ₱80k remotely',
                    ],
                    'worksheet' => 'Mindset Assessment: Where are you stuck?',
                    'action_item' => 'List 3 fears about leaving your job. Write a counter-argument for each.',
                ],
                [
                    'lesson' => 1.2,
                    'title' => 'The Safety Net Strategy',
                    'video_length' => '20 min',
                    'content' => [
                        'Calculate your minimum monthly survival number',
                        'The 3-month savings rule (and how to build it while employed)',
                        'Side-hustle timeline: Start while you are still employed',
                        'Exit strategy: When to quit vs when to stay longer',
                        'The "client first, resignation second" approach',
                    ],
                    'worksheet' => 'Financial Runway Calculator',
                    'action_item' => 'Calculate your exact survival number and months of savings needed.',
                ],
                [
                    'lesson' => 1.3,
                    'Building Your Confidence',
                    'video_length' => '18 min',
                    'content' => [
                        'Imposter syndrome: Everyone feels it (even experts)',
                        'The "good enough" standard: Done beats perfect',
                        'Building evidence: Small wins create confidence',
                        'Your unfair advantage: What you already know',
                        'Reframing: "I am learning" vs "I am not qualified"',
                    ],
                    'worksheet' => 'Confidence Inventory: What do you already know?',
                    'action_item' => 'List 10 skills you have (from any area of life).',
                ],
            ],
            
            'module_deliverable' => 'Personal transition timeline with financial safety net plan',
        ];
    }
    
    /**
     * MODULE 2: Discover Your Marketable Skill (Days 4-7)
     */
    public function module2_DiscoverSkill() {
        return [
            'module_number' => 2,
            'title' => 'Find Your Marketable Skill',
            'duration' => '4 days',
            'objective' => 'Identify what you can sell starting this week',
            
            'lessons' => [
                [
                    'lesson' => 2.1,
                    'title' => 'Skill Audit: What You Already Have',
                    'video_length' => '22 min',
                    'content' => [
                        'Transferable skills from any job (even unrelated)',
                        'Hidden skills: What do friends ask you for help with?',
                        'The 3 skill categories: Admin, Creative, Technical',
                        'Beginner-friendly skills that pay well:',
                        '  • Data entry, email management, customer support',
                        '  • Social media management, content writing',
                        '  • Basic design (Canva), research, scheduling',
                    ],
                    'worksheet' => 'Complete Skills Inventory',
                    'action_item' => 'List 20 things you know how to do (work + personal).',
                ],
                [
                    'lesson' => 2.2,
                    'title' => 'What Pays: Matching Skills to Demand',
                    'video_length' => '25 min',
                    'content' => [
                        'Research method: OnlineJobs.ph job categories',
                        'High-demand, low-barrier skills for beginners',
                        'Philippine market rates by skill (PHP per hour)',
                        'Niche selection: Generalist vs Specialist',
                        'Rule: Start with ONE skill, add later',
                    ],
                    'worksheet' => 'Skill-Market Match Matrix',
                    'action_item' => 'Check OnlineJobs.ph for 5 jobs matching your top 3 skills.',
                ],
                [
                    'lesson' => 2.3,
                    'title' => 'Fast-Track Learning (If You Need a New Skill)',
                    'video_length' => '20 min',
                    'content' => [
                        'You do not need 6 months to learn a skill',
                        'The 80/20 rule: 20% of skills get 80% of results',
                        'Free resources: YouTube, Coursera, Google certifications',
                        'Learn by doing: Take a free client first',
                        'Build portfolio while learning (document your practice)',
                    ],
                    'worksheet' => '30-Day Skill Sprint Plan',
                    'action_item' => 'Pick ONE skill to focus on. Find 3 free learning resources.',
                ],
                [
                    'lesson' => 2.4,
                    'title' => 'Define Your Offer',
                    'video_length' => '18 min',
                    'content' => [
                        'Offer formula: [Result] for [Target Client]',
                        'Examples that work:',
                        '  • "I manage overflowing inboxes for busy coaches"',
                        '  • "I create social media content for local businesses"',
                        '  • "I handle customer support for ecommerce stores"',
                        'What NOT to say: "I am a virtual assistant" (too vague)',
                        'Your unique angle: Personal story + specific skill',
                    ],
                    'worksheet' => 'Offer Statement Builder',
                    'action_item' => 'Write your offer statement in the formula format.',
                ],
            ],
            
            'module_deliverable' => 'Clear offer statement: "I help [WHO] with [WHAT result]"',
        ];
    }
    
    /**
     * MODULE 3: Build Your Presence (Days 8-12)
     */
    public function module3_BuildPresence() {
        return [
            'module_number' => 3,
            'title' => 'Build Your Online Presence',
            'duration' => '5 days',
            'objective' => 'Create profiles that attract clients',
            
            'lessons' => [
                [
                    'lesson' => 3.1,
                    'title' => 'OnlineJobs.ph Profile That Gets Hired',
                    'video_length' => '30 min',
                    'content' => [
                        'Profile headline: Lead with your offer (not "seeking opportunity")',
                        'First 2 sentences: Hook them immediately',
                        'Bad: "I am a hardworking VA with 5 years experience"',
                        'Good: "I help real estate agents save 10 hours/week by managing their inboxes and schedules"',
                        'Skills section: Specific tools, not soft skills',
                        'Portfolio: Create sample work if you have no clients',
                        'ID verification: Do this immediately',
                    ],
                    'worksheet' => 'Profile Optimization Checklist',
                    'action_item' => 'Create or rewrite your OnlineJobs.ph profile using the template.',
                ],
                [
                    'lesson' => 3.2,
                    'title' => 'LinkedIn for Freelancers',
                    'video_length' => '25 min',
                    'content' => [
                        'Headline formula: [What you do] + [Who you help] + [Result]',
                        'About section: Problem you solve + Who you serve + Call to action',
                        'Experience section: Frame past jobs by skills, not titles',
                        'Featured section: Portfolio pieces, testimonials, posts',
                        'Banner image: Simple Canva design stating your offer',
                    ],
                    'worksheet' => 'LinkedIn Profile Template',
                    'action_item' => 'Update LinkedIn profile following the formula.',
                ],
                [
                    'lesson' => 3.3,
                    'title' => 'Portfolio Without Experience',
                    'video_length' => '28 min',
                    'content' => [
                        'The "spec work" method: Create for imaginary clients',
                        'Sample project ideas by skill:',
                        '  • Email: Before/after inbox cleanup screenshots',
                        '  • Social media: 7-day content calendar for a brand',
                        '  • Design: Mock social posts, email headers',
                        '  • Writing: Blog post, email sequence',
                        '  • Admin: Sample spreadsheet, SOP document',
                        'Format: Google Drive folder or simple PDF',
                        'Label clearly: "Sample work for portfolio"',
                    ],
                    'worksheet' => 'Portfolio Project Planner',
                    'action_item' => 'Create 2-3 sample portfolio pieces for your chosen skill.',
                ],
                [
                    'lesson' => 3.4,
                    'title' => 'Your Simple Website (Optional but Powerful)',
                    'video_length' => '22 min',
                    'content' => [
                        'Free options: Carrd.co, Google Sites, Notion',
                        'One-page structure:',
                        '  • Headline: What you do',
                        '  • Problem: Pain point you solve',
                        '  • Solution: How you help',
                        '  • Proof: Portfolio/testimonials',
                        '  • Call to action: How to contact you',
                        'Keep it simple: You do not need a fancy site',
                    ],
                    'worksheet' => 'One-Page Website Template',
                    'action_item' => 'Create a simple Carrd site (or skip and focus on profiles first).',
                ],
                [
                    'lesson' => 3.5,
                    'title' => 'Payment and Logistics Setup',
                    'video_length' => '20 min',
                    'content' => [
                        'PayPal: Create and verify account (for international clients)',
                        'Wise: Lower fees, multi-currency account',
                        'Local options: GCash, Maya for Philippine clients',
                        'Invoicing: Simple templates or free tools (Wave, Invoice.to)',
                        'Contracts: Simple agreement templates (protects both sides)',
                        'Time tracking: Toggl, Clockify (free)',
                    ],
                    'worksheet' => 'Business Setup Checklist',
                    'action_item' => 'Set up PayPal and one backup payment method.',
                ],
            ],
            
            'module_deliverable' => 'Complete OnlineJobs.ph profile + LinkedIn + portfolio ready',
        ];
    }
    
    /**
     * MODULE 4: Get Your First Client (Days 13-21)
     */
    public function module4_GetFirstClient() {
        return [
            'module_number' => 4,
            'title' => 'Land Your First Client',
            'duration' => '9 days',
            'objective' => 'Send applications and get hired',
            
            'lessons' => [
                [
                    'lesson' => 4.1,
                    'title' => 'Where to Find Clients',
                    'video_length' => '20 min',
                    'content' => [
                        'OnlineJobs.ph: Best for Filipinos, no platform fees',
                        'Upwork: More competition, but global reach',
                        'Facebook Groups: "Virtual Assistant Philippines", niche groups',
                        'LinkedIn: Direct outreach to business owners',
                        'Referrals: Tell everyone what you are doing',
                        'Strategy: Start with OnlineJobs.ph + LinkedIn',
                    ],
                    'worksheet' => 'Platform Comparison Sheet',
                    'action_item' => 'Create accounts on OnlineJobs.ph and optimize LinkedIn.',
                ],
                [
                    'lesson' => 4.2,
                    'title' => 'Application That Gets Responses',
                    'video_length' => '25 min',
                    'content' => [
                        'The 3-part formula: Hook + Proof + Ask',
                        'Hook: Show you read their job post (be specific)',
                        'Proof: One sentence showing you can do this',
                        'Ask: Clear next step (call, email, trial task)',
                        'Template example:',
                        '  "Hi [Name], I saw you need help managing customer emails for your skincare brand. I currently handle support for an ecommerce store and maintain a 4-hour response time. Would you be open to a 10-minute call this week?"',
                        'Length: 3-5 sentences maximum',
                    ],
                    'worksheet' => 'Application Template Library',
                    'action_item' => 'Write 3 application templates for different job types.',
                ],
                [
                    'lesson' => 4.3,
                    'title' => 'The Numbers Game',
                    'video_length' => '18 min',
                    'content' => [
                        'Reality check: You will hear "no" often (that is normal)',
                        'Target numbers: 10 applications = 2 responses = 1 call = maybe 1 client',
                        'Daily quota: 5 applications minimum while building',
                        'Track everything: Spreadsheet of applications sent',
                        'Follow up: One polite follow-up after 3 days',
                        'Do not get attached to any single opportunity',
                    ],
                    'worksheet' => 'Application Tracker',
                    'action_item' => 'Set up tracking spreadsheet. Commit to 5 applications/day.',
                ],
                [
                    'lesson' => 4.4,
                    'title' => 'LinkedIn Outreach Strategy',
                    'video_length' => '25 min',
                    'content' => [
                        'Find prospects: Search your target client type',
                        'Connection request: Mention common ground or value',
                        'The 3-message sequence:',
                        '  1. Connection request (no pitch)',
                        '  2. Value message 2 days later (article, insight)',
                        '  3. Soft pitch day 5 (asking about their needs)',
                        'Never spam: Genuine conversations first',
                        'Volume: 5 connections/day minimum',
                    ],
                    'worksheet' => 'LinkedIn Message Templates',
                    'action_item' => 'Send 5 connection requests today using the template.',
                ],
                [
                    'lesson' => 4.5,
                    'title' => 'The Discovery Call',
                    'video_length' => '30 min',
                        'content' => [
                        'Purpose: Understand their needs, not just pitch',
                        'Questions to ask:',
                        '  • "What is your biggest challenge with [task] right now?"',
                        '  • "How is this affecting your business?"',
                        '  • "What would it mean to have this solved?"',
                        '  • "What does success look like for you?"',
                        'Listen more than you talk (70/30 rule)',
                        'End with: "Based on what you shared, here is how I can help..."',
                    ],
                    'worksheet' => 'Discovery Call Script',
                    'action_item' => 'Practice the script with a friend or family member.',
                ],
                [
                    'lesson' => 4.6,
                    'title' => 'Pricing Your First Project',
                    'video_length' => '22 min',
                    'content' => [
                        'First client strategy: Price to get the win, not maximum profit',
                        'Options: Hourly vs Project vs Retainer',
                        'Beginner rates (Philippine market):',
                        '  • Hourly: ₱75-150/hr depending on skill',
                        '  • Packages: ₱4,000-8,000 for 20-40 hours/month',
                        'How to quote: Give a range first, then specifics',
                        'The "introductory rate" framing',
                        'When to negotiate: Always have a walk-away number',
                    ],
                    'worksheet' => 'Pricing Calculator',
                    'action_item' => 'Set your 3 price points: dream rate, acceptable rate, walk-away rate.',
                ],
                [
                    'lesson' => 4.7,
                    'title' => 'Closing the Deal',
                    'video_length' => '20 min',
                    'content' => [
                        'The assumptive close: "When would you like to start?"',
                        'Handle objections:',
                        '  • "I need to think about it" → "What specifically would help you decide?"',
                        '  • "You are too expensive" → "What budget did you have in mind?"',
                        '  • "I have never hired a VA before" → "Let us start with a trial week"',
                        'Trial projects: Lower risk for both sides',
                        'Next steps: Send proposal within 24 hours',
                        'Follow up: 2 days after proposal if no response',
                    ],
                    'worksheet' => 'Objection Response Guide',
                    'action_item' => 'Write your response to the top 3 objections you expect.',
                ],
                [
                    'lesson' => 4.8,
                    'title' => 'Your First Week with a Client',
                    'video_length' => '25 min',
                    'content' => [
                        'Onboarding checklist:',
                        '  • Get all login credentials securely',
                        '  • Understand their tools and systems',
                        '  • Clarify communication preferences',
                        '  • Set expectations for response times',
                        'Over-deliver rule: Always submit early',
                        'Daily updates: What you did, what you need, what is next',
                        'Ask for feedback: "How am I doing? Anything to adjust?"',
                        'Document everything: Build your SOPs as you work',
                    ],
                    'worksheet' => 'Client Onboarding Checklist',
                    'action_item' => 'Create your onboarding process template.',
                ],
                [
                    'lesson' => 4.9,
                    'title' => 'Getting Testimonials',
                    'video_length' => '15 min',
                    'content' => [
                        'When to ask: After 2-3 weeks of good work',
                        'How to ask: "Would you mind sharing a brief testimonial? It helps other business owners find me"',
                        'Make it easy: Give them a template',
                        'Template: "Working with [Name] helped me [specific result]. I especially appreciated [specific thing]. I recommend them to any [target client] who needs [skill]."',
                        'Also ask for: LinkedIn recommendation, referral to others',
                    ],
                    'worksheet' => 'Testimonial Request Template',
                    'action_item' => 'Draft your testimonial request (use after you get a client).',
                ],
            ],
            
            'module_deliverable' => 'First client landed or 50+ applications sent',
        ];
    }
    
    /**
     * MODULE 5: Scale & Sustain (Days 22-28)
     */
    public function module5_ScaleAndSustain() {
        return [
            'module_number' => 5,
            'title' => 'Scale and Build Your Freelance Business',
            'duration' => '7 days',
            'objective' => 'Grow from first client to sustainable income',
            
            'lessons' => [
                [
                    'lesson' => 5.1,
                    'title' => 'Managing Your Money',
                    'video_length' => '25 min',
                    'content' => [
                        'The 50/30/20 rule for freelancers:',
                        '  • 50% personal income',
                        '  • 30% business expenses, tools, learning',
                        '  • 20% taxes and savings buffer',
                        'Track everything: Income, expenses, invoices',
                        'Tools: Google Sheets, Wave (free accounting)',
                        'Set aside tax money monthly (do not wait until April)',
                        'Build 3-month emergency fund as soon as possible',
                    ],
                    'worksheet' => 'Freelancer Budget Template',
                    'action_item' => 'Set up simple tracking system for income and expenses.',
                ],
                [
                    'lesson' => 5.2,
                    'title' => 'Raising Your Rates',
                    'video_length' => '22 min',
                    'content' => [
                        'When to raise: Every 3 months OR after 3 new clients',
                        'How much: 25-50% increase each time',
                        'New clients first: Test higher rates with prospects',
                        'Existing clients: Give 30-day notice',
                        'Script: "I have updated my rates to reflect my experience. Your new rate starting [date] is ₱[new rate]. I appreciate your continued partnership."',
                        'Expect some churn: Not everyone will accept increases',
                    ],
                    'worksheet' => 'Rate Increase Timeline',
                    'action_item' => 'Plan your first rate increase (date and new rate).',
                ],
                [
                    'lesson' => 5.3,
                    'title' => 'Adding More Clients',
                    'video_length' => '20 min',
                    'content' => [
                        'Capacity planning: How many hours can you work?',
                        'Ideal client mix: 2-4 regular clients (not one giant client)',
                        'Avoid: Depending on single client for 50%+ income',
                        'Pipeline: Always be applying (even when fully booked)',
                        'Referral engine: Ask happy clients for introductions',
                    ],
                    'worksheet' => 'Client Capacity Planner',
                    'action_item' => 'Calculate your available hours and ideal client load.',
                ],
                [
                    'lesson' => 5.4,
                    'title' => 'Expanding Your Skills',
                    'video_length' => '20 min',
                    'content' => [
                        'When to add skills: After mastering your first one',
                        'Natural progressions:',
                        '  • Email → Project management',
                        '  • Social media → Marketing strategy',
                        '  • Data entry → Data analysis',
                        '  • Customer support → Customer success',
                        'Stack your skills: Combined skills = higher rates',
                        'Learning while earning: Apply new skills to current clients',
                    ],
                    'worksheet' => 'Skill Expansion Roadmap',
                    'action_item' => 'Identify 2 related skills to learn in the next 6 months.',
                ],
                [
                    'lesson' => 5.5,
                    'title' => 'Productivity and Time Management',
                    'video_length' => '25 min',
                    'content' => [
                        'Structure your day: Core work hours + client hours',
                        'Time blocking: Dedicated blocks for specific clients/tasks',
                        'The 2-minute rule: If it takes 2 minutes, do it now',
                        'Batch similar tasks: All emails at once, all social posts at once',
                        'Tools: Calendar blocking, Toggl for tracking, Notion for organization',
                        'Protect your energy: Most important work when you are freshest',
                    ],
                    'worksheet' => 'Daily Schedule Template',
                    'action_item' => 'Create your ideal daily schedule with time blocks.',
                ],
                [
                    'lesson' => 5.6,
                    'title' => 'Avoiding Burnout',
                    'video_length' => '18 min',
                    'content' => [
                        'Freelancer trap: Saying yes to everything',
                        'Boundaries: Set clear working hours and stick to them',
                        'The "no" script: "I am at capacity right now, but I can refer you to someone"',
                        'Rest days: Schedule them like client work',
                        'Watch for signs: Exhaustion, dreading work, making mistakes',
                        'Long-term thinking: This is a marathon, not a sprint',
                    ],
                    'worksheet' => 'Boundary Setting Worksheet',
                    'action_item' => 'Define your non-negotiable working hours and break times.',
                ],
                [
                    'lesson' => 5.7,
                    'title' => 'Your 90-Day Action Plan',
                    'video_length' => '30 min',
                    'content' => [
                        'Month 1: Foundation',
                        '  • Complete this course',
                        '  • Build profiles and portfolio',
                        '  • Send 100+ applications',
                        '  • Goal: 1 client or 5 serious conversations',
                        'Month 2: Delivery',
                        '  • Over-deliver for first clients',
                        '  • Get testimonials',
                        '  • Document your processes',
                        '  • Goal: 2-3 regular clients',
                        'Month 3: Growth',
                        '  • Raise your rates',
                        '  • Add one new skill',
                        '  • Build referral system',
                        '  • Goal: ₱20,000-40,000/month income',
                    ],
                    'worksheet' => '90-Day Action Plan Template',
                    'action_item' => 'Fill out your personal 90-day plan with specific dates.',
                ],
            ],
            
            'module_deliverable' => 'Complete 90-day action plan for sustainable freelancing',
        ];
    }
    
    /**
     * BONUS RESOURCES
     */
    public function getBonusResources() {
        return [
            'Templates' => [
                'Client proposal template',
                'Invoice template',
                'Simple contract template',
                'Email response templates',
                'Discovery call script',
                'Testimonial request template',
                'Rate increase letter',
            ],
            'Checklists' => [
                'Profile setup checklist',
                'Client onboarding checklist',
                'Daily task checklist',
                'Weekly review checklist',
                'Monthly financial review',
            ],
            'Tools List' => [
                'Free tools for time tracking',
                'Free design tools (Canva)',
                'Free invoicing tools',
                'Free project management tools',
                'Communication tools',
                'Password managers',
            ],
            'Community Access' => [
                'Private Facebook group for course students',
                'Weekly Q&A calls (recorded)',
                'Peer accountability partnerships',
                'Job leads sharing',
            ],
        ];
    }
    
    /**
     * COURSE UPSELL PATH
     */
    public function getUpsellPath() {
        return [
            'Free Course' => [
                'purpose' => 'Lead generation and trust building',
                'outcome' => 'First client or clear roadmap',
            ],
            'Paid VA Coaching' => [
                'price' => '₱2,997-4,997',
                'includes' => [
                    '8-week intensive program',
                    'Weekly group coaching calls',
                    '1-on-1 strategy session',
                    'Done-with-you profile optimization',
                    'Template library',
                    'Job application reviews',
                    'Private community access',
                    'Certificate of completion',
                ],
                'target' => 'Students who complete free course and want accountability + faster results',
            ],
            'Mastermind / Advanced' => [
                'price' => '₱9,997+',
                'includes' => [
                    'Small group (max 10)',
                    'Bi-weekly calls',
                    'Hot seat coaching',
                    'Client referral network',
                    'Advanced strategies',
                ],
                'target' => 'VAs already earning who want to scale to ₱50k+/month',
            ],
        ];
    }
    
    /**
     * Print full course outline
     */
    public function printCourse() {
        $overview = $this->getCourseOverview();
        
        echo "=== {$overview['title']} ===\n";
        echo "{$overview['subtitle']}\n";
        echo "Duration: {$overview['duration']} | Format: {$overview['format']}\n";
        echo "Price: {$overview['price']}\n";
        echo "Outcome: {$overview['outcome']}\n\n";
        
        $modules = [
            $this->module1_MindsetShift(),
            $this->module2_DiscoverSkill(),
            $this->module3_BuildPresence(),
            $this->module4_GetFirstClient(),
            $this->module5_ScaleAndSustain(),
        ];
        
        foreach ($modules as $module) {
            echo str_repeat("=", 60) . "\n";
            echo "MODULE {$module['module_number']}: {$module['title']}\n";
            echo "Duration: {$module['duration']} | Objective: {$module['objective']}\n";
            echo str_repeat("=", 60) . "\n\n";
            
            foreach ($module['lessons'] as $lesson) {
                echo "Lesson {$lesson['lesson']}: {$lesson['title']}\n";
                echo "Video: {$lesson['video_length']} | Worksheet: {$lesson['worksheet']}\n\n";
                
                foreach ($lesson['content'] as $point) {
                    echo "  • $point\n";
                }
                
                echo "\n  ACTION: {$lesson['action_item']}\n\n";
                echo str_repeat("-", 40) . "\n\n";
            }
            
            echo "MODULE DELIVERABLE: {$module['module_deliverable']}\n\n\n";
        }
        
        echo str_repeat("=", 60) . "\n";
        echo "BONUS RESOURCES\n";
        echo str_repeat("=", 60) . "\n\n";
        
        $bonuses = $this->getBonusResources();
        foreach ($bonuses as $category => $items) {
            echo "$category:\n";
            foreach ($items as $item) {
                echo "  • $item\n";
            }
            echo "\n";
        }
        
        echo str_repeat("=", 60) . "\n";
        echo "UPSELL PATH (Revenue Model)\n";
        echo str_repeat("=", 60) . "\n\n";
        
        $upsell = $this->getUpsellPath();
        foreach ($upsell as $tier => $details) {
            echo "$tier:\n";
            if (isset($details['price'])) {
                echo "  Price: {$details['price']}\n";
            }
            if (isset($details['purpose'])) {
                echo "  Purpose: {$details['purpose']}\n";
            }
            if (isset($details['outcome'])) {
                echo "  Outcome: {$details['outcome']}\n";
            }
            if (isset($details['includes'])) {
                echo "  Includes:\n";
                foreach ($details['includes'] as $item) {
                    echo "    • $item\n";
                }
            }
            if (isset($details['target'])) {
                echo "  Target: {$details['target']}\n";
            }
            echo "\n";
        }
    }
}

// ============================================
// OUTPUT THE COURSE
// ============================================

$course = new FreelancingTransitionCourse();
$course->printCourse();

echo "\n\n=== QUICK SUMMARY ===\n\n";
echo "5 MODULES, 28 LESSONS\n";
echo "Module 1: Mindset Shift (3 days)\n";
echo "Module 2: Discover Your Skill (4 days)\n";
echo "Module 3: Build Presence (5 days)\n";
echo "Module 4: Get First Client (9 days)\n";
echo "Module 5: Scale & Sustain (7 days)\n\n";

echo "DELIVERABLES BY MODULE:\n";
echo "1. Personal transition timeline with savings plan\n";
echo "2. Clear offer statement: I help [WHO] with [WHAT]\n";
echo "3. Complete profiles + portfolio ready\n";
echo "4. First client landed (or 50+ applications sent)\n";
echo "5. 90-day action plan for sustainable income\n\n";

echo "UPSALE PATH:\n";
echo "Free Course → Paid Coaching (₱2,997-4,997) → Mastermind (₱9,997+)\n";

?>
