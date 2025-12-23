# Agentic RAG System (FastAPI + MySQL + Ollama)

This project is a **retrieval-first, agentic RAG system** that answers user queries strictly using up-to-date federal documents stored in a MySQL database.

The system avoids hallucinations by refusing to answer when no relevant records exist.

---

## 🔧 Architecture Overview


### Components
- **Data Pipeline**: Downloads and processes daily-updated Federal Register data
- **Database**: MySQL (raw SQL, no ORM)
- **Agent**: Tool-based LLM (Ollama / Qwen 2.5)
- **API**: FastAPI (async)
- **UI**: Streamlit

---

## 🚀 Features

- Daily-updating data pipeline
- Tool-restricted agent (no hallucinations)
- Raw SQL querying (no ORM)
- Async FastAPI backend
- Local LLM via Ollama
- Simple chat UI

---

## 🛠 Tech Stack

- Python
- FastAPI
- MySQL
- aiomysql
- Ollama (Qwen 2.5)
- Streamlit

---
