<?php
/**
 * FREE CHECKLIST PDF - Design & Content Guide
 * Complete layout and content specifications
 */

class ChecklistDesignGuide {
    
    /**
     * DESIGN SPECIFICATIONS
     */
    public function designSpecs() {
        return [
            'format' => 'PDF (portrait)',
            'size' => 'A4 (210mm x 297mm) or Letter (8.5" x 11")',
            'pages' => '8-12 pages',
            'color_scheme' => [
                'primary' => 'Dark blue or teal (professional, trustworthy)',
                'accent' => 'Orange or coral (action, energy)',
                'neutral' => 'Light gray, white',
                'text' => 'Dark gray or black (not pure black)',
            ],
            'fonts' => [
                'headings' => 'Montserrat, Poppins, or Oswald (bold, modern)',
                'body' => 'Open Sans, Lato, or Inter (readable)',
            ],
            'tool' => 'Canva (free) - search "checklist" or "workbook" templates',
        ];
    }
    
    /**
     * PAGE-BY-PAGE LAYOUT
     */
    public function pageLayout() {
        return [
            // Page 1: Cover
            [
                'page' => 1,
                'type' => 'Cover Page',
                'elements' => [
                    'Large title: "THE REMOTE WORK STARTER CHECKLIST"',
                    'Subtitle: "30 Action Steps to Land Your First Online Client"',
                    'Author name and photo (optional)',
                    'Tagline: "Go from employee to remote worker in 30 days"',
                    'Visual: Person working on laptop, coffee, home office vibe',
                    'Color: Bold, eye-catching',
                ],
                'design_notes' => 'Clean, professional, inspiring. Use your brand colors.',
            ],
            
            // Page 2: Welcome
            [
                'page' => 2,
                'type' => 'Welcome Page',
                'elements' => [
                    'Headline: "Welcome"',
                    'Personal message:',
                    '"Hi, I am [Your Name]. Two years ago I was stuck in a job I hated, commuting 3 hours daily. Today I work from home, earn more, and spend time with my family."',
                    '"This checklist is exactly what I wish I had when I started."',
                    'How to use this:',
                    '  • One task per day (30-60 minutes)',
                    '  • Do not skip ahead',
                    '  • Check off each day as you complete it',
                    '  • If you get stuck, email me at [email]',
                    'Signature with photo',
                ],
            ],
            
            // Page 3: Before You Start
            [
                'page' => 3,
                'type' => 'Prep Page',
                'title' => 'Before You Start',
                'content' => [
                    'What you need:' => [
                        '□ Computer or laptop (phone works for some tasks)',
                        '□ Internet connection',
                        '□ 30-60 minutes per day',
                        '□ Commitment to finish',
                    ],
                    'What you do NOT need:' => [
                        '✗ Special degree',
                        '✗ Years of experience',
                        '✗ Expensive courses',
                        '✗ Perfect English',
                        '✗ Tech genius skills',
                    ],
                    'Your commitment:' => [
                        'I, _________________, commit to completing this 30-day checklist.',
                        'Signature: ________________ Date: ____________',
                    ],
                ],
            ],
            
            // Pages 4-9: The Checklist (Week by Week)
            [
                'page' => '4-9',
                'type' => 'Main Content - Weekly Checklists',
                'layout_per_week' => [
                    'header' => 'WEEK [X]: [THEME]',
                    'color_bar' => 'Different color for each week',
                    'days' => [
                        'DAY [X]: [TASK NAME]',
                        'Time: XX minutes',
                        '',
                        '[Description of what to do]',
                        '',
                        '□ Completed',
                        '',
                        'Notes:',
                        '_________________',
                        '_________________',
                    ],
                    'week_review' => [
                        'WEEK [X] COMPLETE!',
                        'What did you accomplish this week?',
                        '_________________',
                        '',
                        'What was hardest?',
                        '_________________',
                    ],
                ],
            ],
            
            // Page 10: Tools & Resources
            [
                'page' => 10,
                'type' => 'Resources Page',
                'title' => 'Tools You Will Need (All Free)',
                'sections' => [
                    'Communication' => [
                        'Gmail (email)',
                        'Google Meet (video calls)',
                        'Zoom (video calls)',
                    ],
                    'Organization' => [
                        'Google Calendar (scheduling)',
                        'Notion or Trello (task management)',
                        'Google Drive (file storage)',
                    ],
                    'Time & Money' => [
                        'Toggl or Clockify (time tracking)',
                        'PayPal (international payments)',
                        'GCash (local payments)',
                    ],
                    'Design & Content' => [
                        'Canva (design)',
                        'Grammarly (writing help)',
                    ],
                ],
            ],
            
            // Page 11: Templates
            [
                'page' => 11,
                'type' => 'Bonus - Templates',
                'title' => 'Bonus: Application Template',
                'content' => [
                    'Copy and customize this for every job application:',
                    '',
                    '─────────────────────',
                    'Subject: Application for [Job Title]',
                    '',
                    'Hi [Name],',
                    '',
                    'I saw your post about needing [specific task] for your [business type]. I help [target client] with exactly this.',
                    '',
                    '[One line about your relevant experience or skill]',
                    '',
                    'I would love to learn more about what you are looking for. Would you be open to a quick 10-minute call this week?',
                    '',
                    'Best,',
                    '[Your Name]',
                    '─────────────────────',
                ],
            ],
            
            // Page 12: What's Next + Upgrade
            [
                'page' => 12,
                'type' => 'Next Steps + Upsell',
                'title' => 'What is Next?',
                'content' => [
                    'Congratulations! You have completed the 30-day checklist.',
                    '',
                    'By now you should have:',
                    '✓ A clear skill to sell',
                    '✓ An active OnlineJobs.ph profile',
                    '✓ Applications sent',
                    '✓ Momentum toward your first client',
                    '',
                    'But here is the thing...',
                    '',
                    'This checklist tells you WHAT to do.',
                    '',
                    'But what if you had video walkthroughs showing you EXACTLY how to do each step?',
                    '',
                    'What if you had:' => [
                        '• Word-for-word profile examples that get hired',
                        '• Screen recordings of how to create your portfolio',
                        '• Exact scripts for discovery calls',
                        '• Pricing calculator and proposal templates',
                        '• A community of people on the same journey',
                        '• Someone to answer your questions when you get stuck',
                    ],
                    '',
                    'That is exactly what you get inside the Zero to Remote Course.',
                    '',
                    '28 video lessons | Done-for-you templates | Private community',
                    '',
                    'Investment: ₱299',
                    '',
                    '[Learn More Button/Link]',
                ],
            ],
        ];
    }
    
    /**
     * DETAILED CONTENT - WEEK BY WEEK
     */
    public function detailedContent() {
        return [
            'week_1' => [
                'theme' => 'MINDSET & FOUNDATION',
                'color' => 'Blue',
                'days' => [
                    [
                        'day' => 1,
                        'task' => 'Calculate Your Survival Number',
                        'time' => '30 min',
                        'description' => 'Write down every expense you NEED to survive: rent, food, bills, transportation. Total them up. This is your minimum monthly number. Example: If total is ₱18,000, that is your survival number.',
                    ],
                    [
                        'day' => 2,
                        'task' => 'Set Your Savings Target',
                        'time' => '15 min',
                        'description' => 'Multiply your survival number by 3. This is your safety net. If you cannot save this yet, plan to build it while still employed. Example: ₱18,000 × 3 = ₱54,000 savings target.',
                    ],
                    [
                        'day' => 3,
                        'task' => 'List 20 Skills You Already Have',
                        'time' => '45 min',
                        'description' => 'Brainstorm EVERYTHING you know how to do. Work skills AND personal skills. Can you organize files? Write emails? Use Excel? Post on Facebook? Manage a calendar? Write them all down. Do not filter.',
                    ],
                    [
                        'day' => 4,
                        'task' => 'Find Your Marketable Skills',
                        'time' => '30 min',
                        'description' => 'From your 20 skills, circle 5 that businesses actually pay for. Go to OnlineJobs.ph and search for your skills. Are there jobs posted? If yes, it is marketable.',
                    ],
                    [
                        'day' => 5,
                        'task' => 'Pick ONE Skill to Focus On',
                        'time' => '20 min',
                        'description' => 'Choose ONE skill that: (1) You are confident in, (2) Has job postings, (3) You do not hate doing. This is your starting skill. You can add more later. For now, focus wins.',
                    ],
                    [
                        'day' => 6,
                        'task' => 'Define Your Target Client',
                        'time' => '20 min',
                        'description' => 'Who needs your skill? Pick ONE type: Online coaches, Ecommerce store owners, Real estate agents, Marketing agencies. The more specific, the better.',
                    ],
                    [
                        'day' => 7,
                        'task' => 'Write Your Offer Statement',
                        'time' => '30 min',
                        'description' => 'Fill in: "I help [target client] with [skill] so they can [result]." Example: "I help online coaches manage their email inbox so they can focus on their clients." This is your positioning.',
                    ],
                ],
            ],
            
            'week_2' => [
                'theme' => 'ONLINE PRESENCE',
                'color' => 'Teal',
                'days' => [
                    [
                        'day' => 8,
                        'task' => 'Take a Professional Photo',
                        'time' => '1 hour',
                        'description' => 'Use your phone. Find good natural light (near window). Use plain background (white wall). Dress professionally. Smile. Take 20 shots, pick the best 3. This photo goes everywhere.',
                    ],
                    [
                        'day' => 9,
                        'task' => 'Create OnlineJobs.ph Account',
                        'time' => '45 min',
                        'description' => 'Go to onlinejobs.ph. Sign up. Verify your ID (upload government ID). Complete basic profile. Set your hourly rate to ₱0 for now (you will update later).',
                    ],
                    [
                        'day' => 10,
                        'task' => 'Write Your Profile Headline',
                        'time' => '30 min',
                        'description' => 'Use your offer statement. NOT: "Hardworking VA seeking opportunity." YES: "Email Manager for Busy Coaches." Keep it under 100 characters. This is the first thing clients see.',
                    ],
                    [
                        'day' => 11,
                        'task' => 'Write Your Profile Summary',
                        'time' => '1 hour',
                        'description' => 'Structure: (1) Hook: Who you help, (2) Proof: Why you can help, (3) Call to action: Invite them to contact you. 200-300 words. First 2 sentences are critical.',
                    ],
                    [
                        'day' => 12,
                        'task' => 'List Your Skills and Tools',
                        'time' => '30 min',
                        'description' => 'Add 5-10 specific skills. List tools you know: Gmail, Google Sheets, Canva, Facebook, etc. Be specific. "Proficient in Microsoft Office" is too generic. List each tool separately.',
                    ],
                    [
                        'day' => 13,
                        'task' => 'Set Up LinkedIn Profile',
                        'time' => '1.5 hours',
                        'description' => 'Create or update LinkedIn. Same photo as OnlineJobs.ph. Headline: "[Skill] for [Client] | Helping [Result]." Fill out About section with your offer statement. Add any past work experience.',
                    ],
                    [
                        'day' => 14,
                        'task' => 'Create One Portfolio Piece',
                        'time' => '2 hours',
                        'description' => 'If you have no client work, create a sample. Email management? Show before/after inbox screenshots. Social media? Create 5 sample posts. Design? Make sample graphics. Save as PDF or screenshots.',
                    ],
                ],
            ],
            
            'week_3' => [
                'theme' => 'APPLICATION PREP',
                'color' => 'Green',
                'days' => [
                    [
                        'day' => 15,
                        'task' => 'Research 10 Job Postings',
                        'time' => '1 hour',
                        'description' => 'Search OnlineJobs.ph for jobs matching your skill. Read 10 different posts. What are employers asking for? What problems do they have? Save the 3 that match you best.',
                    ],
                    [
                        'day' => 16,
                        'task' => 'Create Application Template',
                        'time' => '1 hour',
                        'description' => 'Write a template you can customize. Structure: (1) Hook (mention their specific post), (2) Proof (one line about your ability), (3) Ask (request a call). Keep it under 100 words. See Page 11.',
                    ],
                    [
                        'day' => 17,
                        'task' => 'Customize for 3 Jobs',
                        'time' => '1 hour',
                        'description' => 'Take your template and customize for the 3 jobs you saved. Mention specific details from their post. Show you read it. Do not send yet—just prepare.',
                    ],
                    [
                        'day' => 18,
                        'task' => 'Set Up Payment Accounts',
                        'time' => '45 min',
                        'description' => 'Create PayPal account (for international clients). Set up GCash (for local). Verify both with your ID. Test by sending a small amount to a friend. You need to get paid.',
                    ],
                    [
                        'day' => 19,
                        'task' => 'Create Invoice Template',
                        'time' => '30 min',
                        'description' => 'Make a simple invoice in Google Docs or Canva. Include: Your name, client name, service description, amount, payment details (PayPal email or GCash number), due date.',
                    ],
                    [
                        'day' => 20,
                        'task' => 'Join 3 Facebook Groups',
                        'time' => '30 min',
                        'description' => 'Find groups where your target clients hang out. Examples: "Online Business Owners Philippines," "Ecommerce Entrepreneurs," "Virtual Assistants Philippines." Join and read the rules.',
                    ],
                    [
                        'day' => 21,
                        'task' => 'List 20 Warm Contacts',
                        'time' => '30 min',
                        'description' => 'List friends, family, past colleagues, acquaintances who might know someone who needs your skill. Write their names and how you know them. Do not message yet—just list.',
                    ],
                ],
            ],
            
            'week_4' => [
                'theme' => 'TAKE ACTION',
                'color' => 'Orange',
                'days' => [
                    [
                        'day' => 22,
                        'task' => 'Send 5 Applications',
                        'time' => '1.5 hours',
                        'description' => 'Apply to 5 jobs on OnlineJobs.ph. Use your customized templates. Target jobs posted in the last 24 hours. Hit send. Do not overthink it.',
                    ],
                    [
                        'day' => 23,
                        'task' => 'Send 5 More Applications',
                        'time' => '1.5 hours',
                        'description' => 'Apply to 5 more jobs. Aim for 10 total applications. Remember: You will get rejected. Everyone does. It is part of the process. Keep going.',
                    ],
                    [
                        'day' => 24,
                        'task' => 'Message 5 Warm Contacts',
                        'time' => '45 min',
                        'description' => 'From your list of 20, message 5 people. Script: "Hey [Name], I started offering [service] to [clients]. Do you know anyone who might need this?" Ask for introductions, not for them to hire you.',
                    ],
                    [
                        'day' => 25,
                        'task' => 'Send 5 LinkedIn Connections',
                        'time' => '30 min',
                        'description' => 'Search your target client type on LinkedIn. Send 5 personalized connection requests. Mention something specific from their profile or a common interest.',
                    ],
                    [
                        'day' => 26,
                        'task' => 'Provide Value in 1 Group',
                        'time' => '30 min',
                        'description' => 'Answer a question or provide helpful input in one of the Facebook groups you joined. Do not sell. Just be helpful. Build visibility.',
                    ],
                    [
                        'day' => 27,
                        'task' => 'Follow Up on Applications',
                        'time' => '30 min',
                        'description' => 'Check your OnlineJobs.ph messages. Respond to any replies. If you applied 3+ days ago with no response, send polite follow-up: "Just following up on my application. Happy to answer any questions."',
                    ],
                    [
                        'day' => 28,
                        'task' => 'Review and Plan',
                        'time' => '45 min',
                        'description' => 'What worked? What did not? How many responses did you get? Plan your next 30 days. Set one goal: Get one call with a potential client.',
                    ],
                    [
                        'day' => 29,
                        'task' => 'Send 5 More Applications',
                        'time' => '1 hour',
                        'description' => 'Keep the momentum. Apply to 5 more jobs. Aim for 15 total applications now. Consistency beats intensity.',
                    ],
                    [
                        'day' => 30,
                        'task' => 'Celebrate Your Progress',
                        'time' => '15 min',
                        'description' => 'Look back at Day 1. You have come so far. You have a skill, a profile, a portfolio, and momentum. Most people never start. You did. Celebrate. Then keep going.',
                    ],
                ],
            ],
        ];
    }
    
    /**
     * VISUAL DESIGN ELEMENTS
     */
    public function visualElements() {
        return [
            'checkboxes' => [
                'style' => 'Empty square box (□) that looks hand-drawn or clean lines',
                'size' => 'Large enough to check with pen (if printed)',
                'placement' => 'Left side of each task',
            ],
            'headers' => [
                'week_header' => 'Full width colored bar with white text',
                'day_header' => 'Bold, larger font, colored text matching week theme',
            ],
            'icons' => [
                'source' => 'Canva elements or Flaticon (free)',
                'style' => 'Simple line icons',
                'usage' => 'Next to section headers, for visual interest',
            ],
            'progress_tracker' => [
                'location' => 'Bottom of each week page',
                'content' => '7 empty circles representing 7 days',
                'usage' => 'Fill in as you complete each day',
            ],
            'callout_boxes' => [
                'purpose' => 'Highlight important tips or warnings',
                'design' => 'Colored background box with icon',
                'examples' => [
                    '💡 Tip: Start with jobs posted in last 24 hours',
                    '⚠️ Warning: Never pay to apply for a job',
                    '🎯 Goal: Send 5 applications this week',
                ],
            ],
            'page_numbers' => [
                'location' => 'Bottom center or corner',
                'style' => 'Simple, clean',
            ],
        ];
    }
    
    /**
     * CANVA SETUP STEPS
     */
    public function canvaSetup() {
        return [
            'step_1' => [
                'action' => 'Go to Canva.com (free account)',
            ],
            'step_2' => [
                'action' => 'Click "Create a design"',
                'details' => 'Search for "A4 Document" or "US Letter"',
            ],
            'step_3' => [
                'action' => 'Search templates',
                'details' => 'Type "checklist," "workbook," or "ebook" in templates',
            ],
            'step_4' => [
                'action' => 'Pick a base template',
                'details' => 'Choose one with clean layout, good fonts',
            ],
            'step_5' => [
                'action' => 'Customize colors',
                'details' => 'Change to your brand colors (blue + orange combo works well)',
            ],
            'step_6' => [
                'action' => 'Add your content',
                'details' => 'Copy-paste from this guide, adjust fonts and spacing',
            ],
            'step_7' => [
                'action' => 'Add pages',
                'details' => 'Duplicate pages and modify for each day/week',
            ],
            'step_8' => [
                'action' => 'Download as PDF',
                'details' => 'File → Download → PDF Print (best quality)',
            ],
        ];
    }
    
    /**
     * PRINT THE GUIDE
     */
    public function printGuide() {
        $specs = $this->designSpecs();
        echo "=== CHECKLIST DESIGN SPECS ===\n\n";
        echo "Format: {$specs['format']}\n";
        echo "Size: {$specs['size']}\n";
        echo "Pages: {$specs['pages']}\n\n";
        
        echo "Color Scheme:\n";
        foreach ($specs['color_scheme'] as $type => $color) {
            echo "  $type: $color\n";
        }
        
        echo "\nFonts:\n";
        foreach ($specs['fonts'] as $type => $font) {
            echo "  $type: $font\n";
        }
        
        echo "\nTool: {$specs['tool']}\n\n";
        
        echo str_repeat("=", 60) . "\n";
        echo "PAGE LAYOUT\n";
        echo str_repeat("=", 60) . "\n\n";
        
        $pages = $this->pageLayout();
        foreach ($pages as $page) {
            echo "Page {$page['page']}: {$page['type']}\n";
            if (isset($page['title'])) {
                echo "Title: {$page['title']}\n";
            }
            if (isset($page['design_notes'])) {
                echo "Notes: {$page['design_notes']}\n";
            }
            echo "\n";
        }
        
        echo str_repeat("=", 60) . "\n";
        echo "CANVA SETUP STEPS\n";
        echo str_repeat("=", 60) . "\n\n";
        
        $canva = $this->canvaSetup();
        foreach ($canva as $step => $details) {
            echo strtoupper(str_replace('_', ' ', $step)) . ":\n";
            echo "  {$details['action']}\n";
            if (isset($details['details'])) {
                echo "  {$details['details']}\n";
            }
            echo "\n";
        }
    }
}

// ============================================
// OUTPUT
// ============================================

$guide = new ChecklistDesignGuide();
$guide->printGuide();

?>
