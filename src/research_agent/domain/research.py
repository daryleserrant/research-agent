from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from utils import utc_now
from uuid import UUID, uuid4
from enums import OpenQuestionStatus, ResearchStatus, QuestionStatus, ClaimStatus, ClaimOrigin, EvidenceRelationship, EvidenceType, SourceType

@dataclass
class Research:
    id: UUID = field(default_factory=uuid4)
    main_question: str = ""
    status: ResearchStatus = ResearchStatus.NEW
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)
    completed_at: datetime | None = None
    # Lineage
    parent_research_id: UUID | None = None
    originating_open_question_id: UUID | None = None
    final_answer: str | None = None

@dataclass
class SubQuestion:
    id: UUID = field(default_factory=uuid4)
    research_id: UUID | None = None

    question: str = ""
    status: QuestionStatus = QuestionStatus.UNANSWERED

    answer: str | None = None
    resolution_reason: str | None = None

    required: bool = True
    position: int = 0

    created_at: datetime = field(default_factory=utc_now)
    resolved_at: datetime | None = None

@dataclass
class OpenQuestion:
    id: UUID = field(default_factory=uuid4)
    research_id: UUID | None = None
    question: str = ""
    rationale: str | None = None
    status: OpenQuestionStatus = OpenQuestionStatus.OPEN
    # If we later promote it to its own investigation:
    spawned_research_id: UUID | None = None
    created_at: datetime = field(default_factory=utc_now)

