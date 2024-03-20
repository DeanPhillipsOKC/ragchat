from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Type, Tuple

T = TypeVar("T")


class SqLiteRepository(ABC, Generic[T]):
    @abstractmethod
    def _entity_to_row(self, entity: T) -> Tuple:
        """
        Serialize the entity to a tuple for storage in the database.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def _row_to_entity(self, row: Tuple, entity_class: Type[T]) -> T:
        """
        Deserialize a database row back into an entity.
        Must be implemented by subclasses.
        """
        pass
