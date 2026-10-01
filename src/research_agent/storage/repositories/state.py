from uuid import UUID
from research_agent.domain.state import ResearchState
from research_agent.storage.repositories.execution import ExecutionRepository
from research_agent.storage.repositories.knowledge import KnowledgeRepository
from research_agent.storage.repositories.research import ResearchRepository

class ResearchNotFoundError(Exception):
    """Raised when a requested research investigation does not exist."""

class ResearchStateRepository:
    """
    Assembles the current runtime state of a research investigation.

    This repository does not own persistence for individual domain
    entities. Instead, it composes ResearchRepository,
    KnowledgeRepository, and ExecutionRepository to construct the
    state needed by the research orchestrator.
    """

    def __init__(
        self,
        research_repo: ResearchRepository,
        knowledge_rep: KnowledgeRepository,
        execution_repo: ExecutionRepository,
    ):
        self.research_repo = research_repo
        self.knowledge_repo = knowledge_rep
        self.execution_repo = execution_repo

    def load(
        self,
        research_id: UUID,
        *,
        recent_action_limit: int = 10,
    ) -> ResearchState:
        """
        Load the current state of an investigation.

        Raises:
            ResearchNotFoundError:
                If the requested research investigation does not exist.
        """

        research = self.research_repo.get_research(research_id)

        if research is None:
            raise ResearchNotFoundError(
                f"Research investigation {research_id} was not found."
            )

        subquestions = self.research_repo.list_subquestions(
            research_id
        )

        open_questions = self.research_repo.list_open_questions(
            research_id
        )

        claims = self.knowledge_repo.list_claims(
            research_id
        )

        findings = self.knowledge_repo.list_findings(
            research_id
        )

        active_plan = self.execution_repo.get_active_plan(
            research_id
        )

        current_session = self.execution_repo.get_current_session(
            research_id
        )

        recent_actions = self.execution_repo.list_recent_actions(
            research_id,
            limit=recent_action_limit,
        )

        return ResearchState(
            research=research,
            subquestions=subquestions,
            claims=claims,
            findings=findings,
            open_questions=open_questions,
            active_plan=active_plan,
            current_session=current_session,
            recent_actions=recent_actions,
        )