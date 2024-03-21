from langchain_text_splitters import HTMLHeaderTextSplitter
from ragchat.domain.retrieval.splitters.splitter_interface import (
    IHtmlSplitterInterface,
)
from langchain_core.documents import Document


class HtmlHeaderSplitter(IHtmlSplitterInterface):

    def split(self, html: str) -> list[Document]:
        headers_to_split_on = [
            ("h1", "Header 1"),
            ("h2", "Header 2"),
            ("h3", "Header 3"),
        ]

        html_splitter = HTMLHeaderTextSplitter(
            headers_to_split_on=headers_to_split_on
        )
        html_header_splits = html_splitter.split_text(html)

        return html_header_splits
