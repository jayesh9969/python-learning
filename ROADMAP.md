# Roadmap — Full-Stack AI App Builder

*Teaching rules: `CLAUDE.md` · Meri notes: `NOTES.md`*

**Position:** Full-Stack AI App Builder. **Not** junior ML engineer.
**Target:** remote/freelance AI work for international clients, phir AI Engineer role at a startup.

---

## Ho chuka ✅

- Python fundamentals — loops, if/else, functions, dicts, comprehension, file handling, try/except
- NumPy + statistics — mean, median, std, z-score, correlation, dot product, matrix multiplication
- Pandas — DataFrame, read_csv, filter, groupby, sort, merge, missing data, to_csv
- Projects — CLI expense tracker · LeNet on MNIST

---

## Ab ye — isi order mein

### 1. LLM APIs

> Abhi **Gemini free tier** par seekh rahe hain (`google-genai`, model `gemini-flash-lite-latest`). Concepts wahi hain — baad mein Claude/OpenAI par sirf syntax badlega.

- [x] pehla API call — `llm01.py`
- [x] system instruction — jawab ka shape kaabu karna
- [x] structured output — `response_schema` + enum se jawab **pakka** karna (guzarish nahi, pabandi)
- [x] streaming — `generate_content_stream`, `end=""`, `flush=True`. Pehla shabd 0.9s vs 5.3s
- [x] error handling — `ClientError` (429/404) vs `ServerError` (503), retry loop + `break` on success
- [x] token counting — `count_tokens()` pehle, `usage_metadata` baad mein. System instruction har call mein dobara ginta hai
- [ ] thinking dekhna (`include_thoughts=True`) — model chahiye jo support kare

### 1.5 SQL — Phase 2 se pehle khatam karo
pgvector Postgres par chalta hai, aur Supabase bhi. Bina SQL ke vector DB adhoora rahega.

- [x] `SELECT`, `FROM`, `WHERE`
- [x] `GROUP BY` + `AVG` / `COUNT` / `SUM`
- [x] `ORDER BY`, `LIMIT` — `sql01.py`
- [x] `JOIN` — inner aur left — `sql01.py`
- [x] Python se connect — `sqlite3` + `pd.read_sql`
- [ ] Supabase se connect (Phase 2 ke saath)

### 2. Embeddings + Vector DB
- [x] embedding kya hai — text se numbers (`embed_content`, 3072 values, norm 1.0)
- [x] similarity search — `np.dot` (vectors normalized hain to dot hi cosine hai) + `argmax` — `embed01.py`
- [ ] Chroma ya pgvector (Supabase pehle se aata hai)
- [ ] store, query, metadata filter

### 3. RAG — scratch se, bina framework
- [ ] chunking — size, overlap, kahan todna
- [ ] indexing pipeline
- [ ] retrieval + re-ranking
- [ ] grounded generation, citations
- [ ] hallucination kab hoti hai aur kyun

> **No LangChain, no LlamaIndex** jab tak raw pipeline khud na ban jaye. Framework baad mein, samajhne ke baad.

### 4. Deployment
- [ ] FastAPI — endpoints, request/response models
- [ ] Docker — Dockerfile, image, container
- [ ] live hosting (Render / Railway / Fly)
- [ ] environment variables, secrets

### 5. Evaluation & Observability
- [ ] Langfuse ya Logfire
- [ ] tracing — har step ka record
- [ ] retrieval accuracy naapna
- [ ] latency aur cost tracking

### 6. n8n automation
- [ ] workflows, triggers
- [ ] apne API ko n8n se jodna

### 7. PyTorch — sabse aakhir, kam priority
- [ ] tensors, `nn.Module`, training loop
- [ ] sirf itna ki job description padh ke samajh aaye

---

## Abhi skip

Deep ML theory · scratch se model training · Kaggle · LeetCode · certifications · OOP/classes · recursion/algorithms

---

## Projects

2-3, har ek **kisi asli problem ki shakl ka** — generic demo nahi.

- [ ] **Project 1** — kisi jaan-pehchan wale ki asli problem solve kare
- [ ] **Project 2**
- [ ] **Project 3**

Har project: **live deployed + README + demo video.**

---

## Toolkit ab tak

**Python:** variables · loops · if/else · functions · file read/write · try/except · comprehension · `for/else`

**NumPy:** array · vectorization · boolean filter · `sum` `mean` `max` `min` `std` `argmax` · `shape` `size` `reshape` · 2D indexing · slicing · `axis=0/1` · broadcasting · `np.dot`

**Stats:** `median` · z-score outliers · `corrcoef` · normalization · mode · probability

**Pandas:** `DataFrame` · `read_csv` `to_csv` · `loc` · filter · `groupby` · `sort_values` · `isnull` `dropna` `fillna` · `merge` · `astype('Int64')`

**LLM API (Gemini):** `generate_content` · `system_instruction` · `response_schema` + enum · `generate_content_stream` · `ClientError` / `ServerError` + retry · `count_tokens` · `usage_metadata`

**Aur:** git/GitHub · SQL (`SELECT` `WHERE` `GROUP BY` `ORDER BY` `LIMIT` `JOIN`) · sqlite3

---

## Kaam ka tareeka

- Roz thoda, lagataar. Naya concept ek session mein ek.
- Har teesre din revision — purana exercise khaali file se.
- **3-din wala test:** teen din baad bina dekhe likh paye? Haan matlab aa gaya.
