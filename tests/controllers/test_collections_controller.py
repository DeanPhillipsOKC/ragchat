from uuid import uuid4
import pytest
from ragchat.application.use_cases.collections.dtos import ListCollectionsViewModel
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

@pytest.fixture
def list_fixture(sut):
    list_collections_vm1 = ListCollectionsViewModel(str(uuid4()), "foo", False)
    list_collections_vm2 = ListCollectionsViewModel(str(uuid4()), "bar", False)
    list_collections_vm3 = ListCollectionsViewModel(str(uuid4()), "baz", False)

    list_return_value = [
        list_collections_vm1,
        list_collections_vm2,
        list_collections_vm3
    ]

    sut.collection_use_cases.list.return_value = list_return_value

    return sut, list_return_value

def test_do_list(list_fixture, capsys):
    sut, list_return_value = list_fixture
    
    sut.do_list("")

    # Capture the output
    captured = capsys.readouterr()

    assert f"{list_return_value[0].id} foo" in captured.out
    assert f"{list_return_value[1].id} bar" in captured.out
    assert f"{list_return_value[2].id} baz" in captured.out

def test_do_list_prefixes_selected_collection_row_with_an_asterisk(list_fixture, capsys):
    # Arrange
    sut, list_return_value = list_fixture

    list_return_value[1].is_selected = True

    # Act
    sut.do_list("")
    captured = capsys.readouterr()

    # Assert
    assert f"* {list_return_value[1].id} bar" in captured.out

def test_do_list_displays_a_header(list_fixture, capsys):
    # Arrange
    sut, list_return_value = list_fixture

    # Act
    sut.do_list("")
    captured = capsys.readouterr()

    # Assert
    assert "ID                                     Name" in captured.out
    assert "----------------------------------------------------" in captured.out