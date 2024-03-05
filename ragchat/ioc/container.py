from dependency_injector import containers, providers
from ragchat.application.config.config_provider import ConfigProvider
from ragchat.controllers.utilities_controller import UtilitiesController
from ragchat.data.collections.in_memory_repository import InMemoryCollectionRepository
from ragchat.application.use_cases.collections.use_cases import CollectionsUseCases
from ragchat.controllers.cli import CollectionsController
from ragchat.controllers.cli import Cli
from ragchat.data.collections.sqlite_repository import SqLiteCollectionRepository

class Container(containers.DeclarativeContainer):
    config_provider = providers.Singleton(ConfigProvider, config_path='config.json')

    collection_repository_factory = providers.Factory(
        SqLiteCollectionRepository,
        config_provider
    )

    collection_use_cases_factory = providers.Factory(
        CollectionsUseCases,
        collection_repository_factory
    )

    collections_controller_factory = providers.Factory(
        CollectionsController,
        collection_use_cases_factory
    )

    utilities_controller_factory = providers.Factory(
        UtilitiesController,
        config_provider
    )

    cli_factory = providers.Factory(
        Cli,
        collections_controller_factory,
        utilities_controller_factory
    )