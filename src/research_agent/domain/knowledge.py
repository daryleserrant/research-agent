from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import UUID, uuid4
from utils import utc_now
from enums import ClaimOrigin, ClaimStatus, EvidenceType, EvidenceRelationship, OpenQuestionStatus, QuestionStatus, ResearchStatus, SourceType


@dataclass
class Source:
    id: UUID = field(default_factory=uuid4)
    research_id: UUID | None = None
    source_type: SourceType = SourceType.OTHER
    provider: str = ""
    title: str = ""
    url: str | None = None
    external_id: str | None = None
    authors: list[str] = field(default_factory=list)
    published_at: datetime | None = None
    retrieved_at: datetime = field(default_factory=utc_now)
    # Useful for archive snapshots, versions, etc.
    version: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class Finding:
    id: UUID = field(default_factory=uuid4)
    research_id: UUID | None = None
    subquestion_id: UUID | None = None
    statement: str = ""
    # The action responsible for producing this finding.
    action_id: UUID | None = None
    created_at: datetime = field(default_factory=utc_now)

@dataclass
class Claim:
    id: UUID = field(default_factory=uuid4)
    research_id: UUID | None = None
    subquestion_id: UUID | None = None

    statement: str = ""

    origin: ClaimOrigin = ClaimOrigin.AGENT_DERIVED
    status: ClaimStatus = ClaimStatus.UNVERIFIED

    # 0.0–1.0, but optional.
    confidence: float | None = None

    # Provenance for agent-derived claims
    origin_finding_id: UUID | None = None
    origin_source_id: UUID | None = None
    origin_research_id: UUID | None = None

    assessment: str | None = None

    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

@dataclass
class Evidence:
    id: UUID = field(default_factory=uuid4)
    research_id: UUID | None = None
    evidence_type: EvidenceType = EvidenceType.SOURCE_EXCERPT

    # One or the other normally provides provenance.
    source_id: UUID | None = None
    finding_id: UUID | None = None
    content: str = ""

    # e.g. "Section 4.2", "Table 3", lines, timestamp, etc.
    location: str | None = None
    created_at: datetime = field(default_factory=utc_now)


@dataclass
class ClaimEvidence:
    claim_id: UUID
    evidence_id: UUID
    relationship: EvidenceRelationship
    rationale: str | None = None
    created_at: datetime = field(default_factory=utc_now)

@dataclass
class ResearchFindingReference:
    research_id: UUID
    finding_id: UUID
    rationale: str | None = None
    created_at: datetime = field(default_factory=utc_now)
