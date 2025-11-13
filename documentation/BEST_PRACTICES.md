# Best Practices for AI Product Managers Using Claude Skills

This guide provides AI PM-specific best practices for using Claude Skills effectively, derived from real-world PM workflows and common pitfalls to avoid.

## Table of Contents

1. [General Principles](#general-principles)
2. [Skill Selection](#skill-selection)
3. [Input Crafting](#input-crafting)
4. [Output Refinement](#output-refinement)
5. [Workflow Design](#workflow-design)
6. [Team Collaboration](#team-collaboration)
7. [AI/ML Product-Specific Practices](#aiml-product-specific-practices)
8. [Common Anti-Patterns](#common-anti-patterns)

---

## General Principles

### 1. Start with the Problem, Not the Skill

❌ **Anti-pattern**: "What skills can I use today?"  
✅ **Best practice**: "What PM problem am I trying to solve?"

**Why**: Skills are tools, not the goal. Always start with your PM challenge, then select the appropriate skill(s).

**Example**:
```
❌ Bad: "Let me try the PRD Generator skill"
✅ Good: "I need to spec out this feature for engineering. PRD Generator will help."
```

---

### 2. Treat Skills as Thinking Partners, Not Magic Buttons

❌ **Anti-pattern**: Generate output once, ship it  
✅ **Best practice**: Iterate, refine, validate with humans

**Why**: Skills accelerate your work but don't replace PM judgment. Always review critically.

**Example**:
```
❌ Bad: Generate PRD → Send to engineering
✅ Good: Generate PRD → Review for accuracy → Add context → Validate with team → Refine → Share
```

---

### 3. Combine Skills for End-to-End Workflows

❌ **Anti-pattern**: Use skills in isolation  
✅ **Best practice**: Chain skills for complete workflows

**Why**: PM work is interconnected. Skills are designed to compose together.

**Example**:
```
❌ Bad: Only use PRD Generator
✅ Good: User Research Analyzer → Feature Prioritizer → PRD Generator → Stakeholder Communicator
```

---

### 4. Customize for Your Context

❌ **Anti-pattern**: Use skills as-is without adaptation  
✅ **Best practice**: Fork skills and add company-specific elements

**Why**: Every company has unique processes, terminology, and requirements.

**Example**:
```
❌ Bad: Use generic PRD template
✅ Good: Fork PRD Generator, add company's PRD sections, terminology, and approval workflow
```

---

## Skill Selection

### When to Use Which Skill

#### Use **PRD Generator** when:
- Starting a new feature or product
- Documenting requirements for engineering
- Need comprehensive specification
- Stakeholder review required

#### Use **Feature Prioritizer** when:
- Have multiple features to choose from
- Need data-driven decision justification
- Quarterly/annual planning time
- Resolving disagreements about priorities

#### Use **User Research Analyzer** when:
- Conducted user interviews or surveys
- Have customer feedback to synthesize
- Need to extract themes from qualitative data
- Validating problem before building solution

#### Use **Competitive Analyzer** when:
- Planning feature differentiation
- Need market intelligence
- Responding to competitive threats
- Evaluating market gaps

#### Use **AI Ethics Assessor** when:
- Building AI/ML features
- Concerned about bias or fairness
- Need to comply with AI regulations
- Want to assess ethical implications

#### Use **Roadmap Planner** when:
- Communicating product vision
- Quarterly planning complete
- Need visual representation of priorities
- Stakeholder alignment required

---

### Skill Composition Patterns

#### Pattern 1: Discovery to Delivery
```
User Research Analyzer
  ↓
Competitive Analyzer
  ↓
Feature Prioritizer
  ↓
PRD Generator
  ↓
User Story Generator
  ↓
Metrics Dashboard Builder
```

**When**: Starting a new initiative from scratch

---

#### Pattern 2: AI Feature Launch
```
Competitive Analyzer (see market)
  ↓
AI Ethics Assessor (evaluate risks)
  ↓
PRD Generator (document requirements)
  ↓
Metrics Dashboard Builder (define success)
  ↓
GTM Strategy Builder (plan launch)
```

**When**: Launching AI-powered features responsibly

---

#### Pattern 3: Quarterly Planning
```
User Research Analyzer (understand needs)
  ↓
Feature Prioritizer (score backlog)
  ↓
Roadmap Planner (create roadmap)
  ↓
Stakeholder Communicator (align team)
```

**When**: Regular quarterly planning cycle

---

## Input Crafting

### Principle: Garbage In, Garbage Out

The quality of skill outputs depends entirely on input quality. Follow these guidelines:

### 1. Be Specific About the Problem

❌ **Vague**: "Users have issues with search"  
✅ **Specific**: "Users spend 5+ minutes searching, 40% abandon without finding results, costing $2M annually in lost conversions"

**Template**:
```
[User segment] experiences [specific pain point] which causes [quantified impact] resulting in [business consequence]
```

---

### 2. Provide Quantified Goals

❌ **Vague**: "Improve engagement"  
✅ **Specific**: "Increase DAU from 50K to 65K (+30%) and session duration from 8min to 12min (+50%) within Q1 2026"

**Template**:
```
[Metric] from [baseline] to [target] ([% improvement]) by [date]
```

---

### 3. Include Context, Not Just Facts

❌ **Missing context**: "Build AI recommendations"  
✅ **With context**: "Build AI recommendations because competitors launched similar feature last quarter, we're seeing 15% churn to competitor, and have 6-month window before market consolidates"

**What to include**:
- User research insights
- Competitive landscape
- Technical constraints
- Strategic importance
- Time sensitivity

---

### 4. Use Structured Inputs for Precision

For maximum control, provide structured JSON:

```json
{
  "feature_name": "Specific, clear name",
  "problem_statement": "Detailed problem description",
  "target_users": ["Segment 1", "Segment 2"],
  "business_goals": ["Goal 1 with numbers", "Goal 2 with numbers"],
  "user_research_summary": "Key findings from research",
  "competitive_landscape": "Market dynamics",
  "technical_constraints": ["Constraint 1", "Constraint 2"],
  "success_metrics": [
    {
      "name": "Metric name",
      "baseline": "Current value",
      "target": "Target value",
      "timeline": "When to achieve",
      "measurement": "How to measure"
    }
  ]
}
```

---

## Output Refinement

### 1. Always Review Critically

Skills generate drafts, not final documents. Always:

✓ **Verify accuracy** - Check facts and numbers  
✓ **Add context** - Include company-specific details  
✓ **Validate assumptions** - Confirm with stakeholders  
✓ **Refine language** - Adjust tone for audience  
✓ **Fill gaps** - Add missing information  

---

### 2. Iterate in Stages

Don't try to get perfect output in one shot:

**Stage 1: Structure**
```
Generate PRD outline for [feature]
```

**Stage 2: Fill Content**
```
Expand the Problem Statement section with these user research insights: [insights]
```

**Stage 3: Refine Details**
```
Add more specific technical requirements, particularly around API integration with [system]
```

**Stage 4: Polish**
```
Adjust tone to be more technical for engineering audience
```

---

### 3. Extract and Reuse Patterns

When you get good output, extract the pattern:

1. **Save successful prompts** - Build your own prompt library
2. **Document what worked** - Share with team
3. **Create templates** - Standardize for common use cases
4. **Fork skills** - Customize with your patterns

---

## Workflow Design

### 1. Map Your PM Process First

Before using skills, document your current process:

**Example PM Process**:
```
1. Problem validation (user research)
2. Solution exploration (ideation, prototyping)
3. Prioritization (scoring, roadmapping)
4. Specification (PRD writing)
5. Execution (sprint planning, tracking)
6. Launch (GTM, metrics)
7. Iteration (analysis, refinement)
```

**Then map skills to each stage**:
```
1. Problem validation → User Research Analyzer
2. Solution exploration → Competitive Analyzer, AI Ethics Assessor
3. Prioritization → Feature Prioritizer
4. Specification → PRD Generator, User Story Generator
5. Execution → (Project management tools)
6. Launch → GTM Strategy Builder, Stakeholder Communicator
7. Iteration → Metrics Dashboard Builder
```

---

### 2. Create Reusable Workflows

Document workflows for recurring PM tasks:

**Workflow Template**:
```markdown
## Workflow: [Name]

**When to use**: [Trigger/situation]

**Steps**:
1. [Skill 1] with [input type]
2. [Skill 2] with output from step 1
3. [Skill 3] with combined outputs

**Expected output**: [Deliverable]

**Time estimate**: [Duration]

**Example invocation**: [Sample prompt]
```

**Example**:
```markdown
## Workflow: Feature Concept to PRD

**When to use**: Validated feature idea ready for specification

**Steps**:
1. Competitive Analyzer with feature description
2. AI Ethics Assessor (if AI feature)
3. PRD Generator with insights from steps 1-2

**Expected output**: Production-ready PRD

**Time estimate**: 30-60 minutes

**Example invocation**:
"I want to build [feature]. First analyze competitors, then assess any AI ethics concerns, then generate comprehensive PRD."
```

---

### 3. Build Feedback Loops

Improve workflows over time:

1. **Track what works** - Document successful patterns
2. **Identify bottlenecks** - Where do workflows break?
3. **Refine prompts** - Iterate on input templates
4. **Share learnings** - Teach team what works
5. **Customize skills** - Fork and adapt to findings

---

## Team Collaboration

### 1. Standardize on Core Skills

**Anti-pattern**: Every PM uses different skills differently  
**Best practice**: Align team on core skills and invocation patterns

**How**:
1. Choose 5-7 core skills everyone uses
2. Create team-specific invocation templates
3. Document workflows in team wiki
4. Hold training session on skills
5. Share successful examples

---

### 2. Create Shared Prompt Library

Build a team collection of effective prompts:

```
team-prompt-library/
├── prd-generation/
│   ├── mobile-feature-prd.md
│   ├── ai-feature-prd.md
│   └── integration-prd.md
├── prioritization/
│   ├── quarterly-planning.md
│   └── feature-scoring.md
└── research-analysis/
    ├── interview-synthesis.md
    └── survey-analysis.md
```

---

### 3. Review and Improve Together

Make skills part of PM rituals:

**Weekly PM Sync**:
- Share skill outputs that worked well
- Discuss challenges and solutions
- Refine shared prompts

**Monthly Retrospective**:
- Review which skills are most valuable
- Identify missing capabilities
- Plan custom skill development

**Quarterly Planning**:
- Use Feature Prioritizer collaboratively
- Generate roadmap together
- Align on priorities with skills

---

## AI/ML Product-Specific Practices

### 1. Always Assess Ethics Early

❌ **Anti-pattern**: Build first, assess ethics later  
✅ **Best practice**: Use AI Ethics Assessor before writing PRD

**Why**: Ethical issues are easier to prevent than fix. Bake them into design.

**Process**:
```
1. Describe AI feature concept
2. Run AI Ethics Assessor
3. Incorporate findings into PRD
4. Add monitoring plan for ethical metrics
5. Revisit quarterly
```

---

### 2. Document AI-Specific Requirements

Every AI feature PRD should include:

✓ **Model performance targets** (accuracy, latency, throughput)  
✓ **Data requirements** (volume, quality, labeling)  
✓ **Bias mitigation strategies** (demographic parity, fairness metrics)  
✓ **Explainability approach** (how users understand decisions)  
✓ **Monitoring plan** (drift detection, performance tracking)  
✓ **Fallback behavior** (what happens when AI fails)  
✓ **Human oversight** (when humans review/override)  

**Template**:
```markdown
## AI/ML Specifications

### Model Requirements
- Type: [model architecture]
- Performance: Accuracy > X%, Latency < Yms
- Scale: Z predictions/second

### Data Requirements
- Training: [size, quality requirements]
- Features: [key features needed]
- Labeling: [accuracy requirements]

### Bias & Fairness
- Evaluation: [metrics across demographics]
- Mitigation: [strategies to address bias]
- Monitoring: [ongoing fairness checks]

### Explainability
- User visibility: [what users see]
- Transparency: [how decisions explained]
- Confidence: [when to show uncertainty]

### Monitoring & Maintenance
- Performance tracking: [metrics]
- Drift detection: [triggers]
- Retraining: [frequency/conditions]
```

---

### 3. Balance Innovation and Responsibility

AI PMs must balance:
- **Speed to market** vs. **Thorough testing**
- **Model accuracy** vs. **Fairness across groups**
- **Personalization** vs. **Privacy**
- **Automation** vs. **Human oversight**

**Decision Framework**:
```
For each AI feature, assess:
1. Risk level (low/medium/high)
2. User trust impact
3. Regulatory requirements
4. Reputational risk

High risk → More thorough testing, human oversight, gradual rollout
Low risk → Faster iteration, automated decisions, broader launch
```

---

## Common Anti-Patterns

### Anti-Pattern 1: "Set It and Forget It"

❌ **Problem**: Generate PRD, never update it  
✅ **Solution**: Treat PRDs as living documents, regenerate sections as you learn

---

### Anti-Pattern 2: "The Skill Knows Best"

❌ **Problem**: Accept all skill outputs without question  
✅ **Solution**: Skills are assistants, not authorities. Validate everything.

---

### Anti-Pattern 3: "One Size Fits All"

❌ **Problem**: Use same prompt for every feature type  
✅ **Solution**: Customize inputs for B2B vs. B2C, AI vs. non-AI, etc.

---

### Anti-Pattern 4: "Skip the Context"

❌ **Problem**: Minimal input, expect great output  
✅ **Solution**: Rich context = better output. Always include research, competitive landscape, constraints.

---

### Anti-Pattern 5: "Ignore Dependencies"

❌ **Problem**: Prioritize features independently  
✅ **Solution**: Use Feature Prioritizer with dependency mapping

---

### Anti-Pattern 6: "AI Ethics as Checkbox"

❌ **Problem**: Run AI Ethics Assessor once, forget about it  
✅ **Solution**: Continuous ethical monitoring throughout product lifecycle

---

### Anti-Pattern 7: "Solo PM Hero"

❌ **Problem**: Use skills in isolation, don't share with team  
✅ **Solution**: Collaborative skill usage, shared prompt library, team workflows

---

## Measuring Success

Track these metrics to ensure skills are valuable:

### Efficiency Metrics
- **Time to PRD**: How long to generate production-ready PRD?
- **Prioritization speed**: Time from feature list to ranked backlog?
- **Research synthesis**: Hours to analyze user research?

**Targets**:
- PRD generation: 2-4 hours → 30-60 minutes
- Feature prioritization: 1 day → 1-2 hours
- Research synthesis: 4-8 hours → 1-2 hours

### Quality Metrics
- **PRD completeness**: % PRDs with all required sections
- **Prioritization accuracy**: % features scored correctly vs. retrospective
- **Stakeholder satisfaction**: Feedback on skill-generated docs

**Targets**:
- PRD completeness: 100% (with iteration)
- Prioritization accuracy: > 80% (high-confidence features)
- Stakeholder satisfaction: > 4/5 rating

### Adoption Metrics
- **Skill usage**: % PMs using skills regularly
- **Workflow integration**: % PM processes including skills
- **Team standardization**: % team on common skills/workflows

**Targets**:
- Skill usage: > 80% of PMs
- Workflow integration: > 60% of PM processes
- Team standardization: 100% on core 5 skills

---

## Next Steps

1. **Choose your top 3 pain points** as a PM
2. **Map skills** to those pain points
3. **Try one skill** with a real task today
4. **Refine your prompt** based on output
5. **Share results** with your team
6. **Build a workflow** for your most common PM task
7. **Customize skills** for your company's processes

---

**Remember**: Skills are powerful accelerators, but they don't replace PM judgment, creativity, or strategic thinking. Use them to handle the mechanical parts of PM work so you can focus on the strategic and creative aspects.

**Happy building! 🚀**
