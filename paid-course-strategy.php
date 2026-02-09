<?php
/**
 * PAID COURSE STRATEGY: ₱299 Low-Ticket Offer
 * Delivery + Marketing Plan for Freelancing Transition Course
 */

class PaidCourseStrategy {
    
    /**
     * WHY ₱299 WORKS (My Assessment)
     */
    public function pricingAnalysis() {
        return [
            'price_point' => '₱299',
            'positioning' => 'Low-ticket paid course (not free, not premium)',
            
            'pros' => [
                [
                    'point' => 'Filters for serious students only',
                    'explanation' => 'Free courses get 90% tire-kickers. Paid courses get people who actually do the work.',
                ],
                [
                    'point' => 'Immediate revenue validation',
                    'explanation' => 'If people pay ₱299, they will pay ₱2,997 for coaching. Proves market demand.',
                ],
                [
                    'point' => 'Higher perceived value',
                    'explanation' => 'People value what they pay for. ₱299 course feels more "real" than free.',
                ],
                [
                    'point' => 'Self-liquidating ad spend',
                    'explanation' => '₱299 price can cover Facebook ad costs to acquire customers (break-even or profit).',
                ],
                [
                    'point' => 'Creates buyer list',
                    'explanation' => 'Everyone who buys ₱299 is a hot lead for your ₱2,997 coaching. Easier upsell.',
                ],
            ],
            
            'cons' => [
                [
                    'point' => 'Lower volume than free',
                    'explanation' => 'You will get fewer signups than free course. Need stronger marketing.',
                ],
                [
                    'point' => 'Higher expectation',
                    'explanation' => 'People expect more support for paid courses. You need delivery system.',
                ],
                [
                    'point' => 'Requires payment setup',
                    'explanation' => 'GCash/PayPal integration, refund policy, customer service.',
                ],
            ],
            
            'verdict' => 'GO WITH ₱299 if: You want serious students, plan to run ads, and have coaching upsell ready.',
            'alternative' => 'Go FREE if: You want maximum reach, building email list from scratch, or testing market first.',
        ];
    }
    
    /**
     * COURSE DELIVERY METHODS
     */
    public function deliveryMethods() {
        return [
            'option_1_email_drip' => [
                'name' => 'Email Drip Course (Recommended for ₱299)',
                'setup' => [
                    'Platform: MailerLite (free up to 1,000 subs) or ConvertKit ($29/mo)',
                    'Format: 1 lesson emailed every 2 days (28 lessons = 8 weeks)',
                    'Each email: Video link + Worksheet PDF + Action item',
                    'Videos: Hosted on YouTube (unlisted) or Vimeo',
                ],
                'pros' => [
                    'Simple tech stack',
                    'High open rates (people check email daily)',
                    'No login/password for students',
                    'Easy to automate',
                ],
                'cons' => [
                    'Less "course platform" feel',
                    'Students cannot binge-watch',
                ],
                'cost' => '₱0-1,500/month',
            ],
            
            'option_2_course_platform' => [
                'name' => 'Course Platform (More Professional)',
                'platforms' => [
                    'Teachable: Free plan (₱1.50 + 10% per transaction)',
                    'Thinkific: Free plan available',
                    'Gumroad: 10% fee per sale',
                    'LMS on WordPress: LearnDash or TutorLMS',
                ],
                'setup' => [
                    'Upload all videos to platform',
                    'Organize into modules/lessons',
                    'Add worksheets as downloads',
                    'Student login area with progress tracking',
                ],
                'pros' => [
                    'Professional look',
                    'Progress tracking for students',
                    'Can offer certificates',
                    'Better for higher-priced courses later',
                ],
                'cons' => [
                    'More complex setup',
                    'Students need to remember login',
                    'Monthly fees or transaction fees',
                ],
                'cost' => '₱0-3,000/month + transaction fees',
            ],
            
            'option_3_facebook_group' => [
                'name' => 'Facebook Group + Videos (Community Focus)',
                'setup' => [
                    'Create private Facebook Group for paid members',
                    'Post one lesson every 2 days as video/text',
                    'Worksheets posted as files in group',
                    'Q&A threads for each lesson',
                ],
                'pros' => [
                    'Built-in community',
                    'Students support each other',
                    'No extra platform costs',
                    'Easy to manage from phone',
                ],
                'cons' => [
                    'Not professional looking',
                    'Hard to organize (scroll to find old lessons)',
                    'Facebook algorithm may hide posts',
                ],
                'cost' => '₱0',
            ],
            
            'option_4_hybrid' => [
                'name' => 'HYBRID (My Recommendation)',
                'setup' => [
                    'Main delivery: Email drip (1 lesson every 2 days)',
                    'Videos: Unlisted YouTube links in emails',
                    'Community: Free Facebook Group for Q&A',
                    'Worksheets: Google Drive folder shared once',
                    'Bonus: Weekly live Q&A in Facebook Group',
                ],
                'pros' => [
                    'Best of all worlds',
                    'Professional email delivery',
                    'Community support',
                    'Low tech complexity',
                    'Scalable',
                ],
                'cost' => '₱0-1,500/month',
            ],
        ];
    }
    
    /**
     * MARKETING PLAN
     */
    public function marketingPlan() {
        return [
            'phase_1_pre_launch' => [
                'name' => 'Phase 1: Pre-Launch (2 weeks before)',
                'duration' => '2 weeks',
                'activities' => [
                    [
                        'task' => 'Build anticipation content',
                        'actions' => [
                            'Post "I am creating something" teasers',
                            'Share behind-the-scenes of course creation',
                            'Poll audience: What is your biggest challenge transitioning to remote work?',
                            'Share testimonials from beta testers (if available)',
                        ],
                        'platforms' => ['Facebook', 'LinkedIn', 'Instagram'],
                        'frequency' => '3-4 posts per week',
                    ],
                    [
                        'task' => 'Create waitlist',
                        'actions' => [
                            'Simple Google Form: "Get early access + discount"',
                            'Or Messenger opt-in: "Message COURSE to get notified"',
                            'Goal: 50-100 people on waitlist',
                        ],
                        'cost' => '₱0',
                    ],
                    [
                        'task' => 'Prepare sales assets',
                        'actions' => [
                            'Sales page (simple Google Doc or Carrd site)',
                            'Payment link (GCash QR + PayPal)',
                            'Thank you page with next steps',
                            'Email sequence for buyers',
                        ],
                    ],
                ],
            ],
            
            'phase_2_launch' => [
                'name' => 'Phase 2: Launch Week',
                'duration' => '7 days',
                'activities' => [
                    [
                        'task' => 'Launch to warm audience',
                        'actions' => [
                            'Day 1: Email waitlist with early-bird price (₱199 for 48 hours)',
                            'Day 1: Post on all social media with story',
                            'Day 2: Share first testimonial or case study',
                            'Day 3: Address objections ("Is this worth it?")',
                            'Day 4: Show inside the course (screenshot/clip)',
                            'Day 5: Urgency post ("Early bird ends tonight")',
                            'Day 6: Final push (social proof, last chance)',
                            'Day 7: Thank you post + welcome new students',
                        ],
                    ],
                    [
                        'task' => 'Content themes for launch week',
                        'posts' => [
                            'Your personal story of transitioning to freelancing',
                            'Before/after: What life was like before vs after remote work',
                            'Common mistakes people make when starting',
                            'What is inside the course (module breakdown)',
                            'Who this is for / Who this is NOT for',
                            'FAQ addressing main concerns',
                            'Final reminder with urgency',
                        ],
                    ],
                ],
            ],
            
            'phase_3_evergreen' => [
                'name' => 'Phase 3: Evergreen Sales',
                'duration' => 'Ongoing',
                'activities' => [
                    [
                        'task' => 'Organic content marketing',
                        'actions' => [
                            '2-3 posts per week about freelancing/remote work topics',
                            'Each post soft-sells the course (CTA in comments)',
                            'Share student wins and testimonials',
                            'Answer common questions with "I cover this in my course"',
                        ],
                        'platforms' => ['Facebook', 'LinkedIn', 'TikTok'],
                    ],
                    [
                        'task' => 'Facebook Ads (optional after initial sales)',
                        'setup' => [
                            'Budget: ₱200-500/day to start',
                            'Target: Philippines, ages 22-40, interests: remote work, freelancing',
                            'Ad format: Video of you explaining who course is for',
                            'Landing page: Simple Carrd site with GCash/PayPal',
                            'Goal: Break even or profit on ad spend',
                        ],
                    ],
                    [
                        'task' => 'Partnerships and affiliates',
                        'actions' => [
                            'Offer 30% commission to affiliates',
                            'Partner with complementary businesses (resume writers, coaches)',
                            'Guest posts/podcasts in freelancing niche',
                            'Cross-promote with other course creators',
                        ],
                    ],
                    [
                        'task' => 'Email marketing',
                        'actions' => [
                            'Weekly newsletter with freelancing tips',
                            'Soft pitch course every 4th email',
                            'Nurture sequence for non-buyers',
                        ],
                    ],
                ],
            ],
        ];
    }
    
    /**
     * SALES PAGE STRUCTURE
     */
    public function salesPageStructure() {
        return [
            'headline' => 'Zero to Remote: Your 4-Week Blueprint to Escape the 9-5',
            'subheadline' => 'The exact roadmap to land your first remote client (even if you have zero experience)',
            
            'sections' => [
                'the_problem' => [
                    'hook' => 'Tired of commuting, office politics, and feeling stuck?',
                    'pain_points' => [
                        'You wake up dreading the day',
                        'You are underpaid for the work you do',
                        'You want more time with family',
                        'You know remote work exists but do not know how to start',
                        'You have tried applying online but never hear back',
                    ],
                ],
                'the_solution' => [
                    'intro' => 'I created this course because I was where you are',
                    'what_it_is' => 'A 4-week step-by-step program that takes you from employee to your first remote client',
                    'benefits' => [
                        'Know exactly what skill to sell (even if you think you have none)',
                        'Create a profile that gets you hired (not ignored)',
                        'Send applications that get responses (not silence)',
                        'Land your first client and know what to do next',
                    ],
                ],
                'what_you_get' => [
                    '28 video lessons' => 'Over 6 hours of step-by-step training',
                    'Worksheets & templates' => 'Proposals, contracts, email scripts',
                    'Private community' => 'Connect with other students',
                    'Lifetime access' => 'Watch anytime, anywhere',
                ],
                'module_breakdown' => [
                    'Module 1' => 'Freelancer Mindset + Financial Safety Net',
                    'Module 2' => 'Discover Your Marketable Skill',
                    'Module 3' => 'Build Your Online Presence',
                    'Module 4' => 'Land Your First Client',
                    'Module 5' => 'Scale and Build Sustainable Income',
                ],
                'testimonials' => [
                    'placeholder_1' => '"I got my first client in Week 3. Now I earn ₱35k/month from home." - Maria, former bank employee',
                    'placeholder_2' => '"The application templates alone were worth the price. I went from 0 responses to 3 calls in one week." - John, virtual assistant',
                ],
                'who_this_is_for' => [
                    'Employees who want to transition to remote work',
                    'People with no freelancing experience',
                    'Anyone willing to do the work (this is not a magic button)',
                ],
                'who_this_is_not_for' => [
                    'People looking for get-rich-quick schemes',
                    'Those not willing to spend 5-10 hours per week',
                    'People who want to stay in their comfort zone',
                ],
                'the_offer' => [
                    'price' => '₱299',
                    'value_stack' => [
                        'Course value: ₱4,997',
                        'Templates: ₱1,500',
                        'Community access: ₱997',
                        'Total value: ₱7,494',
                    ],
                    'actual_price' => 'Your investment: ₱299',
                    'guarantee' => '7-day money-back guarantee. If you do the work and do not see progress, I will refund you.',
                ],
                'call_to_action' => [
                    'button_text' => 'Get Instant Access for ₱299',
                    'payment_options' => 'Pay via GCash, Maya, or PayPal',
                    'urgency' => 'Limited time: Price increases to ₱499 soon',
                ],
                'faq' => [
                    'How long do I have access?' => 'Lifetime. Watch as many times as you want.',
                    'What if I am not technical?' => 'No tech skills needed. If you can use Facebook, you can do this.',
                    'How soon can I get a client?' => 'Most students who do the work land a client within 4-6 weeks.',
                    'Is there a refund?' => 'Yes. 7-day guarantee. Do the work, show me, and if no results, full refund.',
                    'Will this work for my skill?' => 'Course covers skills that are in demand: admin, social media, customer support, data entry. If you have a different skill, the marketing principles still apply.',
                ],
            ],
        ];
    }
    
    /**
     * OPERATIONS CHECKLIST
     */
    public function operationsChecklist() {
        return [
            'before_launch' => [
                'All 28 lessons recorded and uploaded',
                'All worksheets created and uploaded',
                'Email automation sequence set up',
                'Sales page published',
                'Payment links working (test with ₱1)',
                'Thank you page with next steps',
                'Facebook Group created and rules posted',
                'Refund policy documented',
                'At least 3 beta testers with feedback',
            ],
            'launch_week' => [
                'Daily social media posts scheduled',
                'Email to waitlist sent',
                'Monitor questions and respond within 2 hours',
                'Track sales daily',
                'Welcome new students within 24 hours',
            ],
            'ongoing' => [
                'Check Facebook Group daily (15 min)',
                'Answer student questions within 24 hours',
                'Weekly Q&A live session (optional but powerful)',
                'Collect testimonials from successful students',
                'Monthly content calendar for organic marketing',
            ],
        ];
    }
    
    /**
     * REVENUE PROJECTIONS
     */
    public function revenueProjections() {
        return [
            'conservative' => [
                'month_1' => '10 sales × ₱299 = ₱2,990',
                'month_2' => '15 sales × ₱299 = ₱4,485',
                'month_3' => '20 sales × ₱299 = ₱5,980',
                'upsell_rate' => '10% of buyers upgrade to ₱2,997 coaching',
                'coaching_revenue_month_3' => '4 sales × ₱2,997 = ₱11,988',
                'total_quarter_1' => '₱25,443',
            ],
            'moderate' => [
                'month_1' => '25 sales × ₱299 = ₱7,475',
                'month_2' => '40 sales × ₱299 = ₱11,960',
                'month_3' => '60 sales × ₱299 = ₱17,940',
                'upsell_rate' => '15% upgrade to coaching',
                'coaching_revenue_month_3' => '18 sales × ₱2,997 = ₱53,946',
                'total_quarter_1' => '₱91,321',
            ],
            'with_ads' => [
                'ad_spend' => '₱10,000/month',
                'cost_per_sale' => '₱200',
                'sales_per_month' => '50',
                'revenue' => '50 × ₱299 = ₱14,950',
                'profit' => '₱14,950 - ₱10,000 = ₱4,950',
                'upsell_value' => '7 coaching sales × ₱2,997 = ₱20,979',
                'total_profit' => '₱25,929/month',
            ],
        ];
    }
    
    /**
     * Print the full strategy
     */
    public function printStrategy() {
        echo "=== PAID COURSE STRATEGY: ₱299 OFFER ===\n\n";
        
        // Pricing Analysis
        $analysis = $this->pricingAnalysis();
        echo "PRICING ANALYSIS: Why ₱299 Works\n";
        echo str_repeat("-", 50) . "\n\n";
        
        echo "PROS:\n";
        foreach ($analysis['pros'] as $pro) {
            echo "✓ {$pro['point']}\n";
            echo "  {$pro['explanation']}\n\n";
        }
        
        echo "CONS:\n";
        foreach ($analysis['cons'] as $con) {
            echo "✗ {$con['point']}\n";
            echo "  {$con['explanation']}\n\n";
        }
        
        echo "VERDICT: {$analysis['verdict']}\n";
        echo "ALTERNATIVE: {$analysis['alternative']}\n\n";
        
        // Delivery Methods
        echo str_repeat("=", 60) . "\n";
        echo "DELIVERY METHODS\n";
        echo str_repeat("=", 60) . "\n\n";
        
        $delivery = $this->deliveryMethods();
        foreach ($delivery as $key => $method) {
            echo "{$method['name']}\n";
            echo "Cost: {$method['cost']}\n\n";
            
            if (isset($method['pros'])) {
                echo "Pros:\n";
                foreach ($method['pros'] as $pro) {
                    echo "  + $pro\n";
                }
                echo "\nCons:\n";
                foreach ($method['cons'] as $con) {
                    echo "  - $con\n";
                }
            }
            echo "\n";
        }
        
        // Marketing Plan
        echo str_repeat("=", 60) . "\n";
        echo "MARKETING PLAN\n";
        echo str_repeat("=", 60) . "\n\n";
        
        $marketing = $this->marketingPlan();
        foreach ($marketing as $phase => $details) {
            echo "{$details['name']}\n";
            echo "Duration: {$details['duration']}\n\n";
            
            foreach ($details['activities'] as $activity) {
                echo "→ {$activity['task']}\n";
                if (isset($activity['actions'])) {
                    foreach ($activity['actions'] as $action) {
                        echo "   • $action\n";
                    }
                }
                if (isset($activity['platforms'])) {
                    echo "   Platforms: " . implode(', ', $activity['platforms']) . "\n";
                }
                if (isset($activity['cost'])) {
                    echo "   Cost: {$activity['cost']}\n";
                }
                echo "\n";
            }
            echo "\n";
        }
        
        // Revenue Projections
        echo str_repeat("=", 60) . "\n";
        echo "REVENUE PROJECTIONS\n";
        echo str_repeat("=", 60) . "\n\n";
        
        $revenue = $this->revenueProjections();
        foreach ($revenue as $scenario => $numbers) {
            echo strtoupper($scenario) . " SCENARIO:\n";
            foreach ($numbers as $label => $value) {
                echo "  $label: $value\n";
            }
            echo "\n";
        }
        
        echo str_repeat("=", 60) . "\n";
        echo "MY RECOMMENDATION\n";
        echo str_repeat("=", 60) . "\n\n";
        
        echo "Go with ₱299 PAID course using HYBRID delivery:\n";
        echo "• Email drip for lessons (MailerLite)\n";
        echo "• Facebook Group for community\n";
        echo "• YouTube unlisted videos\n\n";
        
        echo "Why this works:\n";
        echo "1. Low barrier (₱299) but filters serious students\n";
        echo "2. Creates buyers list for ₱2,997 coaching upsell\n";
        echo "3. Self-liquidating with Facebook ads\n";
        echo "4. Simple to set up and manage\n\n";
        
        echo "First milestone: 10 sales in launch week\n";
        echo "Second milestone: 100 students in 90 days\n";
        echo "Third milestone: 10 coaching upsells (₱30k additional)\n";
    }
}

// ============================================
// OUTPUT STRATEGY
// ============================================

$strategy = new PaidCourseStrategy();
$strategy->printStrategy();

?>
