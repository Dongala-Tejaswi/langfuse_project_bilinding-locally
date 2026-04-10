from langchain_community.vectorstores import FAISS
from rag.embeddings import get_embeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from pathlib import Path

def create_retriever(file_path: str | None = None):
    env_path = os.getenv("RAG_SOURCE_PATH")
    effective_path = file_path or env_path or str(Path(__file__).resolve().parents[1] / "data" / "sample.txt")

    with open(effective_path, "r", encoding="utf-8") as f:
        text = f.read()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.create_documents([text])

    embeddings = get_embeddings()

    db = FAISS.from_documents(docs, embeddings)

    return db.as_retriever()