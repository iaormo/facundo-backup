<?php
/**
 * VA Competitive Pricing Research Tool - PHILIPPINE PESO VERSION
 * Helps Filipino VAs research local competitors and calculate competitive PHP pricing
 */

class VAPricingResearchPH {
    
    // USD to PHP conversion rate (update as needed)
    private $usdToPhp = 58;
    
    // Philippine VA market rates (PHP/hour) - based on local market research
    private $marketRates = [
        // Entry Level (0-1 year experience)
        'entry_admin' => ['min' => 50, 'max' => 120, 'avg' => 75, 'level' => 'entry'],
        'entry_social' => ['min' => 60, 'max' => 150, 'avg' => 85, 'level' => 'entry'],
        'entry_data' => ['min' => 50, 'max' => 110, 'avg' => 70, 'level' => 'entry'],
        'entry_email' => ['min' => 55, 'max' => 130, 'avg' => 80, 'level' => 'entry'],
        
        // Mid Level (1-3 years experience)
        'mid_admin' => ['min' => 120, 'max' => 250, 'avg' => 175, 'level' => 'mid'],
        'mid_social' => ['min' => 150, 'max' => 300, 'avg' => 200, 'level' => 'mid'],
        'mid_customer' => ['min' => 130, 'max' => 280, 'avg' => 180, 'level' => 'mid'],
        'mid_email' => ['min' => 120, 'max' => 250, 'avg' => 170, 'level' => 'mid'],
        'mid_content' => ['min' => 150, 'max' => 350, 'avg' => 220, 'level' => 'mid'],
        
        // Senior Level (3+ years experience)
        'senior_automation' => ['min' => 300, 'max' => 600, 'avg' => 450, 'level' => 'senior'],
        'senior_project' => ['min' => 350, 'max' => 700, 'avg' => 500, 'level' => 'senior'],
        'senior_ecommerce' => ['min' => 300, 'max' => 600, 'avg' => 450, 'level' => 'senior'],
        'senior_social' => ['min' => 250, 'max' => 550, 'avg' => 400, 'level' => 'senior'],
        
        // Specialist/Niche (Expert level)
        'specialist_ai' => ['min' => 400, 'max' => 1000, 'avg' => 650, 'level' => 'specialist'],
        'specialist_marketing' => ['min' => 350, 'max' => 800, 'avg' => 550, 'level' => 'specialist'],
        'specialist_crm' => ['min' => 350, 'max' => 750, 'avg' => 500, 'level' => 'specialist'],
    ];
    
    // Monthly package benchmarks (PHP/month) - Philippine market
    private $packageRates = [
        'starter' => [
            'hours' => 20, 
            'min' => 1500, 
            'max' => 3500, 
            'avg' => 2500,
            'description' => 'Part-time support for small tasks'
        ],
        'basic' => [
            'hours' => 40, 
            'min' => 4000, 
            'max' => 9000, 
            'avg' => 6500,
            'description' => 'Regular part-time support'
        ],
        'standard' => [
            'hours' => 80, 
            'min' => 10000, 
            'max' => 20000, 
            'avg' => 15000,
            'description' => 'Half-time dedicated support'
        ],
        'premium' => [
            'hours' => 120, 
            'min' => 18000, 
            'max' => 35000, 
            'avg' => 28000,
            'description' => 'Near full-time support'
        ],
        'full_time' => [
            'hours' => 160, 
            'min' => 25000, 
            'max' => 50000, 
            'avg' => 38000,
            'description' => 'Full-time dedicated VA'
        ],
    ];
    
    // Known Philippine VA competitors and market data
    private $competitors = [];
    
    // Platform fee structures
    private $platformFees = [
        'direct' => 0,           // Direct client, no platform
        'onlinejobs' => 0,       // Free for VA, client pays
        'upwork' => 0.20,        // 20% then 10%
        'fiverr' => 0.20,        // 20% platform fee
        'belay' => 0,            // Negotiated
        'fancyhands' => 0,       // They set rates
        'taskbullet' => 0,       // Agency model
    ];
    
    public function __construct() {
        $this->loadPhilippineCompetitors();
    }
    
    /**
     * Load Philippine VA market competitor data
     */
    private function loadPhilippineCompetitors() {
        // VA Agencies in Philippines
        $this->competitors = [
            [
                'name' => 'TaskBullet Philippines',
                'type' => 'agency',
                'services' => ['admin', 'social media', 'email management'],
                'hourly_rate' => 120,
                'package_20hr' => 4500,
                'package_40hr' => 8500,
                'package_80hr' => 16000,
                'location' => 'Philippines',
                'target_clients' => 'US small businesses',
                'strengths' => ['trained VAs', 'backup coverage', 'time zone matching'],
                'weaknesses' => ['higher rates', 'less personal'],
            ],
            [
                'name' => 'Philippine Virtual Assistants (PVA)',
                'type' => 'agency',
                'services' => ['general admin', 'real estate', 'ecommerce'],
                'hourly_rate' => 150,
                'package_40hr' => 10000,
                'package_80hr' => 18000,
                'location' => 'Philippines',
                'target_clients' => 'Real estate agents, ecommerce owners',
                'strengths' => ['industry specialization', 'trained VAs'],
                'weaknesses' => ['premium pricing'],
            ],
            [
                'name' => 'Filipino VAs on Upwork',
                'type' => 'platform_aggregate',
                'services' => ['various'],
                'hourly_rate_low' => 50,
                'hourly_rate_high' => 400,
                'hourly_rate_avg' => 150,
                'location' => 'Philippines',
                'target_clients' => 'Global clients',
                'strengths' => ['wide range', 'ratings visible', 'competition drives quality'],
                'weaknesses' => ['platform fees', 'race to bottom on pricing'],
            ],
            [
                'name' => 'OnlineJobs.ph VAs',
                'type' => 'platform_aggregate',
                'services' => ['various'],
                'hourly_rate_low' => 40,
                'hourly_rate_high' => 300,
                'hourly_rate_avg' => 120,
                'location' => 'Philippines',
                'target_clients' => 'US entrepreneurs, small businesses',
                'strengths' => ['no platform fees', 'direct hire', 'large talent pool'],
                'weaknesses' => ['vetting required', 'no escrow protection'],
            ],
            [
                'name' => 'Virtual Coworker',
                'type' => 'agency',
                'services' => ['admin', 'customer service', 'marketing'],
                'hourly_rate' => 180,
                'package_40hr' => 12000,
                'location' => 'Philippines/Australia',
                'target_clients' => 'Australian businesses',
                'strengths' => ['established agency', 'quality screening'],
                'weaknesses' => ['higher rates', 'less flexibility'],
            ],
        ];
    }
    
    /**
     * Calculate competitive hourly rate for Philippine market
     */
    public function calculateCompetitiveRate($skill, $experience, $strategy = 'market_rate') {
        $baseRate = $this->marketRates[$skill]['avg'] ?? 150;
        
        // Experience multipliers
        $experienceMultipliers = [
            'beginner' => 0.7,
            'intermediate' => 1.0,
            'advanced' => 1.3,
            'expert' => 1.6,
        ];
        
        // Pricing strategy adjustments
        $strategyFactors = [
            'budget' => 0.75,        // 25% below market - for gaining first clients
            'market_rate' => 1.0,     // Standard market rate
            'premium' => 1.25,        // 25% above - for specialized skills
            'aggressive_low' => 0.60, // 40% below - for breaking in
        ];
        
        $expMult = $experienceMultipliers[$experience] ?? 1.0;
        $stratFactor = $strategyFactors[$strategy] ?? 1.0;
        
        $calculatedRate = $baseRate * $expMult * $stratFactor;
        $marketRate = $this->marketRates[$skill];
        
        return [
            'skill' => $skill,
            'base_market_rate' => $baseRate,
            'experience_level' => $experience,
            'experience_multiplier' => $expMult,
            'pricing_strategy' => $strategy,
            'strategy_factor' => $stratFactor,
            'suggested_rate' => round($calculatedRate, 0),
            'market_range' => [
                'low' => $marketRate['min'],
                'high' => $marketRate['max'],
            ],
            'competitive_range' => [
                'low' => max(round($calculatedRate * 0.9, 0), $marketRate['min']),
                'high' => min(round($calculatedRate * 1.1, 0), $marketRate['max'] * 1.2),
            ],
            'usd_equivalent' => round($calculatedRate / $this->usdToPhp, 2),
            'monthly_40hr' => round($calculatedRate * 40 * 4, 0),
            'monthly_80hr' => round($calculatedRate * 80 * 4, 0),
            'monthly_160hr' => round($calculatedRate * 160 * 4, 0),
        ];
    }
    
    /**
     * Calculate package pricing in PHP
     */
    public function calculatePackagePricing($tier, $hourlyRate, $customHours = null) {
        $basePackage = $this->packageRates[$tier] ?? null;
        
        if (!$basePackage) {
            return null;
        }
        
        $hours = $customHours ?? $basePackage['hours'];
        $hourlyTotal = $hours * $hourlyRate * 4; // Monthly (4 weeks)
        
        // Package discounts
        $discountRates = [
            'starter' => 0.05,
            'basic' => 0.08,
            'standard' => 0.12,
            'premium' => 0.15,
            'full_time' => 0.20,
        ];
        
        $discount = $discountRates[$tier] ?? 0.10;
        $packagePrice = $hourlyTotal * (1 - $discount);
        
        // Ensure price is within market bounds
        $packagePrice = max($packagePrice, $basePackage['min']);
        $packagePrice = min($packagePrice, $basePackage['max'] * 1.2);
        
        return [
            'tier' => $tier,
            'description' => $basePackage['description'],
            'hours_per_week' => $hours,
            'hours_per_month' => $hours * 4,
            'hourly_rate_input' => $hourlyRate,
            'calculated_monthly_value' => $hourlyTotal,
            'package_discount' => round($discount * 100, 0) . '%',
            'suggested_price_php' => round($packagePrice / 50) * 50, // Round to nearest 50
            'effective_hourly_php' => round($packagePrice / ($hours * 4), 0),
            'effective_hourly_usd' => round(($packagePrice / ($hours * 4)) / $this->usdToPhp, 2),
            'market_comparison' => $this->compareToMarket($tier, $packagePrice),
        ];
    }
    
    /**
     * Compare package price to market
     */
    private function compareToMarket($tier, $price) {
        $market = $this->packageRates[$tier];
        $avg = $market['avg'];
        $diff = (($price - $avg) / $avg) * 100;
        
        if ($diff < -20) return 'significantly_below_market';
        if ($diff < -5) return 'below_market';
        if ($diff < 10) return 'market_rate';
        if ($diff < 25) return 'above_market';
        return 'premium';
    }
    
    /**
     * Analyze Philippine competition
     */
    public function analyzePhilippineCompetition($yourRate, $yourServices = []) {
        $competitorRates = [];
        $avgAgencyRate = 0;
        $avgFreelanceRate = 0;
        $agencyCount = 0;
        $freelanceCount = 0;
        
        foreach ($this->competitors as $comp) {
            if (isset($comp['hourly_rate'])) {
                $competitorRates[] = $comp['hourly_rate'];
                if ($comp['type'] === 'agency') {
                    $avgAgencyRate += $comp['hourly_rate'];
                    $agencyCount++;
                }
            }
            if (isset($comp['hourly_rate_avg'])) {
                $avgFreelanceRate += $comp['hourly_rate_avg'];
                $freelanceCount++;
            }
        }
        
        $avgAgencyRate = $agencyCount > 0 ? $avgAgencyRate / $agencyCount : 0;
        $avgFreelanceRate = $freelanceCount > 0 ? $avgFreelanceRate / $freelanceCount : 0;
        $overallAvg = array_sum($competitorRates) / count($competitorRates);
        
        $rateDiff = (($yourRate - $overallAvg) / $overallAvg) * 100;
        
        // Determine positioning
        if ($yourRate < $avgFreelanceRate * 0.8) {
            $positioning = 'budget_freelancer';
            $strategy = 'Focus on volume, quick wins. Ideal for building portfolio fast.';
        } elseif ($yourRate < $avgAgencyRate) {
            $positioning = 'independent_value';
            $strategy = 'Position between agencies and cheap freelancers. Emphasize personal service.';
        } elseif ($yourRate < $avgAgencyRate * 1.2) {
            $positioning = 'near_agency';
            $strategy = 'Compete with agencies by offering similar quality at lower overhead.';
        } else {
            $positioning = 'specialist';
            $strategy = 'Premium positioning. Requires specialized skills and strong portfolio.';
        }
        
        return [
            'your_rate_php' => $yourRate,
            'your_rate_usd' => round($yourRate / $this->usdToPhp, 2),
            'market_averages' => [
                'agency_average_php' => round($avgAgencyRate, 0),
                'freelance_average_php' => round($avgFreelanceRate, 0),
                'overall_average_php' => round($overallAvg, 0),
            ],
            'rate_difference_percent' => round($rateDiff, 1),
            'positioning' => $positioning,
            'recommended_strategy' => $strategy,
            'competitors_analyzed' => count($this->competitors),
        ];
    }
    
    /**
     * Get low-price entry strategies
     */
    public function getLowerPricingStrategies() {
        return [
            [
                'name' => 'Introductory Rate',
                'description' => 'Start 30% below market for first 3 clients, then raise gradually',
                'discount' => 0.30,
                'duration' => '3 months or 3 clients',
                'pros' => ['Fast client acquisition', 'Quick testimonials'],
                'cons' => ['Lower initial income', 'Must raise prices later'],
                'best_for' => 'Complete beginners with no portfolio',
            ],
            [
                'name' => 'Portfolio Builder',
                'description' => 'Offer first 2 weeks free or 50% off in exchange for case study rights',
                'discount' => 0.50,
                'duration' => 'First 2 weeks',
                'pros' => ['Powerful testimonials', 'Real work samples'],
                'cons' => ['No pay initially', 'Risk of tire kickers'],
                'best_for' => 'Those with skills but no proof',
            ],
            [
                'name' => 'Package Deal',
                'description' => 'Bundle services at lower per-task rate (e.g. 10 hours pre-paid)',
                'discount' => 0.15,
                'duration' => 'Ongoing',
                'pros' => ['Guaranteed income', 'Client commitment'],
                'cons' => ['Locked in rate', 'Cash flow timing'],
                'best_for' => 'Building recurring revenue',
            ],
            [
                'name' => 'Referral Rate',
                'description' => 'Give existing clients discount for successful referrals',
                'discount' => 0.10,
                'duration' => 'Per referral',
                'pros' => ['Organic growth', 'Warm leads'],
                'cons' => ['Reduced margin', 'Dependency on clients'],
                'best_for' => 'Established VAs looking to grow',
            ],
            [
                'name' => 'Off-Peak Discount',
                'description' => 'Lower rates for work done during PH daytime (US night)',
                'discount' => 0.20,
                'duration' => 'Ongoing',
                'pros' => ['Fill empty hours', 'Still competitive globally'],
                'cons' => ['Odd hours', 'Not ideal for client calls'],
                'best_for' => 'VAs with flexible schedules',
            ],
        ];
    }
    
    /**
     * Calculate take-home after platform fees
     */
    public function calculateTakeHome($grossRate, $platform = 'direct', $hoursPerMonth = 160) {
        $feeRate = $this->platformFees[$platform] ?? 0;
        $feeAmount = $grossRate * $feeRate;
        $netRate = $grossRate - $feeAmount;
        $monthlyGross = $grossRate * $hoursPerMonth;
        $monthlyNet = $netRate * $hoursPerMonth;
        
        return [
            'platform' => $platform,
            'gross_hourly_php' => $grossRate,
            'platform_fee_percent' => ($feeRate * 100) . '%',
            'platform_fee_php' => $feeAmount,
            'net_hourly_php' => $netRate,
            'monthly_gross_php' => $monthlyGross,
            'monthly_net_php' => $monthlyNet,
            'effective_yearly_php' => $monthlyNet * 12,
        ];
    }
    
    /**
     * Generate complete pricing report
     */
    public function generatePricingReport($targetSkills = [], $experience = 'beginner', $strategy = 'budget') {
        $report = [
            'generated_at' => date('Y-m-d H:i:s'),
            'exchange_rate' => $this->usdToPhp . ' PHP per 1 USD',
            'skills_analysis' => [],
            'package_options' => [],
            'competition_analysis' => null,
            'strategies' => $this->getLowerPricingStrategies(),
        ];
        
        foreach ($targetSkills as $skill) {
            $rateData = $this->calculateCompetitiveRate($skill, $experience, $strategy);
            
            $packages = [];
            foreach (['starter', 'basic', 'standard', 'premium'] as $tier) {
                $packages[$tier] = $this->calculatePackagePricing($tier, $rateData['suggested_rate']);
            }
            
            $report['skills_analysis'][$skill] = [
                'rate_data' => $rateData,
                'packages' => $packages,
            ];
        }
        
        // Use first skill for competition analysis
        if (!empty($targetSkills)) {
            $firstRate = $report['skills_analysis'][$targetSkills[0]]['rate_data']['suggested_rate'];
            $report['competition_analysis'] = $this->analyzePhilippineCompetition($firstRate);
        }
        
        return $report;
    }
    
    /**
     * Print formatted report
     */
    public function printReport($report) {
        echo "========================================\n";
        echo "  VA PRICING REPORT - PHILIPPINES\n";
        echo "  Generated: {$report['generated_at']}\n";
        echo "  Rate: {$report['exchange_rate']}\n";
        echo "========================================\n\n";
        
        foreach ($report['skills_analysis'] as $skill => $data) {
            echo "--- SKILL: " . strtoupper($skill) . " ---\n";
            $rate = $data['rate_data'];
            echo "Suggested Rate: ₱{$rate['suggested_rate']}/hr (\${$rate['usd_equivalent']})\n";
            echo "Market Range: ₱{$rate['market_range']['low']} - ₱{$rate['market_range']['high']}/hr\n";
            echo "Monthly Income (40hrs): ₱{$rate['monthly_40hr']}\n";
            echo "Monthly Income (80hrs): ₱{$rate['monthly_80hr']}\n";
            echo "Monthly Income (160hrs): ₱{$rate['monthly_160hr']}\n\n";
            
            echo "Package Options:\n";
            foreach ($data['packages'] as $tier => $pkg) {
                if ($pkg) {
                    echo "  {$tier}: ₱{$pkg['suggested_price_php']}/mo | {$pkg['hours_per_week']}hrs/wk | ";
                    echo "Effective: ₱{$pkg['effective_hourly_php']}/hr\n";
                }
            }
            echo "\n";
        }
        
        if ($report['competition_analysis']) {
            $comp = $report['competition_analysis'];
            echo "--- COMPETITION ANALYSIS ---\n";
            echo "Your Rate: ₱{$comp['your_rate_php']}/hr\n";
            echo "Agency Average: ₱{$comp['market_averages']['agency_average_php']}/hr\n";
            echo "Freelance Average: ₱{$comp['market_averages']['freelance_average_php']}/hr\n";
            echo "Difference: {$comp['rate_difference_percent']}%\n";
            echo "Positioning: {$comp['positioning']}\n";
            echo "Strategy: {$comp['recommended_strategy']}\n\n";
        }
        
        echo "--- LOWER PRICING STRATEGIES ---\n";
        foreach ($report['strategies'] as $strat) {
            echo "\n{$strat['name']}:\n";
            echo "  Discount: " . ($strat['discount'] * 100) . "%\n";
            echo "  Duration: {$strat['duration']}\n";
            echo "  Best for: {$strat['best_for']}\n";
        }
    }
}

// ============================================
// DEMO / USAGE EXAMPLES
// ============================================

echo "=== VA COMPETITIVE PRICING TOOL - PHILIPPINE MARKET ===\n\n";

$pricing = new VAPricingResearchPH();

// Example 1: Calculate rates for different skill levels
echo "1. COMPETITIVE RATE CALCULATOR\n";
echo "================================\n\n";

$testCases = [
    ['skill' => 'entry_admin', 'exp' => 'beginner', 'strategy' => 'budget'],
    ['skill' => 'mid_social', 'exp' => 'intermediate', 'strategy' => 'market_rate'],
    ['skill' => 'senior_automation', 'exp' => 'advanced', 'strategy' => 'premium'],
];

foreach ($testCases as $case) {
    $result = $pricing->calculateCompetitiveRate($case['skill'], $case['exp'], $case['strategy']);
    echo "Skill: {$case['skill']} | Exp: {$case['exp']} | Strategy: {$case['strategy']}\n";
    echo "  → Suggested: ₱{$result['suggested_rate']}/hr (\${$result['usd_equivalent']})\n";
    echo "  → Range: ₱{$result['competitive_range']['low']} - ₱{$result['competitive_range']['high']}/hr\n";
    echo "  → Monthly (160hrs): ₱{$result['monthly_160hr']}\n\n";
}

// Example 2: Package pricing
echo "2. PACKAGE PRICING (at ₱150/hr)\n";
echo "================================\n\n";

$hourlyRate = 150;
$tierNames = ['starter', 'basic', 'standard', 'premium'];

foreach ($tierNames as $tier) {
    $pkg = $pricing->calculatePackagePricing($tier, $hourlyRate);
    echo strtoupper($tier) . " PACKAGE:\n";
    echo "  Price: ₱{$pkg['suggested_price_php']}/month\n";
    echo "  Hours: {$pkg['hours_per_week']}/week ({$pkg['hours_per_month']}/month)\n";
    echo "  Effective hourly: ₱{$pkg['effective_hourly_php']} (\${$pkg['effective_hourly_usd']})\n";
    echo "  Market position: {$pkg['market_comparison']}\n\n";
}

// Example 3: Competition analysis
echo "3. PHILIPPINE COMPETITION ANALYSIS\n";
echo "===================================\n\n";

$yourRate = 120; // Example rate
$analysis = $pricing->analyzePhilippineCompetition($yourRate);

echo "Your Rate: ₱{$analysis['your_rate_php']}/hr (\${$analysis['your_rate_usd']})\n";
echo "vs Agency Average: ₱{$analysis['market_averages']['agency_average_php']}/hr\n";
echo "vs Freelance Average: ₱{$analysis['market_averages']['freelance_average_php']}/hr\n";
echo "Difference: {$analysis['rate_difference_percent']}% from market average\n";
echo "Positioning: {$analysis['positioning']}\n";
echo "Strategy: {$analysis['recommended_strategy']}\n\n";

// Example 4: Platform comparison
echo "4. PLATFORM FEE COMPARISON (₱150/hr, 160hrs/mo)\n";
echo "================================================\n\n";

$platforms = ['direct', 'upwork', 'fiverr', 'onlinejobs'];
foreach ($platforms as $platform) {
    $takeHome = $pricing->calculateTakeHome(150, $platform, 160);
    echo strtoupper($platform) . ":\n";
    echo "  Gross: ₱{$takeHome['monthly_gross_php']}/mo\n";
    echo "  Fee: {$takeHome['platform_fee_percent']}\n";
    echo "  Net: ₱{$takeHome['monthly_net_php']}/mo\n";
    echo "  Yearly: ₱{$takeHome['effective_yearly_php']}\n\n";
}

// Example 5: Lower pricing strategies
echo "5. LOWER PRICING STRATEGIES FOR ENTRY\n";
echo "======================================\n\n";

$strategies = $pricing->getLowerPricingStrategies();
foreach ($strategies as $strat) {
    echo "→ {$strat['name']} ({$strat['discount']})\n";
    echo "  {$strat['description']}\n";
    echo "  Best for: {$strat['best_for']}\n";
    echo "  Pros: " . implode(', ', $strat['pros']) . "\n";
    echo "  Cons: " . implode(', ', $strat['cons']) . "\n\n";
}

// Example 6: Full report generation
echo "6. COMPLETE PRICING REPORT\n";
echo "==========================\n\n";

$fullReport = $pricing->generatePricingReport(
    ['entry_admin', 'mid_social', 'senior_automation'],
    'intermediate',
    'market_rate'
);

$pricing->printReport($fullReport);

echo "\n\n=== END OF REPORT ===\n";

?>
