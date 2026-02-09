<?php
/**
 * PAID EBOOK vs FREE LEAD MAGNET STRATEGY
 * Analysis of selling the checklist vs giving it away
 */

class EbookStrategyAnalysis {
    
    /**
     * OPTION 1: Sell as ₱99-149 Ebook (Paid)
     */
    public function paidEbookOption() {
        return [
            'title' => 'OPTION 1: Sell as Paid Ebook (₱99-149)',
            'positioning' => 'Low-ticket "tripwire" product',
            
            'pros' => [
                [
                    'point' => 'Immediate revenue',
                    'explanation' => 'Every sale puts money in your pocket right away. Even ₱99 x 50 sales = ₱4,950.',
                ],
                [
                    'point' => 'Higher quality leads',
                    'explanation' => 'People who pay even a small amount are more committed than free downloaders.',
                ],
                [
                    'point' => 'Self-liquidating ads',
                    'explanation' => '₱99 price can cover Facebook ad costs to acquire customers.',
                ],
                [
                    'point' => 'Creates buyers list',
                    'explanation' => 'People who buy ₱99 are much more likely to buy ₱299 course than free leads.',
                ],
                [
                    'point' => 'Tests market demand',
                    'explanation' => 'If people pay ₱99, you know the topic has real demand.',
                ],
            ],
            
            'cons' => [
                [
                    'point' => 'Much lower volume',
                    'explanation' => 'You might get 50-100 sales instead of 500-1000 free downloads.',
                ],
                [
                    'point' => 'Harder to build email list',
                    'explanation' => 'List grows slower. Less people to market your course to.',
                ],
                [
                    'point' => 'Higher expectations',
                    'explanation' => 'Paid customers expect more support and content than free downloaders.',
                ],
                [
                    'point' => 'More complex delivery',
                    'explanation' => 'Need proper checkout, instant download, customer service.',
                ],
                [
                    'point' => 'Less viral potential',
                    'explanation' => 'People share free stuff, not paid stuff. Less organic reach.',
                ],
            ],
            
            'when_this_works' => 'If you need immediate cash flow OR if you want to validate the market before building a bigger course.',
        ];
    }
    
    /**
     * OPTION 2: Give Free, Sell Course (Recommended)
     */
    public function freeLeadMagnetOption() {
        return [
            'title' => 'OPTION 2: Free Checklist + ₱299 Course (RECOMMENDED)',
            'positioning' => 'Free lead magnet → Paid course funnel',
            
            'pros' => [
                [
                    'point' => 'Massive list building',
                    'explanation' => '500-1000+ downloads vs 50-100 sales. Bigger pool for course sales.',
                ],
                [
                    'point' => 'Course is the main offer',
                    'explanation' => 'Checklist builds trust. Course solves the problem. Natural progression.',
                ],
                [
                    'point' => 'Easier to promote',
                    'explanation' => '"Free checklist" gets more clicks than "₱99 ebook" in ads and posts.',
                ],
                [
                    'point' => 'Viral potential',
                    'explanation' => 'People share free resources. Organic growth from shares.',
                ],
                [
                    'point' => 'Positions you as giver',
                    'explanation' => 'Free value first builds trust before asking for sale.',
                ],
                [
                    'point' => 'Better for course conversion',
                    'explanation' => 'People who consume 30 days of emails are HOT leads for course.',
                ],
            ],
            
            'cons' => [
                [
                    'point' => 'No immediate revenue from checklist',
                    'explanation' => 'You make ₱0 until someone buys the course.',
                ],
                [
                    'point' => 'List has freebie seekers',
                    'explanation' => 'Some people will never buy. Lower quality than paid list.',
                ],
                [
                    'point' => 'Requires patience',
                    'explanation' => 'Takes time to build list before course revenue comes in.',
                ],
            ],
            
            'when_this_works' => 'If you want to build a sustainable business with multiple products and a loyal audience.',
        ];
    }
    
    /**
     * OPTION 3: Hybrid (Best of Both)
     */
    public function hybridOption() {
        return [
            'title' => 'OPTION 3: HYBRID (Advanced Strategy)',
            'positioning' => 'Free mini-version + Paid full ebook + Course',
            
            'funnel_structure' => [
                'step_1' => [
                    'offer' => 'FREE: "7-Day Quick Start Checklist" (condensed version)',
                    'pages' => '3-4 pages',
                    'content' => 'Week 1 only (Days 1-7)',
                    'goal' => 'Build large email list fast',
                ],
                'step_2' => [
                    'offer' => 'PAID: "Complete 30-Day Remote Work Blueprint" (₱149)',
                    'pages' => '40-50 pages',
                    'content' => 'Full ebook with detailed explanations, templates, examples',
                    'delivery' => 'Immediate upsell after free opt-in OR promoted in email sequence',
                    'goal' => 'Tripwire revenue + filter serious buyers',
                ],
                'step_3' => [
                    'offer' => 'PAID: "Zero to Remote Course" (₱299)',
                    'content' => 'Video lessons, community, additional support',
                    'goal' => 'Core offer for committed students',
                ],
                'step_4' => [
                    'offer' => 'PAID: "1-on-1 Coaching" (₱2,997)',
                    'content' => 'Personal guidance and accountability',
                    'goal' => 'High-ticket revenue',
                ],
            ],
            
            'why_this_works' => [
                'Free version builds massive list (top of funnel)',
                'Paid ebook generates revenue + creates buyers list (mid funnel)',
                'Course is main offer for serious students (core offer)',
                'Coaching is premium offer for committed clients (high ticket)',
                'Multiple price points capture different commitment levels',
            ],
            
            'the_math' => [
                '1000 free downloads' => '₱0 but 1000 email subscribers',
                '100 ebook sales (10% of free)' => '₱14,900 revenue + 100 buyers',
                '30 course sales (30% of ebook buyers)' => '₱8,970 revenue',
                '5 coaching sales (15% of course buyers)' => '₱14,985 revenue',
                'total' => '₱38,855 + 1000 person email list',
            ],
        ];
    }
    
    /**
     * COMPARISON TABLE
     */
    public function comparisonTable() {
        return [
            'metrics' => [
                ['Metric', 'Free Checklist', 'Paid Ebook (₱99)', 'Hybrid'],
                ['Download/Sales Volume', '500-1000', '50-100', '1000 free + 100 paid'],
                ['Immediate Revenue', '₱0', '₱4,950-9,900', '₱14,900'],
                ['Email List Growth', 'Fast (500-1000)', 'Slow (50-100)', 'Fast (1000)'],
                ['Course Conversion Rate', '3-5%', '15-25%', '20-30% (from ebook buyers)'],
                ['Customer Quality', 'Mixed', 'High', 'Segmented'],
                ['Setup Complexity', 'Low', 'Medium', 'High'],
                ['Best For', 'Building audience', 'Quick cash', 'Sustainable business'],
            ],
        ];
    }
    
    /**
     * MY RECOMMENDATION FOR YOUR SITUATION
     */
    public function myRecommendation() {
        return [
            'situation' => [
                'you_have' => 'A ₱299 course ready (or nearly ready)',
                'you_want' => 'To build a VA coaching business',
                'goal' => 'Sustainable recurring revenue + coaching clients',
            ],
            
            'recommendation' => 'Go with OPTION 2: Free Checklist + ₱299 Course',
            
            'reasoning' => [
                [
                    'point' => 'Your course is ready to sell now',
                    'explanation' => 'Do not delay course launch to create a paid ebook. The course is your main offer.',
                ],
                [
                    'point' => 'You need a list to sell the course',
                    'explanation' => 'Free checklist builds that list faster than paid ebook.',
                ],
                [
                    'point' => '₱299 is already low-ticket',
                    'explanation' => 'Adding ₱99 ebook before ₱299 course complicates the funnel unnecessarily.',
                ],
                [
                    'point' => 'Course has higher value than ebook',
                    'explanation' => 'Videos + community is worth ₱299. An ebook alone is not.',
                ],
                [
                    'point' => 'You can add ebook later',
                    'explanation' => 'Start simple. Add paid ebook as upsell once course is selling.',
                ],
            ],
            
            'if_you_still_want_to_sell_something' => [
                'option_a' => 'Create a MORE detailed ebook (40-50 pages) for ₱149 as an upsell AFTER the free checklist',
                'option_b' => 'Add templates/workbook as ₱99 add-on to the course',
                'option_c' => 'Bundle: Course + Ebook for ₱349 (save ₱50)',
            ],
            
            'action_plan' => [
                'week_1' => 'Create free 10-page checklist',
                'week_2' => 'Set up landing page + email sequence',
                'week_3' => 'Launch checklist, build list',
                'week_4' => 'Launch ₱299 course to new list',
                'month_2' => 'Create paid ebook (40-50 pages) as upsell',
            ],
        ];
    }
    
    /**
     * IF YOU DO WANT TO SELL THE EBOOK
     */
    public function ebookIfYouSellIt() {
        return [
            'title' => 'IF YOU SELL THE EBOOK: What to Add',
            'base_price' => '₱99-149',
            
            'what_to_add_to_justify_price' => [
                'Expand from 10 pages to 40-50 pages',
                'Add detailed explanations (not just bullet points)',
                'Include real examples and case studies',
                'Add scripts and templates they can copy-paste',
                'Include screenshots and visual guides',
                'Add "Day 0" prep chapter (mindset, savings plan)',
                'Add troubleshooting section (common problems)',
                'Add resource directory (tools, websites, groups)',
                'Make it professionally designed (Canva)',
                'Add author section (your story and credentials)',
            ],
            
            'sample_chapters' => [
                'Chapter 1: Why Remote Work is Possible for You',
                'Chapter 2: The Mindset Shift (Employee to Freelancer)',
                'Chapter 3: Finding Your Marketable Skill',
                'Chapter 4: Building Your Online Presence',
                'Chapter 5: Creating Your Portfolio',
                'Chapter 6: Application Templates That Work',
                'Chapter 7: Handling Discovery Calls',
                'Chapter 8: Pricing Your Services',
                'Chapter 9: Your First Week with a Client',
                'Chapter 10: Scaling to Full-Time Income',
                'Appendix: Tools, Templates, Resources',
            ],
            
            'delivery' => [
                'Format' => 'PDF (professionally designed)',
                'Pages' => '40-60 pages',
                'Bonus' => 'Include worksheets as separate PDFs',
                'Instant delivery' => 'Via email after payment',
                'Platform' => 'Gumroad, PayPal, or simple GCash + manual email',
            ],
            
            'upsell_to_course' => [
                'strategy' => 'Ebook teaches WHAT to do, Course teaches HOW with video walkthroughs',
                'email_sequence' => 'After ebook purchase, send 5 emails pitching the ₱299 course',
                'conversion_expectation' => '20-30% of ebook buyers will buy the course',
                'example_math' => '100 ebook sales @ ₱149 = ₱14,900. 25 buy course @ ₱299 = ₱7,475. Total = ₱22,375.',
            ],
        ];
    }
    
    /**
     * PRINT ANALYSIS
     */
    public function printAnalysis() {
        echo "=== PAID EBOOK vs FREE LEAD MAGNET ===\n\n";
        
        // Option 1
        $paid = $this->paidEbookOption();
        echo "{$paid['title']}\n";
        echo str_repeat("-", 50) . "\n\n";
        
        echo "PROS:\n";
        foreach ($paid['pros'] as $pro) {
            echo "✓ {$pro['point']}\n";
            echo "  {$pro['explanation']}\n\n";
        }
        
        echo "CONS:\n";
        foreach ($paid['cons'] as $con) {
            echo "✗ {$con['point']}\n";
            echo "  {$con['explanation']}\n\n";
        }
        
        echo "Best for: {$paid['when_this_works']}\n\n";
        
        echo str_repeat("=", 60) . "\n\n";
        
        // Option 2
        $free = $this->freeLeadMagnetOption();
        echo "{$free['title']}\n";
        echo str_repeat("-", 50) . "\n\n";
        
        echo "PROS:\n";
        foreach ($free['pros'] as $pro) {
            echo "✓ {$pro['point']}\n";
            echo "  {$pro['explanation']}\n\n";
        }
        
        echo "CONS:\n";
        foreach ($free['cons'] as $con) {
            echo "✗ {$con['point']}\n";
            echo "  {$con['explanation']}\n\n";
        }
        
        echo "Best for: {$free['when_this_works']}\n\n";
        
        // Comparison
        $compare = $this->comparisonTable();
        echo str_repeat("=", 60) . "\n";
        echo "COMPARISON TABLE\n";
        echo str_repeat("=", 60) . "\n\n";
        
        foreach ($compare['metrics'] as $row) {
            printf("%-25s | %-15s | %-15s | %-15s\n", $row[0], $row[1], $row[2], $row[3]);
        }
        
        // My recommendation
        echo "\n\n" . str_repeat("=", 60) . "\n";
        echo "MY RECOMMENDATION\n";
        echo str_repeat("=", 60) . "\n\n";
        
        $rec = $this->myRecommendation();
        echo "Your Situation:\n";
        foreach ($rec['situation'] as $key => $value) {
            echo "  $key: $value\n";
        }
        
        echo "\n{$rec['recommendation']}\n\n";
        
        echo "Why:\n";
        foreach ($rec['reasoning'] as $reason) {
            echo "→ {$reason['point']}\n";
            echo "  {$reason['explanation']}\n\n";
        }
        
        echo "Action Plan:\n";
        foreach ($rec['action_plan'] as $period => $task) {
            echo "  $period: $task\n";
        }
        
        // Ebook details
        echo "\n\n" . str_repeat("=", 60) . "\n";
        $ebook = $this->ebookIfYouSellIt();
        echo "{$ebook['title']}\n";
        echo str_repeat("=", 60) . "\n\n";
        
        echo "To justify ₱99-149 price, add:\n";
        foreach ($ebook['what_to_add_to_justify_price'] as $item) {
            echo "  • $item\n";
        }
    }
}

// ============================================
// OUTPUT
// ============================================

$analysis = new EbookStrategyAnalysis();
$analysis->printAnalysis();

?>
