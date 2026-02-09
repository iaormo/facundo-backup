<?php
/**
 * VA Pricing API - Simple JSON endpoints for pricing research
 * Usage: va-pricing-api.php?action=rate&skill=mid_social&exp=intermediate
 */

require_once 'va-pricing-research.php';

header('Content-Type: application/json');

$pricingTool = new VAPricingResearch();
$action = $_GET['action'] ?? 'help';

switch ($action) {
    case 'rate':
        // Get competitive rate
        // Params: skill, exp (beginner/intermediate/advanced/expert), location
        $skill = $_GET['skill'] ?? 'mid_admin';
        $exp = $_GET['exp'] ?? 'intermediate';
        $location = $_GET['location'] ?? 'philippines';
        
        echo json_encode([
            'success' => true,
            'data' => $pricingTool->calculateCompetitiveRate($skill, $exp, $location)
        ], JSON_PRETTY_PRINT);
        break;
        
    case 'package':
        // Calculate package pricing
        // Params: tier (starter/basic/standard/premium), hourly_rate
        $tier = $_GET['tier'] ?? 'basic';
        $hourly = floatval($_GET['hourly_rate'] ?? 10);
        
        echo json_encode([
            'success' => true,
            'data' => $pricingTool->calculatePackagePricing($tier, $hourly)
        ], JSON_PRETTY_PRINT);
        break;
        
    case 'market':
        // Get all market rates
        echo json_encode([
            'success' => true,
            'data' => $pricingTool->getAllMarketRates()
        ], JSON_PRETTY_PRINT);
        break;
        
    case 'analyze':
        // Analyze competition
        // Params: skill, your_rate
        $skill = $_GET['skill'] ?? 'mid_admin';
        $yourRate = floatval($_GET['your_rate'] ?? 10);
        
        echo json_encode([
            'success' => true,
            'data' => $pricingTool->analyzeCompetition($skill, $yourRate)
        ], JSON_PRETTY_PRINT);
        break;
        
    case 'report':
        // Full pricing report
        // Params: skills (comma-separated), exp, location
        $skillsStr = $_GET['skills'] ?? 'mid_admin,mid_social';
        $skills = explode(',', $skillsStr);
        $exp = $_GET['exp'] ?? 'intermediate';
        $location = $_GET['location'] ?? 'philippines';
        
        echo json_encode([
            'success' => true,
            'data' => $pricingTool->generateReport($skills, $exp, $location)
        ], JSON_PRETTY_PRINT);
        break;
        
    case 'help':
    default:
        echo json_encode([
            'success' => true,
            'message' => 'VA Pricing API',
            'endpoints' => [
                'rate' => '?action=rate&skill=mid_social&exp=intermediate&location=philippines',
                'package' => '?action=package&tier=basic&hourly_rate=12',
                'market' => '?action=market',
                'analyze' => '?action=analyze&skill=automation&your_rate=15',
                'report' => '?action=report&skills=mid_admin,mid_social&exp=intermediate',
            ],
            'skills' => array_keys($pricingTool->getAllMarketRates()),
            'experience_levels' => ['beginner', 'intermediate', 'advanced', 'expert'],
            'locations' => ['philippines', 'india', 'eastern_europe', 'us_remote', 'uk_remote', 'western_europe'],
        ], JSON_PRETTY_PRINT);
}
?>
