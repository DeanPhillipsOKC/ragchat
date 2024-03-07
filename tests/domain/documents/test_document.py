from uuid import uuid4
import pytest
import os
from ragchat.domain.documents.document import Document

def test_can_load_from_url():
    # Arrange
    id = uuid4()
    url = "https://www.google.com/"

    # Act
    doc = Document(id=id, source=url)

    # Assert 
    assert doc.id == id, "The document ID was not set correctly."
    assert str(doc.source) == url, "The document loaded by URL was not set correctly."

def test_can_load_from_path():
    # Arrange
    id = uuid4()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, 'test_documents', 'fake_document.txt')

    # Act
    doc = Document(id=id, source=path)

    # Assert
    assert doc.id == id, "The document ID was not set correctly."
    assert str(doc.source) == path, "The document loaded by path was not set correctly."
    assert doc.type == "txt", "The document type was not correctly determined"

def test_cannot_load_from_invalid_path():
    # Arrange
    id = uuid4()
    path = "./nuke.txt"

    # Act / Assert
    with pytest.raises(Exception):
        Document(id=id, source=path)

def test_cannot_load_from_invalid_url():
    # Arrange
    id = uuid4()
    url = "Not a valid URL"

    # Act / Assert
    with pytest.raises(Exception):
        Document(id=id, source=url)