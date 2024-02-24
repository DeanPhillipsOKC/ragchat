from dependency_injector import containers, providers
from data.in_memory_collection_repository import InMemoryCollectionRepository
from application.use_cases.collection_use_cases import CollectionUseCases

class Container(containers.DeclarativeContainer):
    collection_repository = providers.Factory(
        InMemoryCollectionRepository
    )

    collection_use_cases = providers.Factory(
        CollectionUseCases,
        collection_repository
    )