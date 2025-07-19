from pathlib import Path
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_markdown_documents(markdown_dir: str):
    """Loads markdown files from a directory as LangChain Documents."""
    loader = DirectoryLoader(
        markdown_dir,
        glob="**/*.md",
        loader_cls=TextLoader,
        show_progress=True,
        use_multithreading=True
    )
    documents = loader.load()
    return documents

def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    """Splits documents into chunks using RecursiveCharacterTextSplitter."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        add_start_index=True
    )
    chunks = splitter.split_documents(documents)
    return chunks
