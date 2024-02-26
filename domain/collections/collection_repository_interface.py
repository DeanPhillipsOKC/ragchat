from abc import ABC, abstractmethod
from .collection import Collection

class ICollectionRepository(ABC):
    @abstractmethod
    def add(self, collection): pass

    @abstractmethod
    def list(self) -> list[Collection]: pass

    @abstractmethod
    def select(self, guid): pass