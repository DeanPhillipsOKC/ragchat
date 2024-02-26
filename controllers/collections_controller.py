from cmd import Cmd
from application.use_cases.collections.use_cases import CollectionsUseCases
from common.guid_utilities import is_uuid4, to_uuid4

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
            return

        collection = self.collection_use_cases.add_collection(arg)

        print(f"Added a new collection with ID: {collection.id}")

    def do_list(self, arg):
        """List all collections"""
        collections = self.collection_use_cases.list_collection()

        # Print header
        print(f"{'ID':36} {'Name'}")
        print('-' * 50)

        for collection in collections:
            print(f"{str(collection.id):36} {collection.name}")

    def do_select(self, arg):
        """
        Add a collection to your session context.  This will let 
        you manage documents in that collection, or start an interactive
        chat across documents in that collection.

        Usage: select <ID>

        <ID> is the identifier of the collection that you would like to select
        into your context.
        """
        if not arg:
            print("Error: The 'select' command requires a collection ID.")
            print("Usage: add <ID>")
            return
        
        if not is_uuid4(arg):
            print("Error: The 'select' command requires a valid collection ID (UUID v4)")
            return

        guid = to_uuid4(arg)

        collection = self.collection_use_cases.select_collection(guid)

        if not collection:
            print(f"Error: Could not select the collection with ID: {arg}")
            return

        print(f"Selected collection with ID: {arg}")

    def do_exit(self, arg):
        """Exit the collections management command mode."""
        print("Exiting collections management mode...")
        return True