import os

from ragchat.domain.retrieval.converters.pdf_to_html import PdfToHtmlConverter


def test_can_convert_pdf_to_html():
    # Arrange
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, "test_documents", "h1_to_h4_test.pdf")
    content = None
    with open(path, "rb") as f:
        content = f.read()

    # Act
    sut = PdfToHtmlConverter()
    html = sut.convert(content)

    # Assert
    assert html is not None
    assert "Sample Document Title" in html
    assert "A brief description." in html
    assert "Sample Heading 1" in html
    assert "A brief heading 1 description." in html
    assert "Sample Heading 2" in html
    assert "A brief heading 2 description." in html
    assert "Sample heading 3" in html
    assert "A heading 3 description" in html
    assert "Sample heading 4" in html
