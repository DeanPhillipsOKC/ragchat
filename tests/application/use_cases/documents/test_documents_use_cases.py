from uuid import uuid4
import pytest
from ragchat.application.use_cases.documents.use_cases import DocumentsUseCases
from ragchat.common import is_uuid4

from ragchat.data.documents import InMemoryDocumentRepository
from ragchat.domain.documents import Document


@pytest.fixture
def setup():
    repository = InMemoryDocumentRepository()
    sut = DocumentsUseCases(repository)

    return repository, sut


def test_add_a_new_document(setup):
    # Arrange
    repository, sut = setup

    # Act
    returned_document = sut.add("https://www.google.com")

    # Assert
    assert is_uuid4(str(returned_document.id)), "New ID is not a UUID v4"
    assert returned_document.type == "html"
    assert returned_document.content is not None

    assert returned_document == repository._documents.get(returned_document.id)


def test_add_a_new_document_fails_when_source_is_invalid(setup):
    # Arrange
    repository, sut = setup

    # Act and Assert
    with pytest.raises(Exception):
        sut.add("NotValidPath")


def test_delete_a_document(setup):
    # Arrange
    repository, sut = setup

    # Act
    doc_to_delete = Document(id=uuid4(), source="https://www.google.com")
    repository._documents[doc_to_delete.id] = doc_to_delete

    deleted_doc = sut.delete(doc_to_delete.id)

    # Assert
    assert deleted_doc == doc_to_delete
    assert repository._documents.get(doc_to_delete.id) is None


def test_delete_a_document_returns_none_if_id_is_not_found(setup):
    # Arrange
    repository, sut = setup

    # Act
    deleted_doc = sut.delete(uuid4())

    # Assert
    assert deleted_doc is None


def test_delete_a_document_returns_non_if_id_is_not_specified(setup):
    # Arrange
    repository, sut = setup

    # Act
    deleted_doc = sut.delete(None)

    # Assert
    assert deleted_doc is None


def test_list_returns_list_of_documents(setup):
    # Arrange
    repository, sut = setup

    doc1 = Document(id=uuid4(), source="https://www.google.com")
    doc2 = Document(id=uuid4(), name="https://www.yahoo.com")

    repository._documents[doc1.id] = doc1
    repository._documents[doc2.id] = doc2

    # Act
    list_results = sut.list()

    # Assert
    list_expected = [doc1, doc2]

    for expected, result in zip(list_expected, list_results):
        assert expected.id == result.id
        assert expected.type == result.type
        assert expected.content == result.content


def test_list_returns_nothing_if_list_of_documents_is_empty(setup):
    # Arrange
    repository, sut = setup

    # Act
    list_results = sut.list()

    # Assert
    assert list_results == []
