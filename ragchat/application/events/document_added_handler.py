from langchain_text_splitters import RecursiveCharacterTextSplitter
from ragchat.application.events.event_handler_interface import IEventHandler
from ragchat.domain.documents.document_added_event import DocumentAddedEvent
from langchain_core.documents import Document
from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings


class ChromaDocumentAddedHandler(IEventHandler):

    def handle(self, event: DocumentAddedEvent):
        document = event.document

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200
        )

        text_content = document.content.decode("utf-8")

        document = Document(page_content=text_content)

        split_documents = text_splitter.split_documents(documents=[document])

        # TODO: Move to a chroma configuration like we did for the entities db
        persist_directory = ".chroma"

        vectordb = Chroma.from_documents(
            documents=split_documents,
            embedding=OpenAIEmbeddings(),
            persist_directory=persist_directory,
        )

        vectordb.persist
        vectordb = None
