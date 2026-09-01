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
- [x] Chroma — `PersistentClient(path=...)` disk par save, `get_or_create_collection` — `chroma01.py` (Gemini embeddings), `chroma02.py` (Chroma ke apne)
- [x] store, query, metadata filter — `metadatas=[{...}]` + `where={...}`. `n_results` upar ki hadd hai, guarantee nahi
- [x] `add` vs `upsert` vs `update` — `update()` nayi id par chup-chaap kuch nahi karta, error bhi nahi
- [x] `count()` se pehli-baar wala kaam skip — Gemini ki call bachti hai
- [x] distance ulta hai — `np.dot` mein bada achha, Chroma distance mein chhota achha
- [ ] pgvector / Supabase (SQL ke saath)

### 3. RAG — scratch se, bina framework
- [x] poora RAG loop — retrieve -> prompt -> generate. `rag01.py` (menu + budget), `rag02.py` (college rules)
- [x] chunking — khali line par (`split`) ya fixed size + overlap, har tukda alag embed + alag id
- [x] indexing pipeline — chunk -> embed -> Chroma, `count()` ke guard ke saath
- [x] threshold — sabse kam distance hadd se zyada ho to Gemini call hi mat karo
- [x] grounded generation — "sirf diye gaye data se jawab do", aur "calculation is allowed" ka santulan
- [x] hallucination kab hoti hai aur kyun — instruction guzarish hai, pabandi nahi
- [x] prompt ki shakl — data + sawal ek jagah, saaf label ke saath. Baant do to model confuse
- [x] chunk size aur overlap — `range(0, len(text), size-overlap)`, chhote tukde `len()` se chhaan do — `chunk01.py`
- [x] citations — `enumerate(rules, 1)` se `[1] [2]`, aur prompt mein saaf maango
- [x] re-ranking — Chroma se 8 nikaalo, Gemini se 2-3 chunwao, phir jawab — `rag03.py`
- [ ] **hybrid search (BM25 + embedding)** — embedding matlab dhoondhta hai, BM25 hu-ba-hu shabd. Product code, order number, naam, version — ye embedding se phisal jaate hain (`SKU-4471` vs `SKU-4472` uske liye ek jaise). Dono chalao, score jodo. 2 session.

> Raw pipeline ban gaya. Ab framework seekh sakte ho — par baad mein, deployment ke baad.

### 4. Deployment
- [x] FastAPI — endpoints (`@app.get` / `@app.post`), `uvicorn main:app --reload`, `/docs` khud banta hai — `main.py`
- [x] request/response models — Pydantic `BaseModel`, `response_model=`, class = design / object = bhara hua form
- [x] Docker — `Dockerfile`, `requirements.txt`, `.dockerignore`, `docker build -t` / `docker run -p`. `--host 0.0.0.0` zaroori, warna dabbe se baat nahi hoti
- [x] environment variables, secrets — key Dockerfile mein KABHI nahi (image share hoti hai, parat mein padi rehti hai). `.env` + `--env-file`, aur `.env` dono ignore files mein
- [ ] live hosting (Render / Railway / Fly)
- [ ] container ka data mit jaata hai — volume ya hosted vector DB (Supabase/pgvector)

### 4.5 Project 1 — LIVE karo, yahin, isi jagah par
Deployment ke turant baad. Aur seekhte mat raho — jo aata hai usse ek asli cheez banao.
Client ko skills ki list nahi chahiye, link chahiye.
- [ ] kisi jaan-pehchan wale ki asli problem
- [ ] live URL + README + demo video
- [ ] har nayi skill isi project par lagao — hybrid search isme, eval isi par, agent isi mein

### 4.6 Agents + tool calling — ye sabse bada gap hai
Har job list mein teen shabd saath aate hain: **RAG, agents, evaluation.** RAG ho gaya, evaluation aa raha hai, agents bilkul nahi.
Agent = model sirf jawab nahi deta, **kaam karta hai** — tools chalata hai aur khud tay karta hai kaunsa.
Upwork par clients seedha yahi maangte hain: "AI agents that automate workflows".
- [ ] tool calling — function ko model ke haath mein dena
- [ ] agent loop — soche, tool chalaye, natija dekhe, phir soche
- [ ] kab agent chahiye aur kab sirf RAG kaafi hai

### 4.7 MCP (Model Context Protocol) — agents ke BAAD, chhota
Apne tools ko kisi bhi AI se jodne ka standard tareeka. Anthropic ne banaya, ab OpenAI/Google/Microsoft sab use karte hain, Dec 2025 se Linux Foundation ke paas hai.
- [ ] MCP server banana aur expose karna. 2-3 session. Pehle agents, warna sirf syntax ratoge.

### 4.8 LangChain / LlamaIndex — chhota item, poora phase nahi
Jo khud banaya uske naam seekhne hain: TextSplitter = chunking, VectorStore = Chroma, Retriever = query, PromptTemplate = f-string, Chain = sab jodna.
- [ ] 2-3 session, sirf naam aur syntax. Portfolio mein scratch wala code hi rakhna.

### 5. Evaluation & Observability
> Har senior job description ismein experience maangti hai. Junior aur senior ka farak yahi hai.

- [ ] **pehle haath se eval** — 20 sawal + unke sahi jawab likho, `rag03.py` chalao, gino kitne sahi aaye. Ek din ka kaam, aur isi se pata chalega ki naapna kya hai
- [ ] **RAGAS** — score nikaalta hai. Chunk 200 achha ya 500, dono chalao aur tulna karo. Prayog ke liye
- [ ] **DeepEval** — pytest jaisa, pass/fail. Quality gire to build rok deta hai
- [ ] Langfuse ya Logfire — live app par nazar
- [ ] tracing — har step ka record
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

**Job listing mein dikhte hain par mere raaste ke nahi:** AI video generation (Upwork par sabse tez, +329% — par bilkul alag field) · data annotation/labeling (demand hai par sasta, dohrane wala kaam) · fine-tuning (eval pehle; 95% kaam RAG + prompt se ho jaata hai)

**Alag phase nahi, aadat hai:** cost control (`count()`, token counting — pehle se kar raha hoon) · prompt injection se bachav (Project 1 public hoga, deployment ke saath ek session)

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

**Vector DB (Chroma):** `PersistentClient` · `get_or_create_collection` · `add` / `upsert` / `update` · `count` · `query` (`query_texts` / `query_embeddings`) · `distances` · `metadatas` + `where` · `delete_collection`

**RAG:** chunking (`split`, fixed size + overlap) · `join()` · `enumerate()` · retrieve -> prompt -> generate · distance threshold · grounding instruction · citations · re-ranking (2-parat)

**Deployment:** FastAPI (`@app.get`/`@app.post`, Pydantic models, `/docs`) · `uvicorn` · Docker (`Dockerfile`, `build`, `run -p`, `.dockerignore`) · `.env` + `--env-file`

**Aur:** git/GitHub · SQL (`SELECT` `WHERE` `GROUP BY` `ORDER BY` `LIMIT` `JOIN`) · sqlite3

---

## Kaam ka tareeka

- Roz thoda, lagataar. Naya concept ek session mein ek.
- Har teesre din revision — purana exercise khaali file se.
- **3-din wala test:** teen din baad bina dekhe likh paye? Haan matlab aa gaya.
