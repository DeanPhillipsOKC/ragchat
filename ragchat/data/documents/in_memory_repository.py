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

    def list(self, collection_id: UUID) -> list[Document]:
        docs = self._documents.values()
        return list(filter(lambda d: (d.collection_id == collection_id), docs))
