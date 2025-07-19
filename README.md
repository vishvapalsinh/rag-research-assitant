
# 🧠 Research Assistant with LLM + Chroma Vector Store

This project is designed to assist **researchers or document readers** in **answering questions based on the context of uploaded PDF documents**. By leveraging language models and vector databases, the assistant can understand, store, and retrieve information from your local research documents.

---

## 📂 Project Structure

```
research-assistant/
│
├── main.py                        # Main script to run the pipeline
├── .env                           # Environment variables (not pushed to Git)
├── requirements.txt               # Python dependencies
├── research_assistant.ipynb       # Jupyter notebook version of the pipeline
│
├── config/
│   └── config.py                  # Stores constants like API keys, paths, model names
│
├── embeddings/
│   ├── __init__.py
│   └── embedder.py                # Loads the embedding model
│
├── loaders/
│   ├── __init__.py
│   └── md_loader.py               # Loads and chunks markdown/text files
│
├── vectorstore/
│   ├── __init__.py
│   └── store.py                   # Create/load Chroma vectorstore
│
└── qa_chain/
    ├── __init__.py
    └── chain.py                   # Creates a RetrievalQA chain using the retriever and LLM
```

---

## 🚀 Features

- ✅ Load and chunk local markdown/text documents
- ✅ Generate custom embeddings using OpenAI-compatible APIs
- ✅ Store and retrieve documents from **Chroma vector store**
- ✅ Ask questions using RetrievalQA with source documents
- ✅ Modular design for maintainability and reuse
- ✅ Jupyter Notebook included for exploration

---

## 🧪 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/research-assistant.git
cd research-assistant
```

### 2. Create `.env` file

Create a `.env` file in the root directory with the following variables:

```
API_BASE=https://your-llm-api-base-url
API_KEY=your_api_key
MODEL_NAME=your_embedding_model_name
CHROMA_DB_PATH=./chroma_db
DOCS_PATH=./documents
```

> ✅ Make sure `.env` is listed in `.gitignore` so your keys are not exposed.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Usage

### 🟢 Option 1: Run from Python script

```bash
python main.py
```

### 🟡 Option 2: Explore via Jupyter Notebook

Open `research_assistant.ipynb` in Jupyter or VS Code and run the cells step-by-step.

---

## 🔎 Example Query

```python
query = "What is the function of vitamin B12 in the human body?"
response = qa_chain.run(query)
print(response)
```

---

## 📘 Dependencies

- `langchain`
- `langchain-openai`
- `langchain-community`
- `chromadb`
- `python-dotenv`

---

## 🛡️ Security Notes

- Keep your `.env` file private.
- Never commit API keys or sensitive paths to GitHub.

---

## 📚 Credits

This project uses:
- [LangChain](https://www.langchain.com/)
- [Chroma](https://www.trychroma.com/)
- OpenAI-compatible LLM endpoints

---

## 📌 To Do

- [ ] Add support for PDFs (currently markdown/text support)
- [ ] Add semantic accuracy evaluation
- [ ] Streamlit web interface

---

## 📄 License

MIT License
