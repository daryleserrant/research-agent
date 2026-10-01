from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import Any
from typing import Any
from utils import utc_now
from enums import ActionStatus, ActionType, ExecutionStatus, SessionStatus, PlanStatus
from uuid import UUID, uuid4

@dataclass
class ResearchSession:
    id: UUID = field(default_factory=uuid4)
    research_id: UUID | None = None
    status: SessionStatus = SessionStatus.CREATED
    started_at: datetime = field(default_factory=utc_now)
    ended_at: datetime | None = None
    action_count: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    estimated_cost_usd: Decimal = Decimal("0")
    actual_cost_usd: Decimal = Decimal("0")
    pause_reason: str | None = None

@dataclass(frozen=True)
class ResearchBudget:
    target_actions: int
    target_tokens: int
    target_runtime_minutes: int
    max_cost_usd: Decimal

@dataclass
class ResearchPlan:
    id: UUID = field(default_factory=uuid4)
    research_id: UUID | None = None
    session_id: UUID | None = None
    objective: str = ""
    rationale: str | None = None
    status: PlanStatus = PlanStatus.ACTIVE
    version: int = 1
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

@dataclass
class ResearchAction:
    id: UUID = field(default_factory=uuid4)
    research_id: UUID | None = None
    session_id: UUID | None = None
    plan_id: UUID | None = None
    action_type: ActionType = ActionType.OTHER
    objective: str = ""
    rationale: str | None = None
    # Preferred tool, if already determined.
    tool_name: str | None = None
    status: ActionStatus = ActionStatus.PLANNED
    position: int = 0
    created_at: datetime = field(default_factory=utc_now)
    started_at: datetime | None = None
    completed_at: datetime | None = None

@dataclass
class ToolExecution:
    id: UUID = field(default_factory=uuid4)
    research_id: UUID | None = None
    session_id: UUID | None = None
    action_id: UUID | None = None
    tool_name: str = ""
    operation: str = ""
    arguments: dict[str, Any] = field(default_factory=dict)
    status: ExecutionStatus | None = None
    started_at: datetime = field(default_factory=utc_now)
    completed_at: datetime | None = None
    duration_ms: int | None = None
    # Accounting
    input_tokens: int | None = None
    output_tokens: int | None = None
    estimated_cost_usd: Decimal | None = None
    actual_cost_usd: Decimal | None = None
    error_code: str | None = None
    error_message: str | None = None
    # Small structured summary, NOT necessarily raw full output.
    result_summary: dict[str, Any] = field(default_factory=dict)
