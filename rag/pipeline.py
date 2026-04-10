import os
from dotenv import load_dotenv

from observability.langfuse_config import (
    get_langfuse_callback_handler,
    get_langfuse_client,
)

_retriever = None
_llm = None


def _get_retriever():
    global _retriever
    if _retriever is None:
        from rag.retriever import create_retriever

        _retriever = create_retriever()
    return _retriever


def _retrieve_docs(retriever, query: str):
    # LangChain retriever API varies by version:
    # - older: retriever.get_relevant_documents(query)
    # - newer (Runnable): retriever.invoke(query)
    if hasattr(retriever, "get_relevant_documents"):
        return retriever.get_relevant_documents(query)
    return retriever.invoke(query)


def _get_llm():
    global _llm
    if _llm is None:
        from langchain_groq import ChatGroq

        _llm = ChatGroq(
            model="llama-3.1-8b-instant",
            groq_api_key=os.getenv("GROQ_API_KEY"),
        )
    return _llm


def run_query(query: str):
    # Load env variables first (once per process)
    load_dotenv()

    # 🔍 Retrieve documents
    retriever = _get_retriever()
    docs = _retrieve_docs(retriever, query)
    context = "\n".join([doc.page_content for doc in docs])

    # 🧠 Prepare prompt
    prompt = f"Answer based on context:\n{context}\n\nQuestion: {query}"

    # 🚀 Call Groq
    llm = _get_llm()
    langfuse = get_langfuse_client()
    langfuse_cb = get_langfuse_callback_handler()
    invoke_config = {"callbacks": [langfuse_cb]} if langfuse_cb is not None else {}
    response_msg = llm.invoke(prompt, config=invoke_config)
    answer = response_msg.content

    # 📊 Send trace to Langfuse (SAFE)
    try:
        if langfuse is not None:
            langfuse.trace(
                name="rag-query",
                input={"query": query},
                output={"answer": answer},
            )
            langfuse.flush()
    except Exception as e:
        print("Langfuse tracing skipped:", e)

    return answer