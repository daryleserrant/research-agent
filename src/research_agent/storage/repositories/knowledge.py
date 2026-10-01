from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from research_agent.domain.enums import (
    ClaimStatus,
    EvidenceRelationship,
)
from research_agent.domain.knowledge import (
    Claim,
    ClaimEvidence,
    Evidence,
    Finding,
    ResearchFindingReference,
    Source,
)


class KnowledgeRepository(ABC):
    """
    Persistence interface for knowledge accumulated during research.

    Owns:
        - Sources
        - Findings
        - Claims
        - Evidence
        - Claim/evidence relationships
        - Cross-research finding references

    """

    # ---------------------------------------------------------
    # Sources
    # ---------------------------------------------------------

    @abstractmethod
    def add_source(
        self,
        research_id: UUID,
        source: Source,
        *,
        session_id: UUID | None = None,
        execution_id: UUID | None = None,
    ) -> Source:
        """
        Persist a source and associate it with an investigation.

        Implementations should reuse an existing canonical source
        when possible rather than creating unnecessary duplicates.
        """
        ...

    @abstractmethod
    def get_source(
        self,
        source_id: UUID,
    ) -> Source | None:
        """Load a source by ID."""
        ...

    @abstractmethod
    def list_sources(
        self,
        research_id: UUID,
    ) -> list[Source]:
        """Return sources associated with an investigation."""
        ...

    @abstractmethod
    def find_source(
        self,
        *,
        provider: str,
        external_id: str | None = None,
        canonical_url: str | None = None,
    ) -> Source | None:
        """
        Look for an existing canonical source.

        Primarily used for source deduplication.
        """
        ...

    # ---------------------------------------------------------
    # Findings
    # ---------------------------------------------------------

    @abstractmethod
    def add_finding(
        self,
        finding: Finding,
        *,
        source_ids: list[UUID] | None = None,
    ) -> Finding:
        """
        Persist a finding and optionally associate the sources
        from which it was derived.
        """
        ...

    @abstractmethod
    def get_finding(
        self,
        finding_id: UUID,
    ) -> Finding | None:
        """Load a finding by ID."""
        ...

    @abstractmethod
    def list_findings(
        self,
        research_id: UUID,
        *,
        subquestion_id: UUID | None = None,
    ) -> list[Finding]:
        """
        Return findings for an investigation, optionally limited
        to a particular subquestion.
        """
        ...

    @abstractmethod
    def add_sources_to_finding(
        self,
        finding_id: UUID,
        source_ids: list[UUID],
    ) -> None:
        """Attach additional source provenance to a finding."""
        ...

    @abstractmethod
    def list_finding_sources(
        self,
        finding_id: UUID,
    ) -> list[Source]:
        """Return the sources underlying a finding."""
        ...

    # ---------------------------------------------------------
    # Claims
    # ---------------------------------------------------------

    @abstractmethod
    def add_claim(
        self,
        claim: Claim,
    ) -> Claim:
        """Persist a claim."""
        ...

    @abstractmethod
    def get_claim(
        self,
        claim_id: UUID,
    ) -> Claim | None:
        """Load a claim by ID."""
        ...

    @abstractmethod
    def list_claims(
        self,
        research_id: UUID,
        *,
        subquestion_id: UUID | None = None,
        status: ClaimStatus | None = None,
    ) -> list[Claim]:
        """
        Return claims for an investigation with optional filters.
        """
        ...

    @abstractmethod
    def update_claim(
        self,
        claim: Claim,
    ) -> Claim:
        """
        Persist changes to a claim.

        Used for status, confidence, assessment, etc.
        """
        ...

    # ---------------------------------------------------------
    # Evidence
    # ---------------------------------------------------------

    @abstractmethod
    def add_evidence(
        self,
        evidence: Evidence,
    ) -> Evidence:
        """Persist an evidence object."""
        ...

    @abstractmethod
    def get_evidence(
        self,
        evidence_id: UUID,
    ) -> Evidence | None:
        """Load evidence by ID."""
        ...

    @abstractmethod
    def attach_evidence(
        self,
        claim_id: UUID,
        evidence_id: UUID,
        relationship: EvidenceRelationship,
        *,
        rationale: str | None = None,
    ) -> ClaimEvidence:
        """
        Associate evidence with a claim and describe how that
        evidence bears on the claim.
        """
        ...

    @abstractmethod
    def add_and_attach_evidence(
        self,
        claim_id: UUID,
        evidence: Evidence,
        relationship: EvidenceRelationship,
        *,
        rationale: str | None = None,
    ) -> ClaimEvidence:
        """
        Atomically persist evidence and associate it with a claim.

        This is a convenience operation for the common case where
        evidence is created specifically while evaluating a claim.
        """
        ...

    @abstractmethod
    def list_claim_evidence(
        self,
        claim_id: UUID,
    ) -> list[ClaimEvidence]:
        """Return evidence relationships for a claim."""
        ...

    @abstractmethod
    def list_evidence(
        self,
        research_id: UUID,
    ) -> list[Evidence]:
        """Return evidence accumulated by an investigation."""
        ...

    # ---------------------------------------------------------
    # Previous research
    # ---------------------------------------------------------

    @abstractmethod
    def reference_finding(
        self,
        research_id: UUID,
        finding_id: UUID,
        *,
        rationale: str | None = None,
    ) -> ResearchFindingReference:
        """
        Reference a finding produced by another investigation
        without copying that finding.
        """
        ...

    @abstractmethod
    def list_referenced_findings(
        self,
        research_id: UUID,
    ) -> list[Finding]:
        """Return prior findings referenced by this investigation."""
        ...