from dependency_injector import containers, providers
from ragchat.data.in_memory_collection_repository import InMemoryCollectionRepository
from ragchat.application.use_cases.collections.use_cases import CollectionsUseCases
from ragchat.controllers.cli import CollectionsController
from ragchat.controllers.cli import Cli

class Container(containers.DeclarativeContainer):
    collection_repository_factory = providers.Factory(
        InMemoryCollectionRepository
    )

    collection_use_cases_factory = providers.Factory(
        CollectionsUseCases,
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