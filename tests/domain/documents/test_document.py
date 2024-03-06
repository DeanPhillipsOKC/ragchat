from uuid import uuid4
import pytest
import os
from ragchat.domain.documents.document import Document

def test_can_load_from_url():
    # Arrange
    id = uuid4()
    url = "https://www.google.com/"

    # Act
    doc = Document(id=id, loaded_from_url=url)

    # Assert 
    assert doc.id == id, "The document ID was not set correctly."
    assert str(doc.loaded_from_url) == url, "The document loaded by URL was not set correctly."

def test_can_load_from_path():
    # Arrange
    id = uuid4()
    path = __file__

    # Act
    doc = Document(id=id, loaded_from_path=path)

    # Assert
    assert doc.id == id, "The document ID was not set correctly."
    assert str(doc.loaded_from_path) == path, "The document loaded by path was not set correctly."

def test_cannot_load_from_invalid_path():
    # Arrange
    id = uuid4()
    path = "./nuke.txt"

    # Act / Assert
    with pytest.raises(ValueError):
        Document(id=id, loaded_from_path=path)

def test_cannot_load_from_invalid_url():
    # Arrange
    id = uuid4()
    url = "Not a valid URL"

    # Act / Assert
    with pytest.raises(ValueError):
        Document(id=id, loaded_from_url=url)