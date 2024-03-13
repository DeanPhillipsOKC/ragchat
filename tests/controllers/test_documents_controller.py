import pytest

from ragchat.controllers.documents.documents_controller import (
    DocumentsController,
)


@pytest.fixture
def sut():
    return DocumentsController()


def test_do_exit(sut, capsys):
    # Arrange

    # Act
    result = sut.do_exit("")
    captured = capsys.readouterr()

    # Assert
    assert result
    assert "Exiting document management mode...\n" == captured.out


def test_do_add_using_url(sut, capsys):
    # Arrange
    url = "https://www.google.com"
    name = "HTML doc"
    args = f'{url} "{name}"'

    # Act
    sut.do_add(args)
    captured = capsys.readouterr()

    # Assert
    assert (
        "Added a new document with source: https://www.google.com\n"
        == captured.out
    )


def test_do_add_fails_if_url_not_valid(sut, capsys):
    # Arrange
    url = "NotValidUrl"
    name = "HTML doc"
    args = f'{url} "{name}"'

    # Act
    sut.do_add(args)
    captured = capsys.readouterr()

    # Assert
    assert (
        "The 'add' command requires a valid path or URL."
        "\nUsage: add <path|URL>\n" == captured.out
    )


def test_do_add_using_path(sut, capsys):
    # Arrange

    # Document validator needs a path that points to
    # a file so just use this test script.
    path = __file__
    name = "Some doc"
    args = f'{path} "{name}"'

    # Act
    sut.do_add(args)
    captured = capsys.readouterr()

    # Assert
    assert f"Added a new document with source: {path}\n" == captured.out


def test_do_add_fails_if_path_not_valid(sut, capsys):
    # Arrange
    path = "NotValidPath"
    name = "Some doc"
    args = f'{path} "{name}"'

    # Act
    sut.do_add(args)
    captured = capsys.readouterr()

    # Assert
    assert (
        "The 'add' command requires a valid path or URL."
        "\nUsage: add <path|URL>\n" == captured.out
    )


def test_do_add_fails_if_name_not_supplied(sut, capsys):
    # Arrange
    pass
