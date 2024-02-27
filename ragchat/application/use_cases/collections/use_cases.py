from ragchat.domain.collections.collection_repository_interface import ICollectionRepository
from ragchat.domain.collections.collection import Collection
from .dtos import ListCollectionsViewModel
from uuid import UUID, uuid4

class CollectionsUseCases:
    def __init__(self, repository: ICollectionRepository):
        self.repository = repository

    def add(self, name: str) -> Collection:
        # Logic to add a collection
        collection = Collection(id=uuid4(), name=name)
        self.repository.add(collection)
        return collection

    def delete(self, id: UUID) -> Collection:
        return self.repository.delete(id)

    def list(self) -> list[ListCollectionsViewModel]:
        collections = self.repository.list()
        selected_collection = self.repository.get_selected()

        return [
            ListCollectionsViewModel(
                id=str(collection.id), 
                name=collection.name, 
                is_selected=
                    selected_collection != None and collection.id == selected_collection.id
            ) for collection in collections
        ]
    
    def select(self, id: UUID) -> Collection:
        return self.repository.select(id)
        