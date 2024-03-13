import json

from ragchat.config.entity_db import EntityDbConfig


class ConfigProvider:
    def __init__(self, config_path: str):
        with open(config_path, "r") as file:
            config_data = json.load(file)
            self.entity_db_config = EntityDbConfig(
                **config_data["entity_db_config"]
            )
