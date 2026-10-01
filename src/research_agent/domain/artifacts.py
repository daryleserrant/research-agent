from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from utils import utc_now
from enums import ArtifactType, ReportStatus
from uuid import UUID, uuid4

@dataclass
class Artifact:
    id: UUID = field(default_factory=uuid4)
    research_id: UUID | None = None
    session_id: UUID | None = None
    execution_id: UUID | None = None
    artifact_type: ArtifactType = ArtifactType.OTHER
    name: str = ""
    uri: str = ""
    mime_type: str | None = None
    created_at: datetime = field(default_factory=utc_now)

@dataclass
class ResearchReport:
    id: UUID = field(default_factory=uuid4)
    research_id: UUID | None = None
    version: int = 1
    status: ReportStatus = ReportStatus.DRAFT
    title: str = ""
    executive_summary: str = ""
    main_answer: str = ""
    limitations: list[str] = field(default_factory=list)
    # Structured representation used for rendering.
    content: dict[str, Any] = field(default_factory=dict)
    artifact_uri: str | None = None
    created_at: datetime = field(default_factory=utc_now)
    finalized_at: datetime | None = None
    delivered_at: datetime | None = None