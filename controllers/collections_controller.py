from cmd import Cmd
from application.use_cases.collections_use_cases import CollectionsUseCases

class CollectionsController(Cmd):
    """Sub-command processor for collections management commands."""

    prompt = "(Collections)"

    def __init__(self, collection_use_cases: CollectionsUseCases):
        super().__init__()
        self.collection_use_cases = collection_use_cases

    def do_add(self, arg):
        """
        Add a new collection.

        Usage: add <name>

        <name> is a required argument that specifies the name of the new collection.
        """
        if not arg:
            print("Error: The 'add command requires a name for the new collection.")
            print("Usage: add <name>")
            return False

        self.collection_use_cases.add_collection(arg)

    def do_list(self, arg):
        """List all collections: LIST"""
        collections = self.collection_use_cases.list_collection()

        # Print header
        print(f"{'ID':36} {'Name'}")
        print('-' * 50)

        for collection in collections:
            print(f"{str(collection.id):36} {collection.name}")

    def do_exit(self, arg):
        """Exit the collections management command mode."""
        print("Exiting collections management mode...")
        return True