from uuid import UUID
from ragchat.domain import ICollectionRepository, Collection


class InMemoryCollectionRepository(ICollectionRepository):
    _selected_collection_id = None

    def __init__(self):
        self._collections = {}

    def add(self, collection):
        self._collections[collection.id] = collection

    def delete(self, guid: UUID) -> Collection:
        if guid in self._collections:
            return self._collections.pop(guid)
        else:
            return None

    def list(self) -> list[Collection]:
        return list(self._collections.values())

    def select(self, guid: UUID):
        if guid in self._collections:
            InMemoryCollectionRepository._selected_collection_id = guid
            return self._collections[guid]
        else:
            return None

    def get_selected(self) -> Collection:
        if InMemoryCollectionRepository._selected_collection_id:
            return self._collections[
                InMemoryCollectionRepository._selected_collection_id
            ]
        else:
            return None
