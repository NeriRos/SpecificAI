from langchain import OpenAI
from langchain.embeddings import OpenAIEmbeddings

from src.ai.prepare_data import get_vector_db, get_content_chunks_documents


def init_vector_db(topic):
    if topic is None:
        exit(1)
    print("Initializing vector DB")

    llm = OpenAI(temperature=0)
    embeddings = OpenAIEmbeddings()

    content_chunks_documents = get_content_chunks_documents(topic)

    vector_db = get_vector_db(content_chunks_documents, embeddings)

    print("Vector DB initialized")

    return llm, vector_db
