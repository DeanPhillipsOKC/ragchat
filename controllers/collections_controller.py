from cmd import Cmd
from application.use_cases.collections_use_cases import CollectionsUseCases

class CollectionsController(Cmd):
    """Sub-command processor for collections management commands."""

    prompt = "(Collections)"

    def __init__(self, collection_use_cases: CollectionsUseCases):
        super().__init__()
        self.collection_use_cases = collection_use_cases

    def do_list(self, arg):
        """List all collections: LIST"""
        self.collection_use_cases.list_collection()

    def do_exit(self, arg):
        """Exit the collections management command mode."""
        print("Exiting collections management mode...")
        return True