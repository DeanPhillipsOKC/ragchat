from uuid import uuid4
import pytest
import os
from ragchat.domain.documents import Document


def test_can_load_from_url():
    # Arrange
    id = uuid4()
    url = "https://www.google.com/"
    name = "Test HTML doc"

    # Act
    doc = Document(id=id, source=url, name=name)

    # Assert
    assert doc.id == id
    assert str(doc.source) == url
    assert doc.content is not None


def test_can_load_from_path():
    # Arrange
    id = uuid4()
    path = __file__
    name = "Test file"

    # Act
    doc = Document(id=id, source=path, name=name)

    # Assert
    assert doc.id == id
    assert str(doc.source) == path
    assert doc.content is not None


def test_cannot_load_from_invalid_path():
    # Arrange
    id = uuid4()
    path = "./nuke.txt"
    name = "Test file"

    # Act / Assert
    with pytest.raises(Exception):
        Document(id=id, source=path, name=name)


def test_cannot_load_from_invalid_url():
    # Arrange
    id = uuid4()
    url = "Not a valid URL"
    name = "Test HTML doc"

    # Act / Assert
    with pytest.raises(Exception):
        Document(id=id, source=url, name=name)


def test_can_identify_pdfs():
    # Arrange
    id = uuid4()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, "test_documents", "sample_pdf.pdf")
    name = "Test PDF"

    # Act
    doc = Document(id=id, source=path, name=name)

    # Assert
    assert doc.id == id
    assert str(doc.source) == path
    assert doc.type == "pdf"


def test_can_identify_html():
    # Arrange
    id = uuid4()
    url = "https://www.sanity.io/static-websites"
    name = "Test HTML doc"

    # Act
    doc = Document(id=id, source=url, name=name)

    # Assert
    assert doc.id == id
    assert str(doc.source) == url
    assert doc.type == "html"
