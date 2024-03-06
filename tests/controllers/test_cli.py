import pytest
from ragchat.controllers.cli import Cli  # Adjust the import path according to your project structure

@pytest.fixture
def setup(mocker):
    mock_collections_controller = mocker.MagicMock()
    mock_utilities_controller = mocker.MagicMock()
    mocker.patch('ragchat.controllers.cli.CollectionsController', return_value=mock_collections_controller)
    
    # Initialize the Cli with the mocked CollectionsController
    cli = Cli(collections_controller=mock_collections_controller, utilities_controller=)

    return cli, mock_collections_controller, mock_utilities_controller

def test_do_collections(setup):
    cli, mock_collections_controller, mock_utilities_controller = setup
    
    # Simulate calling the 'collections' command
    cli.do_collections('')
    
    # Assert that cmdloop was called on the collections controller
    mock_collections_controller.cmdloop.assert_called_once()

def test_do_exit(setup, capsys):
    cli, mock_collections_controller, mock_utilities_controller = setup

    result = cli.do_exit('')
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Assert that "Goodbye!" was printed to stdout
    assert "Goodbye!" in captured.out
    
    # Assert that the method returns True
    assert result is True
