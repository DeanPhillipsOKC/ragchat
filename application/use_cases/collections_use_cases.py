from domain.collections.collection_repository_interface import ICollectionRepository
from domain.collections.collection import Collection
from uuid import uuid4

class CollectionsUseCases:
    def __init__(self, repository: ICollectionRepository):
        self.repository = repository

    def add_collection(self, name: str) -> Collection:
        # Logic to add a collection
        collection = Collection(id=uuid4(), name=name)
        self.repository.add(collection)
        return collection

    def list_collection(self) -> list[Collection]:
        return self.repository.list()
    
    def select_collection(self, guid) -> Collection:
        return self.repository.select(guid)
        