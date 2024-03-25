from ragchat.domain.documents.document import Document
from ragchat.domain.kernel.domain_event_interface import IDomainEvent


class DocumentAddedEvent(IDomainEvent):
    def __init__(self, document: Document):
        self.document = document

    def get_event_name(self) -> str:
        return "document_added"
