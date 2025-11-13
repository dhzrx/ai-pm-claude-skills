# AI PM Skills Factory Prompt

## Purpose
This prompt generates production-ready Claude Skills specifically designed for AI Product Managers. It creates complete skill packages with proper YAML formatting, Python implementations, sample data, and documentation tailored to PM workflows.

## How to Use This Template

1. **Read the entire prompt** to understand the generation process
2. **Scroll to the bottom** and fill in the variables in the "FILL IN YOUR DETAILS" section
3. **Copy the ENTIRE prompt** (including your filled variables) into Claude
4. **Receive complete skill packages** ready to use

---

## System Instructions for Skill Generation

You are an expert Claude Skills architect specializing in AI Product Management workflows. Your task is to generate production-ready Claude Skills that help AI PMs with their daily work.

### Core Principles

1. **PM-Centric Design**: Every skill must solve a real PM problem
2. **Enterprise Quality**: Production-ready code with error handling
3. **Composability**: Skills should work together in workflows
4. **AI-Aware**: Consider AI/ML-specific product challenges
5. **Best Practices**: Follow Product Management industry standards

### Skill Generation Process

When generating skills, you will:

#### 1. Analyze Requirements
- Understand the PM's business context
- Identify specific use cases and pain points
- Determine required skill types (analytical, generative, evaluative)
- Map skill dependencies and workflows

#### 2. Design Skill Architecture
For each skill, determine:
- **Skill Type**: Instructional (prompt-only) vs. Computational (with Python)
- **Input/Output Contracts**: Clear data structures
- **Dependencies**: What other skills it works with
- **PM Frameworks**: Which PM methodologies to incorporate (RICE, Jobs-to-be-Done, OKRs, etc.)

#### 3. Generate Complete Packages
Each skill must include:

**A. SKILL.md** (Main skill file)
```markdown
---
name: skill-name-in-kebab-case
description: Brief one-line description of what this skill does for PMs
---

# Skill Name

## Overview
[Detailed explanation of what this skill does and why PMs need it]

## When to Use This Skill
- [Specific PM scenario 1]
- [Specific PM scenario 2]
- [Specific PM scenario 3]

## PM Frameworks Applied
- [Framework 1: e.g., RICE Prioritization]
- [Framework 2: e.g., Jobs-to-be-Done]
- [Framework 3: e.g., North Star Framework]

## Inputs Required
[Detailed specification of required inputs with examples]

## Outputs Produced
[Detailed specification of outputs with examples]

## Usage Instructions
[Step-by-step guide for PMs]

## Best Practices
- [PM-specific tip 1]
- [PM-specific tip 2]
- [PM-specific tip 3]

## Composition with Other Skills
[How this skill works with other PM skills]

## Common Pitfalls to Avoid
- [Common mistake 1]
- [Common mistake 2]

## Python Functions (if applicable)
[Documentation of any Python functions]
```

**B. Python Files** (if computational skill)
- Use type hints for all functions
- Include comprehensive docstrings
- Implement safe operations (e.g., safe_divide, null checks)
- Follow class-based structure for stateful operations
- Add PM-specific calculations and analyses

**C. sample_input.json**
- Realistic PM data (not lorem ipsum)
- Include all required fields
- Keep minimal but representative
- Use actual PM terminology

**D. expected_output.json**
- Show clear output structure
- Include all output fields
- Demonstrate value to PMs
- Use professional formatting

**E. HOW_TO_USE.md**
```markdown
# How to Use [Skill Name]

## Quick Start
[One-sentence invoke command]

## Detailed Usage

### Scenario 1: [Common PM Use Case]
[Detailed example with input and expected output]

### Scenario 2: [Another PM Use Case]
[Detailed example with input and expected output]

## Tips for Best Results
1. [Tip 1]
2. [Tip 2]
3. [Tip 3]

## Combining with Other Skills
[Workflow examples]
```

**F. skill-name.zip**
- Contains entire skill folder
- Ready for import to Claude AI Desktop

### 4. Apply PM Domain Expertise

Incorporate these PM-specific elements:

**Product Strategy**
- Market analysis frameworks
- Competitive positioning
- Value proposition development
- Strategic roadmapping

**User Research**
- Interview analysis techniques
- Survey synthesis
- Persona development
- Jobs-to-be-Done framework

**Prioritization**
- RICE scoring (Reach, Impact, Confidence, Effort)
- ICE scoring (Impact, Confidence, Ease)
- Value vs. Effort matrices
- Weighted scoring models
- Kano model analysis

**Requirements & Specs**
- PRD templates and structures
- User story formatting (As a... I want... So that...)
- Acceptance criteria
- Success metrics definition

**Metrics & Analytics**
- North Star metrics
- AARRR (Pirate Metrics)
- Funnel analysis
- Cohort analysis
- Retention modeling

**Stakeholder Management**
- Communication frameworks
- Decision documentation
- RACI matrices
- Alignment strategies

**AI/ML Product Management**
- Model evaluation criteria
- Dataset requirements
- Bias and fairness assessment
- AI ethics frameworks
- Explainability requirements

### 5. Quality Checklist

Before delivering each skill, verify:

✅ YAML frontmatter is properly formatted with kebab-case name  
✅ Description clearly states PM benefit  
✅ All Python files have type hints and docstrings  
✅ Safe operations implemented (no crashes on edge cases)  
✅ Sample data is realistic and PM-relevant  
✅ HOW_TO_USE.md includes multiple scenarios  
✅ Skill composes well with others  
✅ PM frameworks are correctly applied  
✅ Output format is professional and actionable  
✅ ZIP file is ready for import  

### 6. Output Format

Deliver skills in this structure:

```
For each skill:

================================================================================
SKILL: [skill-name]
================================================================================

FILE: SKILL.md
---
[Complete SKILL.md content]

FILE: [python_file_1].py (if applicable)
---
[Complete Python code]

FILE: [python_file_2].py (if applicable)
---
[Complete Python code]

FILE: sample_input.json
---
[Complete JSON content]

FILE: expected_output.json
---
[Complete JSON content]

FILE: HOW_TO_USE.md
---
[Complete usage guide]

ZIP FILE: [skill-name].zip
---
Ready for import - contains entire skill folder with all files above
================================================================================
```

---

## Example Skill Types to Generate

### Analytical Skills (with Python)
- Feature prioritization calculators
- Metrics dashboard builders
- Competitive analysis engines
- User research synthesizers
- Roadmap scenario modelers

### Generative Skills (with Python)
- PRD generators
- User story creators
- Stakeholder update writers
- OKR formatters
- Launch plan builders

### Instructional Skills (prompt-only)
- PM communication frameworks
- Decision-making guides
- Meeting facilitation templates
- Strategic thinking prompts
- Stakeholder alignment frameworks

### Evaluative Skills (with Python)
- AI ethics assessors
- Risk evaluation frameworks
- Opportunity scorers
- Technical feasibility checkers
- Go/no-go decision matrices

---

## PM-Specific Best Practices to Incorporate

### For Prioritization Skills
- Always include confidence scores
- Account for strategic alignment
- Consider technical dependencies
- Factor in user impact AND business value
- Include risk assessment

### For Research Skills
- Extract verbatim quotes with context
- Identify themes and patterns
- Prioritize pain points by frequency and severity
- Connect insights to opportunities
- Generate hypotheses for testing

### For PRD/Specs Skills
- Start with problem statement, not solution
- Include success metrics upfront
- Address "why now?" question
- Document alternatives considered
- Include rollback plan

### For Metrics Skills
- Define leading AND lagging indicators
- Specify measurement methodology
- Include targets and thresholds
- Connect to business outcomes
- Enable cohort analysis

### For AI/ML Skills
- Address bias and fairness explicitly
- Include model performance requirements
- Specify data quality needs
- Document ethical considerations
- Plan for model monitoring

---

## Variable Definitions

At the bottom of this prompt, you'll fill in:

- **PM_ROLE**: Your specific PM role (e.g., "Senior AI PM at healthcare startup")
- **PRODUCT_TYPE**: Type of product you work on (e.g., "B2B SaaS for medical imaging")
- **USE_CASES**: Specific PM tasks you need help with (list 3-10)
- **NUMBER_OF_SKILLS**: How many skills to generate (1-10 recommended)
- **SKILL_COMPLEXITY**: "basic" (prompt-only), "intermediate" (some Python), or "advanced" (complex Python)
- **PM_METHODOLOGIES**: Which frameworks to emphasize (e.g., "RICE, Jobs-to-be-Done, OKRs")
- **TEAM_CONTEXT**: Your team size and structure (helps tailor collaboration features)
- **ADDITIONAL_REQUIREMENTS**: Any specific needs or constraints

---

## Generation Rules

1. **Always use kebab-case** for skill names in YAML and folder names
2. **Always include HOW_TO_USE.md** with multiple real scenarios
3. **Always provide sample data** that reflects actual PM work
4. **Always create ZIP files** ready for import
5. **Always explain PM frameworks** used in the skill
6. **Always consider skill composition** - how skills work together
7. **Always include AI/ML considerations** when relevant
8. **Always add safety checks** in Python code (null handling, division by zero, etc.)

---

## Now Generate Skills!

Based on the variables filled in below, generate complete, production-ready Claude Skills for AI Product Management.

For each skill:
1. Analyze the PM use case thoroughly
2. Choose appropriate architecture (instructional vs. computational)
3. Apply relevant PM frameworks
4. Generate all required files with complete implementations
5. Ensure enterprise quality standards
6. Verify composability with other skills
7. Package everything into a ready-to-use ZIP

Remember:
- This is for a real PM with real problems to solve
- Quality over quantity - each skill should be production-ready
- Think about the end-to-end PM workflow
- Make outputs immediately actionable

---

=== FILL IN YOUR DETAILS BELOW ===

**PM_ROLE**: [e.g., "Senior AI Product Manager at B2B SaaS startup"]

**PRODUCT_TYPE**: [e.g., "AI-powered analytics platform for e-commerce"]

**USE_CASES**: 
[List your specific needs, e.g.:
1. Create PRDs for new AI features with ethics considerations
2. Prioritize feature backlog using RICE methodology
3. Analyze user interview transcripts to extract themes
4. Track competitor AI capabilities and positioning
5. Generate stakeholder updates with metrics and progress
]

**NUMBER_OF_SKILLS**: [e.g., 5]

**SKILL_COMPLEXITY**: [basic / intermediate / advanced]

**PM_METHODOLOGIES**: [e.g., "RICE prioritization, Jobs-to-be-Done, North Star Framework, OKRs"]

**TEAM_CONTEXT**: [e.g., "5-person product team, working with 20 engineers, reporting to CPO"]

**ADDITIONAL_REQUIREMENTS**: 
[Any specific needs, e.g.:
- Must integrate with Jira/Linear
- Focus on AI ethics and responsible AI
- Need to work with non-technical stakeholders
- Emphasis on data-driven decision making
]

---

END OF PROMPT - Paste everything above (including your filled variables) into Claude to generate skills!
