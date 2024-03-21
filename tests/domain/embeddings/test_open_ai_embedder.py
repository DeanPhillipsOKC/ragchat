import pytest

from ragchat.domain.retrieval.embeddings.open_ai_embedder import OpenAiEmbedder


@pytest.mark.integration
def test_embed_document():
    # Arrange
    document = "Hello world."

    # Act
    sut = OpenAiEmbedder()
    embeddings = sut.embed_document(document)

    # Assert
    assert embeddings is not None
    assert len(embeddings) == 1536


@pytest.mark.integration
def test_embed_query():
    # Arrange
    query = "Why is the sky blue?"

    # Act
    sut = OpenAiEmbedder()
    embeddings = sut.embed_query(query)

    # Assert
    assert embeddings is not None
    assert len(embeddings) == 1536
