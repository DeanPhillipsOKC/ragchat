import os
import sqlite3
from uuid import UUID
from ragchat.config import ConfigProvider
from ragchat.data.kernel import SqLiteRepository
from ragchat.domain.collections import ICollectionRepository, Collection


# TODO: Write integration test for the SqLiteCollectionRepositories
class SqLiteCollectionRepository(
    ICollectionRepository, SqLiteRepository
):  # pragma: no cover
    def __init__(self, config_provider: ConfigProvider):
        self.db_path = config_provider.entity_db_config.path
        self._init_db()

    def _init_db(self):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

        with sqlite3.connect(self.db_path) as conn:
            # Enable foreign key support
            conn.execute("PRAGMA foreign_keys = ON")
            cursor = conn.cursor()
            # Create collections table
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS collections (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL
                )
            """
            )
            # Create selected_collection table
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS selected_collection (
                    id TEXT PRIMARY KEY,
                    collection_id TEXT NOT NULL,
                    FOREIGN KEY (collection_id) REFERENCES collections(id)
                    ON DELETE SET NULL
                )
            """
            )
            conn.commit()

    def add(self, collection):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO collections (id, name) VALUES (?, ?)",
                self._entity_to_row(collection),
            )
            conn.commit()

    def delete(self, guid: UUID) -> Collection:
        collection = self.select(guid)
        if collection:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "DELETE FROM collections WHERE id = ?", (str(guid),)
                )
                conn.commit()
        return collection

    def list(self) -> list[Collection]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM collections")
            return [self._row_to_entity(row) for row in cursor.fetchall()]

    def select(self, guid: UUID):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            # Fetch the collection to ensure it exists
            cursor.execute(
                "SELECT * FROM collections WHERE id = ?", (str(guid),)
            )
            row = cursor.fetchone()
            if row:
                # Use a known, fixed ID for the single selected collection
                selected_id = "selected"
                # Upsert into selected_collection
                cursor.execute(
                    "INSERT OR REPLACE INTO selected_collection "
                    "(id, collection_id) VALUES (?, ?)",
                    (selected_id, str(guid)),
                )
                conn.commit()
                return self._row_to_entity(row)
            else:
                return None

    def get_selected(self) -> Collection:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT collections.* FROM collections JOIN "
                "selected_collection ON collections.id = "
                "selected_collection.collection_id"
            )
            row = cursor.fetchone()
            if row:
                return self._row_to_entity(row)
            return None

    def _entity_to_row(self, collection) -> tuple:
        return (str(collection.id), collection.name)

    def _row_to_entity(self, row) -> Collection:
        id_str, name = row
        return Collection(id=id_str, name=name)
