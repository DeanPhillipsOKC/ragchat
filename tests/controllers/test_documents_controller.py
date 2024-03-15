import re
from uuid import uuid4
import pytest
from ragchat.application.documents.dtos import ListDocumentsViewModel
from ragchat.application.documents.use_cases import DocumentsUseCases

from ragchat.controllers.documents.documents_controller import (
    DocumentsController,
)
from ragchat.domain.documents import Document


@pytest.fixture
def mock_use_cases(mocker):
    return mocker.Mock(spec=DocumentsUseCases)


@pytest.fixture
def sut(mock_use_cases):
    return DocumentsController(documents_use_cases=mock_use_cases)


def test_do_exit(sut, capsys):
    # Arrange

    # Act
    result = sut.do_exit("")
    captured = capsys.readouterr()

    # Assert
    assert result
    assert "Exiting document management mode...\n" == captured.out


@pytest.fixture
def add_fixture(sut):
    document = Document(
        id=uuid4(), source="https://www.google.com", name="Test Document"
    )
    sut.documents_use_cases.add.return_value = document

    return sut, document


def test_do_add_using_url(add_fixture, capsys):
    # Arrange
    sut, returned_document = add_fixture

    url = "https://www.google.com"
    name = "HTML doc"
    args = f'{url} "{name}"'

    # Act
    sut.do_add(args)
    captured = capsys.readouterr()

    # Assert
    assert (
        f"Added a new document with source: {returned_document.source}\n"
        == captured.out
    )


def test_do_add_using_path(add_fixture, capsys):
    # Arrange
    sut, returned_document = add_fixture

    # Document validator needs a path that points to
    # a file so just use this test script.
    path = __file__
    name = "Some doc"
    args = f'{path} "{name}"'

    returned_document.source = path

    # Act
    sut.do_add(args)
    captured = capsys.readouterr()

    # Assert
    assert f"Added a new document with source: {path}\n" == captured.out


def test_do_add_fails_if_no_args_supplied(add_fixture, capsys):
    # Arrange
    sut, returned_document = add_fixture

    args = None

    # Act
    sut.do_add(args)
    captured = capsys.readouterr()

    # Assert
    assert (
        "The 'add' command requires a valid path and name."
        "\nUsage: add <path|URL> <name>"
        "\nNote: If the source, or name has spaces it must be surrounded by "
        "double quotes.\n"
    ) == captured.out


def test_do_add_fails_if_name_not_provided(add_fixture, capsys):
    # Arrange
    sut, returned_document = add_fixture

    args = "https://www.google.com"

    # Act
    sut.do_add(args)
    captured = capsys.readouterr()

    # Assert
    assert (
        "The 'add' command requires a valid path and name."
        "\nUsage: add <path|URL> <name>"
        "\nNote: If the source, or name has spaces it must be surrounded by "
        "double quotes.\n"
    ) == captured.out


def test_do_add_fails_if_name_has_space_and_no_double_quote(
    add_fixture, capsys
):
    # Arrange
    sut, returned_document = add_fixture

    source = "https:www.google.com"
    name = "My File.txt"
    args = f"{source} {name}"

    # Act
    sut.do_add(args)
    captured = capsys.readouterr()

    # Assert
    assert (
        "The 'add' command requires a valid path and name."
        "\nUsage: add <path|URL> <name>"
        "\nNote: If the source, or name has spaces it must be surrounded by "
        "double quotes.\n"
    ) == captured.out


def test_do_add_does_not_fail_if_name_has_space_wrapped_in_quotes(
    add_fixture, capsys
):
    # Arrange
    sut, returned_document = add_fixture

    source = "https://www.google.com"
    name = '"My File.txt"'
    args = f"{source} {name}"
    returned_document.source = source

    # Act
    sut.do_add(args)
    captured = capsys.readouterr()

    # Assert
    assert f"Added a new document with source: {source}\n" == captured.out


@pytest.fixture
def delete_fixture(sut):
    document = Document(
        id=uuid4(), source="https://www.google.com", name="Test Document"
    )
    sut.documents_use_cases.delete.return_value = document

    return sut, document


def test_do_delete(delete_fixture, capsys):
    # Arrange
    sut, returned_document = delete_fixture

    id = uuid4()
    returned_document.id = id

    # Act
    sut.do_delete(id)
    captured = capsys.readouterr()

    # Assert
    assert f"Deleted document with ID: {id}\n" == captured.out


def test_do_delete_fails_if_id_not_provided(delete_fixture, capsys):
    # Arrange
    sut, returned_document = delete_fixture

    id = None

    # Act
    sut.do_delete(id)
    captured = capsys.readouterr()

    # Assert
    assert (
        "The 'delete' command requires a valid ID." "\nUsage: delete <ID>\n"
    ) == captured.out


def test_do_delete_fails_if_document_does_not_exist(delete_fixture, capsys):
    # Arrange
    sut, returned_document = delete_fixture

    id = uuid4()
    sut.documents_use_cases.delete.return_value = None

    # Act
    sut.do_delete(id)
    captured = capsys.readouterr()

    # Assert
    assert (
        f"The document with ID: {id} was not found." "\nUsage: delete <ID>\n"
    ) == captured.out


@pytest.fixture
def list_fixture(sut):
    document1 = Document(
        id=uuid4(), source="https://www.google.com", name="Test Document"
    )
    document2 = Document(
        id=uuid4(), source="https://www.yahoo.com", name="Test Document2"
    )
    document3 = Document(
        id=uuid4(), source="https://www.facebook.com", name="Test Document3"
    )
    sut.documents_use_cases.list.return_value = [
        document1,
        document2,
        document3,
    ]

    return sut, sut.documents_use_cases.list.return_value


def test_do_list(list_fixture, capsys):
    # Arrange
    sut, returned_docs = list_fixture

    id1 = str(uuid4())
    id2 = str(uuid4())
    id3 = str(uuid4())

    expected_documents = [
        {"id": id1, "name": "Foo", "type": "html"},
        {"id": id2, "name": "Bar", "type": "html"},
        {"id": id3, "name": "Baz", "type": "html"},
    ]

    sut.documents_use_cases.list.return_value = [
        ListDocumentsViewModel(
            id=doc["id"], name=doc["name"], type=doc["type"]
        )
        for doc in expected_documents
    ]

    # Act
    sut.do_list(None)
    captured = capsys.readouterr().out

    # Convert captured output to list of rows
    output_rows = captured.strip().split("\n")

    # Assert
    # Check headers
    headers = output_rows[0].split()
    assert headers == [
        "id",
        "name",
        "type",
    ], f"Expected headers ['id', 'name', 'type'], got {headers}"

    # Check each expected document by name and type (IDs can't be predicted
    # in output)
    for doc in expected_documents:
        # Construct a regex pattern to search for name and type in the output
        pattern = re.compile(rf"{doc['name']}\s+{doc['type']}")
        # Check if the pattern is found in any row of the output
        assert any(
            pattern.search(row) for row in output_rows
        ), f"Document with name {doc['name']} and type {doc['type']} not "
        "found in output"
