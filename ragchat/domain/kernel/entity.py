from abc import ABC
from typing import Any
from uuid import UUID
from pydantic import BaseModel


class Entity(BaseModel, ABC):
    id: UUID

    def __hash__(self) -> int:
        # Use the hash of the unique `id` field for the hash value
        return hash(self.id)
    
    def __eq__(self, other: Any) -> bool:
        # Two instances are considered equal if they are of the same type and have the same `id`
        if isinstance(other, type(self)):
            return self.id == other.id
        return False
    
    class Config:
        # This makes Pydantic models behave as if they were immutable,
        # which is a requirement for instances to be hashable.
        frozen = True