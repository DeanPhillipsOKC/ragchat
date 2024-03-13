from cmd import Cmd
import os
from ragchat.config import ConfigProvider


class UtilitiesController(Cmd):
    """Sub-command processor for general utilities."""

    prompt = "(Utilities)"

    def __init__(self, config_provider: ConfigProvider):
        super().__init__()
        self.entity_db_path = config_provider.entity_db_config.path

    def do_delete_entity_database(self, arg):
        """Deletes the entity database file to start from scratch."""
        try:
            os.remove(self.entity_db_path)
            print(
                "Database file deleted successfully.  You will need to "
                "RESTART the app to prevent errors."
            )
        except FileNotFoundError:
            print("Database file does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def do_exit(self, arg):
        """Exit the application."""
        print("Exiting the application.")
        return True  # Returning True breaks out of the Cmd loop and exits
