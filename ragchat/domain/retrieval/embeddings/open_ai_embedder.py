from langchain_openai import OpenAIEmbeddings
from ragchat.domain.retrieval.embeddings.embedder_interface import IEmbedder


class OpenAiEmbedder(IEmbedder):

    def _get_embeddings_model(self):
        return OpenAIEmbeddings()

    def embed_document(self, document_text: str):
        emebeddings_model = self._get_embeddings_model()

        embeddings = emebeddings_model.embed_documents(document_text)[0]
        return embeddings

    def embed_query(self, query_text: str):
        embeddings_model = self._get_embeddings_model()

        embeddings = embeddings_model.embed_query(query_text)
        return embeddings
