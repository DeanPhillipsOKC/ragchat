from ragchat.application.events.event_handler_interface import IEventHandler
from ragchat.domain.kernel.domain_event_interface import IDomainEvent


class EventDispatcher:
    def __init__(self):
        self.handlers = {}

    def subscribe(self, event: IDomainEvent, handler: IEventHandler):
        event_name = event.get_event_name
        if event_name not in self.handlers:
            self.handlers[event_name] = []
        self.handlers[event_name].append(handler)

    def unsubscribe(self, event: IDomainEvent, handler):
        event_name = event.get_event_name
        if event_name in self.handlers:
            try:
                self.handlers[event_name].remove(handler)
                if not self.handlers[event_name]:
                    del self.handlers[event_name]
            except ValueError:
                pass

    def emit(self, event: IDomainEvent):
        event_name = event.get_event_name
        for handler in self.handlers.get(event_name, []):
            handler.handle(event)
