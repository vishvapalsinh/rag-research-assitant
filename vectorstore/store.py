# vectorstore/store.py

from langchain_community.vectorstores import Chroma  # ✅ Correct modern import
from embeddings.embedder import get_embedding_model
from config import CHROMA_DB_PATH

def create_vectorstore(chunks, persist: bool = True):
    """
    Create a Chroma vectorstore from document chunks and optionally persist it.
    
    Args:
        chunks: A list of LangChain Document objects.
        persist: Whether to save the vectorstore to disk.
    
    Returns:
        Chroma vectorstore instance.
    """
    embeddings = get_embedding_model()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DB_PATH
    )

    if persist:
        vectorstore.persist()

    return vectorstore

def load_vectorstore():
    """
    Load an existing Chroma vectorstore from disk.
    
    Returns:
        Chroma vectorstore instance.
    """
    embeddings = get_embedding_model()

    vectorstore = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embeddings
    )

    return vectorstore
