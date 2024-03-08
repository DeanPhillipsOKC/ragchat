from ragchat.domain.documents.document import Document
from ragchat.domain.documents.repository_interface import IDocumentRepository


class DocumentsUseCases:
    def __init__(self, repository: IDocumentRepository):
        self.repository = repository

    def add(self, source: str) -> Document:
        pass