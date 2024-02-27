from dependency_injector.wiring import Provide, inject
from ragchat.ioc.container import Container

@inject
def main():
    container = Container()
    cli = container.cli_factory()
    cli.run()

if __name__ == '__main__':
    # do work
    main()
    print("done")