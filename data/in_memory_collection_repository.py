from uuid import UUID
from domain.collections.collection_repository_interface import ICollectionRepository
from domain.collections.collection import Collection

class InMemoryCollectionRepository(ICollectionRepository):
    selected_collection_id = None

    def __init__(self):
        self.collections = {}
    
    def add(self, collection):
        self.collections[collection.id] = collection
    
    def list(self) -> list[Collection]:
        return list(self.collections.values())

    def select(self, guid: UUID):
        if guid in self.collections:
            InMemoryCollectionRepository.selected_collection_id = guid
            return self.collections[guid]
        else:
            return None

    def get_selected(self) -> Collection:
        if InMemoryCollectionRepository.selected_collection_id:
            return self.collections[InMemoryCollectionRepository.selected_collection_id]
        else:
            return None