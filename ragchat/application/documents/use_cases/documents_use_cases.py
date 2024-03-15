from typing import List
from uuid import UUID, uuid4
from ragchat.application.documents.dtos import ListDocumentsViewModel
from ragchat.domain.documents import Document, IDocumentRepository


class DocumentsUseCases:
    def __init__(self, repository: IDocumentRepository):
        self.repository = repository

    def add(self, source: str, name: str) -> Document:
        doc = Document(id=str(uuid4()), source=source, name=name)

        self.repository.add(doc)

        return doc

    def delete(self, id: UUID) -> Document:
        deleted_doc = self.repository.delete(id)

        return deleted_doc

    def list(self) -> List[Document]:
        docs = self.repository.list()

        docs_view_model = [
            ListDocumentsViewModel(
                id=str(doc.id), name=doc.name, type=doc.type
            )
            for doc in docs
        ]

        return docs_view_model
