# Dummy implementations of the interfaces
from ragchat.application.events.event_dispatcher import EventDispatcher
from ragchat.application.events.event_handler_interface import IEventHandler
from ragchat.domain.kernel.domain_event_interface import IDomainEvent


class DummyEvent(IDomainEvent):
    def get_event_name(self):
        return "dummy_event"


class DummyHandler(IEventHandler):
    def __init__(self):
        self.handled = False

    def handle(self, event: DummyEvent):
        self.handled = True


def test_event_dispatcher_handles_event():
    # Arrange
    sut = EventDispatcher()
    event = DummyEvent()
    handler = DummyHandler()

    # Act
    sut.subscribe(event, handler)
    sut.emit(event)

    # Assert
    assert handler.handled


def test_event_dispatcher_unsubscribes_handler():
    # Arrange
    dispatcher = EventDispatcher()
    event = DummyEvent()
    handler = DummyHandler()

    # Act
    dispatcher.subscribe(event, handler)
    dispatcher.unsubscribe(event, handler)

    # Assert
    dispatcher.emit(event)
    assert not handler.handled
