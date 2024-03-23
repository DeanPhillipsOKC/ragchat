from typing import List
from uuid import UUID, uuid4
from ragchat.application.documents.dtos import ListDocumentsViewModel
from ragchat.application.events.event_dispatcher import EventDispatcher
from ragchat.domain.documents import Document, IDocumentRepository
from ragchat.domain.collections import ICollectionRepository
from ragchat.domain.documents.document_added_event import DocumentAddedEvent


class DocumentsUseCases:
    def __init__(
        self,
        repository: IDocumentRepository,
        collection_repository: ICollectionRepository,
        event_dispatcher: EventDispatcher,
    ):
        self.repository = repository
        self.collection_repository = collection_repository
        self.event_dispatcher = event_dispatcher

    def add(self, source: str, name: str) -> Document:
        collection_id = self.collection_repository.get_selected().id
        doc = Document(
            collection_id=collection_id,
            id=str(uuid4()),
            source=source,
            name=name,
        )

        try:
            self.repository.add(doc)
        except Exception as e:
            print(e)
            raise

        domain_event = DocumentAddedEvent(document=doc)
        self.event_dispatcher.emit(event=domain_event)

        return doc

    def delete(self, id: UUID) -> Document:
        deleted_doc = self.repository.delete(id)

        return deleted_doc

    def list(self) -> List[Document]:
        # TODO: Need to get a test written and get this fixed so that we don't
        # get an NRE if there is no selected collection

        collection_id = self.collection_repository.get_selected().id
        docs = self.repository.list(collection_id)

        docs_view_model = [
            ListDocumentsViewModel(
                id=str(doc.id), name=doc.name, type=doc.type
            )
            for doc in docs
        ]

        return docs_view_model
