from abc import ABC
from typing import Any
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class Entity(BaseModel, ABC):
    model_config = ConfigDict(from_attributes=True, frozen=True)

    id: UUID

    def __hash__(self) -> int:
        # Use the hash of the unique `id` field for the hash value
        return hash(self.id)
    
    def __eq__(self, other: Any) -> bool:
        # Two instances are considered equal if they are of the same type and have the same `id`
        if isinstance(other, type(self)):
            return self.id == other.id