from abc import ABC, abstractmethod
from uuid import UUID
from .document import Document


class IDocumentRepository(ABC):
    @abstractmethod
    def add(self, document):
        pass

    @abstractmethod
    def delete(self, guid: UUID) -> Document:
        pass

    @abstractmethod
    def list(self) -> list[Document]:
        pass
