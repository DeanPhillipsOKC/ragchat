from uuid import UUID
from ragchat.domain.documents import IDocumentRepository, Document


class InMemoryDocumentRepository(IDocumentRepository):

    def __init__(self):
        self._documents = {}

    def add(self, document):
        self._documents[document.id] = document

    def delete(self, guid: UUID) -> Document:
        if guid in self._documents:
            return self._documents.pop(guid)
        else:
            return None

    def list(self) -> list[Document]:
        return list(self._documents.values())
