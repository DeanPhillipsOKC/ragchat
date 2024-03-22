from abc import ABC, abstractmethod


class IDomainEvent(ABC):
    @abstractmethod
    def get_event_name(self) -> str:
        pass
