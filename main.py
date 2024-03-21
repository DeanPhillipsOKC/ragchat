from dependency_injector.wiring import inject
from ragchat.ioc.container import Container
from dotenv import load_dotenv


@inject
def main():
    container = Container()
    cli = container.cli_factory()
    cli.run()


if __name__ == "__main__":
    load_dotenv()
    main()
    print("done")
