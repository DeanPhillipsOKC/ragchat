from abc import ABC
import json
from typing import Generic, Type, TypeVar
from ragchat.domain.kernel import Entity

T = TypeVar("T", bound=Entity)


class SqLiteRepository(ABC, Generic[T]):
    def _entity_to_row(self, entity: T) -> tuple:
        # Serialize entity to JSON for storage
        data = entity.model_dump_json()
        return (str(entity.id), data)

    def _row_to_entity(self, row: tuple, entity_class: Type[T]) -> T:
        # Deserialize JSON back into an entity
        id_str, data_str = row
        data_dict = json.loads(data_str)
        return entity_class(**data_dict)
