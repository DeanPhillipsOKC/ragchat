from uuid import uuid4
import pytest
from ragchat.application.documents.dtos import ListDocumentsViewModel
from ragchat.application.documents.use_cases import DocumentsUseCases
from ragchat.common import is_uuid4

from ragchat.data.collections import InMemoryCollectionRepository
from ragchat.data.documents import InMemoryDocumentRepository
from ragchat.domain.collections import Collection
from ragchat.domain.documents import Document


@pytest.fixture
def setup():
    repository = InMemoryDocumentRepository()
    collection_repository = InMemoryCollectionRepository()
    sut = DocumentsUseCases(repository, collection_repository)

    collection = Collection(id=uuid4(), name="foo")

    collection_repository.add(collection=collection)
    collection_repository.select(collection.id)

    return repository, sut, collection, collection_repository


def test_add_a_new_document(setup):
    # Arrange
    repository, sut, selected_collection, collection_repository = setup
    source = "https://www.google.com"
    name = "Test Doc"

    # Act
    returned_document = sut.add(source=source, name=name)

    # Assert
    assert is_uuid4(str(returned_document.id)), "New ID is not a UUID v4"
    assert returned_document.type == "html"
    assert returned_document.content is not None

    assert returned_document == repository._documents.get(returned_document.id)
    assert returned_document.collection_id == selected_collection.id


def test_add_a_new_document_fails_when_source_is_invalid(setup):
    # Arrange
    repository, sut, selected_collection, collection_repository = setup
    source = "NotValidPath"
    name = "some doc"

    # Act and Assert
    with pytest.raises(Exception):
        sut.add(source=source, name=name)


def test_add_a_new_document_fails_when_name_is_missing(setup):
    # Arrange
    repository, sut, selected_collection, collection_repository = setup
    source = "https://www.google.com"
    name = None

    # Act and Assert
    with pytest.raises(Exception):
        sut.add(source=source, name=name)


def test_delete_a_document(setup):
    # Arrange
    repository, sut, selected_collection, collection_repository = setup

    # Act
    doc_to_delete = Document(
        id=uuid4(),
        collection_id=selected_collection.id,
        source="https://www.google.com",
        name="Google",
    )
    repository._documents[doc_to_delete.id] = doc_to_delete

    deleted_doc = sut.delete(doc_to_delete.id)

    # Assert
    assert deleted_doc == doc_to_delete
    assert repository._documents.get(doc_to_delete.id) is None


def test_delete_a_document_returns_none_if_id_is_not_found(setup):
    # Arrange
    repository, sut, selected_collection, collection_repository = setup

    # Act
    deleted_doc = sut.delete(uuid4())

    # Assert
    assert deleted_doc is None


def test_delete_a_document_returns_non_if_id_is_not_specified(setup):
    # Arrange
    repository, sut, selected_collection, collection_repository = setup

    # Act
    deleted_doc = sut.delete(None)

    # Assert
    assert deleted_doc is None


def test_list_returns_list_of_documents(setup):
    # Arrange
    repository, sut, selected_collection, collection_repository = setup

    doc1 = Document(
        id=uuid4(),
        collection_id=selected_collection.id,
        source="https://www.google.com",
        name="doc1",
    )
    doc2 = Document(
        id=uuid4(),
        collection_id=selected_collection.id,
        source="https://www.yahoo.com",
        name="doc2",
    )

    repository._documents[doc1.id] = doc1
    repository._documents[doc2.id] = doc2

    # Act
    list_results = sut.list(selected_collection.id)

    # Assert
    list_expected = [
        ListDocumentsViewModel(
            id=str(doc1.id), name=doc1.name, type=doc1.type
        ),
        ListDocumentsViewModel(
            id=str(doc2.id), name=doc2.name, type=doc2.type
        ),
    ]

    for expected, result in zip(list_expected, list_results):
        assert expected.id == result.id
        assert expected.name == result.name
        assert expected.type == result.type


def test_list_returns_nothing_if_list_of_documents_is_empty(setup):
    # Arrange
    repository, sut, selected_collection, collection_repository = setup

    # Act
    list_results = sut.list(selected_collection.id)

    # Assert
    assert list_results == []


def test_list_only_returns_documents_in_the_selected_collection(setup):
    # Arrange
    repository, sut, selected_collection, collection_repository = setup

    bar_collection = Collection(id=uuid4(), name="bar")
    baz_collection = Collection(id=uuid4(), name="baz")

    collection_repository.add(bar_collection)
    collection_repository.add(baz_collection)

    foo_doc = Document(
        id=uuid4(),
        collection_id=selected_collection.id,
        source="https://www.google.com",
        name="Foo Doc",
    )
    bar_doc = Document(
        id=uuid4(),
        collection_id=bar_collection.id,
        source="https://www.google.com",
        name="Bar Doc",
    )
    baz_doc = Document(
        id=uuid4(),
        collection_id=bar_collection.id,
        source="https://www.google.com",
        name="Baz Doc",
    )

    repository._documents[foo_doc.id] = foo_doc
    repository._documents[bar_doc.id] = bar_doc
    repository._documents[baz_doc.id] = baz_doc

    # Act
    list_results = sut.list(selected_collection.id)

    # Assert
    assert len(list_results) == 1
