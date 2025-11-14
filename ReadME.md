# 📄 SmartPDF-Chat: A RAG Application

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Talhadeveloperr/SmartPDF-Chat?style=social)](https://github.com/Talhadeveloperr/SmartPDF-Chat/stargazers)

---

> An elegant and lightweight **Retrieval-Augmented Generation (RAG) application** built with Python and Streamlit.
> Upload any PDF, and instantly chat with its content using an **OpenAI**-powered Large Language Model (LLM).
> Contextual answers are guaranteed, as the LLM is restricted to the information retrieved directly from your document.

## 🚀 Key Highlights
* **PDF Processing:** Efficiently upload and extract text from PDF files using **`PyPDF2`**.
* **Vector Store:** Create robust vector embeddings and store them locally using **FAISS** (with OpenAI Embeddings).
* **Contextual Answers:** Utilize Retrieval-Augmented Generation to ensure all responses are grounded in the PDF content.
* **User Interface:** Simple, interactive chat UI built with **Streamlit**.
* **Local History:** Maintains a continuous conversation flow with local chat memory (`chat_history.json`).
* **Secure:** Keeps the API key safe using a local **`.env`** file.

---

## 📸 Application Demo

<p align="center">
  <img src="Screenshot 2025-10-28 015710.png" alt="Upload & Ready Screen" width="700"/>
  <br>
  <em>Figure 1: Upload and processing screen.</em>
</p>

<p align="center">
  <img src="Screenshot 2025-10-28 015801.png" alt="Chat Interface" width="700"/>
  <br>
  <em>Figure 2: The Streamlit chat interface providing contextual answers.</em>
</p>

---

## ⚙️ Quick Setup (Windows/Linux)

Follow these simple steps to get the application running on your local machine.

### 1. Clone the Repository

```bash
git clone [https://github.com/Talhadeveloperr/SmartPDF-Chat.git](https://github.com/Talhadeveloperr/SmartPDF-Chat.git)
cd SmartPDF-Chat
2. Set up Environment & Dependencies
It is highly recommended to use a virtual environment.

```

# Install required packages

```
pip install -r requirements.txt
```

3. Configure API Key
Create a file named .env in the project's root directory and add your OpenAI API key.



# .env file content
``
OPENAI_API_KEY=your_api_key_here
``


4. Run the Application
Execute the application using Streamlit:

PowerShell

streamlit run app.py
The app will open automatically in your browser (usually at http://localhost:8501).

🧠 How It Works: The RAG Workflow
This application uses the core principles of Retrieval-Augmented Generation (RAG) to ensure responses are grounded in the provided PDF content.

Document Loading: The PDF file is uploaded, and its content is extracted page by page using PyPDF2.

Text Chunking: The extracted text is split into smaller, manageable chunks to improve the semantic retrieval accuracy.

Embedding Generation: Each text chunk is converted into a high-dimensional vector (embedding) using the OpenAI Embeddings model.

Vector Store (FAISS): These vectors are stored in a local, memory-efficient vector database (FAISS) for rapid search.

Retrieval: When a question is asked, the query is vectorized, and the system searches the FAISS index to retrieve the most semantically relevant text chunks (the context).

LLM Prompt: The retrieved context, along with the user's question, is packaged into a final prompt for the LLM, which generates an answer strictly based on the provided context.

Chat History: The full conversation is persisted locally in chat_history.json.

✅ Safety & Best Practices
To ensure security and a clean repository, your project should use a .gitignore file containing the following essential entries:

Code snippet
```
# .gitignore
# Local environment and secret files
.env
venv/
__pycache__/
*.pyc
```

# Application state
chat_history.json
Security Reminder: If you ever commit a real API key by accident, you must rotate the key immediately via your OpenAI dashboard. For public deployment, use secure methods like Streamlit's native secrets management instead of environment variables.

requirements.txt 

```
streamlit
python-dotenv
PyPDF2
faiss-cpu
langchain-community
langchain-openai
```



