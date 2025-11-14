import streamlit as st
from dotenv import load_dotenv
import os, json

from langchain_openai import ChatOpenAI
from utils.pdf_loader import load_pdf_text
from utils.embed_store import create_vectorstore_from_text


# ============ ENV SETUP ============ #
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="📄 PDF RAG Chatbot", page_icon="🤖")

st.title("🤖 Chat with PDF (Memory Powered)")
st.write("Upload a PDF → Ask → Continue conversation like ChatGPT 📚✅")

# ============ MEMORY FILE ============ #
MEMORY_FILE = "chat_history.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(MEMORY_FILE, "r") as f:
            messages = json.load(f)
            return [m for m in messages if "role" in m and "content" in m]
    except:
        return []


def save_memory(messages):
    with open(MEMORY_FILE, "w") as f:
        json.dump(messages, f, indent=4)


# ============ SESSION STATE ============ #
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "messages" not in st.session_state:
    st.session_state.messages = load_memory()


# ✅ Reset option
if st.button("🧹 Reset Chat"):
    st.session_state.messages = []
    if os.path.exists(MEMORY_FILE):
        os.remove(MEMORY_FILE)
    st.rerun()


# ============ SIDEBAR ============ #
with st.sidebar:
    st.header("📄 Upload PDF")
    pdf_file = st.file_uploader("Choose a PDF", type=["pdf"])

    if pdf_file:
        with st.spinner("🔍 Processing PDF..."):
            texts = load_pdf_text(pdf_file)
            st.session_state.vectorstore = create_vectorstore_from_text(
                texts=texts,
                openai_api_key=OPENAI_API_KEY
            )

        st.success("✅ PDF Ready to Chat!")
        if not st.session_state.messages:
            st.session_state.messages.append({
                "role": "assistant",
                "content": "PDF loaded! Ask anything from the document 📌"
            })
        save_memory(st.session_state.messages)


# ============ RAG Answering ============ #
def rag_answer(user_query):
    retriever = st.session_state.vectorstore.as_retriever()

    # ✅ Updated Retriever Call
    docs = retriever.invoke(user_query)

    context = "\n\n".join([d.page_content for d in docs])

    history_text = "\n".join([
        f"{m['role'].capitalize()}: {m['content']}"
        for m in st.session_state.messages
        if m["role"] != "system"
    ])

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY from this PDF context below:

Context:
{context}

Conversation History:
{history_text}

User Question: {user_query}

If the answer is not found in context, respond:
"I couldn't find that in the PDF."
"""

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    result = llm.invoke(prompt)

    return result.content


# ✅ Display all chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# ✅ Chat Input
if st.session_state.vectorstore:
    user_input = st.chat_input("Ask anything from the PDF...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        save_memory(st.session_state.messages)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = rag_answer(user_input)
                st.markdown(answer)

        st.session_state.messages.append({"role": "assistant", "content": answer})
        save_memory(st.session_state.messages)

else:
    st.info("📌 Please upload a PDF to begin chatting.")
