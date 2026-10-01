from __future__ import annotations

from abc import ABC, abstractmethod
from decimal import Decimal
from uuid import UUID

from research_agent.domain.enums import (
    ActionStatus,
    ExecutionStatus,
    PlanStatus,
    SessionStatus,
)
from research_agent.domain.execution import (
    ResearchAction,
    ResearchPlan,
    ResearchSession,
    ToolExecution,
)


class ExecutionRepository(ABC):
    """
    Persistence interface for the execution history of an
    investigation.
    """

    # ---------------------------------------------------------
    # Sessions
    # ---------------------------------------------------------

    @abstractmethod
    def create_session(
        self,
        session: ResearchSession,
    ) -> ResearchSession:
        ...

    @abstractmethod
    def get_session(
        self,
        session_id: UUID,
    ) -> ResearchSession | None:
        ...

    @abstractmethod
    def get_current_session(
        self,
        research_id: UUID,
    ) -> ResearchSession | None:
        ...

    @abstractmethod
    def update_session(
        self,
        session: ResearchSession,
    ) -> ResearchSession:
        ...

    @abstractmethod
    def pause_session(
        self,
        session_id: UUID,
        status: SessionStatus,
        *,
        reason: str,
    ) -> ResearchSession:
        ...

    # ---------------------------------------------------------
    # Plans
    # ---------------------------------------------------------

    @abstractmethod
    def create_plan(
        self,
        plan: ResearchPlan,
    ) -> ResearchPlan:
        ...

    @abstractmethod
    def get_active_plan(
        self,
        research_id: UUID,
    ) -> ResearchPlan | None:
        ...

    @abstractmethod
    def supersede_plan(
        self,
        plan_id: UUID,
    ) -> None:
        ...

    # ---------------------------------------------------------
    # Actions
    # ---------------------------------------------------------

    @abstractmethod
    def add_action(
        self,
        action: ResearchAction,
    ) -> ResearchAction:
        ...

    @abstractmethod
    def get_action(
        self,
        action_id: UUID,
    ) -> ResearchAction | None:
        ...

    @abstractmethod
    def get_next_action(
        self,
        research_id: UUID,
    ) -> ResearchAction | None:
        """
        Return the next READY action according to plan ordering.
        """
        ...

    @abstractmethod
    def list_recent_actions(
        self,
        research_id: UUID,
        *,
        limit: int = 10,
    ) -> list[ResearchAction]:
        ...

    @abstractmethod
    def start_action(
        self,
        action_id: UUID,
    ) -> ResearchAction:
        ...

    @abstractmethod
    def complete_action(
        self,
        action_id: UUID,
    ) -> ResearchAction:
        ...

    @abstractmethod
    def fail_action(
        self,
        action_id: UUID,
        *,
        reason: str,
    ) -> ResearchAction:
        ...

    @abstractmethod
    def block_action(
        self,
        action_id: UUID,
        *,
        reason: str,
    ) -> ResearchAction:
        ...

    # ---------------------------------------------------------
    # Tool executions
    # ---------------------------------------------------------

    @abstractmethod
    def start_execution(
        self,
        execution: ToolExecution,
    ) -> ToolExecution:
        ...

    @abstractmethod
    def complete_execution(
        self,
        execution_id: UUID,
        *,
        status: ExecutionStatus,
        result_summary: dict,
        input_tokens: int | None = None,
        output_tokens: int | None = None,
        estimated_cost_usd: Decimal | None = None,
        actual_cost_usd: Decimal | None = None,
    ) -> ToolExecution:
        ...

    @abstractmethod
    def fail_execution(
        self,
        execution_id: UUID,
        *,
        status: ExecutionStatus,
        error_code: str | None = None,
        error_message: str | None = None,
    ) -> ToolExecution:
        ...

    @abstractmethod
    def list_executions_for_action(
        self,
        action_id: UUID,
    ) -> list[ToolExecution]:
        ...