from abc import ABC, abstractmethod


class IEmbedder(ABC):
    @abstractmethod
    def embed_document(self, document_text: str) -> list[float]:
        pass

    @abstractmethod
    def embed_query(self, queyr: str) -> list[float]:
        pass
