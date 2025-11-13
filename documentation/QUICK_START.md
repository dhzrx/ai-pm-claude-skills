# Quick Start Guide: AI PM Skills Repository

Welcome to the AI PM Skills Repository! This guide will help you get started using Claude Skills to supercharge your product management workflow.

## Table of Contents

1. [What Are Claude Skills?](#what-are-claude-skills)
2. [Installation & Setup](#installation--setup)
3. [Your First Skill](#your-first-skill)
4. [Common Workflows](#common-workflows)
5. [Next Steps](#next-steps)

---

## What Are Claude Skills?

Claude Skills are specialized capabilities that teach Claude how to perform specific PM tasks. Think of them as expert consultants you can invoke anytime:

- **PRD Generator**: Create comprehensive product requirement documents
- **Feature Prioritizer**: Use RICE/ICE to rank your backlog
- **User Research Analyzer**: Extract insights from interviews
- **Competitive Analyzer**: Track competitors and identify gaps
- **AI Ethics Assessor**: Evaluate AI features for bias and fairness

Each skill is:
- ✅ **Production-ready**: Used by real PMs at real companies
- ✅ **Composable**: Skills work together in workflows
- ✅ **Customizable**: Fork and adapt to your processes
- ✅ **Portable**: Works on Claude.ai, Claude Code, and API

---

## Installation & Setup

### Option 1: Claude AI Desktop (Easiest)

1. **Download a skill** from the `skills/` directory
2. **Find the `.zip` file** in the skill folder
3. **Open Claude AI Desktop**
4. **Go to Settings → Skills**
5. **Click "Import Skill"** and select the `.zip` file
6. **Done!** The skill is now available

### Option 2: Claude Code (For Developers)

```bash
# Copy skill folder to Claude Code skills directory
cp -r skills/prd-generator ~/.claude/skills/

# Verify installation
ls ~/.claude/skills/
```

### Option 3: Claude API (For Teams)

```python
# Upload skill via API
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

with open("skills/prd-generator/prd-generator.zip", "rb") as f:
    skill = client.skills.create(
        name="prd-generator",
        file=f
    )
```

---

## Your First Skill

Let's start with the **PRD Generator** - one of the most useful skills for PMs.

### Step 1: Install the Skill

Follow the installation steps above for your platform.

### Step 2: Invoke the Skill

Open a conversation with Claude and try this:

```
Create a PRD for an AI-powered recommendation feature that helps users discover relevant content. 

Key details:
- Target users: Content creators and marketers
- Problem: Users spend too much time manually curating content
- Business goal: Increase engagement by 25%
- Timeline: Launch in Q1 2026
```

### Step 3: Review the Output

Claude will generate a comprehensive PRD including:
- ✅ Executive summary
- ✅ Problem statement (using JTBD framework)
- ✅ Success metrics
- ✅ User stories with acceptance criteria
- ✅ Technical requirements
- ✅ AI/ML specifications
- ✅ Risk assessment
- ✅ Launch plan

### Step 4: Iterate

Refine specific sections:

```
Can you expand the AI/ML Specifications section to include:
- Specific model accuracy targets
- Data quality requirements
- Bias mitigation strategies
```

---

## Common Workflows

### Workflow 1: New Feature Development

**Goal**: Take a feature idea from concept to specification

**Steps**:
```
1. User Research Analyzer
   → Analyze user interviews to validate problem
   
2. Competitive Analyzer
   → Understand market landscape
   
3. Feature Prioritizer
   → Validate this feature should be built now
   
4. PRD Generator
   → Create detailed specification
   
5. Stakeholder Communicator
   → Share with team and get buy-in
```

**Example Invocation**:
```
I have 10 user interview transcripts about our search feature. 
Can you analyze them to extract key themes and pain points?

[After analysis]

Based on these insights, help me prioritize our top 5 feature ideas 
using RICE scoring.

[After prioritization]

Generate a PRD for the top-ranked feature: AI-powered search suggestions.
```

---

### Workflow 2: Quarterly Planning

**Goal**: Build a data-driven Q1 roadmap

**Steps**:
```
1. User Research Analyzer
   → Synthesize recent user feedback
   
2. Feature Prioritizer
   → Score entire backlog using RICE
   
3. Roadmap Planner
   → Create visual quarterly roadmap
   
4. Metrics Dashboard Builder
   → Define success metrics for each initiative
   
5. Stakeholder Communicator
   → Create executive presentation
```

**Example Invocation**:
```
I need to plan Q1 2026. Here's my feature backlog:

[List 10-15 features with reach, impact, effort estimates]

Company priorities:
- 60% focus on user growth
- 30% focus on retention
- 10% focus on monetization

Constraint: 20 person-months of engineering capacity

Generate RICE scores, recommend Q1 roadmap, and create exec summary.
```

---

### Workflow 3: AI Feature Evaluation

**Goal**: Responsibly launch an AI-powered feature

**Steps**:
```
1. Competitive Analyzer
   → See how competitors handle AI features
   
2. AI Ethics Assessor
   → Evaluate bias, fairness, privacy concerns
   
3. PRD Generator (with AI/ML focus)
   → Document requirements including ethics
   
4. Metrics Dashboard Builder
   → Define AI-specific metrics (accuracy, fairness, etc.)
   
5. GTM Strategy Builder
   → Plan transparent communication about AI
```

**Example Invocation**:
```
I'm building an AI-powered hiring assistant that screens resumes. 

First, assess potential ethical issues:
- Bias risks across demographics
- Privacy concerns with candidate data
- Transparency requirements
- Regulatory compliance (GDPR, EEOC)

Then create a PRD that addresses these concerns comprehensively.
```

---

### Workflow 4: Stakeholder Alignment

**Goal**: Get executive buy-in for strategic initiative

**Steps**:
```
1. PRD Generator
   → Create comprehensive specification
   
2. Feature Prioritizer
   → Justify with RICE scoring
   
3. Competitive Analyzer
   → Show market opportunity
   
4. Metrics Dashboard Builder
   → Define clear success criteria
   
5. Stakeholder Communicator
   → Create exec-friendly presentation
```

**Example Invocation**:
```
I need to convince the CEO to invest in rebuilding our mobile app.

Generate:
1. PRD for "Native Mobile App Rebuild"
2. RICE score comparison vs. other initiatives
3. Competitive analysis showing we're falling behind
4. Success metrics tied to revenue and retention
5. Executive summary (1-page) with recommendation

Make it compelling but data-driven.
```

---

## Common Invocation Patterns

### Pattern 1: Simple Request
```
Create a PRD for [feature name]
```
**Best for**: Quick drafts, early exploration

### Pattern 2: Detailed Context
```
Generate a PRD for [feature] that solves [problem] for [users].
Business goals: [goals]
Constraints: [constraints]
```
**Best for**: Production-ready documents

### Pattern 3: Structured JSON
```
Generate a PRD using this input:
{
  "feature_name": "...",
  "problem_statement": "...",
  "target_users": [...],
  "business_goals": [...],
  ...
}
```
**Best for**: Maximum customization, batch processing

### Pattern 4: Iterative Refinement
```
[Initial request]

Great! Now expand the [section name] to include [specifics]

Also add [additional requirement]
```
**Best for**: Perfecting documents, learning

---

## Tips for Success

### 1. Start Simple, Then Add Detail
❌ Don't: Provide 10 pages of context upfront  
✅ Do: Start with basics, refine iteratively

### 2. Use Real Data
❌ Don't: "Increase engagement"  
✅ Do: "Increase DAU from 50K to 65K in 3 months"

### 3. Provide Context
❌ Don't: "Create PRD for search feature"  
✅ Do: "Create PRD for AI-powered search that reduces time-to-find from 5min to 30sec for enterprise users"

### 4. Leverage Skill Composition
❌ Don't: Ask one skill to do everything  
✅ Do: Chain skills in logical workflows

### 5. Iterate on Outputs
❌ Don't: Accept first draft  
✅ Do: Refine sections, add details, adjust tone

### 6. Customize for Your Process
❌ Don't: Use skills as-is forever  
✅ Do: Fork skills, modify templates, add company-specific sections

---

## Troubleshooting

### Problem: Skill not found
**Solution**: 
- Verify skill is installed correctly
- Check file paths match expected structure
- Restart Claude application

### Problem: Output is too generic
**Solution**:
- Provide more specific input
- Include user research context
- Add competitive landscape
- Specify constraints

### Problem: Metrics don't make sense
**Solution**:
- Review your reach/impact/effort estimates
- Ensure units are consistent
- Validate with team before using

### Problem: Skills don't work together
**Solution**:
- Check the `Composition with Other Skills` section in each SKILL.md
- Follow recommended workflows
- Pass structured outputs between skills

---

## Next Steps

### For First-Time Users
1. ✅ Install 2-3 skills you'll use most
2. ✅ Try each skill with a real PM task
3. ✅ Review `HOW_TO_USE.md` for detailed examples
4. ✅ Read `BEST_PRACTICES.md` for PM-specific guidance

### For Regular Users
1. Explore advanced workflows in `examples/sample-workflows/`
2. Customize skills for your company's processes
3. Create your own skills using `templates/AI_PM_SKILLS_FACTORY.md`
4. Share learnings with your team

### For Teams
1. Standardize on core skills across PM team
2. Create company-specific skills for your processes
3. Build skills library in shared knowledge base
4. Train new PMs on skill-based workflows

---

## Getting Help

### Documentation
- **Skill Details**: Read `SKILL.md` in each skill folder
- **Usage Examples**: Check `HOW_TO_USE.md` for detailed scenarios
- **Best Practices**: See `documentation/BEST_PRACTICES.md`

### Community
- **Issues**: Report bugs or request features
- **Discussions**: Share workflows and tips
- **Contributing**: Add your own skills

### Support
- Claude Documentation: https://docs.claude.com
- Skills Marketplace: https://github.com/anthropics/skills

---

## What's Next?

Now that you've got the basics, explore these resources:

1. **`documentation/BEST_PRACTICES.md`** - AI PM-specific guidance
2. **`documentation/USE_CASES.md`** - Real-world examples
3. **`examples/sample-workflows/`** - End-to-end workflows
4. **`templates/AI_PM_SKILLS_FACTORY.md`** - Generate custom skills

Ready to transform your PM workflow? Start with a skill that addresses your biggest pain point today!

---

**Happy Building! 🚀**
