from cmd import Cmd
import re
from uuid import uuid4

from ragchat.domain.documents import Document


class DocumentsController(Cmd):

    # TODO: A lot of vaidation needs to get added here

    def do_add(self, arg):
        """
        Add a new document using a local path, or remote URL.

        Usage: add <path|URL>

        <path> Specifies a path to a local file.
        <URL> Specifies a remote URL to a file, or document.
        """

        if not arg:
            print("The 'add' command requires a valid path and name.")
            print("Usage: add <path|URL> <name>")
            print(
                "Note: If the source, or name has spaces it must be "
                "surrounded by double quotes."
            )
            return

        # Use regex to split args but keep quoted arguments together
        args = re.findall(r'[^"\s]\S*|".+?"', arg)

        # Strip quotes from arguments if present
        args = [arg.strip('"') for arg in args]

        if len(args) != 2:
            print("The 'add' command requires a valid path and name.")
            print("Usage: add <path|URL> <name>")
            print(
                "Note: If the source, or name has spaces it must be "
                "surrounded by double quotes."
            )
            return

        source, name = args

        try:
            Document(id=str(uuid4()), source=source, name=name)
        except Exception:
            print("The 'add' command requires a valid path or URL.")
            print("Usage: add <path|URL>")
            return

        print(f"Added a new document with source: {source}")

    def do_exit(self, arg):
        """Exit the document management command mode."""
        print("Exiting document management mode...")
        return True
