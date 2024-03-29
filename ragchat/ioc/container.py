from dependency_injector import containers, providers
from ragchat.application.documents.use_cases import DocumentsUseCases
from ragchat.config import ConfigProvider
from ragchat.application.collections.use_cases import CollectionsUseCases
from ragchat.controllers.collections import CollectionsController
from ragchat.controllers.documents import DocumentsController
from ragchat.controllers.utilities import UtilitiesController
from ragchat.controllers.cli import Cli
from ragchat.data import SqLiteCollectionRepository, SqLiteDocumentRepository


class Container(containers.DeclarativeContainer):
    config_provider = providers.Singleton(
        ConfigProvider, config_path="config.json"
    )

    collection_repository_factory = providers.Factory(
        SqLiteCollectionRepository, config_provider
    )

    document_repository_factory = providers.Factory(
        SqLiteDocumentRepository, config_provider
    )

    collection_use_cases_factory = providers.Factory(
        CollectionsUseCases, collection_repository_factory
    )

    document_use_case_factory = providers.Factory(
        DocumentsUseCases,
        document_repository_factory,
        collection_repository_factory,
    )

    collections_controller_factory = providers.Factory(
        CollectionsController, collection_use_cases_factory
    )

    documents_controller_factory = providers.Factory(
        DocumentsController, document_use_case_factory
    )

    utilities_controller_factory = providers.Factory(
        UtilitiesController, config_provider
    )

    cli_factory = providers.Factory(
        Cli,
        collections_controller_factory,
        utilities_controller_factory,
        documents_controller_factory,
    )
