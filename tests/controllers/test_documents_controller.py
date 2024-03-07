import pytest

from ragchat.controllers.documents_controller import DocumentsController


@pytest.fixture
def sut():
    return DocumentsController()


def test_do_exit(sut, capsys):
    # Arrange

    # Act
    result = sut.do_exit("")
    captured = capsys.readouterr()

    # Assert
    assert result, "do_exit must return True in order to exit to the previous menu."
    assert f"Exiting document management mode...\n" == captured.out


def test_do_add_using_url(sut, capsys):
    # Arrange
    url = "https://www.google.com"

    # Act
    result = sut.do_add(url)
    captured = capsys.readouterr()

    # Assert
    assert f"Added a new document with source: https://www.google.com\n" == captured.out


def test_do_add_fails_if_url_not_valid(sut, capsys):
    # Arrange
    url = "NotValidUrl"

    # Act
    result = sut.do_add(url)
    captured = capsys.readouterr()

    # Assert
    assert (
        f"The 'add' command requires a valid path or URL.\nUsage: add <path|URL>\n"
        == captured.out
    )


def test_do_add_using_path(sut, capsys):
    # Arrange
    path = __file__  # Document validator needs a path that points to a file so just use this test script.

    # Act
    result = sut.do_add(path)
    captured = capsys.readouterr()

    # Assert
    assert f"Added a new document with source: {path}\n" == captured.out


def test_do_add_fails_if_path_not_valid(sut, capsys):
    # Arrange
    path = "NotValidPath"

    # Act
    result = sut.do_add(path)
    captured = capsys.readouterr()

    # Assert
    assert (
        f"The 'add' command requires a valid path or URL.\nUsage: add <path|URL>\n"
        == captured.out
    )
