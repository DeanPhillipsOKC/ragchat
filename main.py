from dependency_injector.wiring import Provide, inject
from ioc.container import Container

@inject
def main():
    container = Container()
    collection_use_cases = container.collection_use_cases()
    collection_use_cases.add_collection("foo")

if __name__ == '__main__':
    # do work
    main()