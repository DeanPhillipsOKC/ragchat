import pytest
from uuid import uuid4

from ragchat.domain.kernel.entity import Entity

class TestEntity(Entity):
    pass

def test_entity_hash():
    entity_id = uuid4()
    entity1 = TestEntity(id=entity_id)
    entity2 = TestEntity(id=entity_id)
    entity3 = TestEntity(id=uuid4())
    
    # Test that two entities with the same ID have the same hash
    assert hash(entity1) == hash(entity2), "Entities with the same ID should have the same hash"
    assert hash(entity1) != hash(entity3), "Entities with different IDs should not have the same hash."

def test_entity_equality():
    entity_id = uuid4()
    entity1 = TestEntity(id=entity_id)
    entity2 = TestEntity(id=entity_id)
    entity3 = TestEntity(id=uuid4())
    
    assert entity1 == entity2, "Entities with the same ID should be considered equal"
    assert entity1 != entity3, "Entities with different IDs should not be considered equal"

def test_entity_inequality_with_different_types():
    entity = TestEntity(id=uuid4())
    non_entity = "Not an entity"
    
    assert entity != non_entity, "Entity should not be considered equal to an object of a different type"
