from config import PDF_DIR, CHROMA_DB_PATH
from loaders.pdf_loader import convert_all_pdfs_to_markdown
from loaders.md_loader import load_markdown_documents, split_documents
from vectorstore.store import create_vectorstore, load_vectorstore
from qa.qa import create_qa_chain

def main():
    # Step 1: Convert PDFs to Markdown
    print("✅ Converting PDFs to markdown...")
    convert_all_pdfs_to_markdown(PDF_DIR)

    # Step 2: Load markdown and split
    print("📄 Loading and splitting markdown files...")
    documents = load_markdown_documents(PDF_DIR)
    chunks = split_documents(documents)

    # Step 3: Create vectorstore
    print("📦 Creating Chroma vector store...")
    vectorstore = create_vectorstore(chunks)

    # Step 4: Setup retriever
    # retriever = vectorstore.as_retriever()
    retriever = vectorstore.as_retriever(
    search_type="similarity",  
    search_kwargs={"k": 3}  )

    # Step 5: Create QA chain
    print("🤖 Initializing QA system...")
    qa_chain = create_qa_chain(retriever)

    # Step 6: Run a test query
    query = "What is patent analysis dataset is about?"
    response = qa_chain(query)

    print("\n💬 Answer:")
    print(response['result'])

    print("\n📚 Source Documents:")
    for doc in response['source_documents']:
        print(f"- {doc.metadata.get('source', 'No source')}")


if __name__ == "__main__":
    main()
