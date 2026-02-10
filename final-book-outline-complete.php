<?php
/**
 * FINAL BOOK OUTLINE: "The 1% Freelancer"
 * Complete with word counts, page counts, and redemption story integrated
 */

class FinalBookOutline {
    
    /**
     * BOOK METADATA
     */
    public function bookMetadata() {
        return [
            'title' => 'The 1% Freelancer',
            'subtitle' => 'Transitioning to Freedom 1 Day at a Time',
            'total_chapters' => 28,
            'target_word_count' => '65,000-75,000 words',
            'estimated_pages' => '260-300 pages',
            'words_per_page' => '250 words',
            'format' => 'Paperback 6" x 9"',
        ];
    }
    
    /**
     * CALCULATION METHOD
     */
    public function calculatePages($wordCount) {
        $pages = ceil($wordCount / 250);
        return $pages;
    }
    
    /**
     * COMPLETE CHAPTER OUTLINE WITH WORDS & PAGES
     */
    public function chapterOutline() {
        return [
            // PART 1: THE FALL AND RISE
            [
                'part' => 'PART 1: THE FALL AND RISE',
                'part_pages' => '60-70 pages',
                'chapters' => [
                    [
                        'chapter' => 1,
                        'title' => 'The Bottom',
                        'subtitle' => 'When everything falls apart',
                        'word_count' => '2,800',
                        'pages' => '11',
                        'content_summary' => 'Your story: 18 years old, dropout, call center, leadership same year. The 10-year climb from agent to Operations Manager leading thousands. The vices that kept you going: smoking, drinking, alcohol dependence. Partying hard to cope with 16-hour workdays. The stress and emptiness of "success."',
                        'key_moments' => [
                            '18 years old, no degree, started at call center',
                            'Same year: became team leader while friends in college',
                            '10 years to Operations Manager leading thousands',
                            'The hidden cost: alcohol dependence, smoking, partying',
                            'Work hard, drink harder mentality',
                            '2017: The termination. No warning. Everything collapses.',
                        ],
                    ],
                    [
                        'chapter' => 2,
                        'title' => 'Starting From Scratch',
                        'subtitle' => 'No credentials, no safety net, just desperation',
                        'word_count' => '2,600',
                        'pages' => '10',
                        'content_summary' => 'The 2 AM panic. No degree, no network, no options. Family to feed. Rebuilding from rock bottom. The decision to change everything. First steps into the unknown.',
                        'key_moments' => [
                            'No credentials, no connections, no backup plan',
                            'The desperation that drives real action',
                            'Humbling yourself to take any work',
                            'First client story: How you got it',
                            'The fear and uncertainty of starting over',
                        ],
                    ],
                    [
                        'chapter' => 3,
                        'title' => 'The Transformation',
                        'subtitle' => 'From vices to victory',
                        'word_count' => '2,800',
                        'pages' => '11',
                        'content_summary' => 'The unexpected side effect of transitioning: You stopped smoking. Stopped drinking. The stress that required alcohol disappeared. Finding purpose beyond survival. Becoming active in ministry. How work that matters heals what work that drains destroys.',
                        'key_moments' => [
                            'Corporate stress required vices to cope',
                            'Freelancing removed the stress that drove drinking',
                            'Natural healing: No longer needed to numb yourself',
                            'Finding purpose and meaning in your work',
                            'Becoming active in ministry: Serving others',
                            'The whole-life transformation, not just career',
                        ],
                        'faith_element' => 'Light mention of finding purpose and serving others',
                    ],
                    [
                        'chapter' => 4,
                        'title' => 'Doing Everything',
                        'subtitle' => 'The hustle phase that built the foundation',
                        'word_count' => '2,600',
                        'pages' => '10',
                        'content_summary' => 'First year: Virtual assistant, executive assistant, real estate support, graphics, video, copywriting, social media. Learning on the job. Making mistakes. Getting better. The portfolio of desperation that became expertise.',
                        'key_moments' => [
                            'VA work: Inbox management, scheduling',
                            'Executive assistant: Supporting business owners',
                            'Real estate: Listings, client communication',
                            'Creative: Graphics, video editing',
                            'Writing: Copywriting, social media content',
                            'Why doing everything first was the right move',
                        ],
                    ],
                    [
                        'chapter' => 5,
                        'title' => 'The 1% Rule',
                        'subtitle' => 'How small daily actions saved my life',
                        'word_count' => '2,400',
                        'pages' => '10',
                        'content_summary' => 'The philosophy that got you through. When everything is overwhelming, just do 1% better today. Compound effect in real life. Consistency beats intensity. Your turning point moment.',
                        'key_moments' => [
                            'The 1% philosophy explained',
                            'Compound effect: Small actions, big results',
                            'Why consistency beats intensity',
                            'Real examples from your journey',
                            'How to apply this when you are desperate',
                        ],
                    ],
                ],
            ],
            
            // PART 2: THE MINDSET
            [
                'part' => 'PART 2: THE MINDSET',
                'part_pages' => '48-52 pages',
                'chapters' => [
                    [
                        'chapter' => 6,
                        'title' => 'The Fear is Real',
                        'subtitle' => 'And that is okay',
                        'word_count' => '2,400',
                        'pages' => '10',
                        'content_summary' => 'Fear of instability vs reality of corporate "security." What if I fail vs what if I never try. Imposter syndrome without credentials. How to act scared.',
                        'key_points' => [
                            'Fear is normal and expected',
                            'Corporate "security" is an illusion',
                            'Acting despite fear (not waiting for confidence)',
                            'Your fear story: Applying while terrified',
                        ],
                    ],
                    [
                        'chapter' => 7,
                        'title' => 'No Credentials, No Problem',
                        'subtitle' => 'You do not need a degree to get paid',
                        'word_count' => '2,600',
                        'pages' => '10',
                        'content_summary' => 'You are the proof. High school dropout who led thousands. Skills matter more than diplomas. Portfolio beats resume every time. Confidence without credentials.',
                        'key_points' => [
                            'Your story: Dropout to Operations Manager',
                            'What actually matters: Results, not degrees',
                            'Building proof through work samples',
                            'How to present yourself without credentials',
                        ],
                    ],
                    [
                        'chapter' => 8,
                        'title' => 'The Hustle Phase',
                        'subtitle' => 'Why doing everything first is the right move',
                        'word_count' => '2,400',
                        'pages' => '10',
                        'content_summary' => 'Saying yes before you are ready. Learning fast through YouTube, practice, delivery. The generalist advantage when starting. When to specialize (not day one).',
                        'key_points' => [
                            'The value of being a generalist at first',
                            'Learning on the job (and getting paid for it)',
                            'How to learn fast: Resources and methods',
                            'When and how to niche down later',
                        ],
                    ],
                    [
                        'chapter' => 9,
                        'title' => 'From Surviving to Thriving',
                        'subtitle' => 'The mindset shift that changes everything',
                        'word_count' => '2,200',
                        'pages' => '9',
                        'content_summary' => 'Moving from desperation to choice. Building instead of scrambling. Long-term thinking when you are used to monthly panic. Creating stability in instability.',
                        'key_points' => [
                            'Survival mode vs growth mode',
                            'Building systems that create stability',
                            'Long-term thinking as a freelancer',
                            'From reactive to proactive',
                        ],
                    ],
                ],
            ],
            
            // PART 3: THE PREPARATION
            [
                'part' => 'PART 3: THE PREPARATION',
                'part_pages' => '60-65 pages',
                'chapters' => [
                    [
                        'chapter' => 10,
                        'title' => 'The Financial Reality Check',
                        'subtitle' => 'How much you really need',
                        'word_count' => '2,600',
                        'pages' => '10',
                        'content_summary' => 'Survival number calculation. 3-month minimum runway. Building savings while employed (or after termination like you did). Side income strategies.',
                        'key_points' => [
                            'Calculating bare minimum survival number',
                            '3-month vs 6-month runway',
                            'Building savings while working',
                            'Emergency strategies when you have no savings',
                        ],
                    ],
                    [
                        'chapter' => 11,
                        'title' => 'What Can You Actually Sell?',
                        'subtitle' => 'Skills audit and market reality',
                        'word_count' => '2,800',
                        'pages' => '11',
                        'content_summary' => 'Transferable skills from corporate life. High-demand skills you can learn in 30 days. The skills that actually pay. Your beginner skill stack.',
                        'key_points' => [
                            'Skills audit: What do you have right now?',
                            'Corporate skills that transfer to freelancing',
                            'Quick-learn skills that pay immediately',
                            'Building your starter skill stack',
                        ],
                    ],
                    [
                        'chapter' => 12,
                        'title' => 'Pick a Niche (Or Do Not)',
                        'subtitle' => 'The specialist vs generalist debate',
                        'word_count' => '2,400',
                        'pages' => '10',
                        'content_summary' => 'When to specialize. Why being a generalist first was right for you. Profitable niches for beginners. Your "do everything" phase was valid and valuable.',
                        'key_points' => [
                            'Specialist vs generalist: Pros and cons',
                            'Why generalist first worked for you',
                            'When to niche down (later, not now)',
                            'Profitable niches to consider',
                        ],
                    ],
                    [
                        'chapter' => 13,
                        'title' => 'Who Will Actually Pay You?',
                        'subtitle' => 'Finding your target clients',
                        'word_count' => '2,600',
                        'pages' => '10',
                        'content_summary' => 'Client avatar exercise. Where your clients hang out. Researching what they need. Building relationships before you need them.',
                        'key_points' => [
                            'Creating your ideal client profile',
                            'Where to find clients (platforms, groups)',
                            'Understanding client pain points',
                            'Relationship building before selling',
                        ],
                    ],
                    [
                        'chapter' => 14,
                        'title' => 'Build Before You Leap',
                        'subtitle' => 'Creating proof while you can',
                        'word_count' => '2,400',
                        'pages' => '10',
                        'content_summary' => 'Side hustle timeline. First client before quitting. Portfolio from scratch. Signs you are ready. What to do if you are already forced out (like you were).',
                        'key_points' => [
                            'Building while employed (ideal scenario)',
                            'Creating portfolio pieces without clients',
                            'Signs you are ready to make the jump',
                            'If you are already out: Emergency ramp-up plan',
                        ],
                    ],
                ],
            ],
            
            // PART 4: THE TOOLS & PLATFORMS
            [
                'part' => 'PART 4: THE TOOLS & PLATFORMS',
                'part_pages' => '48-52 pages',
                'chapters' => [
                    [
                        'chapter' => 15,
                        'title' => 'The Starter Toolkit',
                        'subtitle' => 'Free and cheap tools to run your business',
                        'word_count' => '2,400',
                        'pages' => '10',
                        'content_summary' => 'Communication, organization, time tracking, design, payments. What you actually need vs what marketers sell you.',
                        'key_tools' => [
                            'Gmail, Google Meet, Zoom',
                            'Notion, Trello, Google Calendar',
                            'Toggl, Clockify',
                            'Canva',
                            'PayPal, Wise, GCash',
                        ],
                    ],
                    [
                        'chapter' => 16,
                        'title' => 'Where to Actually Find Work',
                        'subtitle' => 'Platforms that work for Filipinos',
                        'word_count' => '2,600',
                        'pages' => '10',
                        'content_summary' => 'OnlineJobs.ph, Upwork, LinkedIn, Facebook Groups, warm outreach. Which to focus on first. Platform pros and cons.',
                        'key_platforms' => [
                            'OnlineJobs.ph: Best for Filipinos',
                            'Upwork: Global reach, high competition',
                            'LinkedIn: Direct outreach strategy',
                            'Facebook Groups: Community approach',
                            'Warm outreach: Using your network',
                        ],
                    ],
                    [
                        'chapter' => 17,
                        'title' => 'Profiles That Get Hired',
                        'subtitle' => 'Standing out in a sea of applicants',
                        'word_count' => '2,600',
                        'pages' => '10',
                        'content_summary' => 'OnlineJobs.ph optimization. LinkedIn for freelancers. Portfolio without experience. Getting early testimonials.',
                        'key_points' => [
                            'Profile optimization checklist',
                            'Headlines that hook',
                            'Creating portfolio from scratch',
                            'Testimonial strategies for beginners',
                        ],
                    ],
                    [
                        'chapter' => 18,
                        'title' => 'Getting Paid',
                        'subtitle' => 'Payments, invoices, and taxes',
                        'word_count' => '2,400',
                        'pages' => '10',
                        'content_summary' => 'Payment methods compared. Invoicing basics. Tax essentials for Philippine freelancers. Preparing for dry months.',
                        'key_points' => [
                            'Payment method pros and cons',
                            'Invoice templates and best practices',
                            'Tax basics (Philippines focus)',
                            'Setting aside for inconsistent income',
                        ],
                    ],
                ],
            ],
            
            // PART 5: GETTING CLIENTS
            [
                'part' => 'PART 5: GETTING CLIENTS',
                'part_pages' => '60-65 pages',
                'chapters' => [
                    [
                        'chapter' => 19,
                        'title' => 'The Numbers Game',
                        'subtitle' => 'Why volume beats perfection',
                        'word_count' => '2,400',
                        'pages' => '10',
                        'content_summary' => '10 applications a day rule. Rejection is normal (share your stats). Tracking your outreach. Following up without being annoying.',
                        'key_points' => [
                            'The volume approach: Why it works',
                            'Rejection statistics (yours and industry)',
                            'Tracking system for applications',
                            'Follow-up strategies that work',
                        ],
                    ],
                    [
                        'chapter' => 20,
                        'title' => 'Applications That Work',
                        'subtitle' => 'Writing proposals that get responses',
                        'word_count' => '2,800',
                        'pages' => '11',
                        'content_summary' => 'The hook + proof + ask formula. Customizing fast. What to include and skip. Templates that worked for you. Real examples.',
                        'key_points' => [
                            'The 3-part formula explained',
                            'Customization at scale',
                            'Common mistakes to avoid',
                            'Templates with real examples',
                        ],
                    ],
                    [
                        'chapter' => 21,
                        'title' => 'Discovery Calls',
                        'subtitle' => 'Turning conversations into clients',
                        'word_count' => '2,600',
                        'pages' => '10',
                        'content_summary' => 'What to say on calls. Questions to ask them. Handling objections. Closing techniques. Scripts that work.',
                        'key_points' => [
                            'Call structure and flow',
                            'Discovery questions that work',
                            'Handling common objections',
                            'Closing without being pushy',
                            'Scripts and frameworks',
                        ],
                    ],
                    [
                        'chapter' => 22,
                        'title' => 'Pricing Your Work',
                        'subtitle' => 'What to charge and when to raise it',
                        'word_count' => '2,800',
                        'pages' => '11',
                        'content_summary' => 'Beginner rates vs market rates. Hourly vs project vs retainer. When and how to raise prices. Handling price objections. Your pricing journey.',
                        'key_points' => [
                            'Pricing models compared',
                            'Beginner rates (real numbers)',
                            'When to raise prices (milestones)',
                            'Scripts for price conversations',
                            'Your progression: From X to Y rates',
                        ],
                    ],
                ],
            ],
            
            // PART 6: THE DAY-TO-DAY
            [
                'part' => 'PART 6: THE DAY-TO-DAY',
                'part_pages' => '60-65 pages',
                'chapters' => [
                    [
                        'chapter' => 23,
                        'title' => 'The Daily Routine',
                        'subtitle' => 'What a freelancer\'s day actually looks like',
                        'word_count' => '2,400',
                        'pages' => '10',
                        'content_summary' => 'Morning routine (flexible). The non-negotiables: Outreach, delivery, admin. Time blocking that works. When to stop working. Your daily structure.',
                        'key_points' => [
                            'Flexible morning routines',
                            'Daily non-negotiables',
                            'Time blocking strategies',
                            'Setting work boundaries',
                            'Your actual daily schedule',
                        ],
                    ],
                    [
                        'chapter' => 24,
                        'title' => 'Weekly and Monthly Systems',
                        'subtitle' => 'Staying organized without a boss',
                        'word_count' => '2,600',
                        'pages' => '10',
                        'content_summary' => 'Weekly review process. Monthly financial check-in. Pipeline management. Planning ahead to prevent panic. Your systems.',
                        'key_points' => [
                            'Weekly review framework',
                            'Monthly financial review',
                            'Client pipeline tracking',
                            'Planning and goal setting',
                            'Tools and templates',
                        ],
                    ],
                    [
                        'chapter' => 25,
                        'title' => 'Client Management',
                        'subtitle' => 'Working with people without HR',
                        'word_count' => '2,600',
                        'pages' => '10',
                        'content_summary' => 'Onboarding new clients. Communication frequency. Handling scope creep. Firing bad clients. Setting boundaries professionally.',
                        'key_points' => [
                            'Client onboarding process',
                            'Communication best practices',
                            'Handling scope creep',
                            'When and how to fire clients',
                            'Professional boundary setting',
                        ],
                    ],
                    [
                        'chapter' => 26,
                        'title' => 'From One Client to Many',
                        'subtitle' => 'Building a sustainable business',
                        'word_count' => '2,600',
                        'pages' => '10',
                        'content_summary' => 'The 3-client minimum. Getting referrals (how to ask). Repeat business vs constant hunting. Building a reliable pipeline. Your client acquisition evolution.',
                        'key_points' => [
                            'Why 3 clients minimum matters',
                            'Referral generation strategies',
                            'Repeat business systems',
                            'Pipeline building',
                            'Your journey from 1 to many clients',
                        ],
                    ],
                ],
            ],
            
            // PART 7: THE LONG GAME
            [
                'part' => 'PART 7: THE LONG GAME',
                'part_pages' => '60-65 pages',
                'chapters' => [
                    [
                        'chapter' => 27,
                        'title' => 'When the Honeymoon Ends',
                        'subtitle' => 'Dealing with the grind',
                        'word_count' => '2,400',
                        'pages' => '10',
                        'content_summary' => 'The loneliness of working alone. Income roller coasters. Difficult clients and conversations. Remembering why you started. The reality after the excitement fades.',
                        'key_points' => [
                            'Isolation and loneliness',
                            'Managing income inconsistency',
                            'Difficult client situations',
                            'Staying motivated long-term',
                            'Your low points and how you got through',
                        ],
                    ],
                    [
                        'chapter' => 28,
                        'title' => 'Boundaries Matter',
                        'subtitle' => 'Protecting your time and sanity',
                        'word_count' => '2,400',
                        'pages' => '10',
                        'content_summary' => 'Setting work hours and keeping them. Protecting family time. Saying no without guilt. Rest as non-negotiable. How boundaries saved you from burnout.',
                        'key_points' => [
                            'Setting and enforcing work hours',
                            'Family time protection',
                            'Saying no strategically',
                            'The importance of rest',
                            'Your boundary evolution',
                        ],
                    ],
                    [
                        'chapter' => 29,
                        'title' => 'Comparison Kills',
                        'subtitle' => 'Staying in your lane',
                        'word_count' => '2,200',
                        'pages' => '9',
                        'content_summary' => 'Social media highlight reels. Your journey is unique. Celebrating small wins. Finding your community, not your competition. Ignoring the noise.',
                        'key_points' => [
                            'The comparison trap',
                            'Social media vs reality',
                            'Celebrating progress',
                            'Finding supportive community',
                            'Focusing on your own growth',
                        ],
                    ],
                    [
                        'chapter' => 30,
                        'title' => 'The Dip',
                        'subtitle' => 'What to do when you want to quit',
                        'word_count' => '2,400',
                        'pages' => '10',
                        'content_summary' => 'Hard season vs wrong path. When to pivot vs persist. Getting help: Coaches, community, support. The power of showing up one more day. Your dip stories.',
                        'key_points' => [
                            'Recognizing temporary vs permanent struggles',
                            'Signs to pivot vs persist',
                            'Seeking help and support',
                            'Perseverance strategies',
                            'Your moments of wanting to quit',
                        ],
                    ],
                    [
                        'chapter' => 31,
                        'title' => 'Leveling Up',
                        'subtitle' => 'From freelancer to business owner',
                        'word_count' => '2,400',
                        'pages' => '10',
                        'content_summary' => 'Raising rates as you grow. Adding skills strategically. Hiring help. Building assets, not just trading time. Your evolution from survival to growth.',
                        'key_points' => [
                            'Strategic rate increases',
                            'Skill expansion timing',
                            'When to hire help',
                            'Building business assets',
                            'Your growth journey',
                        ],
                    ],
                    [
                        'chapter' => 32,
                        'title' => 'One Year Later',
                        'subtitle' => 'What freedom actually looks like',
                        'word_count' => '2,200',
                        'pages' => '9',
                        'content_summary' => 'Life after the transition. Challenges overcome. Freedom earned. The transformation complete: From alcoholic corporate manager to sober freelancer and ministry leader. The view from here. Invitation to begin.',
                        'key_points' => [
                            'The reality of freedom',
                            'Challenges you overcame',
                            'The complete transformation',
                            'What you would tell your past self',
                            'Invitation to the reader',
                        ],
                        'faith_element' => 'Light mention of purpose and serving others through your work',
                    ],
                ],
            ],
        ];
    }
    
    /**
     * SUMMARY TABLE
     */
    public function summaryTable() {
        return [
            ['Part', 'Chapters', 'Words', 'Pages'],
            ['Part 1: Fall and Rise', '5', '13,200', '52'],
            ['Part 2: Mindset', '4', '9,600', '39'],
            ['Part 3: Preparation', '5', '12,600', '51'],
            ['Part 4: Tools & Platforms', '4', '10,000', '40'],
            ['Part 5: Getting Clients', '4', '10,600', '42'],
            ['Part 6: Day-to-Day', '4', '10,200', '40'],
            ['Part 7: Long Game', '6', '14,000', '57'],
            ['TOTALS', '32', '80,200', '321'],
        ];
    }
    
    /**
     * PRINT THE OUTLINE
     */
    public function printOutline() {
        $meta = $this->bookMetadata();
        echo "=== {$meta['title']} ===\n";
        echo "{$meta['subtitle']}\n\n";
        echo "Total Chapters: {$meta['total_chapters']}\n";
        echo "Target: {$meta['target_word_count']}\n";
        echo "Estimated Pages: {$meta['estimated_pages']}\n";
        echo "Format: {$meta['format']}\n\n";
        
        echo "KEY STORY ELEMENTS:\n";
        echo "• 18-year-old dropout, call center, leadership same year\n";
        echo "• 10 years to Operations Manager (thousands led)\n";
        echo "• 16-hour workdays, alcohol dependence, smoking, partying\n";
        echo "• 2017: Terminated, no safety net\n";
        echo "• Rebuilt from scratch: VA, EA, real estate, graphics, video, copy, social\n";
        echo "• Transition healed the vices: Stopped drinking/smoking\n";
        echo "• Became active in ministry\n";
        echo "• Complete life transformation story\n\n";
        
        $outline = $this->chapterOutline();
        foreach ($outline as $part) {
            echo "\n" . str_repeat("=", 70) . "\n";
            echo "{$part['part']}\n";
            echo "Pages: {$part['part_pages']}\n";
            echo str_repeat("=", 70) . "\n\n";
            
            foreach ($part['chapters'] as $ch) {
                echo "Chapter {$ch['chapter']}: {$ch['title']}\n";
                echo "{$ch['subtitle']}\n";
                echo "Words: {$ch['word_count']} | Pages: {$ch['pages']}\n\n";
            }
        }
        
        echo "\n" . str_repeat("=", 70) . "\n";
        echo "SUMMARY TABLE\n";
        echo str_repeat("=", 70) . "\n\n";
        
        $table = $this->summaryTable();
        foreach ($table as $row) {
            printf("%-25s | %8s | %8s | %8s\n", $row[0], $row[1], $row[2], $row[3]);
        }
        
        echo "\n\nNOTE: Total came to 32 chapters and 80k words.\n";
        echo "Can trim to 28 chapters / 65-70k words if needed.\n";
    }
}

// ============================================
// OUTPUT
// ============================================

$outline = new FinalBookOutline();
$outline->printOutline();

?>
