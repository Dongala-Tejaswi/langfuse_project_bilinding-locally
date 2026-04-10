# 🚀 Local RAG System with Langfuse Observability + Groq

A **production-ready Retrieval-Augmented Generation (RAG) pipeline** built with modern LLM tooling, featuring **end-to-end observability using Langfuse** and **high-speed inference via Groq**.

---

## 📌 Overview

This project demonstrates how to build a **scalable, traceable LLM system** by combining:

* 🔍 Retrieval (FAISS + Embeddings)
* 🧠 Generation (Groq LLM)
* 📊 Observability (Langfuse)
* 🐳 Containerization (Docker)

---

## 🏗️ Architecture

```
User Query
    ↓
Retriever (FAISS + Embeddings)
    ↓
Context Injection
    ↓
LLM (Groq API)
    ↓
Response
    ↓
Langfuse (Tracing + Monitoring)
```

---

## ⚙️ Tech Stack

| Component        | Technology           |
| ---------------- | -------------------- |
| LLM              | Groq (LLaMA 3.1)     |
| Embeddings       | HuggingFace (MiniLM) |
| Vector DB        | FAISS                |
| Observability    | Langfuse             |
| Backend          | Python               |
| Containerization | Docker               |

---

## 📂 Project Structure

```
local_langfuse/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .env.example
├── rag/
│   ├── retriever.py
│
├── observability/
│   ├── langfuse_config.py
│
└── README.md
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
LANGFUSE_PUBLIC_KEY=your_public_key
LANGFUSE_SECRET_KEY=your_secret_key
LANGFUSE_HOST=http://localhost:3000
```

---

## 🐳 Docker Setup

### 1️⃣ Build Docker Image

```bash
docker build -t rag-langfuse-app .
```

### 2️⃣ Run Container

```bash
docker run --env-file .env rag-langfuse-app
```

---

## 📊 Langfuse Setup (Local)

Run Langfuse using Docker:

```bash
docker run -d -p 3000:3000 langfuse/langfuse
```

👉 Open dashboard:
http://localhost:3000

---

## 🔍 Features

✅ Retrieval-Augmented Generation (RAG)
✅ Semantic Search with FAISS
✅ Fast LLM inference via Groq
✅ End-to-End tracing with Langfuse
✅ Dockerized for portability
✅ Clean modular architecture

---

## 📈 Observability (Langfuse)

This project integrates **Langfuse tracing** to:

* Track input/output of LLM calls
* Monitor latency and performance
* Debug prompt + response flow
* Analyze production behavior

---

## 🚀 Example Query

```
Enter your question: What is RAG?
```

💡 Output:

```
RAG stands for Retrieval-Augmented Generation...
```

---

## 🧠 Key Learnings

* Separation of **retrieval vs generation**
* Importance of **observability in LLM systems**
* Using **vector databases for semantic search**
* Managing **LLM pipelines in production**

---

## ⚠️ Notes

* Do NOT commit:

  * `venv/`
  * `.env`
* Use `.gitignore` and `.dockerignore` properly

---

## 💼 Use Cases

* AI Chatbots
* Knowledge Base Assistants
* Document QA Systems
* Enterprise Search

---

## 🔮 Future Improvements

* Add UI (Streamlit / React)
* Multi-document ingestion
* Hybrid search (BM25 + vector)
* Deployment (AWS / GCP)

---

## 👨‍💻 Author

**Tejaswi Dongala**

---

## ⭐ Final Thought

> “LLMs are powerful — but without observability, they are black boxes.
> This project turns them into transparent, production-ready systems.”

---
