from uuid import uuid4
import pytest
from ragchat.application.use_cases.collections.dtos import ListCollectionsViewModel
from ragchat.application.use_cases.collections.use_cases import CollectionsUseCases
from ragchat.common.guid_utilities import is_uuid4
from ragchat.data.in_memory_collection_repository import InMemoryCollectionRepository
from ragchat.domain.collections.collection import Collection

@pytest.fixture
def setup():
    repository = InMemoryCollectionRepository()
    sut = CollectionsUseCases(repository)

    yield repository, sut

def test_add_a_new_collection(setup):
    repository, sut = setup

    new_collection = sut.add("Test Collection")
    assert new_collection.name == "Test Collection"
    assert is_uuid4(str(new_collection.id)), "New ID is not a UUID v4"
    assert new_collection.id in repository._collections

def test_add_a_new_collection_fails_if_name_is_not_provided(setup):
    repository, sut = setup

    with pytest.raises(ValueError):
        sut.add(None)

def test_delete_a_collection(setup):
    repository, sut = setup

    collection = Collection(uuid4(), "Test")
    repository._collections[collection.id] = collection

    sut.delete(collection.id)

    assert collection not in repository._collections
    assert not repository._collections

def test_delete_a_collection_fails_if_id_is_not_provided(setup):
    repository, sut = setup

    collection = Collection(uuid4(), "Test")
    repository._collections[collection.id] = collection

    with pytest.raises(ValueError):
        sut.delete(None)

def test_list_collections(setup):
    repository, sut = setup

    collection1 = Collection(uuid4(), "Test1")
    collection2 = Collection(uuid4(), "test2")

    repository._collections[collection1.id] = collection1
    repository._collections[collection2.id] = collection2
    InMemoryCollectionRepository._selected_collection_id = collection2.id

    list_results = sut.list()

    list_expected = [
        ListCollectionsViewModel(str(collection1.id), collection1.name, False),
        ListCollectionsViewModel(str(collection2.id), collection2.name, True)
    ]
    
    for expected, result in zip(list_expected, list_results):
        assert expected.id == result.id
        assert expected.name == result.name
        assert expected.is_selected == result.is_selected
 
def test_select_collection(setup):
    repository, sut = setup

    collection1 = Collection(uuid4(), "Test1")
    collection2 = Collection(uuid4(), "Test2")

    repository._collections[collection1.id] = collection1
    repository._collections[collection2.id] = collection2

    selected_collection = sut.select(collection2.id)
    print(selected_collection)

    assert selected_collection.id == collection2.id
    assert selected_collection.name == collection2.name
