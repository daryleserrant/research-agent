from __future__ import annotations
from datetime import datetime, timezone
from enum import StrEnum

class ResearchStatus(StrEnum):
    NEW = "new"
    PLANNING = "planning"
    IN_PROGRESS = "in_progress"
    PAUSED = "paused"
    PAUSED_BUDGET = "paused_budget"
    BLOCKED = "blocked"
    COMPLETED = "completed"
    FAILED = "failed"

class SessionStatus(StrEnum):
    CREATED = "created"
    RUNNING = "running"
    SOFT_LIMIT_REACHED = "soft_limit_reached"
    BUDGET_EXHAUSTED = "budget_exhausted"
    HUMAN_INPUT_REQUIRED = "human_input_required"
    COMPLETED = "completed"
    FAILED = "failed"

class QuestionStatus(StrEnum):
    UNANSWERED = "unanswered"
    INVESTIGATING = "investigating"
    ANSWERED = "answered"
    INSUFFICIENT_EVIDENCE = "insufficient_evidence"

class ClaimStatus(StrEnum):
    UNVERIFIED = "unverified"
    INVESTIGATING = "investigating"
    SUPPORTED = "supported"
    PARTIALLY_SUPPORTED = "partially_supported"
    CONTRADICTED = "contradicted"
    INSUFFICIENT_EVIDENCE = "insufficient_evidence"

class ClaimOrigin(StrEnum):
    USER_PROVIDED = "user_provided"
    AGENT_DERIVED = "agent_derived"
    SOURCE_DERIVED = "source_derived"
    PRIOR_RESEARCH = "prior_research"

class EvidenceRelationship(StrEnum):
    SUPPORTS = "supports"
    CONTRADICTS = "contradicts"
    QUALIFIES = "qualifies"
    CONTEXTUALIZES = "contextualizes"

class EvidenceType(StrEnum):
    SOURCE_EXCERPT = "source_excerpt"
    SOURCE_DATA = "source_data"
    DERIVED_FINDING = "derived_finding"
    PRIOR_RESEARCH_FINDING = "prior_research_finding"

class SourceType(StrEnum):
    WEB_PAGE = "web_page"
    ACADEMIC_PAPER = "academic_paper"
    PDF = "pdf"
    DATASET = "dataset"
    YOUTUBE_VIDEO = "youtube_video"
    REDDIT_THREAD = "reddit_thread"
    HACKER_NEWS_THREAD = "hacker_news_thread"
    GITHUB_REPOSITORY = "github_repository"
    GITHUB_ISSUE = "github_issue"
    ARCHIVED_PAGE = "archived_page"
    RADAR_RECORD = "radar_record"
    OTHER = "other"

class ActionType(StrEnum):
    SEARCH = "search"
    READ = "read"
    ANALYZE = "analyze"
    COMPARE = "compare"
    VERIFY = "verify"
    CHALLENGE = "challenge"
    FOLLOW_CITATION = "follow_citation"
    SYNTHESIZE = "synthesize"
    OTHER = "other"

class ActionStatus(StrEnum):
    PLANNED = "planned"
    READY = "ready"
    RUNNING = "running"
    COMPLETED = "completed"
    SKIPPED = "skipped"
    BLOCKED = "blocked"
    FAILED = "failed"

class ExecutionStatus(StrEnum):
    SUCCESS = "success"
    EMPTY = "empty"
    RATE_LIMITED = "rate_limited"
    TEMPORARY_FAILURE = "temporary_failure"
    PERMANENT_FAILURE = "permanent_failure"
    MISSING_DEPENDENCY = "missing_dependency"
    HUMAN_INPUT_REQUIRED = "human_input_required"
    TIMEOUT = "timeout"

class PlanStatus(StrEnum):
    ACTIVE = "active"
    SUPERSEDED = "superseded"
    COMPLETED = "completed"
    ABANDONED = "abandoned"

class OpenQuestionStatus(StrEnum):
    OPEN = "open"
    PROMOTED_TO_RESEARCH = "promoted_to_research"
    DISMISSED = "dismissed"

class ReportStatus(StrEnum):
    DRAFT = "draft"
    FINAL = "final"
    DELIVERY_PENDING = "delivery_pending"
    DELIVERED = "delivered"
    DELIVERY_FAILED = "delivery_failed"

class ArtifactType(StrEnum):
    CHART = "chart"
    DATASET = "dataset"
    TABLE = "table"
    CODE = "code"
    REPORT = "report"
    OTHER = "other"