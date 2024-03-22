from abc import ABC, abstractmethod

from ragchat.domain.kernel.domain_event_interface import IDomainEvent


class IEventHandler(ABC):
    @abstractmethod
    def handle(self, event: IDomainEvent) -> str:
        pass
