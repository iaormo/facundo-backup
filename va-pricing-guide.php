<?php
/**
 * VA Pricing Research - Quick Reference Guide
 * This file shows how to use the pricing tool with practical examples
 */

require_once 'va-pricing-research.php';

$tool = new VAPricingResearch();

echo "=== VA PRICING QUICK REFERENCE ===\n\n";

// =====================================================
// SCENARIO 1: New VA figuring out starting rate
// =====================================================
echo "SCENARIO 1: New VA (Beginner, Admin Support)\n";
echo "---------------------------------------------\n";
$newVA = $tool->calculateCompetitiveRate('entry_admin', 'beginner', 'philippines');
echo "Suggested Starting Rate: \${$newVA['suggested_rate']}/hour\n";
echo "Acceptable Range: \${$newVA['competitive_range']['low']} - \${$newVA['competitive_range']['high']}/hour\n";
echo "Strategy: Start at lower end, raise \$1 after 3 successful clients\n\n";

// =====================================================
// SCENARIO 2: Experienced VA with specialization
// =====================================================
echo "SCENARIO 2: Social Media VA (2+ years experience)\n";
echo "--------------------------------------------------\n";
$socialVA = $tool->calculateCompetitiveRate('mid_social', 'intermediate', 'philippines');
echo "Suggested Rate: \${$socialVA['suggested_rate']}/hour\n";
echo "Monthly Packages:\n";
foreach (['starter', 'basic', 'standard'] as $tier) {
    $pkg = $tool->calculatePackagePricing($tier, $socialVA['suggested_rate']);
    echo "  {$tier}: \${$pkg['suggested_price']}/mo ({$pkg['hours_included']} hrs)\n";
}
echo "\n";

// =====================================================
// SCENARIO 3: Premium automation specialist
// =====================================================
echo "SCENARIO 3: Automation Specialist (Advanced Skills)\n";
echo "----------------------------------------------------\n";
$autoVA = $tool->calculateCompetitiveRate('senior_automation', 'advanced', 'philippines');
echo "Suggested Rate: \${$autoVA['suggested_rate']}/hour\n";
echo "Note: At this level, consider value-based pricing over hourly\n";
echo "Example project rates: \$500-2000 per automation setup\n\n";

// =====================================================
// SCENARIO 4: Price comparison for client proposal
// =====================================================
echo "SCENARIO 4: Client Wants 40hrs/week Package\n";
echo "-------------------------------------------\n";
$hourlyRate = 10;
$standardPkg = $tool->calculatePackagePricing('standard', $hourlyRate);
echo "At \${$hourlyRate}/hour x 80 hrs = \$800 value\n";
echo "With 12% package discount: \${$standardPkg['suggested_price']}/mo\n";
echo "Effective hourly: \${$standardPkg['effective_hourly']}/hr\n";
echo "Client saves: \$" . (800 - $standardPkg['suggested_price']) . "/mo\n\n";

// =====================================================
// COMPETITIVE POSITIONING GUIDE
// =====================================================
echo "=== COMPETITIVE POSITIONING GUIDE ===\n\n";

echo "BUDGET Positioning (< 15% below market avg):\n";
echo "  - Target: Price-sensitive clients, startups\n";
echo "  - Strategy: Emphasize value, efficiency, reliability\n";
echo "  - Risk: Race to bottom, attract difficult clients\n\n";

echo "COMPETITIVE Positioning (within 5% of market):\n";
echo "  - Target: Most small businesses\n";
echo "  - Strategy: Differentiate with specialization, testimonials\n";
echo "  - Sweet spot for most VAs\n\n";

echo "PREMIUM Positioning (15-25% above market):\n";
echo "  - Target: Established businesses, high-value clients\n";
echo "  - Strategy: Results-focused, ROI-driven, case studies\n";
echo "  - Requires: Strong portfolio, proven track record\n\n";

echo "LUXURY Positioning (>25% above market):\n";
echo "  - Target: Enterprise, high-ticket clients only\n";
echo "  - Strategy: White-glove service, exclusivity\n";
echo "  - Requires: 5+ years experience, elite portfolio\n\n";

// =====================================================
// PRICING ESCALATION PATH
// =====================================================
echo "=== SUGGESTED PRICING ESCALATION ===\n\n";
echo "Month 1-3: Entry rate to build portfolio\n";
echo "Month 4-6: Raise 20-30% after testimonials\n";
echo "Month 7-12: Move to mid-level pricing\n";
echo "Year 2+: Specialist/premium rates with niche focus\n\n";

echo "=== KEY INSIGHT ===\n";
echo "Philippines VAs can price 40-60% below US rates\n";
echo "while still earning well locally. Focus on:\n";
echo "  1. Specialization (pays 2-3x general admin)\n";
echo "  2. Value-based pricing for projects\n";
echo "  3. Retainers over one-off tasks\n";
?>
