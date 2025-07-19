from langchain_openai import OpenAIEmbeddings
from config import API_BASE, API_KEY, MODEL_NAME

def get_embedding_model():
    """Initializes and returns the embedding model."""
    embeddings = OpenAIEmbeddings(
        openai_api_base=API_BASE,
        api_key=API_KEY,
        model=MODEL_NAME
    )
    return embeddings