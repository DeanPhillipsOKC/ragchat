from cmd import Cmd
from ragchat.controllers.documents_controller import DocumentsController

from ragchat.controllers.utilities_controller import UtilitiesController
from .collections_controller import CollectionsController


class Cli(Cmd):
    intro = "Welcome to the RAGChat.  Type help or ? to list commands.\n"
    prompt = ">>>"

    def __init__(
        self,
        collections_controller: CollectionsController,
        utilities_controller: UtilitiesController,
        documents_controller: DocumentsController,
    ):
        super().__init__()
        self.collections_controller = collections_controller
        self.utilities_controller = utilities_controller
        self.documents_controller = documents_controller

    def do_collections(self, arg):
        """Enter collections management mode."""
        self.collections_controller.cmdloop()

    def do_documents(self, arg):
        """Enter documents management mode."""
        self.documents_controller.cmdloop()

    def do_utilities(self, arg):
        """Enter utilities mode."""
        self.utilities_controller.cmdloop()

    def do_exit(self, arg):
        """Exit the CLI"""
        print("Goodbye!")
        return True

    def emptyline(self):
        pass  # Do nothing on empty line input

    def run(self):
        self.cmdloop()
