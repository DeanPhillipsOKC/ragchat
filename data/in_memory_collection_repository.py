from domain.collections.collection_repository_interface import ICollectionRepository
from domain.collections.collection import Collection

class InMemoryCollectionRepository(ICollectionRepository):
    def __init__(self):
        self.collections = {}
    
    def add(self, collection):
        self.collections[collection.id] = collection
    
    def list(self):
        return list(self.collections.values())

    def select(self, guid):
        pass 