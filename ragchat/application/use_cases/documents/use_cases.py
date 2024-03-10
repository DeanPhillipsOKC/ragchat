from typing import List
from uuid import UUID, uuid4
from ragchat.domain.documents import Document, IDocumentRepository


class DocumentsUseCases:
    def __init__(self, repository: IDocumentRepository):
        self.repository = repository

    def add(self, source: str) -> Document:
        doc = Document(id=str(uuid4()), source=source)

        self.repository.add(doc)

        return doc

    def delete(self, id: UUID) -> Document:
        deleted_doc = self.repository.delete(id)

        return deleted_doc

    def list(self) -> List[Document]:
        docs = self.repository.list()

        return docs
