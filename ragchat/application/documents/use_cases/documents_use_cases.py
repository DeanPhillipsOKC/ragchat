from typing import List
from uuid import UUID, uuid4
from ragchat.application.documents.dtos import ListDocumentsViewModel
from ragchat.domain.documents import Document, IDocumentRepository
from ragchat.domain.collections import ICollectionRepository


class DocumentsUseCases:
    def __init__(
        self,
        repository: IDocumentRepository,
        collection_repository: ICollectionRepository,
    ):
        self.repository = repository
        self.collection_repository = collection_repository

    def add(self, source: str, name: str) -> Document:
        collection_id = self.collection_repository.get_selected().id
        doc = Document(
            collection_id=collection_id,
            id=str(uuid4()),
            source=source,
            name=name,
        )

        self.repository.add(doc)

        return doc

    def delete(self, id: UUID) -> Document:
        deleted_doc = self.repository.delete(id)

        return deleted_doc

    def list(self) -> List[Document]:
        collection_id = self.collection_repository.get_selected().id
        docs = self.repository.list(collection_id)

        docs_view_model = [
            ListDocumentsViewModel(
                id=str(doc.id), name=doc.name, type=doc.type
            )
            for doc in docs
        ]

        return docs_view_model
