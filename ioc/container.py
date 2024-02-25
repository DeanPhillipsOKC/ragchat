from dependency_injector import containers, providers
from data.in_memory_collection_repository import InMemoryCollectionRepository
from application.use_cases.collection_use_cases import CollectionUseCases
from controllers.cli import CollectionsController
from controllers.cli import Cli

class Container(containers.DeclarativeContainer):
    collection_repository_factory = providers.Factory(
        InMemoryCollectionRepository
    )

    collection_use_cases_factory = providers.Factory(
        CollectionUseCases,
        collection_repository_factory
    )

    collections_controller_factory = providers.Factory(
        CollectionsController,
        collection_use_cases_factory
    )

    cli_factory = providers.Factory(
        Cli,
        collections_controller_factory
    )