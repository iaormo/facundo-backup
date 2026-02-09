<?php
/**
 * COURSE CREATOR DELIVERABLES & ROLE
 * What Ian needs to do vs what is automated
 */

class CourseCreatorResponsibilities {
    
    /**
     * WHAT YOU NEED TO CREATE (One-Time Setup)
     */
    public function oneTimeCreation() {
        return [
            'section' => 'ONE-TIME CREATION (Do This Once)',
            
            'content_creation' => [
                'title' => 'Course Content',
                'items' => [
                    [
                        'item' => '28 Video Lessons',
                        'details' => 'Record 28 videos (15-30 min each). Total ~10-12 hours of content.',
                        'tools' => 'Phone/laptop camera, Canva for slides, CapCut for editing (or no editing)',
                        'time_estimate' => '2-3 weeks (record 2-3 per day)',
                        'format' => 'Screen share + voiceover OR talking head. Your choice.',
                    ],
                    [
                        'item' => '28 Worksheets / Templates',
                        'details' => 'One PDF worksheet per lesson. Can be simple Google Docs exported to PDF.',
                        'examples' => [
                            'Mindset Assessment worksheet',
                            'Financial Runway Calculator',
                            'Skills Inventory',
                            'Offer Statement Builder',
                            'Profile Optimization Checklist',
                            'Application Tracker',
                            'Pricing Calculator',
                            'Client Onboarding Checklist',
                        ],
                        'time_estimate' => '1 week (create template, duplicate for each lesson)',
                    ],
                    [
                        'item' => 'Email Sequence',
                        'details' => '28 emails (one per lesson) with video link + worksheet download + action item.',
                        'structure' => [
                            'Subject line',
                            'Personal opening (1-2 sentences)',
                            'Lesson overview (2-3 sentences)',
                            'Video link',
                            'Worksheet download link',
                            'Action item for the day',
                            'Encouragement/closing',
                        ],
                        'time_estimate' => '2-3 days (use template, customize per lesson)',
                    ],
                    [
                        'item' => 'Welcome Sequence',
                        'details' => '3-5 emails for new students after purchase.',
                        'emails' => [
                            'Email 1: Welcome + What to expect + Join Facebook Group',
                            'Email 2: How to get the most out of this course',
                            'Email 3: Your first lesson is waiting',
                            'Email 4: Common questions answered',
                            'Email 5: Reminder to start if they have not yet',
                        ],
                        'time_estimate' => '1 day',
                    ],
                ],
            ],
            
            'tech_setup' => [
                'title' => 'Tech Setup',
                'items' => [
                    [
                        'item' => 'Email Marketing Platform',
                        'options' => 'MailerLite (free) or ConvertKit ($29/mo)',
                        'setup_tasks' => [
                            'Create account',
                            'Import email list (when you have one)',
                            'Create automation sequence (28 emails)',
                            'Set trigger: When someone buys, start sequence',
                        ],
                        'time_estimate' => '1 day',
                    ],
                    [
                        'item' => 'Video Hosting',
                        'options' => 'YouTube (unlisted videos) or Vimeo',
                        'setup_tasks' => [
                            'Upload all 28 videos',
                            'Set to unlisted (not public)',
                            'Organize in playlist',
                            'Copy links for emails',
                        ],
                        'time_estimate' => '1 day (upload while doing other things)',
                    ],
                    [
                        'item' => 'File Storage',
                        'options' => 'Google Drive (free) or Dropbox',
                        'setup_tasks' => [
                            'Create folder: "Zero to Remote - Worksheets"',
                            'Upload all 28 PDFs',
                            'Set sharing: Anyone with link can view',
                            'Copy links for emails',
                        ],
                        'time_estimate' => '2 hours',
                    ],
                    [
                        'item' => 'Facebook Group',
                        'options' => 'Free',
                        'setup_tasks' => [
                            'Create group: "Zero to Remote - Alumni"',
                            'Write group description',
                            'Set 3-5 group rules',
                            'Create welcome post template',
                            'Add cover image (Canva)',
                        ],
                        'time_estimate' => '2 hours',
                    ],
                    [
                        'item' => 'Payment System',
                        'options' => 'GCash QR, PayPal, Maya, or Stripe',
                        'setup_tasks' => [
                            'Set up business accounts',
                            'Create payment links',
                            'Test with ₱1 transaction',
                            'Set up confirmation email/message',
                        ],
                        'time_estimate' => '1 day',
                    ],
                    [
                        'item' => 'Sales Page',
                        'options' => 'Carrd.co (free), WordPress, or simple Google Doc',
                        'sections_needed' => [
                            'Headline',
                            'Problem',
                            'Solution',
                            'What you get',
                            'Module breakdown',
                            'Testimonials (use later)',
                            'Price + Guarantee',
                            'FAQ',
                            'Payment button/link',
                        ],
                        'time_estimate' => '1-2 days',
                    ],
                ],
            ],
        ];
    }
    
    /**
     * YOUR ONGOING ROLE (Weekly/Monthly)
     */
    public function ongoingResponsibilities() {
        return [
            'section' => 'YOUR ONGOING ROLE (After Launch)',
            
            'daily_tasks' => [
                'title' => 'Daily (15-30 minutes)',
                'tasks' => [
                    [
                        'task' => 'Check Facebook Group',
                        'time' => '10 min',
                        'what_to_do' => [
                            'Answer questions',
                            'Approve new members',
                            'Like/comment on student posts',
                            'Pin important announcements',
                        ],
                    ],
                    [
                        'task' => 'Check Email/Messages',
                        'time' => '10 min',
                        'what_to_do' => [
                            'Respond to student emails',
                            'Handle payment issues',
                            'Answer pre-sale questions',
                        ],
                    ],
                ],
            ],
            
            'weekly_tasks' => [
                'title' => 'Weekly (2-3 hours)',
                'tasks' => [
                    [
                        'task' => 'Live Q&A Session (Optional but Powerful)',
                        'time' => '1 hour',
                        'format' => 'Facebook Live or Zoom in the Facebook Group',
                        'what_to_do' => [
                            'Announce 24 hours before',
                            'Answer questions submitted by students',
                            'Share wins and updates',
                            'Record and post replay',
                        ],
                        'frequency' => 'Once per week (e.g., Wednesday 8PM)',
                    ],
                    [
                        'task' => 'Content Creation for Marketing',
                        'time' => '1-2 hours',
                        'what_to_do' => [
                            'Create 2-3 social media posts for the week',
                            'Share student wins (with permission)',
                            'Post tips related to course content',
                            'Answer questions in public (builds authority)',
                        ],
                        'platforms' => ['Facebook', 'LinkedIn', 'TikTok'],
                    ],
                ],
            ],
            
            'monthly_tasks' => [
                'title' => 'Monthly (4-6 hours)',
                'tasks' => [
                    [
                        'task' => 'Course Improvements',
                        'time' => '2 hours',
                        'what_to_do' => [
                            'Review student feedback',
                            'Update outdated information',
                            'Add new resources',
                            'Fix any broken links',
                        ],
                    ],
                    [
                        'task' => 'Marketing Push',
                        'time' => '2-4 hours',
                        'what_to_do' => [
                            'Plan next month\'s content calendar',
                            'Create promotional campaign',
                            'Run Facebook ads (if budget allows)',
                            'Collaborate with affiliates/partners',
                        ],
                    ],
                    [
                        'task' => 'Financial Review',
                        'time' => '1 hour',
                        'what_to_do' => [
                            'Track sales and revenue',
                            'Calculate profit/loss',
                            'Plan coaching upsell outreach',
                            'Pay yourself (transfer to personal account)',
                        ],
                    ],
                ],
            ],
            
            'as_needed_tasks' => [
                'title' => 'As Needed',
                'tasks' => [
                    [
                        'task' => 'Refund Requests',
                        'frequency' => 'Rare (expect 5-10% max)',
                        'what_to_do' => [
                            'Ask what did not work (feedback)',
                            'Process refund within policy (7 days)',
                            'Remove from email sequence',
                            'Learn from feedback',
                        ],
                    ],
                    [
                        'task' => 'Coaching Upsell Outreach',
                        'frequency' => 'When students finish Module 4',
                        'what_to_do' => [
                            'Send personalized email to engaged students',
                            'Offer free 15-min strategy call',
                            'Pitch ₱2,997 coaching program',
                            'Handle objections',
                        ],
                    ],
                    [
                        'task' => 'Student Success Stories',
                        'frequency' => 'When students get results',
                        'what_to_do' => [
                            'Ask for testimonial',
                            'Request case study interview',
                            'Create social proof content',
                            'Feature in marketing',
                        ],
                    ],
                ],
            ],
        ];
    }
    
    /**
     * WHAT IS AUTOMATED (No Work Required)
     */
    public function automatedParts() {
        return [
            'section' => 'AUTOMATED (Set and Forget)',
            
            'automation' => [
                [
                    'what' => 'Lesson Delivery',
                    'how' => 'Email automation sends 1 lesson every 2 days automatically',
                    'your_involvement' => 'None (after initial setup)',
                ],
                [
                    'what' => 'Welcome Emails',
                    'how' => 'Trigger: New purchase → Send welcome sequence',
                    'your_involvement' => 'None',
                ],
                [
                    'what' => 'Payment Confirmation',
                    'how' => 'GCash/PayPal sends automatic receipt',
                    'your_involvement' => 'None (or copy-paste thank you message)',
                ],
                [
                    'what' => 'Facebook Group Access',
                    'how' => 'Link in welcome email (students request to join)',
                    'your_involvement' => 'Just approve requests (30 seconds/day)',
                ],
                [
                    'what' => 'Progress Tracking',
                    'how' => 'Students self-track via lessons received',
                    'your_involvement' => 'None (unless you want to check in personally)',
                ],
            ],
        ];
    }
    
    /**
     * TIME COMMITMENT SUMMARY
     */
    public function timeCommitment() {
        return [
            'section' => 'TIME COMMITMENT',
            
            'phases' => [
                [
                    'phase' => 'Creation Phase (Before Launch)',
                    'duration' => '4-6 weeks',
                    'hours_per_week' => '10-15 hours',
                    'breakdown' => [
                        'Content creation: 40-50 hours',
                        'Tech setup: 10-15 hours',
                        'Sales page + marketing: 10 hours',
                        'Testing + refinements: 5 hours',
                    ],
                ],
                [
                    'phase' => 'Launch Week',
                    'duration' => '1 week',
                    'hours_per_week' => '15-20 hours',
                    'breakdown' => [
                        'Daily social media posts: 1-2 hours/day',
                        'Answering questions: 2-3 hours/day',
                        'Welcoming new students: 1 hour/day',
                        'Live Q&A: 1 hour',
                    ],
                ],
                [
                    'phase' => 'Evergreen (Ongoing)',
                    'duration' => 'Permanent',
                    'hours_per_week' => '5-8 hours',
                    'breakdown' => [
                        'Daily community management: 30 min/day (3.5 hrs/week)',
                        'Weekly live Q&A: 1 hour',
                        'Content creation: 2-3 hours/week',
                        'Coaching upsell calls: 1-2 hours/week',
                    ],
                ],
            ],
        ];
    }
    
    /**
     * YOUR ROLE AS INSTRUCTOR
     */
    public function yourRole() {
        return [
            'section' => 'YOUR ROLE: What You Actually Do',
            
            'primary_role' => 'Course Creator + Community Leader',
            
            'what_you_are_NOT' => [
                'You are NOT a 1-on-1 coach for every student (that is the ₱2,997 upsell)',
                'You are NOT responsible for student results (they must do the work)',
                'You are NOT available 24/7 (set office hours)',
                'You are NOT rewriting content constantly (set it and improve monthly)',
            ],
            
            'what_you_ARE' => [
                [
                    'role' => 'Content Creator',
                    'description' => 'You record lessons once. They are reused forever.',
                    'frequency' => 'One-time + monthly updates',
                ],
                [
                    'role' => 'Community Facilitator',
                    'description' => 'You create space for students to help each other.',
                    'frequency' => 'Daily (15 min)',
                ],
                [
                    'role' => 'Question Answerer',
                    'description' => 'You answer questions in group or via email.',
                    'frequency' => 'Daily (15 min)',
                ],
                [
                    'role' => 'Cheerleader',
                    'description' => 'You celebrate wins and encourage students.',
                    'frequency' => 'Weekly',
                ],
                [
                    'role' => 'Marketer',
                    'description' => 'You promote the course to get new students.',
                    'frequency' => 'Weekly (2-3 hours)',
                ],
                [
                    'role' => 'Coach (for upsells)',
                    'description' => 'You offer 1-on-1 coaching to serious students.',
                    'frequency' => 'As needed (for ₱2,997 coaching clients)',
                ],
            ],
        ];
    }
    
    /**
     * DELIVERABLES CHECKLIST
     */
    public function deliverablesChecklist() {
        return [
            'section' => 'COMPLETE DELIVERABLES CHECKLIST',
            
            'before_launch' => [
                'title' => 'MUST HAVE Before Launch',
                'items' => [
                    '[ ] All 28 videos recorded and uploaded',
                    '[ ] All 28 worksheets created and uploaded',
                    '[ ] 28-lesson email sequence written and scheduled',
                    '[ ] Welcome email sequence (3-5 emails) set up',
                    '[ ] Facebook Group created with rules',
                    '[ ] Sales page published',
                    '[ ] Payment system working (tested)',
                    '[ ] Thank you page with next steps',
                    '[ ] At least 3 beta testers who gave feedback',
                ],
            ],
            
            'nice_to_have' => [
                'title' => 'NICE TO HAVE (Can Add Later)',
                'items' => [
                    '[ ] 3-5 testimonials from beta testers',
                    '[ ] Case study from successful student',
                    '[ ] Bonus lessons or resources',
                    '[ ] Certificate of completion',
                    '[ ] Affiliate program set up',
                    '[ ] Facebook ads running',
                ],
            ],
            
            'ongoing' => [
                'title' => 'ONGOING (After Students Enroll)',
                'items' => [
                    '[ ] Daily: Check Facebook Group (15 min)',
                    '[ ] Daily: Answer emails/messages (15 min)',
                    '[ ] Weekly: Live Q&A session (1 hour)',
                    '[ ] Weekly: Create marketing content (2 hours)',
                    '[ ] Monthly: Course updates (2 hours)',
                    '[ ] Monthly: Financial review (1 hour)',
                    '[ ] As needed: Coaching upsell outreach',
                ],
            ],
        ];
    }
    
    /**
     * Print the full breakdown
     */
    public function printResponsibilities() {
        // One-time creation
        $oneTime = $this->oneTimeCreation();
        echo "=== {$oneTime['section']} ===\n\n";
        
        foreach ($oneTime['content_creation']['items'] as $item) {
            echo "→ {$item['item']}\n";
            echo "   {$item['details']}\n";
            echo "   Time: {$item['time_estimate']}\n\n";
        }
        
        echo str_repeat("-", 50) . "\n\n";
        
        foreach ($oneTime['tech_setup']['items'] as $item) {
            echo "→ {$item['item']}\n";
            echo "   Options: {$item['options']}\n";
            echo "   Time: {$item['time_estimate']}\n\n";
        }
        
        // Ongoing responsibilities
        $ongoing = $this->ongoingResponsibilities();
        echo "\n=== {$ongoing['section']} ===\n\n";
        
        foreach (['daily_tasks', 'weekly_tasks', 'monthly_tasks'] as $period) {
            $section = $ongoing[$period];
            echo "{$section['title']}\n";
            foreach ($section['tasks'] as $task) {
                echo "  → {$task['task']} ({$task['time']})\n";
            }
            echo "\n";
        }
        
        // Automated parts
        $auto = $this->automatedParts();
        echo "\n=== {$auto['section']} ===\n\n";
        foreach ($auto['automation'] as $item) {
            echo "✓ {$item['what']}\n";
            echo "  {$item['how']}\n\n";
        }
        
        // Time commitment
        $time = $this->timeCommitment();
        echo "\n=== {$time['section']} ===\n\n";
        foreach ($time['phases'] as $phase) {
            echo "{$phase['phase']}\n";
            echo "  Duration: {$phase['duration']}\n";
            echo "  Hours/week: {$phase['hours_per_week']}\n\n";
        }
        
        // Your role
        $role = $this->yourRole();
        echo "\n=== {$role['section']} ===\n\n";
        echo "Primary Role: {$role['primary_role']}\n\n";
        
        echo "You are NOT:\n";
        foreach ($role['what_you_are_NOT'] as $not) {
            echo "  ✗ $not\n";
        }
        
        echo "\nYou ARE:\n";
        foreach ($role['what_you_ARE'] as $r) {
            echo "  ✓ {$r['role']}: {$r['description']}\n";
        }
        
        // Checklist
        $checklist = $this->deliverablesChecklist();
        echo "\n\n=== {$checklist['section']} ===\n\n";
        foreach (['before_launch', 'nice_to_have', 'ongoing'] as $cat) {
            $section = $checklist[$cat];
            echo "{$section['title']}\n";
            foreach ($section['items'] as $item) {
                echo "  $item\n";
            }
            echo "\n";
        }
    }
}

// ============================================
// OUTPUT
// ============================================

$responsibilities = new CourseCreatorResponsibilities();
$responsibilities->printResponsibilities();

?>
