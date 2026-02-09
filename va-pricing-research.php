<?php
/**
 * VA Competitive Pricing Research Tool
 * Helps VAs research competitors and calculate competitive pricing
 */

class VAPricingResearch {
    
    // Market rate benchmarks (USD/hour)
    private $marketRates = [
        'entry_admin' => ['min' => 3, 'max' => 8, 'avg' => 5],
        'entry_social' => ['min' => 4, 'max' => 10, 'avg' => 6],
        'entry_data' => ['min' => 3, 'max' => 8, 'avg' => 5.5],
        'mid_admin' => ['min' => 8, 'max' => 15, 'avg' => 11],
        'mid_social' => ['min' => 10, 'max' => 18, 'avg' => 13],
        'mid_customer' => ['min' => 9, 'max' => 16, 'avg' => 12],
        'mid_email' => ['min' => 8, 'max' => 15, 'avg' => 11],
        'senior_automation' => ['min' => 15, 'max' => 30, 'avg' => 22],
        'senior_project' => ['min' => 18, 'max' => 35, 'avg' => 25],
        'senior_ecommerce' => ['min' => 15, 'max' => 30, 'avg' => 22],
        'specialist_ai' => ['min' => 20, 'max' => 50, 'avg' => 32],
        'specialist_marketing' => ['min' => 18, 'max' => 40, 'avg' => 28],
    ];
    
    // Monthly package benchmarks (USD/month)
    private $packageRates = [
        'starter' => ['hours' => 20, 'min' => 100, 'max' => 300, 'avg' => 200],
        'basic' => ['hours' => 40, 'min' => 250, 'max' => 600, 'avg' => 425],
        'standard' => ['hours' => 80, 'min' => 500, 'max' => 1200, 'avg' => 850],
        'premium' => ['hours' => 160, 'min' => 1000, 'max' => 2400, 'avg' => 1700],
        'full_time' => ['hours' => 160, 'min' => 1500, 'max' => 3500, 'avg' => 2500],
    ];
    
    private $competitors = [];
    
    /**
     * Add a competitor to research database
     */
    public function addCompetitor($name, $services, $hourlyRate, $packageRates = [], $location = 'unknown', $notes = '') {
        $this->competitors[] = [
            'name' => $name,
            'services' => is_array($services) ? $services : [$services],
            'hourly_rate' => $hourlyRate,
            'package_rates' => $packageRates,
            'location' => $location,
            'notes' => $notes,
            'added_date' => date('Y-m-d'),
        ];
        return true;
    }
    
    /**
     * Get market rate for a specific skill
     */
    public function getMarketRate($skill) {
        return $this->marketRates[$skill] ?? null;
    }
    
    /**
     * Calculate competitive hourly rate
     */
    public function calculateCompetitiveRate($skill, $experience, $location = 'philippines') {
        $baseRate = $this->marketRates[$skill]['avg'] ?? 10;
        
        // Experience multiplier
        $experienceMultipliers = [
            'beginner' => 0.7,
            'intermediate' => 1.0,
            'advanced' => 1.4,
            'expert' => 1.8,
        ];
        
        // Location adjustment (cost of living factor)
        $locationFactors = [
            'philippines' => 0.6,
            'india' => 0.5,
            'eastern_europe' => 0.8,
            'us_remote' => 1.2,
            'uk_remote' => 1.1,
            'western_europe' => 1.15,
        ];
        
        $expMult = $experienceMultipliers[$experience] ?? 1.0;
        $locFactor = $locationFactors[$location] ?? 0.6;
        
        $calculatedRate = $baseRate * $expMult * $locFactor;
        
        return [
            'base_rate' => $baseRate,
            'experience_multiplier' => $expMult,
            'location_factor' => $locFactor,
            'suggested_rate' => round($calculatedRate, 2),
            'competitive_range' => [
                'low' => round($calculatedRate * 0.85, 2),
                'high' => round($calculatedRate * 1.15, 2),
            ],
        ];
    }
    
    /**
     * Calculate monthly package pricing
     */
    public function calculatePackagePricing($tier, $hourlyRate, $customHours = null) {
        $basePackage = $this->packageRates[$tier] ?? null;
        
        if (!$basePackage) {
            return null;
        }
        
        $hours = $customHours ?? $basePackage['hours'];
        $hourlyTotal = $hours * $hourlyRate;
        
        // Package discount (more hours = more discount)
        $discountRates = [
            'starter' => 0.05,      // 5% discount
            'basic' => 0.08,        // 8% discount
            'standard' => 0.12,     // 12% discount
            'premium' => 0.15,      // 15% discount
            'full_time' => 0.20,    // 20% discount
        ];
        
        $discount = $discountRates[$tier] ?? 0.10;
        $packagePrice = $hourlyTotal * (1 - $discount);
        
        return [
            'tier' => $tier,
            'hours_included' => $hours,
            'hourly_rate' => $hourlyRate,
            'hourly_total_value' => $hourlyTotal,
            'package_discount' => round($discount * 100, 0) . '%',
            'suggested_price' => round($packagePrice, 0),
            'effective_hourly' => round($packagePrice / $hours, 2),
        ];
    }
    
    /**
     * Analyze competitors and suggest positioning
     */
    public function analyzeCompetition($targetSkill, $yourRate) {
        $marketRate = $this->marketRates[$targetSkill] ?? null;
        $relevantCompetitors = [];
        
        // Find competitors with similar services
        foreach ($this->competitors as $comp) {
            foreach ($comp['services'] as $service) {
                if (stripos($service, $targetSkill) !== false || stripos($targetSkill, $service) !== false) {
                    $relevantCompetitors[] = $comp;
                    break;
                }
            }
        }
        
        // Calculate average competitor rate
        $competitorRates = array_column($relevantCompetitors, 'hourly_rate');
        $avgCompetitorRate = !empty($competitorRates) ? array_sum($competitorRates) / count($competitorRates) : $marketRate['avg'] ?? 10;
        
        // Positioning analysis
        $rateDiff = $yourRate - $avgCompetitorRate;
        $rateDiffPercent = ($rateDiff / $avgCompetitorRate) * 100;
        
        if ($rateDiffPercent < -15) {
            $positioning = 'budget';
            $strategy = 'Emphasize value and efficiency. Consider raising prices gradually.';
        } elseif ($rateDiffPercent < 5) {
            $positioning = 'competitive';
            $strategy = 'Well positioned. Differentiate with specialization or added value.';
        } elseif ($rateDiffPercent < 25) {
            $positioning = 'premium';
            $strategy = 'Position as premium service. Highlight expertise and results.';
        } else {
            $positioning = 'luxury';
            $strategy = 'Requires strong portfolio and proven ROI. Target high-value clients only.';
        }
        
        return [
            'your_rate' => $yourRate,
            'market_average' => $marketRate['avg'] ?? null,
            'competitor_average' => round($avgCompetitorRate, 2),
            'rate_difference_percent' => round($rateDiffPercent, 1),
            'positioning' => $positioning,
            'strategy' => $strategy,
            'competitor_count' => count($relevantCompetitors),
        ];
    }
    
    /**
     * Generate pricing report
     */
    public function generateReport($targetSkills = [], $experience = 'intermediate', $location = 'philippines') {
        $report = [];
        
        foreach ($targetSkills as $skill) {
            $competitiveRate = $this->calculateCompetitiveRate($skill, $experience, $location);
            $packages = [];
            
            foreach (['starter', 'basic', 'standard', 'premium'] as $tier) {
                $packages[$tier] = $this->calculatePackagePricing($tier, $competitiveRate['suggested_rate']);
            }
            
            $report[$skill] = [
                'competitive_rate' => $competitiveRate,
                'package_options' => $packages,
            ];
        }
        
        return $report;
    }
    
    /**
     * Get all market rates
     */
    public function getAllMarketRates() {
        return $this->marketRates;
    }
    
    /**
     * Get all package benchmarks
     */
    public function getAllPackageRates() {
        return $this->packageRates;
    }
}

// ============================================
// USAGE EXAMPLES & DEMO
// ============================================

echo "=== VA COMPETITIVE PRICING RESEARCH TOOL ===\n\n";

$pricingTool = new VAPricingResearch();

// Example 1: Calculate competitive rate for different skills
echo "1. COMPETITIVE RATE CALCULATION\n";
echo "--------------------------------\n";

$skills = [
    ['skill' => 'entry_admin', 'exp' => 'beginner'],
    ['skill' => 'mid_social', 'exp' => 'intermediate'],
    ['skill' => 'senior_automation', 'exp' => 'advanced'],
];

foreach ($skills as $s) {
    $result = $pricingTool->calculateCompetitiveRate($s['skill'], $s['exp'], 'philippines');
    echo "\nSkill: {$s['skill']} | Experience: {$s['exp']}\n";
    echo "  Suggested Rate: \${$result['suggested_rate']}/hour\n";
    echo "  Range: \${$result['competitive_range']['low']} - \${$result['competitive_range']['high']}/hour\n";
}

// Example 2: Calculate package pricing
echo "\n\n2. PACKAGE PRICING CALCULATION\n";
echo "-------------------------------\n";

$hourlyRate = 12; // Example hourly rate
$packageTiers = ['starter', 'basic', 'standard', 'premium'];

foreach ($packageTiers as $tier) {
    $pkg = $pricingTool->calculatePackagePricing($tier, $hourlyRate);
    echo "\n{$tier} Package:\n";
    echo "  Hours: {$pkg['hours_included']} | Price: \${$pkg['suggested_price']}/mo\n";
    echo "  Effective hourly: \${$pkg['effective_hourly']}/hr ({$pkg['package_discount']} off)\n";
}

// Example 3: Add competitors and analyze
echo "\n\n3. COMPETITOR ANALYSIS\n";
echo "----------------------\n";

$pricingTool->addCompetitor(
    'VirtualHelper Pro',
    ['social media', 'admin support'],
    8,
    ['basic' => 280, 'standard' => 550],
    'philippines',
    'Strong social media focus, weak on automation'
);

$pricingTool->addCompetitor(
    'Elite VA Solutions',
    ['automation', 'project management'],
    25,
    ['premium' => 3500],
    'us_remote',
    'Premium positioning, niching in AI/automation'
);

$pricingTool->addCompetitor(
    'TaskMaster VA',
    ['data entry', 'admin support'],
    5,
    ['starter' => 120, 'basic' => 220],
    'india',
    'Budget option, high volume, lower quality'
);

// Analyze your position
echo "\n--- Competition Analysis for Automation Services ---\n";
$analysis = $pricingTool->analyzeCompetition('automation', 15);
echo "Your Rate: \${$analysis['your_rate']}/hour\n";
echo "Market Average: \${$analysis['market_average']}/hour\n";
echo "Competitor Average: \${$analysis['competitor_average']}/hour\n";
echo "Difference: {$analysis['rate_difference_percent']}%\n";
echo "Positioning: " . strtoupper($analysis['positioning']) . "\n";
echo "Strategy: {$analysis['strategy']}\n";

// Example 4: Full pricing report
echo "\n\n4. COMPLETE PRICING REPORT\n";
echo "--------------------------\n";

$report = $pricingTool->generateReport(
    ['mid_social', 'senior_automation'],
    'intermediate',
    'philippines'
);

foreach ($report as $skill => $data) {
    echo "\n=== " . strtoupper($skill) . " ===\n";
    echo "Suggested Hourly: \${$data['competitive_rate']['suggested_rate']}/hr\n";
    echo "Package Options:\n";
    foreach ($data['package_options'] as $tier => $pkg) {
        if ($pkg) {
            echo "  {$tier}: \${$pkg['suggested_price']}/mo ({$pkg['hours_included']} hrs)\n";
        }
    }
}

// Example 5: Market rate reference
echo "\n\n5. CURRENT MARKET RATES REFERENCE\n";
echo "----------------------------------\n";
$allRates = $pricingTool->getAllMarketRates();
foreach ($allRates as $skill => $rates) {
    printf("%-25s | Avg: \$%5.2f/hr | Range: \$%4.1f - \$%4.1f\n", 
        $skill, $rates['avg'], $rates['min'], $rates['max']);
}

echo "\n\n=== END OF REPORT ===\n";

?>
