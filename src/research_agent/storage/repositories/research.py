from abc import ABC, abstractmethod
from uuid import UUID
from research_agent.domain.research import Research, SubQuestion, OpenQuestion


class ResearchRepository(ABC):

    @abstractmethod
    def create_research(
        self,
        research: Research,
    ) -> Research:
        ...

    @abstractmethod
    def get_research(
        self,
        research_id: UUID,
    ) -> Research | None:
        ...

    @abstractmethod
    def update_research(
        self,
        research: Research,
    ) -> Research:
        ...

    @abstractmethod
    def add_subquestion(
        self,
        subquestion: SubQuestion,
    ) -> SubQuestion:
        ...

    @abstractmethod
    def get_subquestion(
        self,
        subquestion_id: UUID,
    ) -> SubQuestion | None:
        ...

    @abstractmethod
    def list_subquestions(
        self,
        research_id: UUID,
    ) -> list[SubQuestion]:
        ...

    @abstractmethod
    def update_subquestion(
        self,
        subquestion: SubQuestion,
    ) -> SubQuestion:
        ...

    @abstractmethod
    def add_open_question(
        self,
        question: OpenQuestion,
    ) -> OpenQuestion:
        ...

    @abstractmethod
    def list_open_questions(
        self,
        research_id: UUID,
    ) -> list[OpenQuestion]:
        ...

    @abstractmethod
    def list_incomplete(self) -> list[Research]:
        ...