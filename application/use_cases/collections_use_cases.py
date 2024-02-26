from domain.collections.collection_repository_interface import ICollectionRepository

class CollectionsUseCases:
    def __init__(self, repository: ICollectionRepository):
        self.repository = repository

    def add_collection(self, name):
        # Logic to add a collection
        print(f"In add_collection with name of {name}")

    def list_collection(self):
        self.repository.list()
    
    def select_collection(self, guid):
        # return self.repository.select(guid)
        pass