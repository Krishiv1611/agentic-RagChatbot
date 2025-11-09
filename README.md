# Agentic-RAG Chatbot

An advanced agentic Retrieval-Augmented Generation (RAG) chatbot system with modular **backend** and **frontend** architecture.  
This system integrates vector storage, session tracking, UI components, and multi-stage agent orchestration to generate intelligent, context-aware responses from external dataset sources.

---

## 📁 Project Structure

agentic-chatbot/
│
├── backend/
│ ├── main.py # FastAPI backend entry point
│ ├── agent.py # Agent orchestration, tools, retrieval and reasoning logic
│ ├── config.py # Backend configuration, environment variables, paths
│ ├── vectorstore.py # Vector DB handling: embeddings, retrieval, storage
│ ├── pycache/ # Compiled python cache files
│ └── ... # Additional backend utilities (if added later)
│
├── frontend/
│ ├── app.py # Frontend UI application launcher
│ ├── backend_api.py # Functions to communicate with backend FastAPI API
│ ├── config.py # Frontend settings, constants, URLs
│ ├── session_manager.py # Conversation/session state handling
│ ├── ui_components.py # UI layout, rendering and interaction components
│ ├── requirements.txt # Dependencies for frontend environment
│ └── pycache/ # Cached python files
│
├── .env # Environment variables (keys, config)
├── .gitignore # Files/folders ignored by Git
├── .python-version # Python version lockfile
├── pyproject.toml # Project metadata and configurations
├── requirements.txt # Global requirements (if used)
└── README.md # Documentation

yaml
Copy code

---

## 🧠 Project Overview

This project implements an intelligent, multi-agent RAG chatbot system where:

- The **backend** handles embeddings, storage, retrieval, and reasoning.
- The **frontend** provides an interactive UI with session-awareness and streamlined communication.
- A structured agent pipeline enhances accuracy, reliability, and contextual depth.

Key capabilities:

- Document ingestion and vector storage
- Retrieval-Augmented Generation (RAG)
- Multi-agent orchestration (retrieve → evaluate → generate)
- Persistent sessions and context flow
- Clean frontend-backend separation

---

## ⚙️ Backend Description

The backend uses **FastAPI** to expose endpoints for querying, extraction, and agent-driven reasoning.

### Backend components:

| File | Description |
|------|-------------|
| `main.py` | Defines API routes, runs FastAPI server, orchestrates request handling. |
| `agent.py` | Core agent logic: retrieval, reasoning, chain-of-actions, tool usage. |
| `vectorstore.py` | Handles embeddings, similarity search, persistent Chroma/other vector DB logic. |
| `config.py` | Stores backend constants, environment variables, paths, model references. |

---

## 🖥️ Frontend Description

The frontend provides a Python-based UI layer (Streamlit or custom UI via `app.py`).

### Frontend components:

| File | Description |
|------|-------------|
| `app.py` | Entry point to run the frontend UI interface. |
| `backend_api.py` | Wrapper for backend API calls (query, ingest, retrieval). |
| `session_manager.py` | Stores and updates user sessions, chat history, context flow. |
| `ui_components.py` | Contains UI building blocks, rendering logic, interaction elements. |
| `config.py` | Frontend-specific configuration (API URL, constants). |
| `requirements.txt` | Dependencies required to run frontend. |

---

## 🔧 Installation & Setup

### ✅ Clone the repository

```bash
git clone https://github.com/your-username/agentic-chatbot.git
cd agentic-chatbot
✅ Backend Setup
bash
Copy code
cd backend
python -m venv venv
source venv/bin/activate       # For Linux/Mac
venv\Scripts\activate          # For Windows

pip install -r ../requirements.txt
Start backend:

bash
Copy code
uvicorn main:app --reload --port 8000
✅ Frontend Setup
bash
Copy code
cd frontend
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows

pip install -r requirements.txt
Launch the frontend UI:

bash
Copy code
python app.py
🧩 How the System Works
pgsql
Copy code
User Input → Frontend UI → backend_api.py → FastAPI Backend
                         ↓
                Backend Agent (agent.py)
                         ↓
                Vectorstore Retrieval
                         ↓
                LLM Response Generation
                         ↓
                 Back to Frontend UI
Steps summary:

User types a query.

Frontend sends query to backend using backend_api.

Backend agent calls vectorstore for relevant chunks.

Agent synthesizes retrieved context.

Final answer generated and sent back.

UI displays formatted output.

✨ Features
✅ Retrieval-Augmented Generation

✅ Multi-agent reasoning pipeline

✅ Persistent vector database

✅ Session-aware conversations

✅ Modular architecture

✅ Extensible design for adding new tools/agents

🚀 Future Enhancements
Docker deployment (backend + frontend)

UI improvements

Adding multiple data ingestion formats

Authentication and user management

Streaming responses

👨‍💻 Author
Krishiv Arora
GitHub: https://github.com/Krishiv1611
