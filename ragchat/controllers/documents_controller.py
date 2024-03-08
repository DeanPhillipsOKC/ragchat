from cmd import Cmd
from uuid import uuid4

from ragchat.domain.documents.document import Document


class DocumentsController(Cmd):

    def do_add(self, arg):
        """
        Add a new document using a local path, or remote URL.

        Usage: add <path|URL>

        <path> Specifies a path to a local file.
        <URL> Specifies a remote URL to a file, or document.
        """
        if not arg:
            print("Error: The 'add' command requires a path or URL.")
            print("Usage: add <path|URL>")
            return

        document = any
        try:
            document = Document(id=str(uuid4()), source=arg)
        except Exception as e:
            print("The 'add' command requires a valid path or URL.")
            print("Usage: add <path|URL>")
            return

        print(f"Added a new document with source: {arg}")

    def do_exit(self, arg):
        """Exit the document management command mode."""
        print("Exiting document management mode...")
        return True
