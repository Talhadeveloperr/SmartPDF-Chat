# 📘 PDF-RAG App

A lightweight Retrieval-Augmented Generation (RAG) application in Python.  
Upload a PDF → the app extracts text → builds vector embeddings → and answers questions about the document using an LLM.

---

## 🚀 Highlights
- Upload and process PDF files (PyPDF2)  
- Create embeddings and store vectors (FAISS / OpenAI embeddings)  
- Retrieval-augmented answers (contextual responses limited to PDF content)  
- Simple Streamlit UI and local chat memory (`chat_history.json`)  
- Safe: keep API keys in `.env` (never commit secrets)



---

## 📸 Screenshots



![App - Upload & Ready](Screenshot 2025-10-28 015710.png)  


![App - Chat Interface](Screenshot 2025-10-28 015801.png)  


---

## ⚙️ Setup (Windows)

1. Create & activate a venv:
```powershell
python -m venv venv
venv\Scripts\activate
Install dependencies:

powershell
Copy code
pip install -r requirements.txt
Add your API key to .env (already present in your project):

ini
Copy code
OPENAI_API_KEY=your_api_key_here
Important: Add .env to .gitignore to avoid committing keys.

Run the app:

powershell
Copy code
python app.py
Open the URL printed by Streamlit (or http://localhost:8501) in your browser.

🧠 How it works (brief)
PDF upload → pages extracted by PyPDF2.

Text chunks → preprocessed to sensible chunk sizes.

Embeddings → created with OpenAI embeddings (or alternative).

FAISS vector store → stores and retrieves top relevant chunks.

LLM prompt → LLM answers using only retrieved context and chat history.

Chat history → saved locally to chat_history.json.

✅ Recommendations & Notes
Never commit credentials — keep .env local and add to .gitignore:

bash
Copy code
# .gitignore
.env
chat_history.json
__pycache__/
*.pyc
If you use real AWS/OpenAI keys and accidentally commit them, rotate the keys immediately.

If you plan to deploy publicly, consider backend token management (server-side) and not exposing keys in client code.

🧩 requirements.txt (example)
Add these to your requirements.txt (adjust versions if needed):

nginx
Copy code
streamlit
python-dotenv
PyPDF2
faiss-cpu
langchain-community
langchain-openai
🤝 Contributing
PRs and issues welcome. If you add new features (chunking, caching, multi-file upload, search UI), please document them in the README.

📜 License
MIT License — feel free to reuse or improve.

ℹ Contact
If you want a polished README badge set, a demo GIF, or an architecture diagram added, tell me which style you prefer and I’ll add it.

yaml
Copy code

---

If you want, I can:
- Add GitHub badges (build, license, python)  
- Provide a shorter README for the repo description + a longer `docs/` file  
- Produce a ready `.gitignore` and updated `requirements.txt` tuned to your environment

Which one shall I add next?











