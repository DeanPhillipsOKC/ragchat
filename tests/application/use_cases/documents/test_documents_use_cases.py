import pytest
from ragchat.application.use_cases.documents.use_cases import DocumentsUseCases
from ragchat.common.guid_utilities import is_uuid4

from ragchat.data.documents.in_memory_repository import InMemoryDocumentRepository


@pytest.fixture
def setup():
    repository = InMemoryDocumentRepository()
    sut = DocumentsUseCases(repository)

    return repository, sut


def test_add_a_new_document(setup):
    pass
