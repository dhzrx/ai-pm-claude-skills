# AI PM Skills Repository - Navigation Index

Welcome! This index will help you navigate the repository and find exactly what you need.

## 🚀 Start Here

**New to the repository?**
→ [README.md](README.md) - Overview of the entire repository

**Want to get started quickly?**
→ [documentation/QUICK_START.md](documentation/QUICK_START.md) - Step-by-step guide

**Looking for best practices?**
→ [documentation/BEST_PRACTICES.md](documentation/BEST_PRACTICES.md) - Expert guidance

## 📚 Core Documentation

| Document | Purpose | Time to Read |
|----------|---------|--------------|
| [README.md](README.md) | Repository overview, all skills | 10 min |
| [QUICK_START.md](documentation/QUICK_START.md) | Getting started guide | 15 min |
| [BEST_PRACTICES.md](documentation/BEST_PRACTICES.md) | PM-specific best practices | 20 min |
| [USE_CASES.md](documentation/USE_CASES.md) | Real-world examples | 15 min |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute | 10 min |
| [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) | Complete project overview | 10 min |

## 🛠️ Skills

### Available Skills

| Skill | Purpose | Files |
|-------|---------|-------|
| **PRD Generator** | Create comprehensive Product Requirements Documents | [View Skill](skills/prd-generator/) |
| **Feature Prioritizer** | RICE/ICE scoring and Value vs. Effort matrices | [View Skill](skills/feature-prioritizer/) |

### Each Skill Contains:
- `SKILL.md` - Complete skill documentation
- `*.py` - Python implementation (if applicable)
- `sample_input.json` - Example input
- `expected_output.json` - Example output
- `HOW_TO_USE.md` - Detailed usage guide with scenarios

## 🏭 Create Your Own Skills

**Want to generate custom skills?**
→ [templates/AI_PM_SKILLS_FACTORY.md](templates/AI_PM_SKILLS_FACTORY.md)

This comprehensive prompt template lets you generate production-ready skills tailored to your specific PM needs.

## 📖 Quick Reference Guides

### Installation
- **Claude.ai Desktop**: Import `.zip` file → Settings → Skills
- **Claude Code**: Copy folder to `~/.claude/skills/`
- **Claude API**: Use `/v1/skills` endpoint

### Common Workflows

**New Feature Development:**
```
User Research Analyzer → Competitive Analyzer → Feature Prioritizer 
→ PRD Generator → User Story Generator → Stakeholder Communicator
```

**Quarterly Planning:**
```
User Research Analyzer → Feature Prioritizer → Roadmap Planner 
→ Metrics Dashboard Builder → Stakeholder Communicator
```

**AI Feature Launch:**
```
Competitive Analyzer → AI Ethics Assessor → PRD Generator 
→ Metrics Dashboard Builder → GTM Strategy Builder
```

## 🎯 Use Cases by Role

### For Individual PMs
- [Quick Start Guide](documentation/QUICK_START.md)
- [PRD Generator Usage](skills/prd-generator/HOW_TO_USE.md)
- [Feature Prioritization](skills/feature-prioritizer/SKILL.md)

### For PM Teams
- [Best Practices for Teams](documentation/BEST_PRACTICES.md#team-collaboration)
- [Creating Shared Workflows](documentation/BEST_PRACTICES.md#workflow-design)
- [Standardization Guidelines](CONTRIBUTING.md)

### For Tool Builders
- [Skills Factory Template](templates/AI_PM_SKILLS_FACTORY.md)
- [Contribution Guidelines](CONTRIBUTING.md)
- [Technical Standards](CONTRIBUTING.md#skill-standards)

## 🔍 Find by Problem

| I need to... | Use this... |
|-------------|-------------|
| Write a PRD | [PRD Generator](skills/prd-generator/) |
| Prioritize features | [Feature Prioritizer](skills/feature-prioritizer/) |
| Plan quarterly roadmap | Feature Prioritizer → Roadmap Planner |
| Launch AI feature | AI Ethics Assessor → PRD Generator |
| Get stakeholder buy-in | PRD Generator → Stakeholder Communicator |
| Synthesize user research | User Research Analyzer |
| Track competitors | Competitive Analyzer |

## 📊 Learn by Example

### Real-World Case Studies
1. [Building an AI Recommendation Engine](documentation/USE_CASES.md#case-study-1-building-an-ai-recommendation-engine) - 8 weeks, multi-skill workflow
2. [Adding Dark Mode](documentation/USE_CASES.md#case-study-2-adding-dark-mode-to-mobile-app) - 2 days, quick prioritization
3. [Quarterly Roadmap Planning](documentation/USE_CASES.md#case-study-3-quarterly-roadmap-planning-q1-2026) - 1 week, complete planning
4. [Getting CEO Buy-In](documentation/USE_CASES.md#case-study-4-getting-ceo-buy-in-for-platform-rebuild) - 2 weeks, stakeholder alignment
5. [AI Content Moderation](documentation/USE_CASES.md#case-study-5-launching-ai-powered-content-moderation) - 12 weeks, responsible AI
6. [Competitive Response](documentation/USE_CASES.md#case-study-6-responding-to-competitors-ai-features) - 4 weeks, market response
7. [User Research Synthesis](documentation/USE_CASES.md#case-study-7-synthesizing-50-user-interviews) - 3 days, research analysis

## 🎓 Learning Path

### Beginner (Week 1)
1. Read [README.md](README.md)
2. Follow [QUICK_START.md](documentation/QUICK_START.md)
3. Try PRD Generator with sample input
4. Review output and iterate

### Intermediate (Week 2-3)
1. Read [BEST_PRACTICES.md](documentation/BEST_PRACTICES.md)
2. Try Feature Prioritizer with real backlog
3. Create your first multi-skill workflow
4. Share learnings with team

### Advanced (Month 1+)
1. Review [USE_CASES.md](documentation/USE_CASES.md)
2. Use [AI PM Skills Factory](templates/AI_PM_SKILLS_FACTORY.md) to generate custom skill
3. Contribute workflow to repository
4. Help other PMs adopt skills

## 🤝 Get Involved

### Ways to Contribute
- Share your custom skills
- Improve existing skills
- Add workflow examples
- Update documentation
- Report issues
- Help other PMs

**Read**: [CONTRIBUTING.md](CONTRIBUTING.md)

## 📞 Support

### Documentation Issues?
- Check if answer is in docs first
- Open GitHub issue
- Tag with `documentation`

### Skill Issues?
- Review `HOW_TO_USE.md` for that skill
- Check sample input format
- Open GitHub issue with details

### Feature Requests?
- Review existing skills first
- Check if factory prompt can generate it
- Open GitHub discussion
- Tag with `enhancement`

## 📈 What's Next?

### Planned Skills
- User Research Analyzer
- Competitive Analyzer
- AI Ethics Assessor
- Roadmap Planner
- Metrics Dashboard Builder
- Stakeholder Communicator
- User Story Generator
- GTM Strategy Builder

### Planned Features
- Jira/Linear integration
- PowerPoint export
- Real-time metrics
- Collaborative roadmapping
- AI model evaluation

**Want to help build these?** See [CONTRIBUTING.md](CONTRIBUTING.md)

## 🗺️ File Structure

```
ai-pm-skills-repository/
├── README.md                          # Start here
├── PROJECT_SUMMARY.md                 # Complete project overview
├── CONTRIBUTING.md                    # Contribution guidelines
├── INDEX.md                          # This file
│
├── skills/                           # Production-ready skills
│   ├── prd-generator/                # PRD generation skill
│   │   ├── SKILL.md                  # Skill documentation
│   │   ├── generate_prd.py           # Python implementation
│   │   ├── sample_input.json         # Example input
│   │   ├── expected_output.json      # Example output
│   │   └── HOW_TO_USE.md            # Detailed usage guide
│   └── feature-prioritizer/          # Feature prioritization
│       └── SKILL.md                  # Skill documentation
│
├── templates/                        # Skill generation
│   └── AI_PM_SKILLS_FACTORY.md      # Factory prompt template
│
└── documentation/                    # Guides and references
    ├── QUICK_START.md                # Getting started
    ├── BEST_PRACTICES.md             # PM best practices
    └── USE_CASES.md                  # Real-world examples
```

## 💡 Pro Tips

1. **Start Small**: Begin with 1-2 skills, master them, then expand
2. **Use Real Data**: Try skills with actual PM tasks, not toy examples
3. **Iterate**: First output is a draft, refine iteratively
4. **Compose**: Chain skills together for end-to-end workflows
5. **Customize**: Fork and adapt skills to your company's processes
6. **Share**: Document your learnings and help other PMs

## 🎉 Success Stories

Want to see how other PMs are using these skills? Check out:
- [Real-world case studies](documentation/USE_CASES.md)
- [Community workflows](#) (coming soon)
- [Success story submissions](#) (coming soon)

---

**Questions?** Check the documentation first, then open an issue.

**Found this helpful?** Star the repository and share with other PMs!

**Have a success story?** We'd love to hear about it - open a discussion!

---

*Happy PM-ing! 🚀*
