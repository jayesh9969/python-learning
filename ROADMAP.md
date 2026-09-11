# Roadmap — Full-Stack Applied AI / GenAI Engineer

*Teaching rules: `CLAUDE.md` · Meri notes: `NOTES.md`*

**Position:** Entry-Level Applied AI / GenAI Engineer.
**Target:** Remote/freelance AI work for international clients, phir AI Engineer role at a startup/tech company.
**Final Principle:** The goal is NOT to learn every AI technology. The goal is to independently **build, deploy, test, evaluate, debug, secure, and explain** a production-style AI application.

---

## Ho chuka ✅

- Python fundamentals — loops, if/else, functions, dicts, comprehension, file handling, try/except
- NumPy + statistics — mean, median, std, z-score, correlation, dot product, matrix multiplication
- Pandas — DataFrame, read_csv, filter, groupby, sort, merge, missing data, to_csv
- Projects — CLI expense tracker · LeNet on MNIST

---

## Learning Path (Order of Execution)

### 1. LLM APIs
> Abhi **Gemini free tier** par seekh rahe hain (`google-genai`, model `gemini-flash-lite-latest`). Concepts wahi hain — baad mein Claude/OpenAI par sirf syntax badlega.

- [x] pehla API call — `llm_apis/01_first_call_and_classifier.py`
- [x] system instruction — jawab ka shape kaabu karna
- [x] structured output — `response_schema` + enum se jawab **pakka** karna (`llm_apis/02_structured_output.py`)
- [x] streaming — `generate_content_stream` (`llm_apis/03_streaming.py`)
- [x] error handling — `ClientError` (429/404) vs `ServerError` (503), retry loop (`llm_apis/04_error_handling_and_retries.py`)
- [x] token counting — `count_tokens()` pehle, `usage_metadata` baad mein (`llm_apis/05_token_counting.py`)
- [ ] thinking dekhna (`include_thoughts=True`) — model chahiye jo support kare

---

### 1.5 SQL, PostgreSQL & pgvector — HIGH Priority
Postgres + pgvector production standard hai. Vector DB aur structured data dono ek jagah.

- [x] `SELECT`, `FROM`, `WHERE`
- [x] `GROUP BY` + `AVG` / `COUNT` / `SUM`
- [x] `ORDER BY`, `LIMIT` — `sql/sqlite_basics_and_joins.py`
- [x] `JOIN` — inner aur left — `sql/sqlite_basics_and_joins.py`
- [x] Python se connect — `sqlite3` + `pd.read_sql`
- [ ] PostgreSQL basics & setup
- [ ] primary / foreign keys, indexes
- [ ] transactions & database migrations
- [ ] connection pooling basics
- [ ] Supabase setup & connection
- [ ] pgvector extension & vector similarity search (`<->`, `<=>`)
- [ ] metadata filtering in PostgreSQL

---

### 2. Embeddings & Vector DBs
- [x] embedding kya hai — text se numbers (`embeddings/semantic_search_scratch.py`, 3072 values, norm 1.0)
- [x] similarity search — `np.dot` (vectors normalized hain to dot hi cosine hai) + `argmax`
- [x] Chroma — `PersistentClient(path=...)` disk par save, `get_or_create_collection` — `embeddings/chroma_gemini_embeddings.py` (Gemini), `embeddings/chroma_metadata_filtering.py` (Chroma)
- [x] store, query, metadata filter — `metadatas=[{...}]` + `where={...}`. `n_results` upar ki hadd hai, guarantee nahi
- [x] `add` vs `upsert` vs `update` — `update()` nayi id par chup-chaap kuch nahi karta, error bhi nahi
- [x] `count()` se pehli-baar wala kaam skip — Gemini ki call bachti hai
- [x] distance ulta hai — `np.dot` mein bada achha, Chroma distance mein chhota achha
- [ ] pgvector vs Chroma trade-offs (kab embedded DB, kab external DB)

---

### 3. Production RAG (Scratch to Production) — HIGH Priority
- [x] poora RAG loop — retrieve -> prompt -> generate. `rag/rag_basic_loop.py` (menu + budget), `rag/chunking_and_citations.py` (college rules)
- [x] chunking — khali line par (`split`) ya fixed size + overlap, har tukda alag embed + alag id
- [x] indexing pipeline — chunk -> embed -> Chroma, `count()` ke guard ke saath
- [x] threshold — sabse kam distance hadd se zyada ho to Gemini call hi mat karo
- [x] grounded generation — "sirf diye gaye data se jawab do", aur "calculation is allowed" ka santulan
- [x] hallucination kab hoti hai aur kyun — instruction guzarish hai, pabandi nahi
- [x] prompt ki shakl — data + sawal ek jagah, saaf label ke saath. Baant do to model confuse
- [x] chunk size aur overlap — `range(0, len(text), size-overlap)`, chhote tukde `len()` se chhaan do — `rag/fixed_size_overlap_chunking.py`
- [x] citations — `enumerate(rules, 1)` se `[1] [2]`, aur prompt mein saaf maango
- [x] re-ranking — Chroma se 8 nikaalo, Gemini se 2-3 chunwao, phir jawab — `rag/rag_reranking.py`
- [ ] **document ingestion pipeline** — real documents handle karna
- [ ] PDF extraction (`pypdf` / `pdfplumber`)
- [ ] HTML / Web extraction
- [ ] metadata design & filtering strategy
- [ ] duplicate detection & incremental indexing (sirf naye/badle documents embed karo)
- [ ] **hybrid search (BM25 + embedding)** — semantic + exact keyword match (`rank_bm25` + dense vectors)
- [ ] query rewriting (user query ko search-friendly banana)
- [ ] contextual compression
- [ ] retrieval evaluation

---

### 4. Backend, Deployment & Containers — HIGH Priority
- [x] FastAPI — endpoints (`@app.get` / `@app.post`), `uvicorn`, `/docs` khud banta hai — `deployment/fastapi_rag_api.py`
- [x] request/response models — Pydantic `BaseModel`, `response_model=`, class = design / object = bhara hua form
- [x] Docker — `Dockerfile`, `requirements.txt`, `.dockerignore`, `docker build -t` / `docker run -p`. `--host 0.0.0.0` zaroori
- [x] environment variables, secrets — `.env` + `--env-file`, `.env` ignore files mein
- [x] live hosting on Render — deployed FastAPI (`https://rag-api-zgoi.onrender.com`)
- [ ] REST API design best practices & HTTP status codes (200, 201, 400, 401, 403, 404, 429, 500)
- [ ] input/output validation & error schemas
- [ ] authentication & authorization basics (API keys, JWT tokens)
- [ ] middleware & CORS handling
- [ ] async endpoints & background tasks (`async def`, `BackgroundTasks`)
- [ ] rate limiting basics (abusive users/DDoS protection)
- [ ] container volumes vs hosted DB (data persistence across container restarts)

---

### 4.1 Python Engineering (Production-Ready Code) — HIGH Priority
Scripting se nikalke software engineer level Python likhna:

- [ ] modules, packages, imports structure
- [ ] virtual environments (`venv`)
- [ ] pip and dependency management (`requirements.txt` pinning)
- [ ] `pyproject.toml` basics
- [ ] type hints (`typing` module, Union, Optional, Callable)
- [ ] dataclasses (`@dataclass` vs Pydantic)
- [ ] basic OOP / classes (encapsulation, methods, `__init__`, `__repr__`)
- [ ] `pathlib` for file/path management
- [ ] JSON handling (robust serialization/deserialization)
- [ ] structured logging (`logging` module, log levels, formatting)
- [ ] async/await and `asyncio` fundamentals

---

### 4.2 Testing & Quality Assurance — HIGH Priority
Production apps bina tests ke deploy nahi hote:

- [ ] `pytest` setup and execution
- [ ] unit tests for core logic
- [ ] API integration tests with FastAPI `TestClient`
- [ ] test fixtures (`@pytest.fixture`)
- [ ] mocking LLM / API responses (bina paisa/tokens kharch kiye test chalana)
- [ ] testing error and failure edge cases
- [ ] regression testing

---

### 4.3 Git & GitHub Professional Workflow — HIGH Priority
- [ ] branches & branch strategy (`main`, feature branches)
- [ ] pull requests (PR) & code review
- [ ] merge conflicts resolve karna
- [ ] rebase basics
- [ ] good commit practices (conventional commits)
- [ ] GitHub Issues & tracking
- [ ] GitHub Actions basics
- [ ] basic CI workflow — push/PR par automatically tests run karna

---

### 4.5 Project 1 — LIVE Portfolio Project ✅
- [x] Marathi WhatsApp Guide RAG Assistant (`whatsapp_rag.py` + Streamlit `app.py`)
- [x] Live deployed on Render: https://rag-api-zgoi.onrender.com/ (Verified 200 OK)
- [x] README.md portfolio presentation
- [ ] **Progressive Upgrades to Project 1:**
  - [ ] Hybrid search (BM25 + Gemini embeddings)
  - [ ] Evaluation benchmark (accuracy & faithfulness score)
  - [ ] Observability (Langfuse tracing)
  - [ ] Security guards against prompt injection

---

### 4.6 Agents & Reliable Tool Calling — CURRENT FOCUS (HIGH Priority)
Job market ka sabse bada gap: **RAG + Agents + Evaluation**. Model sirf text nahi bolta, **actions leta hai**.

- [ ] tool calling — function ko model ke haath mein dena
- [ ] agent loop — soche, tool chalaye, natija dekhe, phir soche (ReAct pattern)
- [ ] kab agent chahiye aur kab sirf RAG kaafi hai
- [ ] tool schema design (parameters, docstrings, type annotations)
- [ ] tool validation (model ke bheje inputs validate karna)
- [ ] tool error handling, retries, timeouts
- [ ] maximum agent steps (infinite loop safety guard)
- [ ] state management & agent memory basics
- [ ] human-in-the-loop approval (critical actions se pehle insaan se poochna)
- [ ] agent evaluation
- [ ] deterministic workflow vs autonomous agent (kab rule-based flow, kab LLM decision)

---

### 4.7 LangGraph (Practical Multi-Step Workflows) — MEDIUM-HIGH Priority
Agents scratch se seekhne ke baad reliable workflows banane ke liye:

- [ ] LangGraph fundamentals & state graph concept
- [ ] state schema
- [ ] nodes (agents / functions)
- [ ] edges & conditional routing
- [ ] tool integration inside graph
- [ ] checkpointing / memory persistence
- [ ] error & retry handling inside graphs

---

### 4.8 MCP (Model Context Protocol) — MEDIUM-HIGH Priority
Tools ko kisi bhi AI model/client se connect karne ka open standard:

- [ ] MCP concepts & architecture (client-server model)
- [ ] MCP server banana
- [ ] tools & resources expose karna
- [ ] MCP server ko agent ke saath connect karna
- [ ] basic authentication & security considerations

---

### 4.9 LangChain / LlamaIndex — CHHOTA OVERVIEW
Jo scratch se banaya uske ecosystem names samajhna (2-3 sessions, interview lookup):
- [ ] TextSplitter, VectorStore, Retriever, PromptTemplate, Chains
- [ ] Portfolio mein primary code scratch + FastAPI + LangGraph hi rahega

---

### 5. Evaluation & Observability — HIGH Priority
Senior aur junior engineer ka sabse bada farak: *kya tum prove kar sakte ho ki tumhara AI sahi kaam kar raha hai?*

#### AI Evaluation:
- [ ] evaluation dataset creation (test set of 20-50 questions + ground truth)
- [ ] retrieval metrics (Hit Rate, MRR, Context Recall, Context Precision)
- [ ] generation metrics (Answer Relevance, Faithfulness/Groundedness)
- [ ] LLM-as-judge pattern & prompt design
- [ ] **RAGAS** framework integration
- [ ] **DeepEval** (pytest-style automated test suite for LLMs)
- [ ] regression evaluation (prompt/chunk change karne par purani quality giri to nahi?)

#### Observability & Tracing:
- [ ] structured logging for AI systems
- [ ] request tracing & span breakdown
- [ ] LLM input/output tracing
- [ ] token usage, latency, and cost tracking per request
- [ ] error tracking & rate monitoring
- [ ] **Langfuse** (ya equivalent open-source tool) setup & dashboard

---

### 5.5 AI Security & Guardrails — HIGH Priority
Public AI apps ko hack hone aur galat jawab dene se bachana:

- [ ] prompt injection (direct jailbreaking)
- [ ] indirect prompt injection (document/data ke andar chhupa hua malicious prompt)
- [ ] input validation & sanitization
- [ ] output validation & Pydantic schema enforcement
- [ ] secrets management (API keys, credentials leak prevention)
- [ ] sensitive data leakage prevention (PII detection)
- [ ] tool abuse prevention (unauthorized actions rokna)
- [ ] rate limiting & abuse prevention
- [ ] basic guardrails (NeMo Guardrails ya custom validator rules)

---

### 6. Cloud & CI/CD Fundamentals — MEDIUM Priority
Basic cloud infrastructure samajhna (mastery nahi, foundational literacy):

- [ ] cloud concepts (compute, object storage, managed databases, secrets, networking)
- [ ] AWS / GCP / Azure basics overview
- [ ] CI/CD pipeline principles
- [ ] GitHub Actions deployment workflow (build, test, deploy to Render/Cloud)

---

### 7. Basic Machine Learning (Compact) — MEDIUM Priority
Applied AI engineer ke liye foundational ML intuition:

- [ ] train / validation / test splits
- [ ] supervised vs unsupervised learning
- [ ] overfitting vs underfitting, data leakage
- [ ] classification vs regression
- [ ] evaluation metrics: confusion matrix, precision, recall, F1-score, ROC-AUC
- [ ] cross-validation
- [ ] basic `scikit-learn` pipeline workflow

---

### 8. PyTorch & Deep Learning — LOW-MEDIUM Priority
Sirf itna ki job description samajh aaye aur custom embeddings/models ka intuition ho:

- [ ] tensors, autograd
- [ ] `Dataset` / `DataLoader`
- [ ] `nn.Module`, loss functions, optimizers
- [ ] training loop & validation loop
- [ ] save / load model weights (`torch.save`, `torch.load`)
- [ ] model inference

---

### 9. Minimal Frontend for AI Backends — LOW-MEDIUM Priority
AI backend ko user ke haath mein dene ke liye zaroori frontend (not a separate career track):

- [ ] HTML / CSS basics
- [ ] JavaScript basics & `fetch()` API calls
- [ ] basic React components & state
- [ ] React frontend ko FastAPI backend se connect karna

---

## Portfolio Projects Strategy

Client ko skills ki list nahi, **working links aur code** chahiye. Har major project mein:
`Live Deployed URL + Clean README + Architecture Diagram + Tests + Eval Metrics + Demo Video`

- [x] **Project 1: Marathi WhatsApp Guide RAG Assistant (LIVE)**
  - Deployed on Render: [https://rag-api-zgoi.onrender.com/](https://rag-api-zgoi.onrender.com/)
  - RAG with Gemini Flash, ChromaDB, Streamlit UI.
  - Progressive updates: hybrid search, evaluation benchmarks, observability.
- [ ] **Project 2: Autonomous Production AI Agent (Flagship Job-Ready Project)**
  - Real-world workflow automation.
  - Tool calling, agent loop/state, reliable error recovery.
  - FastAPI backend, PostgreSQL + pgvector, authentication, Docker.
  - Automated testing with pytest + mocking.
  - Full evaluation (RAGAS/DeepEval) & Observability (Langfuse).
  - Deployed live with CI/CD.
- [ ] **Project 3: Specialized Domain Solution (Optional / Flagship)**
  - Enterprise-style multi-agent or hybrid search RAG addressing complex document workflows.

---

## Job-Readiness Checklist (Kab Apply Karna Shuru Karein)

Har low-priority item khatam hone ka intezar mat karo. Jab ye checklist poori ho jaye, **actively apply karna shuru kar do**:

- [ ] Python engineering fundamentals (modules, typing, async, logging)
- [ ] SQL / PostgreSQL basics
- [ ] LLM APIs (structured outputs, streaming, error handling)
- [ ] Embeddings & Vector search
- [ ] Production RAG with hybrid search (BM25 + dense)
- [ ] Agents & reliable tool calling with error handling
- [ ] AI Evaluation (RAGAS / DeepEval metrics)
- [ ] FastAPI backend + Pydantic validation
- [ ] Docker containerization
- [ ] Git & GitHub workflow with basic CI (GitHub Actions)
- [ ] Testing with pytest (unit + integration + mocks)
- [ ] Basic AI security & secret management
- [ ] Deployment & live hosting
- [ ] Observability & tracing (Langfuse)
- [ ] At least 2 strong deployed projects (Project 1 live + Project 2 flagship)

---

## Abhi Skip (Out of Scope for Entry-Level)

Deep ML research theory · scratch se transformer train karna · Kaggle competitions · LeetCode hard · expensive certifications · Kubernetes cluster administration · distributed MLOps pipelines (Kubeflow) · Spark / Kafka · Terraform infrastructure-as-code · extensive fine-tuning (eval pehle; 95% industry problems RAG + prompt + agent se solve hote hain).

---

## Toolkit Ab Tak (Verified Skills)

**Python:** variables · loops · if/else · functions · file read/write · try/except · comprehension · `for/else`
**NumPy & Stats:** arrays · vectorization · boolean filter · `mean`/`median`/`std`/`z-score`/`argmax` · `shape`/`reshape` · `axis=0/1` · broadcasting · `np.dot` · correlation · mode · probability
**Pandas:** `DataFrame` · `read_csv`/`to_csv` · `loc` · filter · `groupby` · `sort_values` · `isnull`/`dropna`/`fillna` · `merge` · `astype('Int64')`
**SQL:** `SELECT` · `WHERE` · `GROUP BY` · `ORDER BY` · `LIMIT` · `JOIN` · `sqlite3` + `pd.read_sql`
**LLM API (Gemini):** `generate_content` · `system_instruction` · `response_schema` + enum · `generate_content_stream` · `ClientError`/`ServerError` retry · `count_tokens` · `usage_metadata`
**Vector DB (Chroma):** `PersistentClient` · `get_or_create_collection` · `add`/`upsert`/`update` · `count()` · `query` · `distances` · `metadatas` + `where` · `delete_collection`
**RAG (Scratch):** chunking (split + fixed size with overlap) · retrieval pipeline · distance threshold · grounding instruction · citations · 2-tier re-ranking
**Deployment & Containers:** FastAPI (`@app.get`/`@app.post`, Pydantic models, `/docs`) · `uvicorn` · Docker (`Dockerfile`, `build`, `run -p`, `.dockerignore`) · `.env` + `--env-file` · Render hosting · Streamlit UI (`st.session_state`, `st.chat_message`)
**Projects Live:** Project 1 (Marathi WhatsApp RAG Assistant deployed on Render)
