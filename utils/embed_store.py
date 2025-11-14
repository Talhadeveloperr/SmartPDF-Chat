from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def create_vectorstore_from_text(texts, openai_api_key):
    """Create FAISS vector store from PDF texts."""
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectorstore = FAISS.from_texts(texts, embedding=embeddings)
    return vectorstore
