# How to Use PRD Generator

## Quick Start

**Simplest Invocation:**
```
Create a PRD for an AI-powered recommendation engine that helps e-commerce users discover relevant products
```

**With More Context:**
```
Generate a comprehensive PRD for a smart reply feature in our customer support tool that reduces agent response time
```

## Detailed Usage Examples

### Scenario 1: New AI Feature for Existing Product

**Context**: You're a PM at a SaaS company adding AI capabilities to an existing product.

**Invocation:**
```
I need a PRD for an AI-powered feature with these details:

Feature Name: Predictive Task Prioritization
Problem: Project managers waste 2 hours daily manually prioritizing tasks
Target Users: Project managers, team leads, executives
Business Goals:
- Reduce time spent on task prioritization by 60%
- Increase on-time project completion by 25%
- Improve resource utilization by 15%

Key Requirements:
- ML model that learns from historical project data
- Must integrate with existing project management tool
- Real-time predictions with < 1 second latency
- Explainable AI - show why tasks are prioritized certain way

Include full AI/ML specifications and ethical considerations.
```

**What You Get:**
- Complete PRD with 13+ sections
- RICE prioritization score calculated
- AI/ML specifications including model requirements, bias assessment, explainability
- User stories with acceptance criteria
- Risk assessment and mitigation strategies
- Phased launch plan

---

### Scenario 2: Responding to Competitive Threat

**Context**: Competitor launched a similar feature, you need to move fast with a differentiated approach.

**Invocation:**
```
Generate a PRD for our competitive response:

Feature: Real-time Collaboration with AI Assistance
Problem: Users struggle to collaborate on documents, competitors just launched basic co-editing
Target: 50,000 enterprise users
Business Impact: Retain at-risk customers, prevent 15% churn ($5M annual revenue)

Competitive Context:
- Competitor has basic co-editing
- We need AI-powered suggestions to differentiate
- Must launch within 3 months

Technical Constraints:
- Use existing infrastructure
- Support 100K concurrent users
- GDPR compliant

Prioritize speed to market while maintaining quality.
```

**What You Get:**
- Emphasis on competitive differentiation in problem statement
- Aggressive but achievable timeline in launch plan
- MVP scope clearly defined (MoSCoW prioritization)
- Risk assessment highlighting time-to-market risks
- Technical requirements optimized for speed

---

### Scenario 3: Internal Tool Development

**Context**: Building an internal tool to improve team productivity.

**Invocation:**
```
Create a PRD for internal tool:

Feature: Automated Meeting Notes with Action Items
Problem: Engineers lose 30 minutes per meeting on note-taking and follow-ups
Target Users: 200 engineers across 15 teams
Business Goals:
- Save 100 hours/week in engineering time
- Increase meeting effectiveness
- Improve accountability on action items

This is an internal tool, so:
- Focus on engineering-specific needs
- Lower bar for polish, higher bar for usefulness
- Integrate with Slack and Google Calendar
- Consider privacy concerns with recording meetings
```

**What You Get:**
- Internal tool considerations in executive summary
- Success metrics focused on time savings and adoption
- Privacy and consent requirements prominent in technical specs
- Simplified launch plan appropriate for internal tools
- Integration requirements with existing internal tools

---

### Scenario 4: Using Structured JSON Input

**Context**: You have detailed requirements already documented and want maximum customization.

**Invocation:**
```
Generate a PRD using this structured input:

[Paste JSON from sample_input.json]
```

**What You Get:**
- Most detailed and customized PRD
- All your specific metrics preserved
- Competitive landscape integrated throughout document
- User research findings woven into problem statement
- Custom AI/ML specifications based on your requirements

---

### Scenario 5: Iterative Refinement

**Context**: You've generated a PRD and want to refine specific sections.

**First Request:**
```
Create a PRD for a mobile app feature that uses computer vision to identify plants
```

**Refinement:**
```
The PRD looks good, but can you expand the AI/ML Specifications section to include:
- Model accuracy requirements for different plant types
- Handling of poor lighting conditions
- Edge cases like hybrid plants or damaged specimens
- Mobile-specific model optimization (size < 50MB)
```

**What You Get:**
- Expanded AI/ML section with specific details
- Updated risk assessment reflecting model complexity
- Modified technical requirements for mobile constraints

---

## Tips for Best Results

### 1. Be Specific About the Problem
❌ "Users want better recommendations"  
✅ "Users spend 15 minutes daily scrolling through irrelevant content, leading to 30% abandonment rate"

### 2. Provide Quantified Business Goals
❌ "Increase engagement"  
✅ "Increase daily active users by 20% and session duration by 35%"

### 3. Include User Research Context When Available
❌ No context  
✅ "Based on 20 user interviews, top pain point is..."

### 4. Specify Technical Constraints Upfront
❌ Let skill guess  
✅ "Must integrate with Salesforce API, support 10K concurrent users, < 200ms latency"

### 5. Clarify AI/ML Requirements for AI Features
❌ "Use AI for recommendations"  
✅ "Need collaborative filtering model with 85%+ accuracy, explainable suggestions, bias mitigation across demographics"

### 6. Indicate Urgency and Context
❌ Generic PRD  
✅ "Competitive response, need MVP in 6 weeks" or "Strategic initiative, can take 6 months for best-in-class solution"

---

## Combining with Other Skills

### Recommended Workflow for New Features

```
1. user-research-analyzer
   ↓ [Extract insights from interviews/surveys]
   
2. competitive-analyzer
   ↓ [Understand market positioning]
   
3. feature-prioritizer
   ↓ [Validate this feature should be built now]
   
4. prd-generator (THIS SKILL)
   ↓ [Create comprehensive PRD]
   
5. ai-ethics-assessor (if AI feature)
   ↓ [Evaluate ethical implications]
   
6. user-story-generator
   ↓ [Break down into development tickets]
   
7. stakeholder-communicator
   ↓ [Share PRD and get alignment]
```

### Using PRD Output with Other Skills

**After generating PRD, you can:**

1. **Extract user stories** → Feed to `user-story-generator` for detailed tickets
2. **Share with stakeholders** → Use `stakeholder-communicator` for different audiences
3. **Build metrics dashboard** → Use `metrics-dashboard-builder` with your success metrics
4. **Plan launch** → Enhance with `gtm-strategy-builder` for go-to-market strategy

---

## Common Pitfalls and How to Avoid Them

### Pitfall 1: "Generate PRD for feature X"
**Problem**: Too vague, results in generic PRD  
**Solution**: Add problem statement, target users, business goals

### Pitfall 2: Skipping User Research Context
**Problem**: PRD lacks depth and user insights  
**Solution**: Include summary of user research findings

### Pitfall 3: Not Specifying AI Requirements
**Problem**: AI/ML section is incomplete or generic  
**Solution**: Provide model type, data needs, performance targets

### Pitfall 4: Unrealistic Expectations
**Problem**: PRD promises features that can't be delivered  
**Solution**: Include technical constraints and effort estimates

### Pitfall 5: Forgetting to Update
**Problem**: PRD becomes stale as you learn more  
**Solution**: Treat PRD as living document, regenerate sections as needed

---

## Customization Options

### Adjusting Output Length

**For shorter PRD:**
```
Create a lean PRD (max 5 pages) for [feature] focusing only on: problem, success metrics, requirements, and risks
```

**For comprehensive PRD:**
```
Create a detailed enterprise PRD for [feature] including all sections, detailed user research integration, and extensive technical specifications
```

### Focusing on Specific Sections

```
From the PRD you created, expand the Technical Requirements section to include:
- Detailed API specifications
- Database schema requirements
- Security architecture
- Infrastructure scaling plan
```

### Adapting for Different Audiences

```
Modify this PRD for executive review - emphasize business impact, ROI, and strategic alignment. Keep technical details high-level.
```

---

## Troubleshooting

### Issue: PRD is too generic
**Solution**: Provide more specific inputs, especially user research and competitive context

### Issue: RICE score seems off
**Solution**: Verify your reach, impact, confidence, and effort estimates are realistic

### Issue: Missing AI/ML section
**Solution**: Explicitly include `ai_ml_requirements` in your input or mention it's an AI feature

### Issue: Technical requirements too vague
**Solution**: Specify your tech stack and constraints in the initial request

### Issue: Success metrics aren't SMART
**Solution**: Provide baseline metrics and specific targets with timelines

---

## Examples of Good Inputs

### Example 1: B2B SaaS Feature
```json
{
  "feature_name": "Usage Analytics Dashboard",
  "problem_statement": "Customers don't understand product usage patterns, leading to underutilization and 22% higher churn",
  "target_users": ["Customer success managers", "Account executives", "End users"],
  "business_goals": [
    "Reduce churn from 18% to 12%",
    "Increase feature adoption by 40%",
    "Drive upsells through usage insights"
  ]
}
```

### Example 2: Consumer Mobile App
```json
{
  "feature_name": "Personalized Workout Recommendations",
  "problem_statement": "Users abandon fitness apps after 2 weeks due to generic workout plans that don't match their goals or fitness level",
  "target_users": ["Fitness beginners", "Intermediate gym-goers"],
  "business_goals": [
    "Increase 30-day retention from 35% to 55%",
    "Grow premium conversions by 25%"
  ],
  "ai_ml_requirements": {
    "model_type": "Recommendation engine with collaborative filtering",
    "accuracy_target": "80%",
    "latency_target": "< 1 second"
  }
}
```

---

## Next Steps After PRD Creation

1. **Review with stakeholders** - Get feedback from engineering, design, data science
2. **Refine estimates** - Work with engineering for effort estimates
3. **Create technical design doc** - Engineering translates PRD into technical spec
4. **Generate user stories** - Use `user-story-generator` skill
5. **Build prototype** - Create low-fidelity mockups
6. **Validate with users** - Test assumptions before building
7. **Update PRD** - Incorporate learnings from validation

---

## Getting Help

If you need assistance:
- Check `SKILL.md` for detailed documentation
- Review `sample_input.json` for input format examples
- Examine `expected_output.json` to see what structure to expect
- Open an issue if you find bugs or have feature requests

---

**Remember**: A great PRD answers "why" before "what," and "what" before "how." Use this skill to focus on the problem and impact, let engineering figure out the implementation details.
