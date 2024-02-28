from uuid import uuid4
import pytest
from ragchat.application.use_cases.collections.dtos import ListCollectionsViewModel
from ragchat.application.use_cases.collections.use_cases import CollectionsUseCases
from ragchat.common.exceptions.entity_not_found_exception import EntityNotFoundException
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

@pytest.fixture
def delete_collection_fixture(setup):
    repository, sut = setup

    collection = Collection(uuid4(), "Test")
    repository._collections[collection.id] = collection

    return repository, sut, collection

def test_delete_a_collection(delete_collection_fixture):
    repository, sut, collection = delete_collection_fixture

    sut.delete(collection.id)

    assert collection not in repository._collections
    assert not repository._collections

def test_delete_a_collection_fails_if_id_is_not_provided(delete_collection_fixture):
    repository, sut, collection = delete_collection_fixture

    with pytest.raises(ValueError):
        sut.delete(None)

def test_delete_a_collection_fails_if_id_is_invalid(delete_collection_fixture):
    repository, sut, collection = delete_collection_fixture

    with pytest.raises(EntityNotFoundException):
        sut.delete(uuid4())

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
 
@pytest.fixture
def select_collection_fixture(setup):
    repository, sut = setup

    collection1 = Collection(uuid4(), "Test1")
    collection2 = Collection(uuid4(), "Test2")

    repository._collections[collection1.id] = collection1
    repository._collections[collection2.id] = collection2

    return repository, sut, collection1, collection2

def test_select_collection(select_collection_fixture):
    repository, sut, collection1, collection2 = select_collection_fixture

    selected_collection = sut.select(collection2.id)

    assert selected_collection.id == collection2.id
    assert selected_collection.name == collection2.name

def test_select_collection_fails_if_id_not_provided(select_collection_fixture):
    repository, sut, collection1, collection2 = select_collection_fixture

    with pytest.raises(ValueError):
        selected_collection = sut.select(None)

def test_select_collection_fails_if_id_invalid(select_collection_fixture):
    repository, sut, collection1, collection2 = select_collection_fixture

    with pytest.raises(EntityNotFoundException):
        selected_collection = sut.select(uuid4())