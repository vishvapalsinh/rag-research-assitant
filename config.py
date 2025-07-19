import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API and model settings
API_KEY = os.getenv("LLM_API_KEY")
MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME")
CHAT_MODEL_NAME = os.getenv("CHAT_MODEL_NAME")
API_BASE = os.getenv("API_BASE")

# Paths
PDF_DIR = os.getenv("PDF_DIR", "./data/papers")
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "./chroma_db")
