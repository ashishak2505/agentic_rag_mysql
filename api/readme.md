# Agentic RAG System (FastAPI + MySQL + Ollama)

This project is a **retrieval-first, agentic RAG system** that answers user queries strictly using up-to-date federal documents stored in a MySQL database.

The system avoids hallucinations by refusing to answer when no relevant records exist.

---

## 🔧 Architecture Overview
## 🧠 How the Agent Works (Agentic Flow)

1. User submits a query via UI or API
2. Intent is extracted deterministically (no LLM guessing)
3. Agent calls a single allowed tool (`search_docs`)
4. Tool executes raw SQL against MySQL
5. If results exist → they are returned
6. If no results exist → agent refuses to answer
7. LLM is used only for formatting/summarization

⚠️ The agent is **not allowed** to:
- Query external APIs
- Generate answers without database evidence
- Write SQL or invent tools


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
## 🏗 System Architecture

      ┌────────────┐
      │   User UI  │  (Streamlit)
      └─────┬──────┘
            │
            ▼
    ┌────────────────┐
    │ FastAPI Server │
    │   /chat API    │
    └─────┬──────────┘
          │
          ▼
  ┌──────────────────┐
  │ Agent Controller │
  │ (Intent + Rules) │
  └─────┬────────────┘
        │ tool call
        ▼
 ┌───────────────────┐
 │ search_docs Tool  │
 │ (Raw SQL)         │
 └─────┬─────────────┘
       │
       ▼
 ┌───────────────────┐
 │   MySQL Database  │
 │ federal_docs      │
 └───────────────────┘
