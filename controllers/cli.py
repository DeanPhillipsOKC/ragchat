import click
from application.use_cases.collection_use_cases import CollectionUseCases

@click.group
def cli():
    pass

@click.command()
def list_collections():
    pass

# Initialize and inject dependencies
repository = InMemoryCollectionRepository()
collection_use_cases = CollectionUseCases(repository)