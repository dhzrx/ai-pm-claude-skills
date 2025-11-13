# AI PM Skills Repository

A comprehensive collection of Claude Skills specifically designed for AI Product Managers. This repository provides production-ready skills to help AI PMs with product strategy, roadmapping, user research, competitive analysis, feature prioritization, stakeholder management, and AI-specific product development.

## 🎯 What's Inside

This repository contains specialized Claude Skills built for the unique needs of AI Product Managers, including:

- **Product Strategy & Planning**: PRD generation, roadmap creation, OKR setting
- **User Research & Insights**: Interview analysis, survey synthesis, persona development
- **Feature Prioritization**: RICE scoring, value vs. effort mapping, impact analysis
- **Competitive Intelligence**: Market analysis, competitor tracking, positioning strategies
- **AI/ML Product Workflows**: Model evaluation, dataset requirements, AI ethics assessment
- **Stakeholder Management**: Communication templates, alignment frameworks, decision logs
- **Metrics & Analytics**: North Star metrics, funnel analysis, retention modeling
- **Go-to-Market**: Launch planning, adoption strategies, success criteria

## 📚 Repository Structure

```
ai-pm-skills-repository/
├── README.md                          # This file
├── skills/                            # All AI PM skills
│   ├── prd-generator/                 # Generate comprehensive PRDs
│   ├── user-research-analyzer/        # Analyze user interviews & surveys
│   ├── feature-prioritizer/           # RICE, ICE, Value/Effort scoring
│   ├── competitive-analyzer/          # Competitive intelligence & positioning
│   ├── roadmap-planner/              # Product roadmap creation
│   ├── ai-ethics-assessor/           # AI ethics & bias evaluation
│   ├── metrics-dashboard-builder/     # Define & track product metrics
│   ├── stakeholder-communicator/      # Stakeholder update templates
│   ├── user-story-generator/          # Generate user stories from features
│   └── gtm-strategy-builder/         # Go-to-market planning
├── templates/                         # Factory prompts for generating new skills
│   ├── AI_PM_SKILLS_FACTORY.md       # Main factory prompt
│   └── SKILL_TEMPLATE.md             # Template for new skills
├── documentation/
│   ├── QUICK_START.md                # Getting started guide
│   ├── BEST_PRACTICES.md             # AI PM-specific best practices
│   └── USE_CASES.md                  # Real-world examples
└── examples/
    └── sample-workflows/              # End-to-end workflow examples
```

## 🚀 Quick Start

### Using Existing Skills

1. **Browse the Skills**: Check the `skills/` directory for available capabilities
2. **Import a Skill**: 
   - Claude AI Desktop: Import the `.zip` file from any skill folder
   - Claude Code: Copy skill folder to `~/.claude/skills/`
   - Claude API: Use the `/v1/skills` endpoint

3. **Invoke the Skill**: Follow the invocation examples in each skill's `HOW_TO_USE.md`

### Example Usage

```
Human: I need to create a PRD for an AI-powered recommendation feature

Claude: [uses prd-generator skill]
I'll help you create a comprehensive PRD. Let me gather the key information...

[Generates structured PRD with problem statement, user stories, 
success metrics, technical requirements, and rollout plan]
```

### Generating New Skills

1. Open `templates/AI_PM_SKILLS_FACTORY.md`
2. Fill in your specific requirements at the bottom
3. Copy the entire prompt into Claude
4. Receive production-ready skills tailored to your needs

## 📦 Featured Skills

### 1. PRD Generator
**Purpose**: Create comprehensive Product Requirements Documents with AI PM best practices

**Key Features**:
- Problem statement & opportunity sizing
- User stories with acceptance criteria
- Success metrics & KPIs
- Technical requirements & dependencies
- Risk assessment & mitigation
- AI-specific considerations (model requirements, data needs, bias mitigation)

**Files**: `SKILL.md`, `generate_prd.py`, `sample_input.json`, `expected_output.json`, `HOW_TO_USE.md`

### 2. Feature Prioritizer
**Purpose**: Evaluate and prioritize features using multiple frameworks

**Key Features**:
- RICE scoring (Reach, Impact, Confidence, Effort)
- ICE scoring (Impact, Confidence, Ease)
- Value vs. Effort matrix visualization
- Dependency mapping
- Strategic alignment scoring
- AI impact assessment

**Files**: `SKILL.md`, `calculate_scores.py`, `visualize_matrix.py`, `sample_input.json`, `expected_output.json`

### 3. User Research Analyzer
**Purpose**: Synthesize user interviews, surveys, and feedback into actionable insights

**Key Features**:
- Interview transcript analysis
- Theme extraction & clustering
- Pain point identification
- Opportunity scoring
- Persona generation
- Quote extraction with context

**Files**: `SKILL.md`, `analyze_research.py`, `extract_themes.py`, `sample_input.json`, `expected_output.json`

### 4. Competitive Analyzer
**Purpose**: Track competitors and develop differentiation strategies

**Key Features**:
- Feature comparison matrices
- SWOT analysis
- Positioning maps
- Pricing analysis
- Market gap identification
- AI capability benchmarking

**Files**: `SKILL.md`, `analyze_competitors.py`, `generate_positioning.py`, `sample_input.json`, `expected_output.json`

### 5. AI Ethics Assessor
**Purpose**: Evaluate AI features for ethical considerations and bias risks

**Key Features**:
- Fairness assessment framework
- Bias detection checklist
- Privacy impact analysis
- Transparency requirements
- Accountability mapping
- Regulatory compliance check (GDPR, AI Act, etc.)

**Files**: `SKILL.md`, `assess_ethics.py`, `generate_report.py`, `sample_input.json`, `expected_output.json`

## 🎨 Skill Composition Workflows

Skills are designed to work together for complete PM workflows:

### Workflow 1: Feature Development Cycle
```
user-research-analyzer 
    → feature-prioritizer 
    → prd-generator 
    → user-story-generator 
    → stakeholder-communicator
```

### Workflow 2: AI Product Launch
```
competitive-analyzer 
    → ai-ethics-assessor 
    → prd-generator 
    → metrics-dashboard-builder 
    → gtm-strategy-builder
```

### Workflow 3: Strategic Planning
```
competitive-analyzer 
    → user-research-analyzer 
    → roadmap-planner 
    → stakeholder-communicator
```

## 🛠️ Technical Standards

All skills in this repository follow enterprise standards:

- **YAML Format**: Proper frontmatter with kebab-case naming
- **Type Safety**: Python files use type hints and error handling
- **Documentation**: Comprehensive docs with examples
- **Testing**: Sample inputs and expected outputs included
- **Portability**: Works across Claude.ai, Claude Code, and API

## 📖 Best Practices for AI PMs

### When to Use Which Skill

- **Starting a new feature?** → Use `competitive-analyzer` + `user-research-analyzer` first
- **Need buy-in?** → Use `prd-generator` + `stakeholder-communicator`
- **Prioritizing backlog?** → Use `feature-prioritizer`
- **Launching AI feature?** → Always use `ai-ethics-assessor` first
- **Quarterly planning?** → Use `roadmap-planner` + `metrics-dashboard-builder`

### Skill Composition Tips

1. **Chain outputs**: Use JSON output from one skill as input to another
2. **Iterate**: Run skills multiple times with refined inputs
3. **Customize**: Fork skills and adjust for your company's processes
4. **Validate**: Always review AI-generated content before sharing

## 🌟 Real-World Examples

### Example 1: Building an AI Recommendation System

```
1. Run competitive-analyzer to understand market landscape
2. Use ai-ethics-assessor to identify potential bias risks
3. Generate PRD with prd-generator including ethical guidelines
4. Build metrics dashboard with metrics-dashboard-builder
5. Create launch plan with gtm-strategy-builder
```

### Example 2: Quarterly Roadmap Planning

```
1. Analyze latest user research with user-research-analyzer
2. Score all backlog items with feature-prioritizer
3. Create quarterly roadmap with roadmap-planner
4. Generate stakeholder updates with stakeholder-communicator
```

## 🤝 Contributing

We welcome contributions from the AI PM community!

### Adding New Skills

1. Fork this repository
2. Use `templates/SKILL_TEMPLATE.md` as starting point
3. Follow naming conventions (kebab-case)
4. Include complete implementation + samples
5. Submit pull request

### Suggesting Improvements

- Open an issue with your suggestion
- Tag it with `enhancement` or `new-skill`
- Describe the PM problem it solves

## 📝 License

This repository provides templates and examples for creating Claude Skills. The skills you generate are yours to use as you see fit.

## 🔗 Resources

- [Claude Skills Documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
- [Original Skill Factory Repository](https://github.com/alirezarezvani/claude-code-skill-factory)
- [Product Management Resources](#) (Add your favorite PM resources)
- [AI Ethics Guidelines](#) (Add relevant AI ethics resources)

## 📞 Support

- Questions? Open an issue
- Suggestions? Start a discussion
- Found a bug? Submit a bug report

---

**Version**: 1.0.0  
**Last Updated**: November 2025  
**Maintained by**: AI PM Community  
**Compatible with**: Claude Skills (all platforms) and Claude Code

---

## Quick Reference

- **Create Skills**: Use `templates/AI_PM_SKILLS_FACTORY.md`
- **Browse Skills**: Check `skills/` directory
- **Learn Best Practices**: Read `documentation/BEST_PRACTICES.md`
- **See Examples**: Explore `examples/sample-workflows/`

Ready to supercharge your AI PM workflow? Start with `documentation/QUICK_START.md`!
