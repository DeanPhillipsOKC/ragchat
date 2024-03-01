from abc import ABC, abstractmethod
from uuid import UUID
from .collection import Collection

class ICollectionRepository(ABC):
    @abstractmethod
    def add(self, collection): pass

    @abstractmethod
    def delete(self, guid: UUID) -> Collection: pass

    @abstractmethod
    def list(self) -> list[Collection]: pass

    @abstractmethod
    def select(self, guid: UUID) -> Collection: pass

    @abstractmethod
    def get_selected(self) -> Collection: pass