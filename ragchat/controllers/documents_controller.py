from cmd import Cmd
from uuid import uuid4

from ragchat.domain.documents.document import Document

class DocumentsController(Cmd):
    
    def do_add_from_url(self, arg):
        """
        Add a new document using a URL.

        Usage: add_from_url <URL>

        <URL> specifies a remote URL to a file, or document.
        """
        if not arg:
            print("Error: The 'add_from_url' command requires a URL.")
            print("Usage: add_from_url <URL>")
            return

        document = any
        try:
            document = Document(id=uuid4(), loaded_from_url=arg)
        except:
            print("The 'add_from_url' command requires a valid URL")
            print("Usage: add_from_url <URL>")
            return

        print(f"Added a new document with URL: {arg}")

    def do_exit(self, arg):
        """Exit the document management command mode."""
        print("Exiting document management mode...")
        return True