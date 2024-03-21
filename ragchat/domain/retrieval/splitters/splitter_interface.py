from abc import ABC, abstractmethod

from ragchat.domain.documents import Document


class IHtmlSplitterInterface(ABC):
    @abstractmethod
    def split(self, html: str) -> list[Document]:
        pass
