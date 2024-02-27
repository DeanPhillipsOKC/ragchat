from cmd import Cmd
from .collections_controller import CollectionsController

class Cli(Cmd):
    intro = 'Welcome to the RAGChat.  Type help or ? to list commands.\n'
    prompt = ">>>"

    def __init__(self, collections_controller: CollectionsController):
        super().__init__()
        self.collections_controller = collections_controller

    def do_collections(self, arg):
        """Enter collections management mode."""
        self.collections_controller.cmdloop()

    def do_exit(self, arg):
        """Exit the CLI"""
        print("Goodbye!")
        return True
    
    def emptyline(self):
        pass # Do nothing on empty line input
    
    def run(self):
        self.cmdloop()