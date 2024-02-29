from cmd import Cmd
from ragchat.application.use_cases.collections.use_cases import CollectionsUseCases
from ragchat.common.guid_utilities import is_uuid4, to_uuid4

class CollectionsController(Cmd):
    """Sub-command processor for collections management commands."""

    prompt = "(Collections)"

    def __init__(self, collection_use_cases: CollectionsUseCases):
        super().__init__()
        self.collection_use_cases = collection_use_cases

    def _validate_id(self, id: str, command_name: str) -> bool:
        if not id:
            print(f"Error: The '{command_name}' command requires a collection ID.")
            return False
        
        if not is_uuid4(id):
            print(f"Error: The '{command_name}' command requires a valid collection ID (UUID v4)")
            return False
        
        return True

    def do_add(self, arg):
        """
        Add a new collection.

        Usage: add <name>

        <name> is a required argument that specifies the name of the new collection.
        """
        if not arg:
            print("Error: The 'add' command requires a name for the new collection.")
            print("Usage: add <name>")
            return

        collection = self.collection_use_cases.add(arg)

        print(f"Added a new collection with ID: {collection.id}")

    def do_delete(self, arg):
        """
        Delete a collection.

        Usage: delete <ID>

        <ID> is a required argument that specifies the collection that you want to delete.
        """
        if not self._validate_id(arg, "delete"):
            print("Usage: delete <ID>")
            return
        
        guid = to_uuid4(arg)

        deleted_collection = self.collection_use_cases.delete(guid)
        
        if deleted_collection:
            print(f"Deleted colection with ID: {deleted_collection.id} and Name: {deleted_collection.name}")
        else:
            print(f"Error: Could not find a collection with ID: {arg} to delete.")

    def do_list(self, arg):
        """List all collections"""
        collections = self.collection_use_cases.list()

        # Print header
        print(f"{'ID':38} {'Name'}")
        print('-' * 52)  # Adjusted width for the 'Selected' column

        for collection in collections:
            selected_mark = "*" if collection.is_selected else " "
            print(f"{selected_mark} {collection.id:36} {collection.name}")

    def do_select(self, arg):
        """
        Add a collection to your session context.  This will let 
        you manage documents in that collection, or start an interactive
        chat across documents in that collection.

        Usage: select <ID>

        <ID> is the identifier of the collection that you would like to select
        into your context.
        """
        if not self._validate_id(arg, command_name="select"):
            print("Usage: select <ID>")
            return

        guid = to_uuid4(arg)

        collection = self.collection_use_cases.select(guid)

        if not collection:
            print(f"Error: Could not select the collection with ID: {arg}")
            return

        print(f"Selected collection with ID: {arg}")

    def do_exit(self, arg):
        """Exit the collections management command mode."""
        print("Exiting collections management mode...")
        return True