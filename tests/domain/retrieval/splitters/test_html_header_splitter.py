# test_html_header_splitter.py

import pytest

from ragchat.domain.retrieval.splitters.html_header_splitter import (
    HtmlHeaderSplitter,
)

# Sample HTML content for testing
HTML_WITHOUT_HEADERS = "<p>This is a test paragraph.</p>"
HTML_WITH_HEADERS = """
<html>
<body>
<h1>Header 1 Content</h1>
<p>Some text under header 1.</p>
<h2>Header 2 Content</h2>
<p>Some text under header 2.</p>
<h3>Header 3 Content</h3>
<p>Some text under header 3.</p>
</body>
</html>
"""


@pytest.fixture
def splitter():
    return HtmlHeaderSplitter()


def test_split_no_headers(splitter):
    """Test splitting HTML with no headers."""

    results = splitter.split(HTML_WITHOUT_HEADERS)
    assert len(results) == 1
    assert results[0].page_content == "This is a test paragraph."


def test_split_with_headers(splitter):
    """Test splitting HTML with headers."""
    results = splitter.split(HTML_WITH_HEADERS)
    assert isinstance(results, list)

    assert len(results) == 3
    assert results[0].page_content == "Some text under header 1."
    assert results[1].page_content == "Some text under header 2."
    assert results[2].page_content == "Some text under header 3."
