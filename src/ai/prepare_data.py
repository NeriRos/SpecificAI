import pathlib

from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma


def get_contents_of_directory(path):
    directory_path = pathlib.Path(path)
    files = list(directory_path.glob("**/*"))
    for file in files:
        with open(file, "r") as f:
            yield Document(page_content=f.read(), metadata={"source": f.name})


def get_content_chunks_documents(topic):
    sources = get_contents_of_directory('./content/' + topic)
    source_chunks = []

    splitter = CharacterTextSplitter(separator=" ", chunk_size=1024, chunk_overlap=0)
    for source in sources:
        for chunk in splitter.split_text(source.page_content):
            source_chunks.append(Document(page_content=chunk, metadata=source.metadata))

    return source_chunks


def get_vector_db(docs, embeddings):
    persist_directory = 'db'

    if not pathlib.Path(persist_directory).exists():
        pathlib.Path(persist_directory).mkdir()

    return Chroma.from_documents(docs, embeddings, persist_directory=persist_directory)
