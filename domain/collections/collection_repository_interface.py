from abc import ABC, abstractmethod

class ICollectionRepository(ABC):
    @abstractmethod
    def add(self, collection): pass

    @abstractmethod
    def list(self): pass

    @abstractmethod
    def select(self, guid): pass