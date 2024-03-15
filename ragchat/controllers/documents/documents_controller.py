from cmd import Cmd
import re

from tabulate import tabulate
from ragchat.application.documents.use_cases.documents_use_cases import (
    DocumentsUseCases,
)

from ragchat.domain.kernel import TableUtilities


class DocumentsController(Cmd):

    def __init__(self, documents_use_cases: DocumentsUseCases):
        super().__init__()
        self.documents_use_cases = documents_use_cases

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
            document = self.documents_use_cases.add(source, name)
        except Exception:
            print("The 'add' command requires a valid path or URL.")
            print("Usage: add <path|URL>")
            return

        print(f"Added a new document with source: {document.source}")

    def do_delete(self, arg):
        if not arg:
            print("The 'delete' command requires a valid ID.")
            print("Usage: delete <ID>")
            return

        document = self.documents_use_cases.delete(id=arg)

        if not document:
            print(f"The document with ID: {arg} was not found.")
            print("Usage: delete <ID>")
            return

        print(f"Deleted document with ID: {document.id}")

    def do_list(self, arg):
        docs = self.documents_use_cases.list()

        if docs and len(docs) > 0:
            headers, rows = (
                TableUtilities.convert_to_tabulate_headers_and_rows(docs)
            )
            print(tabulate(rows, headers=headers))

    def do_exit(self, arg):
        """Exit the document management command mode."""
        print("Exiting document management mode...")
        return True


# TODO: fix broken test
