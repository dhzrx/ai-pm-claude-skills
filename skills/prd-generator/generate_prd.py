"""
PRD Generator - Python Implementation
Generates comprehensive Product Requirements Documents for AI Product Managers
"""

from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import json


class PRDGenerator:
    """
    Generates comprehensive Product Requirements Documents following PM best practices.
    Incorporates JTBD, SMART goals, RICE prioritization, and AI-specific considerations.
    """
    
    def __init__(self):
        self.prd_version = "1.0.0"
        self.frameworks = ["JTBD", "SMART", "RICE", "MoSCoW", "RACI"]
    
    def generate_prd(self, input_data: Dict[str, Any]) -> str:
        """
        Generate a complete PRD from input data.
        
        Args:
            input_data: Dictionary containing feature requirements including:
                - feature_name: Name of the feature
                - problem_statement: User problem to solve
                - target_users: User segments affected
                - business_goals: List of business objectives
                - user_research_summary: Optional research insights
                - competitive_landscape: Optional competitor analysis
                - technical_constraints: Optional technical limitations
                - success_metrics: Optional predefined metrics
                - ai_ml_requirements: Optional AI/ML specifications
        
        Returns:
            Complete PRD in Markdown format
        """
        sections = []
        
        # Header
        sections.append(self._generate_header(input_data))
        
        # Executive Summary
        sections.append(self._generate_executive_summary(input_data))
        
        # Problem Statement (JTBD Framework)
        sections.append(self._generate_problem_statement(input_data))
        
        # Opportunity Sizing
        sections.append(self._generate_opportunity_sizing(input_data))
        
        # Success Metrics (SMART Framework)
        sections.append(self._generate_success_metrics(input_data))
        
        # User Stories
        sections.append(self._generate_user_stories(input_data))
        
        # Functional Requirements (MoSCoW)
        sections.append(self._generate_functional_requirements(input_data))
        
        # Technical Requirements
        sections.append(self._generate_technical_requirements(input_data))
        
        # AI/ML Specifications (if applicable)
        if input_data.get("ai_ml_requirements"):
            sections.append(self._generate_ai_ml_specs(input_data))
        
        # User Experience
        sections.append(self._generate_ux_section(input_data))
        
        # Risk Assessment
        sections.append(self._generate_risk_assessment(input_data))
        
        # Launch Plan
        sections.append(self._generate_launch_plan(input_data))
        
        # Stakeholder Matrix (RACI)
        sections.append(self._generate_stakeholder_matrix(input_data))
        
        # Appendix
        sections.append(self._generate_appendix(input_data))
        
        return "\n\n".join(sections)
    
    def _generate_header(self, data: Dict[str, Any]) -> str:
        """Generate PRD header with metadata."""
        today = datetime.now().strftime("%B %d, %Y")
        return f"""# PRD: {data['feature_name']}

**Document Version**: {self.prd_version}  
**Last Updated**: {today}  
**Status**: Draft  
**Owner**: [Product Manager Name]  
**Stakeholders**: [Engineering Lead, Design Lead, Data Science Lead]

---
"""
    
    def _generate_executive_summary(self, data: Dict[str, Any]) -> str:
        """Generate executive summary section."""
        return f"""## Executive Summary

### Overview
{data['feature_name']} addresses the need for {data.get('problem_statement', 'improved user experience')} among {self._format_target_users(data.get('target_users', 'our users'))}.

### Business Goals
{self._format_list(data.get('business_goals', ['Improve user engagement', 'Drive revenue growth']))}

### Expected Impact
This feature is expected to reach {data.get('reach_estimate', 'a significant portion')} of our user base and deliver {data.get('impact_estimate', 'meaningful improvements')} in key metrics.

### The Ask
- **Engineering Resources**: [To be determined based on technical design]
- **Timeline**: [To be determined after estimation]
- **Dependencies**: [To be identified during planning]
"""
    
    def _generate_problem_statement(self, data: Dict[str, Any]) -> str:
        """Generate problem statement using JTBD framework."""
        problem = data.get('problem_statement', 'Users need a better way to accomplish their goals')
        
        return f"""## Problem Statement

### Jobs-to-be-Done Framework

**When** users need to accomplish their goals,  
**They want** a solution that {problem},  
**So they can** achieve better outcomes and satisfaction.

### Current Experience
Users currently face the following challenges:
- Friction in current workflow
- Time-consuming manual processes
- Lack of intelligent assistance
- Suboptimal outcomes

### Desired Experience
With this feature, users will be able to:
- Accomplish tasks more efficiently
- Receive intelligent recommendations
- Make better-informed decisions
- Achieve superior outcomes

### Why Now?
- User research indicates strong demand
- Competitive pressure in the market
- Technical capabilities now available
- Strategic alignment with company vision
"""
    
    def _generate_opportunity_sizing(self, data: Dict[str, Any]) -> str:
        """Generate opportunity sizing using TAM/SAM/SOM framework."""
        reach = data.get('reach_estimate', 10000)
        impact = data.get('impact_estimate', 0.20)
        confidence = data.get('confidence_level', 0.80)
        effort = data.get('effort_estimate', 5)
        
        rice_score = self.calculate_rice_score(reach, impact, confidence, effort)
        
        return f"""## Opportunity Sizing

### Market Analysis
- **TAM** (Total Addressable Market): [Total potential users who could benefit]
- **SAM** (Serviceable Addressable Market): [Users we can realistically reach]
- **SOM** (Serviceable Obtainable Market): [Users we expect to capture in next 12 months]

### RICE Prioritization Score
- **Reach**: {reach:,} users affected per quarter
- **Impact**: {impact:.1%} improvement in key metrics
- **Confidence**: {confidence:.0%} confidence in estimates
- **Effort**: {effort} person-months

**RICE Score**: {rice_score:.1f}

### Expected Business Impact
- **Revenue Impact**: [Projected increase in revenue]
- **User Growth**: [Expected new user acquisition]
- **Retention**: [Improvement in retention metrics]
- **Competitive Position**: [Improvement in market standing]
"""
    
    def _generate_success_metrics(self, data: Dict[str, Any]) -> str:
        """Generate SMART success metrics."""
        metrics = data.get('success_metrics', [
            {
                'name': 'User Engagement',
                'baseline': 'Current: X%',
                'target': 'Target: Y%',
                'timeline': '3 months post-launch',
                'measurement': 'Weekly active usage rate'
            }
        ])
        
        metrics_table = "| Metric | Baseline | Target | Timeline | Measurement Method |\n"
        metrics_table += "|--------|----------|--------|----------|-------------------|\n"
        
        for metric in metrics:
            metrics_table += f"| {metric.get('name', 'Metric')} | {metric.get('baseline', 'TBD')} | {metric.get('target', 'TBD')} | {metric.get('timeline', 'TBD')} | {metric.get('measurement', 'TBD')} |\n"
        
        return f"""## Success Metrics

### Primary Metrics (North Star)
The primary metric we're optimizing for is **[Primary Metric Name]** because it best reflects the value delivered to users and the business.

### Key Performance Indicators

{metrics_table}

### Leading vs. Lagging Indicators
- **Leading Indicators**: Early signals of success (e.g., feature adoption rate)
- **Lagging Indicators**: Ultimate outcome measures (e.g., retention, revenue)

### Measurement Methodology
- **Data Collection**: [How data will be captured]
- **Analysis Cadence**: [How often metrics will be reviewed]
- **Reporting**: [Who receives metric updates and how often]
- **Thresholds**: [When to intervene if metrics underperform]
"""
    
    def _generate_user_stories(self, data: Dict[str, Any]) -> str:
        """Generate user stories with acceptance criteria."""
        return f"""## User Stories

### Primary User Flows

#### Story 1: [Core Feature Usage]
**As a** {self._format_target_users(data.get('target_users', 'user'))},  
**I want** to access this feature,  
**So that** I can accomplish my goals more effectively.

**Acceptance Criteria:**
- ✓ User can discover the feature from [entry point]
- ✓ User receives clear guidance on how to use the feature
- ✓ User can complete the primary action within [X] clicks
- ✓ User receives confirmation of successful completion
- ✓ User can undo or modify their action if needed

#### Story 2: [Secondary Feature Usage]
**As a** power user,  
**I want** advanced capabilities,  
**So that** I can optimize my workflow.

**Acceptance Criteria:**
- ✓ Advanced options are available but not overwhelming
- ✓ User can customize settings to their preferences
- ✓ User can save and reuse configurations
- ✓ User receives performance insights

### Edge Cases
- What happens when [edge case scenario]?
- How does the system handle [error condition]?
- What if user has [unusual permissions/data state]?
"""
    
    def _generate_functional_requirements(self, data: Dict[str, Any]) -> str:
        """Generate functional requirements using MoSCoW method."""
        return f"""## Functional Requirements

### Must Have (MVP)
These features are essential for v1 launch:
1. **Core Functionality**: [Primary feature capability]
2. **User Onboarding**: [Introduction and guidance]
3. **Basic Analytics**: [Usage tracking and feedback]
4. **Error Handling**: [Graceful degradation]
5. **Documentation**: [Help content and FAQs]

### Should Have (Post-MVP)
Important features for v1.1-v1.2:
1. **Advanced Features**: [Enhanced capabilities]
2. **Customization**: [User preferences and settings]
3. **Integrations**: [Connect with other tools]
4. **Performance Optimization**: [Speed improvements]

### Could Have (Future)
Nice-to-have features for v2+:
1. **Premium Features**: [Advanced functionality]
2. **Collaboration**: [Multi-user capabilities]
3. **API Access**: [Programmatic interface]
4. **Mobile Optimization**: [Native mobile experience]

### Won't Have (Out of Scope)
Explicitly out of scope:
1. **Feature X**: [Reason for exclusion]
2. **Feature Y**: [Alternative approach]
3. **Feature Z**: [Deferred to future version]
"""
    
    def _generate_technical_requirements(self, data: Dict[str, Any]) -> str:
        """Generate technical requirements and constraints."""
        constraints = data.get('technical_constraints', ['Performance', 'Scalability', 'Security'])
        
        return f"""## Technical Requirements

### Architecture
- **Frontend**: [Technology stack and frameworks]
- **Backend**: [Services, APIs, databases]
- **Infrastructure**: [Hosting, CDN, caching]
- **Third-Party Services**: [External dependencies]

### Performance Requirements
- **Response Time**: < 200ms for 95th percentile
- **Throughput**: Support X concurrent users
- **Availability**: 99.9% uptime SLA
- **Data Latency**: Real-time updates within 1 second

### Security & Privacy
- **Authentication**: [How users are authenticated]
- **Authorization**: [Permission model]
- **Data Encryption**: [At rest and in transit]
- **Privacy Compliance**: [GDPR, CCPA considerations]
- **Audit Logging**: [What actions are logged]

### Technical Constraints
{self._format_list(constraints)}

### APIs & Integrations
- **Internal APIs**: [Services required]
- **External APIs**: [Third-party dependencies]
- **Webhooks**: [Event notifications]
- **Data Sync**: [Cross-system consistency]

### Dependencies
- **Upstream Dependencies**: [What must be completed first]
- **Downstream Dependencies**: [What depends on this]
- **Cross-Team Dependencies**: [Other teams involved]
"""
    
    def _generate_ai_ml_specs(self, data: Dict[str, Any]) -> str:
        """Generate AI/ML specifications and ethical considerations."""
        ai_reqs = data.get('ai_ml_requirements', {})
        
        return f"""## AI/ML Specifications

### Model Requirements
- **Model Type**: {ai_reqs.get('model_type', 'TBD')}
- **Performance Targets**:
  - Accuracy: {ai_reqs.get('accuracy_target', '> 90%')}
  - Latency: {ai_reqs.get('latency_target', '< 100ms')}
  - Throughput: {ai_reqs.get('throughput_target', 'X predictions/second')}

### Data Requirements
- **Training Data**: {ai_reqs.get('data_requirements', 'TBD')}
- **Data Volume**: [Minimum dataset size]
- **Data Quality**: [Labeling accuracy requirements]
- **Data Freshness**: [How often to retrain]
- **Feature Engineering**: [Key features required]

### Bias & Fairness
- **Demographic Parity**: Model performs equally across user segments
- **Evaluation Criteria**: Test against protected attributes
- **Mitigation Strategy**: [How to address identified biases]
- **Monitoring**: [Ongoing fairness assessment]

### Explainability
- **User Visibility**: How users understand AI decisions
- **Feature Importance**: What factors influenced the prediction
- **Confidence Scores**: When to show uncertainty
- **Human Override**: When users can override AI

### Model Monitoring
- **Performance Tracking**: [Metrics to monitor]
- **Drift Detection**: [When to trigger retraining]
- **A/B Testing**: [Gradual rollout strategy]
- **Fallback Behavior**: [What happens if model fails]

### Ethical Considerations
- **Transparency**: Users know when AI is involved
- **Consent**: Users can opt-out of AI features
- **Privacy**: No PII used without explicit consent
- **Accountability**: Clear ownership of AI decisions
- **Regulatory Compliance**: [GDPR, AI Act, industry-specific]

### Responsible AI Checklist
✓ Fairness evaluated across demographics  
✓ Explainability provided to users  
✓ Privacy by design implemented  
✓ Security measures in place  
✓ Human oversight maintained  
✓ Feedback mechanisms enabled  
✓ Documentation complete  
"""
    
    def _generate_ux_section(self, data: Dict[str, Any]) -> str:
        """Generate UX requirements section."""
        return f"""## User Experience

### Key User Flows
1. **Discovery Flow**: How users find the feature
   - Entry points: [Navigation, notifications, recommendations]
   - First-time user experience: [Onboarding flow]
   
2. **Core Usage Flow**: Primary interaction pattern
   - Happy path: [Step-by-step ideal scenario]
   - Alternative paths: [Different ways to accomplish goal]
   
3. **Error Recovery Flow**: Handling failures gracefully
   - Error prevention: [Input validation]
   - Error messages: [Clear, actionable guidance]
   - Recovery options: [How users can resolve issues]

### Design Principles
- **Simplicity**: Progressive disclosure of complexity
- **Clarity**: Clear labeling and instructions
- **Feedback**: Immediate response to user actions
- **Consistency**: Aligned with design system
- **Accessibility**: WCAG 2.1 AA compliance

### Mobile Considerations
- Responsive design for all screen sizes
- Touch-optimized interactions
- Offline capability where appropriate
- Performance on slower networks

### Accessibility Requirements
- Screen reader compatibility
- Keyboard navigation support
- Color contrast compliance
- Alt text for images
- Captions for media
"""
    
    def _generate_risk_assessment(self, data: Dict[str, Any]) -> str:
        """Generate risk assessment with mitigation strategies."""
        return f"""## Risk Assessment

### Technical Risks
| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|--------|---------------------|
| Performance degradation | Medium | High | Load testing, incremental rollout |
| Integration failures | Low | High | Comprehensive testing, fallback plans |
| Data quality issues | Medium | Medium | Validation rules, monitoring |

### Product Risks
| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|--------|---------------------|
| Low user adoption | Medium | High | User research, pilot testing |
| Feature not solving problem | Low | Critical | Prototype validation, feedback loops |
| Competitive response | High | Medium | Speed to market, unique value props |

### Business Risks
| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|--------|---------------------|
| Resource constraints | Medium | High | Phased delivery, MVP scope |
| Market timing | Low | Medium | Competitive analysis, user research |
| Regulatory changes | Low | High | Legal review, compliance monitoring |

### Rollback Plan
If critical issues arise post-launch:
1. **Immediate**: Feature flag to disable for all users
2. **Within 1 hour**: Root cause analysis and decision to fix or rollback
3. **Within 24 hours**: Communication to affected users
4. **Within 1 week**: Resolution or permanent rollback with alternative plan
"""
    
    def _generate_launch_plan(self, data: Dict[str, Any]) -> str:
        """Generate phased launch plan."""
        return f"""## Launch Plan

### Phase 1: Alpha (Internal)
- **Audience**: Internal team members (50 users)
- **Duration**: 2 weeks
- **Goals**: Validate core functionality, identify major bugs
- **Success Criteria**: < 5 P0 bugs, > 80% positive feedback

### Phase 2: Beta (Limited)
- **Audience**: Selected power users (500 users)
- **Duration**: 4 weeks
- **Goals**: Validate product-market fit, gather feedback
- **Success Criteria**: > 60% weekly active users, NPS > 40

### Phase 3: General Availability
- **Audience**: All eligible users (phased rollout)
- **Duration**: 4 weeks (25% → 50% → 75% → 100%)
- **Goals**: Scale safely, monitor metrics
- **Success Criteria**: Meet all primary KPIs, < 1% error rate

### Go/No-Go Criteria
Before proceeding to GA:
- ✓ All P0 and P1 bugs resolved
- ✓ Performance meets SLAs
- ✓ Security review approved
- ✓ Documentation complete
- ✓ Support team trained
- ✓ Monitoring and alerting in place
- ✓ Rollback plan tested

### Communication Plan
- **T-2 weeks**: Announce to internal stakeholders
- **T-1 week**: Email to beta users
- **Launch day**: Blog post, in-app announcement
- **T+1 week**: Results update to leadership
- **T+1 month**: Full retrospective
"""
    
    def _generate_stakeholder_matrix(self, data: Dict[str, Any]) -> str:
        """Generate RACI matrix for stakeholders."""
        return f"""## Stakeholder Matrix (RACI)

### Decision Rights

| Decision | Responsible | Accountable | Consulted | Informed |
|----------|-------------|-------------|-----------|----------|
| Product vision | PM | CPO | Design, Eng | All stakeholders |
| Technical approach | Eng Lead | CTO | PM, Design | Product team |
| Design decisions | Designer | Design Lead | PM, Eng | Stakeholders |
| Launch timing | PM | CPO | Eng, Marketing | Company |
| Success metrics | PM | CPO | Data, Eng | Leadership |

### Approval Required From
- **Product scope**: CPO, VP Engineering
- **Design**: Design Lead
- **Technical architecture**: CTO, Principal Engineer
- **Security & Privacy**: Security Lead, Legal
- **Go-to-Market**: VP Marketing, VP Sales

### Communication Cadence
- **Weekly**: PM → Engineering team (standup updates)
- **Bi-weekly**: PM → Design team (review sessions)
- **Monthly**: PM → Leadership (progress reports)
- **Quarterly**: PM → Company (roadmap updates)
"""
    
    def _generate_appendix(self, data: Dict[str, Any]) -> str:
        """Generate appendix with additional context."""
        return f"""## Appendix

### User Research Summary
{data.get('user_research_summary', 'See separate user research document for detailed findings.')}

### Competitive Landscape
{data.get('competitive_landscape', 'See competitive analysis document for market positioning.')}

### Alternatives Considered
1. **Alternative 1**: [Description]
   - Pros: [Advantages]
   - Cons: [Disadvantages]
   - Why not chosen: [Reason]

2. **Alternative 2**: [Description]
   - Pros: [Advantages]
   - Cons: [Disadvantages]
   - Why not chosen: [Reason]

### Open Questions
- [ ] Question 1: [To be resolved by whom/when]
- [ ] Question 2: [To be resolved by whom/when]
- [ ] Question 3: [To be resolved by whom/when]

### References
- [User Research Report](#)
- [Competitive Analysis](#)
- [Technical Design Doc](#)
- [Design Spec](#)

### Revision History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| {self.prd_version} | {datetime.now().strftime("%Y-%m-%d")} | PM | Initial draft |

---

*This PRD is a living document and will be updated as we learn more through development and user feedback.*
"""
    
    @staticmethod
    def calculate_rice_score(reach: int, impact: float, confidence: float, effort: float) -> float:
        """
        Calculate RICE prioritization score.
        
        Args:
            reach: Number of users/customers affected per time period
            impact: Degree of impact (0.25=minimal, 0.5=low, 1.0=medium, 2.0=high, 3.0=massive)
            confidence: Confidence level in estimates (0.0-1.0)
            effort: Estimated person-months of work
        
        Returns:
            RICE score (higher is better)
        """
        if effort == 0:
            return 0.0
        return (reach * impact * confidence) / effort
    
    @staticmethod
    def _format_target_users(users: Any) -> str:
        """Format target users for display."""
        if isinstance(users, list):
            return ", ".join(users)
        return str(users)
    
    @staticmethod
    def _format_list(items: List[str]) -> str:
        """Format list items as markdown bullets."""
        return "\n".join(f"- {item}" for item in items)


# Helper function for easy invocation
def generate_prd(input_data: Dict[str, Any]) -> str:
    """
    Convenience function to generate a PRD.
    
    Args:
        input_data: Feature requirements dictionary
    
    Returns:
        Complete PRD in Markdown format
    """
    generator = PRDGenerator()
    return generator.generate_prd(input_data)
