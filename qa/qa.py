from langchain.chains import RetrievalQA
from langchain.schema import SystemMessage, HumanMessage
from langchain.chat_models import ChatOpenAI
from config import API_KEY, API_BASE, CHAT_MODEL_NAME

def get_chat_model():
    """Initialize and return a ChatOpenAI model (local or hosted)."""
    return ChatOpenAI(
        openai_api_base=API_BASE,
        api_key=API_KEY,
        model=CHAT_MODEL_NAME,
        temperature=0.1
    )

def create_qa_chain(retriever):
    """Create a RetrievalQA chain using the retriever and chat model."""
    chat_model = get_chat_model()
    qa_chain = RetrievalQA.from_chain_type(
        llm=chat_model,
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain
