from ragchat.common.exceptions import EntityNotFoundException
from ragchat.domain.collections import ICollectionRepository, Collection
from ragchat.application.collections.dtos import ListCollectionsViewModel
from uuid import UUID, uuid4


class CollectionsUseCases:
    def __init__(self, repository: ICollectionRepository):
        self.repository = repository

    def add(self, name: str) -> Collection:
        if not name:
            raise ValueError(
                "In order to add a new collection, a name must be provided."
            )

        # Logic to add a collection
        collection = Collection(id=uuid4(), name=name)
        self.repository.add(collection)
        return collection

    def delete(self, id: UUID) -> Collection:
        if not id:
            raise ValueError(
                "In order to delete a collection, an ID must be " "provided."
            )

        deleted_collection = self.repository.delete(id)

        if not deleted_collection:
            raise EntityNotFoundException(id)

        return deleted_collection

    def list(self) -> list[ListCollectionsViewModel]:
        collections = self.repository.list()
        selected_collection = self.repository.get_selected()

        return [
            ListCollectionsViewModel(
                id=str(collection.id),
                name=collection.name,
                is_selected=selected_collection is not None
                and collection.id == selected_collection.id,
            )
            for collection in collections
        ]

    def select(self, id: UUID) -> Collection:
        if not id:
            raise ValueError(
                "In order to select a collection, an ID must be " "provided."
            )

        selected_collection = self.repository.select(id)

        if not selected_collection:
            raise EntityNotFoundException(id)

        return selected_collection
