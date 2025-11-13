# Contributing to AI PM Skills Repository

Thank you for your interest in contributing! This repository is built by the AI PM community, for the AI PM community. We welcome contributions of all kinds.

## Ways to Contribute

### 1. Share Your Skills
Have you created a custom skill that helps with PM work? We'd love to include it!

**What we're looking for**:
- Production-ready skills (not experiments)
- Clear documentation (SKILL.md + HOW_TO_USE.md)
- Sample inputs and expected outputs
- Solves a real PM problem

**How to contribute**:
1. Fork this repository
2. Add your skill to `skills/your-skill-name/`
3. Follow the structure of existing skills
4. Submit a pull request

### 2. Improve Existing Skills
Found a bug? Have an enhancement idea?

**Examples**:
- Better Python implementations
- More comprehensive sample data
- Improved documentation
- Additional use cases in HOW_TO_USE.md

**How to contribute**:
1. Open an issue describing the improvement
2. Fork and make your changes
3. Submit a pull request referencing the issue

### 3. Share Workflows
Have you created effective multi-skill workflows?

**What we're looking for**:
- End-to-end PM workflows using multiple skills
- Real-world examples with results
- Reusable patterns others can adapt

**How to contribute**:
1. Document your workflow in `examples/sample-workflows/`
2. Include: problem, skills used, invocation examples, results
3. Submit a pull request

### 4. Add Documentation
Help improve guides and best practices.

**Examples**:
- New use cases for `documentation/USE_CASES.md`
- Best practices for `documentation/BEST_PRACTICES.md`
- FAQ entries
- Tutorial improvements

### 5. Report Issues
Found a problem? Let us know!

**When reporting issues, include**:
- Skill name and version
- What you expected to happen
- What actually happened
- Sample input that triggered the issue
- Your environment (Claude.ai, Claude Code, API)

## Contribution Guidelines

### Skill Standards

All contributed skills must meet these standards:

#### 1. File Structure
```
skill-name/
├── SKILL.md                 # Main skill documentation
├── skill_file.py            # Python implementation (if needed)
├── sample_input.json        # Example input
├── expected_output.json     # Example output
├── HOW_TO_USE.md           # Detailed usage guide
└── skill-name.zip          # Ready-to-import package
```

#### 2. SKILL.md Format
Must include:
- YAML frontmatter with `name` (kebab-case) and `description`
- Overview section
- "When to Use This Skill" section
- "PM Frameworks Applied" section
- Inputs/Outputs specification
- Usage instructions
- Best practices
- Composition with other skills
- Common pitfalls

#### 3. Python Code Standards (if applicable)
- Type hints for all functions
- Comprehensive docstrings (Google style)
- Error handling and edge cases
- No external dependencies beyond standard library (or justify why needed)
- Safe operations (no crashes on invalid input)
- Class-based structure for complex logic

#### 4. Sample Data
- Realistic PM data (not lorem ipsum)
- Minimal but representative
- Includes all required fields
- Shows real use case

#### 5. HOW_TO_USE.md
- Quick start example
- 3+ detailed scenarios
- Tips for best results
- Composition examples with other skills
- Troubleshooting common issues

### Code Review Process

1. **Automated Checks**: YAML validation, Python linting
2. **Peer Review**: At least 1 maintainer review required
3. **Testing**: Sample inputs must produce expected outputs
4. **Documentation**: All required docs present and complete

### Naming Conventions

- **Skills**: kebab-case (e.g., `feature-prioritizer`)
- **Python files**: snake_case (e.g., `calculate_scores.py`)
- **Classes**: PascalCase (e.g., `FeaturePrioritizer`)
- **Functions**: snake_case (e.g., `calculate_rice_score`)

### Commit Messages

Follow conventional commits format:

```
type(scope): brief description

Longer explanation if needed.

Fixes #issue-number
```

**Types**:
- `feat`: New skill or major feature
- `fix`: Bug fix
- `docs`: Documentation only
- `refactor`: Code improvement without functionality change
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples**:
```
feat(prd-generator): add AI ethics section

Added comprehensive AI/ML ethics assessment section to PRD Generator.
Includes bias mitigation, explainability, and monitoring requirements.

Fixes #42
```

```
docs(best-practices): add section on skill composition

Added new section explaining how to chain multiple skills effectively
in end-to-end PM workflows.
```

## Skill Development Guide

### Creating a New Skill

1. **Identify the PM Problem**
   - What pain point does this solve?
   - Who is the target user?
   - What's the current manual process?

2. **Choose Skill Type**
   - **Instructional**: Guidance-based (no Python)
   - **Analytical**: Data processing (with Python)
   - **Generative**: Content creation (with Python)
   - **Evaluative**: Assessment/scoring (with Python)

3. **Design Input/Output Contracts**
   - What inputs are required?
   - What outputs are produced?
   - What format (JSON, Markdown, etc.)?

4. **Apply PM Frameworks**
   - Which frameworks make sense? (RICE, JTBD, OKRs, etc.)
   - How to incorporate them?

5. **Build and Test**
   - Implement Python functions (if needed)
   - Create sample data
   - Test with real PM scenarios
   - Iterate based on feedback

6. **Document Thoroughly**
   - Write SKILL.md
   - Create HOW_TO_USE.md with multiple scenarios
   - Add to README.md in skills directory

7. **Package for Distribution**
   - Create .zip file
   - Test import on Claude.ai Desktop
   - Verify all files included

### Using the Skills Factory

The fastest way to create a new skill is using the AI PM Skills Factory prompt:

1. Open `templates/AI_PM_SKILLS_FACTORY.md`
2. Fill in your requirements at the bottom
3. Copy entire prompt into Claude
4. Receive production-ready skill!

Then refine and contribute back to the repository.

## Community Guidelines

### Be Respectful
- Treat all contributors with respect
- Assume good intentions
- Provide constructive feedback
- Help newcomers learn

### Be Collaborative
- Share your learnings
- Credit others' work
- Build on existing skills
- Think "community first"

### Be Professional
- Test before contributing
- Document your work
- Follow coding standards
- Respond to feedback

## Getting Help

### Questions About Contributing?
- Open a GitHub Discussion
- Tag with `question` label
- Check existing discussions first

### Need Technical Help?
- Open an issue with `help wanted` label
- Describe what you're trying to do
- Include relevant code/errors
- Be patient - we're all volunteers

### Want to Discuss Ideas?
- Open a Discussion (not an Issue)
- Tag appropriately (`ideas`, `enhancement`, etc.)
- Engage with community feedback

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Credited in skill documentation
- Highlighted in release notes
- Appreciated by the PM community!

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

## Quick Contribution Checklist

Before submitting a pull request:

- [ ] Followed file structure standards
- [ ] YAML frontmatter properly formatted (kebab-case name)
- [ ] Python code has type hints and docstrings
- [ ] Sample input/output files included
- [ ] HOW_TO_USE.md with 3+ scenarios
- [ ] SKILL.md is comprehensive
- [ ] Tested skill with real data
- [ ] Added skill to main README.md
- [ ] Created .zip file for distribution
- [ ] Commit messages follow convention
- [ ] PR description explains contribution

---

Thank you for helping make AI PM work better for everyone! 🙏

**Questions?** Open a Discussion or reach out to maintainers.

**Ready to contribute?** Fork the repo and submit your first PR!
