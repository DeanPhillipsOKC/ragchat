import json
import os
import sqlite3
from uuid import UUID
from ragchat.application.config.config_provider import ConfigProvider
from ragchat.data.entity_db_config import EntityDbConfig
from ragchat.domain.collections.collection import Collection
from ragchat.domain.collections.repository_interface import ICollectionRepository


class SqLiteCollectionRepository(ICollectionRepository):
    def __init__(self, config_provider: ConfigProvider):
        self.db_path = config_provider.entity_db_config.path
        self._init_db()

    def _init_db(self):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS collections (
                    id TEXT PRIMARY KEY,
                    data TEXT NOT NULL
                )
            ''')
            conn.commit()

    def _collection_to_row(self, collection: Collection) -> tuple:
        # Use Pydantic model for serialization
        model = Collection.model_validate(collection)
        data = model.model_dump_json()
        return str(collection.id), data

    def _row_to_collection(self, row: tuple) -> Collection:
        data_dict = json.loads(row[1])  # Assuming row[1] is a JSON string of the dictionary
        return Collection(**data_dict)

    def add(self, collection):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO collections (id, data) VALUES (?, ?)', self._collection_to_row(collection))
            conn.commit()

    def delete(self, guid: UUID) -> Collection:
        collection = self.select(guid)
        if collection:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM collections WHERE id = ?', (str(guid),))
                conn.commit()
        return collection

    def list(self) -> list[Collection]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM collections')
            return [self._row_to_collection(row) for row in cursor.fetchall()]

    def select(self, guid: UUID):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM collections WHERE id = ?', (str(guid),))
            row = cursor.fetchone()
            if row:
                return self._row_to_collection(row)
            else:
                return None

    def get_selected(self) -> Collection:
        # Implementing a persistent selected collection logic would require storing the selected collection's ID elsewhere in the database or another strategy
        pass