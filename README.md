# Python Learning Journey

This repo is my programming journey from beginner python learner to AI/ML engineer

## Learning Goals

- Python fundamentals
- Data handling with NumPy and Pandas
- Machine Learning models
- Deep Learning with PyTorch
- RAG and LLM applications


## 🚀 Featured Project: Marathi WhatsApp Guide (RAG Assistant)

An AI-powered assistant designed for native Marathi speakers to easily learn and use WhatsApp features (creating groups, UPI payments, checking balance, security).

- **Live URL:** [https://rag-api-zgoi.onrender.com/](https://rag-api-zgoi.onrender.com/)
- **Tech Stack:** Streamlit, Google Gemini (`gemini-flash-lite-latest`), Gemini Embeddings (`gemini-embedding-001`), ChromaDB, Docker, Render
- **How it works:**
  1. Procedural steps stored and chunked as complete multi-step guides in ChromaDB vector database.
  2. Semantic similarity search retrieves exact procedural instructions.
  3. Grounded Gemini generation translates and explains the steps cleanly in authentic Marathi text with zero hallucination.

---

## 🛠️ Other Projects & Milestones

1. **Production RAG API (FastAPI + Docker):** Containerized REST API with Pydantic request/response validation, similarity threshold guards, and re-ranking pipeline deployed to Render.
2. **CLI Expense Tracker:** Python fundamentals, file handling, category analytics.
3. **LeNet on MNIST:** Deep learning classifier built with PyTorch.

---

## 📚 Repository Structure

The codebase is organized by learning phases and applied topics:

```text
python-learning/
├── python_basics/             # Core Python (variables, loops, functions, error handling, files)
├── numpy_and_stats/           # Vector math, arrays, 2D indexing, statistics & correlation
├── pandas/                    # DataFrames, filtering, groupby, merging, missing values
├── sql/                       # SQLite, relational queries, joins
├── llm_apis/                  # Gemini API calls, structured outputs, streaming, token counting
├── embeddings/                # Semantic search from scratch, ChromaDB collections & filters
├── rag/                       # Full RAG loop, chunking with overlap, citations, 2-tier re-ranking
├── deployment/                # FastAPI REST API, Pydantic models, Docker setup
├── agents/                    # Autonomous agents, tool calling, multi-step loops
├── revisions_and_practice/    # Practice drills, revision scripts, exams
└── projects/
    ├── expense_tracker/       # CLI personal finance tracker
    └── project1_whatsapp_guide/ # Live deployed Streamlit WhatsApp RAG guide
```

---

## 📚 Roadmap & Progress
See [ROADMAP.md](ROADMAP.md) for current learning phases and upcoming milestones (Agents + Tool Calling).
