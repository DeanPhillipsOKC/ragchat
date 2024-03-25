from dependency_injector.wiring import inject
from ragchat.domain.documents.document_added_event import DocumentAddedEvent
from ragchat.ioc.container import Container


def register_event_handlers(container: Container):
    event_dispatcher = container.event_dispatcher_factory()

    event_dispatcher.subscribe(
        DocumentAddedEvent(None), container.document_added_handler_factory()
    )


@inject
def main():
    container = Container()
    container.event_dispatcher_factory()
    register_event_handlers(container=container)

    cli = container.cli_factory()
    cli.run()


if __name__ == "__main__":
    # do work
    main()
    print("done")
