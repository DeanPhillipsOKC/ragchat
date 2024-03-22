from xml.dom.minidom import Document
from ragchat.domain.kernel.domain_event_interface import IDomainEvent


class DocumentAddedEvent(IDomainEvent):
    def __init__(self, document: Document):
        self.document = document

    def get_event_name() -> str:
        return "document_added"
