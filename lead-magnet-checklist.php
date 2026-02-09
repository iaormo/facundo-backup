<?php
/**
 * FREE LEAD MAGNET: The Remote Work Starter Checklist
 * PDF content for email list building
 */

class LeadMagnet {
    
    /**
     * LEAD MAGNET OVERVIEW
     */
    public function overview() {
        return [
            'title' => 'The Remote Work Starter Checklist',
            'subtitle' => '30 Action Steps to Land Your First Online Client',
            'promise' => 'Follow this checklist and you will have everything ready to start applying for remote jobs in 30 days',
            'pages' => '8-10 pages',
            'format' => 'PDF (downloadable)',
            'upgrade_path' => 'Full course (28 lessons) after they consume checklist',
            
            'why_this_works' => [
                'Specific: 30 concrete steps (not vague advice)',
                'Time-bound: 30 days (feels achievable)',
                'Actionable: Checkboxes they can actually tick',
                'Complete: Covers mindset to first application',
                'Leads to course: Checklist = "what to do", Course = "how to do it"',
            ],
        ];
    }
    
    /**
     * THE CHECKLIST CONTENT
     */
    public function checklistContent() {
        return [
            [
                'week' => 'WEEK 1',
                'theme' => 'MINDSET & FOUNDATION',
                'days' => [
                    [
                        'day' => 1,
                        'task' => 'Calculate your survival number',
                        'details' => 'How much do you NEED to earn monthly to survive? Include rent, food, bills, minimum expenses. Write this number down.',
                        'time' => '30 min',
                        'deliverable' => 'Your exact survival number (example: ₱20,000)',
                    ],
                    [
                        'day' => 2,
                        'task' => 'Set your transition savings goal',
                        'details' => 'Multiply your survival number by 3. This is your safety net target. If you cannot save this yet, plan to build it while working your current job.',
                        'time' => '15 min',
                        'deliverable' => 'Savings target amount and timeline',
                    ],
                    [
                        'day' => 3,
                        'task' => 'List 20 skills you already have',
                        'details' => 'Include work skills AND personal skills. Can you organize? Write emails? Use Excel? Manage a calendar? Post on social media? List everything.',
                        'time' => '45 min',
                        'deliverable' => 'List of 20 skills (no filtering yet)',
                    ],
                    [
                        'day' => 4,
                        'task' => 'Circle your top 5 marketable skills',
                        'details' => 'From your list of 20, pick 5 that businesses actually pay for. Look at OnlineJobs.ph job postings to see what is in demand.',
                        'time' => '30 min',
                        'deliverable' => 'Top 5 skills that have market demand',
                    ],
                    [
                        'day' => 5,
                        'task' => 'Pick ONE skill to focus on',
                        'details' => 'Choose the skill that: (1) You are confident in, (2) Has demand, (3) You do not hate doing. This is your starting skill.',
                        'time' => '20 min',
                        'deliverable' => 'One clear skill to sell',
                    ],
                    [
                        'day' => 6,
                        'task' => 'Define your target client',
                        'details' => 'Who needs your skill? Be specific: "Online coaches," "Ecommerce store owners," "Real estate agents." Pick one type.',
                        'time' => '20 min',
                        'deliverable' => 'One target client type',
                    ],
                    [
                        'day' => 7,
                        'task' => 'Write your offer statement',
                        'details' => 'Fill in the blank: "I help [target client] with [skill] so they can [result]." Example: "I help coaches manage their inbox so they can focus on clients."',
                        'time' => '30 min',
                        'deliverable' => 'Your one-sentence offer statement',
                    ],
                ],
            ],
            [
                'week' => 'WEEK 2',
                'theme' => 'ONLINE PRESENCE',
                'days' => [
                    [
                        'day' => 8,
                        'task' => 'Take a professional profile photo',
                        'details' => 'Use your phone. Good lighting, plain background, smile, professional attire. This photo will be used everywhere.',
                        'time' => '1 hour',
                        'deliverable' => '3-5 good profile photos to choose from',
                    ],
                    [
                        'day' => 9,
                        'task' => 'Create OnlineJobs.ph account',
                        'details' => 'Go to onlinejobs.ph. Sign up. Verify your ID. Complete basic profile information. Do not write your full profile yet.',
                        'time' => '45 min',
                        'deliverable' => 'Active OnlineJobs.ph account',
                    ],
                    [
                        'day' => 10,
                        'task' => 'Write your OnlineJobs.ph headline',
                        'details' => 'This is the first thing clients see. Use your offer statement. Not "Hardworking VA" but "Email Manager for Busy Coaches."',
                        'time' => '30 min',
                        'deliverable' => 'Profile headline (max 100 characters)',
                    ],
                    [
                        'day' => 11,
                        'task' => 'Write your profile summary',
                        'details' => 'First 2 sentences are critical. Hook: Who you help. Proof: Why you can help them. Call to action: Invite them to contact you.',
                        'time' => '1 hour',
                        'deliverable' => '200-300 word profile summary',
                    ],
                    [
                        'day' => 12,
                        'task' => 'List your skills and tools',
                        'details' => 'Add 5-10 specific skills. List tools you know (Gmail, Canva, Excel, etc.). Be specific, not generic.',
                        'time' => '30 min',
                        'deliverable' => 'Skills section completed',
                    ],
                    [
                        'day' => 13,
                        'task' => 'Set up LinkedIn profile',
                        'details' => 'Create or update LinkedIn. Use same photo. Headline: "[Skill] for [Client] | Helping [Result]." Fill out About section.',
                        'time' => '1.5 hours',
                        'deliverable' => 'Complete LinkedIn profile',
                    ],
                    [
                        'day' => 14,
                        'task' => 'Create one portfolio piece',
                        'details' => 'If you have no client work, create a sample. Example: If email management, show a before/after inbox cleanup. If social media, create 5 sample posts.',
                        'time' => '2 hours',
                        'deliverable' => 'One portfolio piece saved as PDF or screenshots',
                    ],
                ],
            ],
            [
                'week' => 'WEEK 3',
                'theme' => 'APPLICATION PREP',
                'days' => [
                    [
                        'day' => 15,
                        'task' => 'Research 10 job postings',
                        'details' => 'Search OnlineJobs.ph for jobs matching your skill. Read 10 different posts. Note what clients are asking for. Save the best 3.',
                        'time' => '1 hour',
                        'deliverable' => '3 ideal job postings saved/bookmarked',
                    ],
                    [
                        'day' => 16,
                        'task' => 'Create application template',
                        'details' => 'Write a template you can customize. Structure: (1) Hook (show you read the post), (2) Proof (one line about your ability), (3) Ask (request a call). Keep it under 100 words.',
                        'time' => '1 hour',
                        'deliverable' => 'Application template document',
                    ],
                    [
                        'day' => 17,
                        'task' => 'Customize for 3 specific jobs',
                        'details' => 'Take your template and customize it for the 3 jobs you saved. Make each one specific to that job posting. Mention details from their post.',
                        'time' => '1 hour',
                        'deliverable' => '3 customized applications ready to send',
                    ],
                    [
                        'day' => 18,
                        'task' => 'Set up payment accounts',
                        'details' => 'Create PayPal account (for international clients). Set up GCash (for local). Verify both. Test with small amount.',
                        'time' => '45 min',
                        'deliverable' => 'Working PayPal and GCash accounts',
                    ],
                    [
                        'day' => 19,
                        'task' => 'Create simple invoice template',
                        'details' => 'Make a simple invoice template in Google Docs or Canva. Include: Your name, client name, service, amount, payment details.',
                        'time' => '30 min',
                        'deliverable' => 'Invoice template ready to use',
                    ],
                    [
                        'day' => 20,
                        'task' => 'Join 3 Facebook groups',
                        'details' => 'Find groups where your target clients hang out. Examples: "Online Business Owners," "Ecommerce Entrepreneurs." Join and read the rules.',
                        'time' => '30 min',
                        'deliverable' => 'Member of 3 relevant groups',
                    ],
                    [
                        'day' => 21,
                        'task' => 'List 20 warm contacts',
                        'details' => 'List friends, family, past colleagues, acquaintances who might know someone who needs your skill. Do not message yet, just list.',
                        'time' => '30 min',
                        'deliverable' => 'List of 20 names with contact info',
                    ],
                ],
            ],
            [
                'week' => 'WEEK 4',
                'theme' => 'TAKE ACTION',
                'days' => [
                    [
                        'day' => 22,
                        'task' => 'Send 5 OnlineJobs.ph applications',
                        'details' => 'Apply to 5 jobs that match your skill. Use your customized templates. Do not wait for perfect, just send.',
                        'time' => '1.5 hours',
                        'deliverable' => '5 applications sent',
                    ],
                    [
                        'day' => 23,
                        'task' => 'Send 5 more applications',
                        'details' => 'Apply to 5 more jobs. Target recent postings (last 24 hours). Fresh posts get fewer applicants.',
                        'time' => '1.5 hours',
                        'deliverable' => '10 total applications sent',
                    ],
                    [
                        'day' => 24,
                        'task' => 'Message 5 warm contacts',
                        'details' => 'From your list of 20, message 5 people. Script: "I started offering [service]. Do you know anyone who might need this?"',
                        'time' => '45 min',
                        'deliverable' => '5 messages sent',
                    ],
                    [
                        'day' => 25,
                        'task' => 'Send 5 LinkedIn connection requests',
                        'details' => 'Search your target client type. Send 5 personalized connection requests. Mention common ground or why you want to connect.',
                        'time' => '30 min',
                        'deliverable' => '5 LinkedIn connections requested',
                    ],
                    [
                        'day' => 26,
                        'task' => 'Provide value in 1 Facebook group',
                        'details' => 'Answer a question or provide helpful input in one of the groups you joined. Do not sell yet, just be helpful.',
                        'time' => '30 min',
                        'deliverable' => '1 helpful comment/post in group',
                    ],
                    [
                        'day' => 27,
                        'task' => 'Follow up on applications',
                        'details' => 'Check your OnlineJobs.ph messages. Respond to any replies. Follow up on applications from 3+ days ago with polite message.',
                        'time' => '30 min',
                        'deliverable' => 'All responses replied to',
                    ],
                    [
                        'day' => 28,
                        'task' => 'Review and plan',
                        'details' => 'What worked? What did not? How many responses did you get? Plan your next 30 days. Set goal: Get one call with a potential client.',
                        'time' => '45 min',
                        'deliverable' => '30-day review and next month plan',
                    ],
                    [
                        'day' => 29,
                        'task' => 'Send 5 more applications',
                        'details' => 'Keep going. Consistency wins. Apply to 5 more jobs.',
                        'time' => '1 hour',
                        'deliverable' => '15 total applications sent',
                    ],
                    [
                        'day' => 30,
                        'task' => 'Celebrate progress',
                        'details' => 'You have done more in 30 days than most people do in a year. You have a profile, portfolio, applications sent, and momentum. Keep going.',
                        'time' => '15 min',
                        'deliverable' => 'Acknowledge your progress',
                    ],
                ],
            ],
        ];
    }
    
    /**
     * BONUS SECTIONS
     */
    public function bonusSections() {
        return [
            [
                'title' => 'TOOLS YOU NEED',
                'content' => [
                    'Communication: Gmail, Google Meet, Zoom (free versions)',
                    'Organization: Google Calendar, Notion (free), Trello (free)',
                    'Time Tracking: Toggl (free), Clockify (free)',
                    'Design: Canva (free)',
                    'Storage: Google Drive (15GB free)',
                    'Passwords: Bitwarden or LastPass (free)',
                ],
            ],
            [
                'title' => 'SAMPLE APPLICATION TEMPLATE',
                'content' => [
                    'Hi [Name],',
                    '',
                    'I saw your post about needing [specific task] for your [business type]. I help [target client] with exactly this.',
                    '',
                    '[One line of proof: experience, result, or relevant skill]',
                    '',
                    'I would love to learn more about what you are looking for. Would you be open to a quick 10-minute call this week?',
                    '',
                    'Best,',
                    '[Your Name]',
                ],
            ],
            [
                'title' => 'RED FLAGS TO AVOID',
                'content' => [
                    'Jobs asking for money upfront (scam)',
                    'Vague job descriptions (waste of time)',
                    'Unrealistic pay for the work (too good to be true)',
                    'Requests for personal info before hiring (SSS, bank details)',
                    'Clients who refuse video calls (possible scam)',
                ],
            ],
            [
                'title' => 'WHEN YOU GET STUCK',
                'content' => [
                    'Day 3 (skill selection): Pick the skill you are most confident in, not the most exciting.',
                    'Day 14 (portfolio): Create ONE sample piece. Done is better than perfect.',
                    'Day 22 (applications): Fear of rejection is normal. Send anyway. 90% of people never apply.',
                    'Day 27 (no responses): Check if your applications are specific enough. Generic = ignored.',
                ],
            ],
        ];
    }
    
    /**
     * UPGRADE PATH TO COURSE
     */
    public function upgradePath() {
        return [
            'the_gap' => [
                'checklist_gives' => 'What to do and when to do it',
                'checklist_missing' => [
                    'How to actually write your profile (word-for-word examples)',
                    'How to create portfolio pieces (step-by-step walkthrough)',
                    'How to handle discovery calls (exact scripts)',
                    'How to price your services (pricing calculator)',
                    'How to close the deal (objection handling)',
                    'How to deliver for your first client (onboarding checklist)',
                    'Video lessons showing you exactly how to do each step',
                    'Community support when you get stuck',
                ],
            ],
            'upgrade_prompt' => [
                'location' => 'Last page of checklist',
                'text' => 'Want the exact scripts, templates, and video walkthroughs for every step in this checklist? The Zero to Remote course includes 28 video lessons, done-for-you templates, and a community of people on the same journey. Get started for just ₱299.',
                'cta' => 'Yes, I want the full course',
            ],
        ];
    }
    
    /**
     * LANDING PAGE COPY
     */
    public function landingPageCopy() {
        return [
            'headline' => 'Free Checklist: 30 Days to Your First Remote Client',
            'subheadline' => 'The exact step-by-step actions to escape your 9-5 and start earning online',
            'bullet_points' => [
                '30 specific action items (no guessing what to do next)',
                'Week-by-week breakdown from mindset to first application',
                'Takes 30-60 minutes per day (while keeping your job)',
                'Used by 500+ Filipinos to start their remote work journey',
            ],
            'form_fields' => [
                'First Name',
                'Email Address',
            ],
            'button_text' => 'Send Me the Free Checklist',
            'privacy_note' => 'We respect your privacy. Unsubscribe anytime.',
            'deliverable' => 'PDF will be emailed to you immediately',
            'upgrade_page' => 'After submitting, show thank you page with soft pitch for ₱299 course',
        ];
    }
    
    /**
     * EMAIL SEQUENCE FOR LEADS
     */
    public function emailSequence() {
        return [
            [
                'email' => 1,
                'timing' => 'Immediately after opt-in',
                'subject' => 'Your Remote Work Checklist is here',
                'content' => [
                    'Hi [Name],',
                    '',
                    'Here is your checklist: [DOWNLOAD LINK]',
                    '',
                    'Print it out. Start with Day 1 today.',
                    '',
                    'Quick tip: Do not skip ahead. Each day builds on the previous one.',
                    '',
                    'If you get stuck, reply to this email. I read every one.',
                    '',
                    'To your freedom,',
                    '[Your Name]',
                ],
            ],
            [
                'email' => 2,
                'timing' => 'Day 3',
                'subject' => 'Day 3: The hardest part',
                'content' => [
                    'Hi [Name],',
                    '',
                    'How is Day 3 going? Listing 20 skills can feel overwhelming.',
                    '',
                    'Here is the secret: You have more skills than you think.',
                    '',
                    'Can you:',
                    '- Write an email?',
                    '- Use Excel?',
                    '- Post on Facebook?',
                    '- Answer a customer question?',
                    '- Organize files?',
                    '',
                    'Those are all billable skills.',
                    '',
                    'Keep going.',
                    '[Your Name]',
                    '',
                    'P.S. If you want video walkthroughs for each day, check out the full course.',
                ],
            ],
            [
                'email' => 3,
                'timing' => 'Day 7',
                'subject' => 'Week 1 complete?',
                'content' => [
                    'Hi [Name],',
                    '',
                    'If you have been following the checklist, today you wrote your offer statement.',
                    '',
                    'That is huge. Most people never get that clear.',
                    '',
                    'Week 2 is about building your online presence. This is where people get stuck on perfection.',
                    '',
                    'Do not aim for perfect. Aim for done.',
                    '',
                    'A "good enough" profile that is live beats a "perfect" profile that is never published.',
                    '',
                    'Keep going,',
                    '[Your Name]',
                ],
            ],
            [
                'email' => 4,
                'timing' => 'Day 14',
                'subject' => 'Halfway point checkpoint',
                'content' => [
                    'Hi [Name],',
                    '',
                    'You are halfway through the checklist.',
                    '',
                    'Quick check:',
                    '- Is your OnlineJobs.ph profile live?',
                    '- Do you have one portfolio piece?',
                    '- Have you joined at least one Facebook group?',
                    '',
                    'If yes, you are ahead of 90% of people who never take action.',
                    '',
                    'If no, what is holding you back?',
                    '',
                    'Reply and let me know. I might be able to help.',
                    '',
                    '[Your Name]',
                ],
            ],
            [
                'email' => 5,
                'timing' => 'Day 21',
                'subject' => 'Week 3: The fear kicks in',
                'content' => [
                    'Hi [Name],',
                    '',
                    'Week 3 is when fear usually shows up.',
                    '',
                    'You have done the setup. You are ready to apply.',
                    '',
                    'But then the voice says: "What if they reject me?"',
                    '',
                    'Here is the truth: You will get rejected. Everyone does.',
                    '',
                    'I got rejected 47 times before my first client.',
                    '',
                    'But here is what I learned: Each rejection taught me something.',
                    '',
                    'Apply anyway. Send the application.',
                    '',
                    'Need help with your application? I cover exact scripts in the full course.',
                    '',
                    '[Your Name]',
                ],
            ],
            [
                'email' => 6,
                'timing' => 'Day 30',
                'subject' => 'You made it to Day 30',
                'content' => [
                    'Hi [Name],',
                    '',
                    '30 days ago you downloaded this checklist.',
                    '',
                    'If you followed it, you now have:',
                    '- A clear skill to sell',
                    '- An active profile on OnlineJobs.ph',
                    '- A portfolio piece',
                    '- Applications sent',
                    '',
                    'That is more progress than most people make in a year.',
                    '',
                    'But here is the thing: The checklist tells you WHAT to do.',
                    '',
                    'If you want to know HOW to do each step (with video walkthroughs, templates, and scripts), I created the Zero to Remote course.',
                    '',
                    'It includes:',
                    '- 28 video lessons (6+ hours)',
                    '- Done-for-you templates and scripts',
                    '- Private community',
                    '- Everything in the checklist, explained in detail',
                    '',
                    'Investment: ₱299',
                    '',
                    'If you are serious about landing your first client, check it out here: [LINK]',
                    '',
                    'Either way, keep going. You are closer than you think.',
                    '',
                    '[Your Name]',
                ],
            ],
        ];
    }
    
    /**
     * PRINT THE LEAD MAGNET
     */
    public function printLeadMagnet() {
        $overview = $this->overview();
        echo "=== {$overview['title']} ===\n";
        echo "{$overview['subtitle']}\n\n";
        echo "Promise: {$overview['promise']}\n";
        echo "Format: {$overview['pages']} page PDF\n\n";
        
        echo "Why This Works:\n";
        foreach ($overview['why_this_works'] as $reason) {
            echo "  • $reason\n";
        }
        
        echo "\n\n" . str_repeat("=", 60) . "\n";
        echo "CHECKLIST CONTENT\n";
        echo str_repeat("=", 60) . "\n\n";
        
        $content = $this->checklistContent();
        foreach ($content as $week) {
            echo "\n{$week['week']}: {$week['theme']}\n";
            echo str_repeat("-", 40) . "\n\n";
            
            foreach ($week['days'] as $day) {
                echo "Day {$day['day']}: {$day['task']}\n";
                echo "Time: {$day['time']}\n";
                echo "{$day['details']}\n";
                echo "Deliverable: {$day['deliverable']}\n\n";
            }
        }
        
        echo "\n\n" . str_repeat("=", 60) . "\n";
        echo "BONUS SECTIONS\n";
        echo str_repeat("=", 60) . "\n\n";
        
        foreach ($this->bonusSections() as $bonus) {
            echo "{$bonus['title']}\n";
            foreach ($bonus['content'] as $item) {
                echo "  • $item\n";
            }
            echo "\n";
        }
        
        echo "\n\n" . str_repeat("=", 60) . "\n";
        echo "LANDING PAGE COPY\n";
        echo str_repeat("=", 60) . "\n\n";
        
        $landing = $this->landingPageCopy();
        echo "Headline: {$landing['headline']}\n";
        echo "Subheadline: {$landing['subheadline']}\n\n";
        echo "Bullet Points:\n";
        foreach ($landing['bullet_points'] as $bullet) {
            echo "  • $bullet\n";
        }
        echo "\nButton: {$landing['button_text']}\n";
        
        echo "\n\n" . str_repeat("=", 60) . "\n";
        echo "EMAIL SEQUENCE (6 emails over 30 days)\n";
        echo str_repeat("=", 60) . "\n\n";
        
        foreach ($this->emailSequence() as $email) {
            echo "Email {$email['email']}: {$email['subject']}\n";
            echo "Timing: {$email['timing']}\n\n";
        }
        
        echo "\n\n=== UPGRADE PATH ===\n\n";
        $upgrade = $this->upgradePath();
        echo "Checklist gives: {$upgrade['the_gap']['checklist_gives']}\n\n";
        echo "Checklist is missing (course provides):\n";
        foreach ($upgrade['the_gap']['checklist_missing'] as $missing) {
            echo "  • $missing\n";
        }
    }
}

// ============================================
// OUTPUT
// ============================================

$leadMagnet = new LeadMagnet();
$leadMagnet->printLeadMagnet();

?>
