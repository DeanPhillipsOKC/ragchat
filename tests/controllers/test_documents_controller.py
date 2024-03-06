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

def test_do_add_from_url(sut, capsys):
    # Arrange

    # Act
    result = sut.do_add_from_url("https://www.google.com")
    captured = capsys.readouterr()

    # Assert
    assert f"Added a new document with URL: https://www.google.com\n" == captured.out

def test_do_add_fails_if_url_not_valid(sut, capsys):
    # Arrange

    # Act
    result = sut.do_add_from_url("NotValidUrl")
    captured = capsys.readouterr()

    # Assert
    assert f"The 'add_from_url' command requires a valid URL\nUsage: add_from_url <URL>\n" == captured.out