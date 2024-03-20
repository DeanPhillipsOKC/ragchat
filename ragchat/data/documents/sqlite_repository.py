import os
import sqlite3
from typing import Tuple
from uuid import UUID
from ragchat.config import ConfigProvider
from ragchat.data.kernel import SqLiteRepository
from ragchat.domain.documents import IDocumentRepository, Document


class SqLiteDocumentRepository(IDocumentRepository, SqLiteRepository):
    def __init__(self, config_provider: ConfigProvider):
        self.db_path = config_provider.entity_db_config.path
        self._init_db()

    def _init_db(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

        with sqlite3.connect(self.db_path) as conn:
            conn.execute("PRAGMA foreign_keys = ON")
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS documents (
                    id TEXT PRIMARY KEY,
                    collection_id TEXT NOT NULL,
                    source TEXT NOT NULL,
                    name TEXT NOT NULL,
                    type TEXT NOT NULL,
                    content BLOB NOT NULL,
                    FOREIGN KEY (collection_id) REFERENCES collections(id)
                )
                """
            )
            conn.commit()

    def add(self, document):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            # Use _entity_to_row to serialize the document
            document_tuple = self._entity_to_row(document)
            cursor.execute(
                "INSERT INTO documents "
                "(id, collection_id, source, name, type, content) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                document_tuple,
            )
            conn.commit()

    def _get(self, guid: UUID) -> Document:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM documents WHERE id = ?", (str(guid),)
            )
            row = cursor.fetchone()
            if row:
                return self._row_to_entity(row, Document)
            return None

    def delete(self, guid: UUID) -> Document:
        document = self._get(guid)
        if document:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "DELETE FROM documents WHERE id = ?", (str(guid),)
                )
                conn.commit()
        return document

    def list(self, collection_id: UUID) -> list[Document]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM documents WHERE collection_id = ?",
                (str(collection_id),),
            )
            return [
                self._row_to_entity(row, Document) for row in cursor.fetchall()
            ]

    def _entity_to_row(self, document) -> Tuple:
        # Example implementation for Document entity
        return (
            str(document.id),
            str(document.collection_id),
            str(document.source),
            document.name,
            document.type,
            document.content,
        )

    def _row_to_entity(self, row, entity_class) -> Document:
        # Example implementation for Document entity
        id, collection_id, source, name, type, content = row
        return entity_class(
            id=id,
            collection_id=collection_id,
            source=source,
            name=name,
            type=type,
            content=content,
        )
