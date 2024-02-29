from uuid import uuid4
import pytest
from ragchat.application.use_cases.collections.use_cases import CollectionsUseCases
from ragchat.controllers.collections_controller import CollectionsController
from ragchat.domain.collections.collection import Collection

@pytest.fixture
def mock_use_cases(mocker):
    return mocker.Mock(spec=CollectionsUseCases)

@pytest.fixture
def sut(mock_use_cases):
    return CollectionsController(collection_use_cases=mock_use_cases)

@pytest.fixture
def add_fixture(sut):
    collection = Collection(uuid4(), "Test Collection")
    sut.collection_use_cases.add.return_value = collection

    return sut, collection

def test_do_add(add_fixture, capsys):    
    sut, collection = add_fixture

    sut.do_add("Test Collection")

    assert capsys.readouterr().out == f"Added a new collection with ID: {str(collection.id)}\n"

def test_do_add_fails_if_name_not_provided(add_fixture, capsys):
    sut, collection = add_fixture

    sut.do_add(None)

    assert capsys.readouterr().out == "Error: The 'add' command requires a name for the new collection.\nUsage: add <name>\n"

@pytest.fixture
def delete_fixture(sut):
    collection = Collection(uuid4(), "Test Collection")
    sut.collection_use_cases.delete.return_value = collection

    return sut, collection

def test_do_delete(delete_fixture, capsys):
    sut, collection = delete_fixture

    sut.do_delete(str(collection.id))

    assert capsys.readouterr().out == f"Deleted colection with ID: {str(collection.id)} and Name: {collection.name}\n"

def test_do_delete_fails_if_id_not_supplied(delete_fixture, capsys):
    sut, collection = delete_fixture

    sut.do_delete(None)

    assert capsys.readouterr().out == f"Error: The 'delete' command requires a collection ID.\nUsage: delete <ID>\n"

def test_do_delete_fails_if_id_not_valid(delete_fixture, capsys):
    sut, collection = delete_fixture

    sut.do_delete("Not a valid UUID")

    assert capsys.readouterr().out == f"Error: The 'delete' command requires a valid collection ID (UUID v4)\nUsage: delete <ID>\n"

def test_do_delete_fails_if_id_does_not_match_a_known_collection(delete_fixture, capsys):
    sut, collection = delete_fixture
    sut.collection_use_cases.delete.return_value = None

    sut.do_delete(str(collection.id))

    assert capsys.readouterr().out == f"Error: Could not find a collection with ID: {collection.id} to delete.\n"