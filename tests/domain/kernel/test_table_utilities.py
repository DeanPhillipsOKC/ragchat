from uuid import uuid4

from ragchat.domain.collections import Collection
from ragchat.domain.kernel import TableUtilities


def test_convert_to_tabulate_headers_and_rows():
    # Arrange
    test_collections = [
        Collection(id=uuid4(), name="Collection 1"),
        Collection(id=uuid4(), name="Collection 2"),
        Collection(id=uuid4(), name="Collection 3"),
    ]

    expected_headers = ["id", "name"]
    expected_rows = [
        [test_collections[0].id, "Collection 1"],
        [test_collections[1].id, "Collection 2"],
        [test_collections[2].id, "Collection 3"],
    ]

    # Act
    headers, rows = TableUtilities.convert_to_tabulate_headers_and_rows(
        test_collections
    )

    # Assert
    assert headers == expected_headers
    assert rows == expected_rows
