<?php
/**
 * BOOK WRITING TIMELINE ESTIMATE
 * "The 1% Freelancer" - 27 chapters, 60-75k words
 */

class BookTimelineEstimate {
    
    /**
     * SCOPE BREAKDOWN
     */
    public function projectScope() {
        return [
            'total_chapters' => 27,
            'target_word_count' => '60,000 - 75,000 words',
            'average_chapter_length' => '2,200 - 2,800 words',
            'estimated_pages' => '240 - 300 pages (paperback)',
        ];
    }
    
    /**
     * WRITING PHASES & TIMELINE
     */
    public function writingPhases() {
        return [
            'phase_1_research_planning' => [
                'name' => 'Phase 1: Research & Planning',
                'duration' => '2-3 weeks',
                'tasks' => [
                    'Deep dive into Atomic Habits framework (study notes)',
                    'Interview 20-30 successful freelancers (case studies)',
                    'Research existing freelancing books (gap analysis)',
                    'Create detailed chapter outlines (27 chapters)',
                    'Build writing schedule and milestones',
                    'Set up writing environment and tools',
                ],
                'deliverable' => 'Complete book outline + research notes + interview transcripts',
            ],
            
            'phase_2_first_draft' => [
                'name' => 'Phase 2: First Draft',
                'duration' => '4-5 months',
                'daily_output' => '800-1,200 words/day (sustainable pace)',
                'weekly_output' => '5,000-7,000 words/week',
                'schedule' => [
                    'Part 1 (Ch 1-3): 3 weeks',
                    'Part 2 - Law 1 (Ch 4-6): 3 weeks',
                    'Part 2 - Law 2 (Ch 7-9): 3 weeks',
                    'Part 2 - Law 3 (Ch 10-12): 3 weeks',
                    'Part 2 - Law 4 (Ch 13-15): 3 weeks',
                    'Part 3 (Ch 16-20): 4 weeks',
                    'Part 4 (Ch 21-24): 3 weeks',
                    'Part 5 (Ch 25-27): 3 weeks',
                    'Buffer time': '2-3 weeks (for life/illness/slow days)',
                ],
                'challenges' => [
                    'Writer\'s block (inevitable)',
                    'Life interruptions',
                    'Research gaps requiring more interviews',
                    'Changing direction mid-book',
                ],
                'deliverable' => 'Complete first draft (60-75k words)',
            ],
            
            'phase_3_self_editing' => [
                'name' => 'Phase 3: Self-Editing',
                'duration' => '4-6 weeks',
                'passes' => [
                    'Pass 1: Structural edit (flow, order, big cuts) - 2 weeks',
                    'Pass 2: Chapter-by-chapter edit (clarity, examples) - 2 weeks',
                    'Pass 3: Line edit (sentences, word choice) - 1-2 weeks',
                ],
                'word_count_change' => '-10% to +5% (usually cuts)',
                'deliverable' => 'Second draft ready for beta readers',
            ],
            
            'phase_4_beta_reading' => [
                'name' => 'Phase 4: Beta Reading',
                'duration' => '3-4 weeks',
                'activities' => [
                    'Send to 10-15 beta readers (freelancers, coaches, target audience)',
                    'Wait for feedback (2-3 weeks)',
                    'Compile and analyze feedback',
                    'Identify major issues and fixes needed',
                ],
                'deliverable' => 'Feedback report + revision plan',
            ],
            
            'phase_5_revisions' => [
                'name' => 'Phase 5: Revisions',
                'duration' => '3-4 weeks',
                'activities' => [
                    'Address beta reader feedback',
                    'Add/delete chapters if needed',
                    'Strengthen weak sections',
                    'Add more case studies/examples',
                    'Final polish pass',
                ],
                'deliverable' => 'Third draft (final manuscript)',
            ],
            
            'phase_6_professional_edit' => [
                'name' => 'Phase 6: Professional Editing',
                'duration' => '6-8 weeks',
                'types' => [
                    'Developmental edit' => '3-4 weeks (if budget allows)',
                    'Copy edit' => '2-3 weeks (grammar, style)',
                    'Proofread' => '1 week (final errors)',
                ],
                'cost_estimate' => '₱50,000-150,000 ($1,000-3,000 USD)',
                'deliverable' => 'Publication-ready manuscript',
            ],
            
            'phase_7_final_polish' => [
                'name' => 'Phase 7: Final Polish',
                'duration' => '1-2 weeks',
                'activities' => [
                    'Final read-through',
                    'Table of contents finalization',
                    'Acknowledgments, about author',
                    'Reference checks',
                    'Formatting for submission',
                ],
                'deliverable' => 'Final manuscript ready for publishing',
            ],
        ];
    }
    
    /**
     * TOTAL TIMELINE SCENARIOS
     */
    public function timelineScenarios() {
        return [
            'aggressive_fast' => [
                'name' => 'AGGRESSIVE (Full-time writing, no delays)',
                'writing_schedule' => '6-8 hours/day, 6 days/week',
                'daily_word_count' => '1,500-2,000 words',
                'phases' => [
                    'Research & Planning' => '2 weeks',
                    'First Draft' => '3 months',
                    'Self-Editing' => '3 weeks',
                    'Beta Reading' => '3 weeks',
                    'Revisions' => '3 weeks',
                    'Professional Edit' => '6 weeks',
                    'Final Polish' => '1 week',
                ],
                'total_time' => '7-8 months',
                'realistic' => 'Only if: No day job, no family obligations, high discipline',
                'success_rate' => '20% (most burn out or hit obstacles)',
            ],
            
            'moderate_realistic' => [
                'name' => 'MODERATE (Part-time writing, steady progress)',
                'writing_schedule' => '2-3 hours/day, 5 days/week',
                'daily_word_count' => '600-800 words',
                'phases' => [
                    'Research & Planning' => '3 weeks',
                    'First Draft' => '5 months',
                    'Self-Editing' => '5 weeks',
                    'Beta Reading' => '4 weeks',
                    'Revisions' => '4 weeks',
                    'Professional Edit' => '8 weeks',
                    'Final Polish' => '2 weeks',
                ],
                'total_time' => '12-13 months',
                'realistic' => 'Most sustainable pace while keeping day job',
                'success_rate' => '70% (achievable with consistency)',
            ],
            
            'conservative_safe' => [
                'name' => 'CONSERVATIVE (Writing as side project)',
                'writing_schedule' => '1-2 hours/day, 4-5 days/week',
                'daily_word_count' => '300-500 words',
                'phases' => [
                    'Research & Planning' => '4 weeks',
                    'First Draft' => '8-10 months',
                    'Self-Editing' => '8 weeks',
                    'Beta Reading' => '6 weeks',
                    'Revisions' => '6 weeks',
                    'Professional Edit' => '10 weeks',
                    'Final Polish' => '2 weeks',
                ],
                'total_time' => '18-24 months',
                'realistic' => 'Very doable alongside full-time work',
                'success_rate' => '85% (low pressure, high completion)',
            ],
        ];
    }
    
    /**
     * MY REALISTIC ESTIMATE FOR ME
     */
    public function myRealisticEstimate() {
        return [
            'my_pace' => 'Moderate (as part of existing workflow)',
            'daily_capacity' => '1,500-2,000 words/day when focused',
            'effective_writing_days' => '4-5 days/week',
            'breakdown' => [
                'Phase 1 (Research)' => '2 weeks',
                'Phase 2 (First Draft)' => '3-4 months',
                'Phase 3 (Self-Edit)' => '4 weeks',
                'Phase 4 (Beta)' => '3 weeks',
                'Phase 5 (Revisions)' => '3 weeks',
                'Phase 6 (Pro Edit)' => '6-8 weeks (outsourced)',
                'Phase 7 (Final)' => '1 week',
            ],
            'total_estimate' => '8-10 months',
            'caveats' => [
                'Assumes consistent priority on this project',
                'No major life interruptions',
                'Your active collaboration on case studies/examples',
                'Professional editing outsourced (not me)',
            ],
            'if_prioritized' => 'Could compress to 6-7 months',
            'if_backburner' => 'Could stretch to 12+ months',
        ];
    }
    
    /**
     * COMPARISON: AI-ASSISTED WRITING
     */
    public function aiAssistedComparison() {
        return [
            'traditional_writing' => [
                'method' => 'Human writes every word',
                'first_draft_time' => '4-5 months',
                'quality' => 'Highest (personal voice, unique insights)',
                'authenticity' => '100%',
            ],
            'ai_assisted' => [
                'method' => 'Human outlines, AI expands, human edits heavily',
                'first_draft_time' => '2-3 months',
                'quality' => 'Good (needs heavy editing for voice)',
                'authenticity' => '60-70% (requires humanization)',
            ],
            'ai_heavy' => [
                'method' => 'AI writes most, human edits lightly',
                'first_draft_time' => '1-2 months',
                'quality' => 'Generic (sounds like every other book)',
                'authenticity' => '30-40%',
            ],
            'recommendation' => 'AI-assisted for speed, but heavy human editing for authenticity. Your personal stories and insights cannot be AI-generated.',
        ];
    }
    
    /**
     * RECOMMENDED APPROACH FOR SPEED + QUALITY
     */
    public function recommendedApproach() {
        return [
            'title' => 'RECOMMENDED: Hybrid Approach',
            'total_time' => '6-8 months',
            'method' => [
                'step_1' => [
                    'week' => 'Weeks 1-2',
                    'activity' => 'Deep planning and detailed chapter outlines',
                    'output' => '27 detailed chapter outlines (500-800 words each)',
                ],
                'step_2' => [
                    'week' => 'Weeks 3-14',
                    'activity' => 'Rapid first draft with AI assistance',
                    'method' => 'I draft key sections, use AI to expand explanations, examples, transitions',
                    'pace' => '2 chapters/week',
                ],
                'step_3' => [
                    'week' => 'Weeks 15-18',
                    'activity' => 'Heavy editing pass',
                    'method' => 'Humanize voice, add personal stories, strengthen frameworks',
                ],
                'step_4' => [
                    'week' => 'Weeks 19-22',
                    'activity' => 'Beta reading',
                    'method' => 'Send to 15 beta readers, collect feedback',
                ],
                'step_5' => [
                    'week' => 'Weeks 23-26',
                    'activity' => 'Revisions based on feedback',
                    'method' => 'Address issues, add case studies, polish',
                ],
                'step_6' => [
                    'week' => 'Weeks 27-34',
                    'activity' => 'Professional editing (outsourced)',
                    'method' => 'Developmental + copy edit + proofread',
                ],
                'step_7' => [
                    'week' => 'Weeks 35-36',
                    'activity' => 'Final polish and formatting',
                    'output' => 'Publication-ready manuscript',
                ],
            ],
            'advantages' => [
                'Faster than pure human writing (6-8 months vs 12-14 months)',
                'Maintains authentic voice and personal insights',
                'High quality through professional editing',
                'Sustainable pace without burnout',
            ],
        ];
    }
    
    /**
     * PRINT THE ESTIMATE
     */
    public function printEstimate() {
        $scope = $this->projectScope();
        echo "=== BOOK PROJECT SCOPE ===\n\n";
        foreach ($scope as $key => $value) {
            echo ucfirst(str_replace('_', ' ', $key)) . ": $value\n";
        }
        
        echo "\n\n" . str_repeat("=", 60) . "\n";
        echo "TIMELINE SCENARIOS\n";
        echo str_repeat("=", 60) . "\n\n";
        
        $scenarios = $this->timelineScenarios();
        foreach ($scenarios as $scenario) {
            echo "{$scenario['name']}\n";
            echo str_repeat("-", 40) . "\n";
            echo "Schedule: {$scenario['writing_schedule']}\n";
            echo "Daily Output: {$scenario['daily_word_count']}\n";
            echo "Total Time: {$scenario['total_time']}\n";
            echo "Realistic: {$scenario['realistic']}\n";
            echo "Success Rate: {$scenario['success_rate']}\n\n";
        }
        
        echo str_repeat("=", 60) . "\n";
        echo "MY REALISTIC ESTIMATE\n";
        echo str_repeat("=", 60) . "\n\n";
        
        $myEstimate = $this->myRealisticEstimate();
        echo "My Pace: {$myEstimate['my_pace']}\n";
        echo "Daily Capacity: {$myEstimate['daily_capacity']}\n";
        echo "Effective Days: {$myEstimate['effective_writing_days']}\n\n";
        
        echo "Phase Breakdown:\n";
        foreach ($myEstimate['breakdown'] as $phase => $time) {
            echo "  $phase: $time\n";
        }
        
        echo "\nTotal Estimate: {$myEstimate['total_estimate']}\n\n";
        
        echo "If Prioritized: {$myEstimate['if_prioritized']}\n";
        echo "If Backburner: {$myEstimate['if_backburner']}\n\n";
        
        echo "Caveats:\n";
        foreach ($myEstimate['caveats'] as $caveat) {
            echo "  • $caveat\n";
        }
        
        echo "\n\n" . str_repeat("=", 60) . "\n";
        echo "RECOMMENDED APPROACH\n";
        echo str_repeat("=", 60) . "\n\n";
        
        $recommended = $this->recommendedApproach();
        echo "{$recommended['title']}\n";
        echo "Total Time: {$recommended['total_time']}\n\n";
        
        foreach ($recommended['method'] as $step => $details) {
            echo "{$details['week']}: {$details['activity']}\n";
            if (isset($details['output'])) {
                echo "  Output: {$details['output']}\n";
            }
            if (isset($details['method'])) {
                echo "  Method: {$details['method']}\n";
            }
            if (isset($details['pace'])) {
                echo "  Pace: {$details['pace']}\n";
            }
            echo "\n";
        }
        
        echo "Advantages:\n";
        foreach ($recommended['advantages'] as $adv) {
            echo "  • $adv\n";
        }
        
        echo "\n\n=== BOTTOM LINE ===\n\n";
        echo "Pure human writing: 12-14 months\n";
        echo "AI-assisted (recommended): 6-8 months\n";
        echo "My commitment to you: 8-10 months realistic\n\n";
        
        echo "The book that gets finished beats the perfect book that never ships.\n";
    }
}

// ============================================
// OUTPUT
// ============================================

$estimate = new BookTimelineEstimate();
$estimate->printEstimate();

?>
