
from dataclasses import dataclass
from research import Research, SubQuestion, OpenQuestion 
from knowledge import Claim, Finding
from execution import ResearchPlan, ResearchSession, ResearchAction

@dataclass
class ResearchState:
    research: Research
    subquestions: list[SubQuestion]
    claims: list[Claim]
    findings: list[Finding]
    open_questions: list[OpenQuestion]

    active_plan: ResearchPlan | None
    current_session: ResearchSession | None

    recent_actions: list[ResearchAction]