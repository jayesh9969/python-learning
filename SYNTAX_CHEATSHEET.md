# Python & AI Engineering — Syntax Cheat Sheet

Actionable, ready-to-use syntax blocks for quick lookup.

---

## 1. Python Core Patterns

### File Read & Write
```python
# Safe read lines
with open("data.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

# Write / append
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("naya record\n")
```

### List & Dict Comprehension
```python
# Filter and transform list
evens_squared = [x**2 for x in numbers if x % 2 == 0]

# Dict comprehension
price_lookup = {item["name"]: item["price"] for item in catalog}

# Safe string join (join string par lagta hai, list par nahi)
joined_text = "\n".join(["line 1", "line 2"])
```

### Robust Error Handling (`try-except-else-finally`)
```python
try:
    value = int(user_input)
    result = 100 / value
except ValueError:
    print("Invalid number input")
except ZeroDivisionError:
    print("Division by zero nahi chalega")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print(f"Success: {result}")
finally:
    print("Cleanup done")
```

---

## 2. NumPy & Statistics

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
mat = np.array([[1, 2, 3], [4, 5, 6]])

# Shape & Reshape
shape = mat.shape          # (2, 3) -> (rows, cols)
flat = mat.reshape(3, 2)   # Total elements same hone chahiye

# Axis Operations
col_sum = mat.sum(axis=0)  # [5, 7, 9] (vertically column-wise)
row_sum = mat.sum(axis=1)  # [6, 15]   (horizontally row-wise)

# Boolean Filtering (vectorized)
filtered = arr[arr > 25]   # array([30, 40, 50])

# Basic Stats
mean_val = np.mean(arr)
median_val = np.median(arr)
std_val = np.std(arr)
z_scores = (arr - mean_val) / std_val

# Dot Product (Kirana bill: qty x price)
qty = np.array([2, 5, 1])
price = np.array([30, 10, 50])
bill_total = np.dot(qty, price)   # 2*30 + 5*10 + 1*50 = 160

# Max index (Argmax)
best_idx = np.argmax(arr)  # Position of max value (int)
```

---

## 3. Pandas DataFrames

```python
import pandas as pd

# CSV read & write
df = pd.read_csv("students.csv")
df.to_csv("clean_students.csv", index=False)

# Quick inspect
df.head(5)
df.info()
df.describe()

# Column access & Boolean Filtering
df["marks"]
top_students = df[df["marks"] > 80]
mumbai_toppers = df[(df["city"] == "Mumbai") & (df["marks"] >= 75)]

# loc (row index, column name)
cell_value = df.loc[0, "naam"]

# GroupBy Aggregation (city-wise average marks)
avg_marks = df.groupby("city")["marks"].mean().reset_index()

# Sorting
sorted_df = df.sort_values(by="marks", ascending=False)

# Handling Missing Values (NaN)
missing_counts = df.isnull().sum()
clean_df = df.dropna()                            # Drop rows with any NaN
df["marks"] = df["marks"].fillna(df["marks"].median())
df["city"] = df["city"].fillna("Unknown")

# Type Casting with Null Support
df["age"] = df["age"].astype("Int64")            # Capital 'I' handles NaN safely

# Merge (SQL JOIN equivalent)
merged = pd.merge(df1, df2, on="student_id", how="left")
```

---

## 4. SQL via SQLite & Pandas

```python
import sqlite3
import pandas as pd

con = sqlite3.connect("school.db")

# 1. Basic SELECT & WHERE
q1 = "SELECT naam, marks FROM students WHERE city = 'Mumbai'"
df_mumbai = pd.read_sql(q1, con)

# 2. GROUP BY & Aggregates
q2 = "SELECT city, AVG(marks) as avg_marks, COUNT(*) as total FROM students GROUP BY city"
df_grouped = pd.read_sql(q2, con)

# 3. ORDER BY & LIMIT
q3 = "SELECT naam, marks FROM students ORDER BY marks DESC LIMIT 3"
df_top3 = pd.read_sql(q3, con)

# 4. LEFT JOIN
q4 = """
SELECT s.naam, s.city, a.days_present
FROM students s
LEFT JOIN attendance a ON s.naam = a.naam
"""
df_join = pd.read_sql(q4, con)

con.close()
```

---

## 5. Google GenAI LLM API (`google-genai`)

### Basic Call & System Instruction
```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents="Explain APIs in 1 line.",
    config=types.GenerateContentConfig(
        system_instruction="You are a helpful Hinglish mentor. Give plain 1 line answers."
    )
)
print(response.text.strip())
```

### Structured Output with Pydantic Schema & Enum
```python
from enum import Enum
from pydantic import BaseModel
from google import genai
from google.genai import types

class Sentiment(str, Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"

class ReviewAnalysis(BaseModel):
    sentiment: Sentiment
    confidence: float
    summary: str

client = genai.Client()

response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents="Khana bohot tasty tha par delivery thodi late thi.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=ReviewAnalysis
    )
)
print(response.text)
```

### Streaming Response
```python
from google import genai

client = genai.Client()
response_stream = client.models.generate_content_stream(
    model="gemini-flash-lite-latest",
    contents="Write a 3-step guide to make chai."
)

for chunk in response_stream:
    print(chunk.text, end="", flush=True)
print()
```

### Error Handling & Retry with Exponential Backoff
```python
import time
from google import genai
from google.genai.errors import ClientError, ServerError

client = genai.Client()

def call_with_retry(prompt: str, max_retries: int = 3) -> str:
    delay = 1.0
    for attempt in range(max_retries):
        try:
            res = client.models.generate_content(
                model="gemini-flash-lite-latest",
                contents=prompt
            )
            return res.text
        except ClientError as e:
            # 4xx error (quota/bad request) — do not retry blindly
            print(f"ClientError: {e}")
            raise
        except ServerError as e:
            # 5xx error (service overloaded) — wait and retry
            print(f"ServerError attempt {attempt + 1}: {e}. Retrying in {delay}s...")
            time.sleep(delay)
            delay *= 2.0
    raise RuntimeError("Max retries exceeded")
```

### Token Counting
```python
from google import genai

client = genai.Client()

# Estimate tokens before call
est = client.models.count_tokens(
    model="gemini-flash-lite-latest",
    contents="Kitne tokens kharch honge is sawal mein?"
)
print("Estimated input tokens:", est.total_tokens)

# Actual tokens after call
res = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents="Kitne tokens kharch honge is sawal mein?"
)
print("Actual tokens used:", res.usage_metadata.total_token_count)
```

---

## 6. Embeddings & Semantic Search

```python
import numpy as np
from google import genai

client = genai.Client()

items = ["Masala Dosa", "Paneer Tikka", "Gulab Jamun", "Cold Coffee"]
query = "kuch meetha khana hai"

# 1. Embed documents
doc_res = client.models.embed_content(
    model="gemini-embedding-001",
    contents=items
)
doc_vectors = [np.array(e.values) for e in doc_res.embeddings]

# 2. Embed query
query_res = client.models.embed_content(
    model="gemini-embedding-001",
    contents=query
)
query_vector = np.array(query_res.embeddings[0].values)

# 3. Cosine similarity via dot product (Gemini vectors are normalized, norm=1.0)
scores = [np.dot(query_vector, doc_vec) for doc_vec in doc_vectors]
best_idx = int(np.argmax(scores))

print("Best Match:", items[best_idx], "| Similarity Score:", scores[best_idx])
```

---

## 7. ChromaDB (Vector Database)

```python
import chromadb
from google import genai

# Disk persistent client
client = chromadb.PersistentClient(path="chroma_data")
collection = client.get_or_create_collection(name="store_items")

genai_client = genai.Client()
docs = ["Paneer Chilli", "Cold Coffee", "Veg Biryani", "Gulab Jamun"]
metadatas = [
    {"type": "food", "spicy": True, "price": 180},
    {"type": "beverage", "spicy": False, "price": 80},
    {"type": "food", "spicy": True, "price": 220},
    {"type": "dessert", "spicy": False, "price": 50}
]
ids = [f"id_{i}" for i in range(len(docs))]

# Add only if collection is empty (saves API calls)
if collection.count() == 0:
    emb_res = genai_client.models.embed_content(
        model="gemini-embedding-001",
        contents=docs
    )
    vectors = [e.values for e in emb_res.embeddings]
    collection.add(ids=ids, documents=docs, embeddings=vectors, metadatas=metadatas)

# Query with Vector + Metadata Filter ($lt, $eq)
q_emb = genai_client.models.embed_content(
    model="gemini-embedding-001",
    contents="budget spicy food"
).embeddings[0].values

results = collection.query(
    query_embeddings=[q_emb],
    n_results=2,
    where={"$and": [{"spicy": {"$eq": True}}, {"price": {"$lt": 200}}]}
)

# Chroma returns distances: CHHOTA = BETTER
print("Matched Docs:", results["documents"][0])
print("Distances:", results["distances"][0])
```

---

## 8. RAG (Retrieval Augmented Generation)

### Fixed Size Chunking with Overlap
```python
text = "Hamari dukaan subah 9 baje khulti hai... Delivery Mumbai mein free hai..."
size = 120
overlap = 30
chunks = []

for i in range(0, len(text), size - overlap):
    chunk = text[i:i + size].strip()
    if len(chunk) > 40:    # Chhote kachra tukde filter out
        chunks.append(chunk)
```

### Complete RAG Query Pipeline with Citations & Grounding
```python
from google import genai
import chromadb

genai_client = genai.Client()
chroma_client = chromadb.PersistentClient(path="chroma_rules")
collection = chroma_client.get_collection(name="rules")

def answer_query(user_query: str) -> str:
    # 1. Embed query
    q_emb = genai_client.models.embed_content(
        model="gemini-embedding-001",
        contents=user_query
    ).embeddings[0].values

    # 2. Retrieve top matches
    res = collection.query(query_embeddings=[q_emb], n_results=3)
    best_distance = res["distances"][0][0]
    matched_docs = res["documents"][0]

    # 3. Distance threshold guard
    if best_distance > 0.8:
        return "Ye sawal hamare rules/documents se bahar hai."

    # 4. Format citations [1], [2]
    context_lines = [f"[{i}] {doc}" for i, doc in enumerate(matched_docs, 1)]
    formatted_context = "\n".join(context_lines)

    # 5. Grounded prompt with citations
    prompt = f"""RULES:
{formatted_context}

QUESTION:
{user_query}

INSTRUCTION:
Answer strictly using the RULES above. Mention citations like [1], [2] next to facts.
If the information is not present, reply 'Pata nahi'."""

    ai_response = genai_client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=prompt
    )
    return ai_response.text.strip()
```

### 2-Tier LLM Re-Ranking
```python
# 1. Chroma se 8 chunks nikaalo
res = collection.query(query_embeddings=[q_emb], n_results=8)
docs = res["documents"][0]
docs_formatted = "\n".join([f"{i}. {doc}" for i, doc in enumerate(docs, 1)])

# 2. Manager call: Gemini se pucho kaunse 2-3 chunks mein answer hai
rank_prompt = f"""QUESTION: {user_query}
DOCUMENTS:
{docs_formatted}

Return only comma separated numbers of 2-3 documents that directly answer the question (e.g. 1,4):"""

selected_indices_text = genai_client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents=rank_prompt
).text.strip()

# Convert "1, 4" string to python 0-indexed list
selected_nums = [int(n.strip()) - 1 for n in selected_indices_text.split(",") if n.strip().isdigit()]
selected_docs = [docs[i] for i in selected_nums if i < len(docs)]
```

---

## 9. FastAPI & Pydantic Backend

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI(title="AI RAG Backend")

# Request & Response Schemas
class QueryRequest(BaseModel):
    query: str = Field(..., min_length=2, example="Lunch timing kya hai?")

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]

@app.get("/")
def health_check():
    return {"status": "healthy", "service": "rag-api"}

@app.post("/ask", response_model=QueryResponse)
def ask_question(body: QueryRequest):
    if not body.query:
        raise HTTPException(status_code=400, detail="Query empty nahi ho sakti")
    
    # Asli RAG execution
    return QueryResponse(
        answer="Lunch timing 2:30pm to 3:00pm hai [1]",
        sources=["Rule #5: lunch time starts from 2:30pm to 3pm."]
    )

# Run with: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 10. AI Agents & Tool Calling

### SDK Tool Definition with Validation & Types
```python
from typing import Literal
from google import genai
from google.genai import types

def transfer_money(recipient: str, amount: int, mode: Literal["UPI", "NEFT"]) -> str:
    """Transfers money to a recipient after checking safety limits.
    
    Args:
        recipient: Name or UPI ID of the person.
        amount: Positive amount in INR.
        mode: Transfer method ('UPI' or 'NEFT').
    """
    # Tool validation
    if amount <= 0:
        return "Error: Amount must be greater than zero."
    if amount > 50000:
        return "Error: Limit exceeded. Max transfer is 50000."
    return f"Success: Rs {amount} transferred to {recipient} via {mode}."

client = genai.Client()

# Multi-turn chat with automatic tool execution
chat = client.chats.create(
    model="gemini-flash-lite-latest",
    config=types.GenerateContentConfig(
        tools=[transfer_money]
    )
)

response = chat.send_message("Raju ko UPI se 1200 rupaye bhej do")
print(response.text)
```

### Human-in-the-Loop (HITL) inside Tool
```python
def cancel_subscription(user_id: str, plan_name: str) -> str:
    """Cancels a paid subscription with human confirmation."""
    confirm = input(f"Kya aap sach me user {user_id} ka {plan_name} plan cancel karna chahte hain? (yes/no): ")
    if confirm.strip().lower() == "yes":
        return f"Success: {plan_name} for user {user_id} cancelled."
    return "Action aborted by human user."
```

### Max Steps Guard (ReAct Loop)
```python
max_steps = 5
step_count = 0

while True:
    step_count += 1
    if step_count > max_steps:
        print("Safety Stop: Max steps reached to prevent infinite loop.")
        break
    # Run Agent step...
```

### Smart Router (Deterministic Code vs LLM)
```python
def smart_router(query: str):
    # Rule-based fast track (0ms, $0 cost)
    if "order status" in query.lower() or "track" in query.lower():
        return "Order #9988 is out for delivery. (Instant deterministic route)"
    # LLM Agent route for complex/unstructured queries
    return client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=query
    ).text
```

---

## 11. LangGraph Workflows

### Linear Flow (`StateGraph` + `TypedDict`)
```python
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class OrderState(TypedDict):
    order_id: int
    status: str
    rider: str

def cook_food(state: OrderState) -> dict:
    return {"status": "Food is ready"}

def assign_rider(state: OrderState) -> dict:
    return {"rider": "Raju Delivery Partner", "status": "Out for delivery"}

builder = StateGraph(OrderState)
builder.add_node("cook", cook_food)
builder.add_node("delivery", assign_rider)

builder.add_edge(START, "cook")
builder.add_edge("cook", "delivery")
builder.add_edge("delivery", END)

app = builder.compile()
result = app.invoke({"order_id": 101, "status": "Placed", "rider": ""})
```

### Conditional Routing & Branching
```python
def router(state: OrderState) -> str:
    if state["order_id"] < 0:
        return "invalid"
    return "valid"

builder.add_conditional_edges(
    "start_node",
    router,
    {"valid": "process_node", "invalid": END}
)
```

### Tool Agent in LangGraph (`ToolNode` + `tools_condition`)
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition

def add_numbers(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b

tools = [add_numbers]
llm = ChatGoogleGenerativeAI(model="gemini-flash-lite-latest").bind_tools(tools)

def call_model(state: MessagesState) -> dict:
    return {"messages": [llm.invoke(state["messages"])]}

builder = StateGraph(MessagesState)
builder.add_node("agent", call_model)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge("tools", "agent")

app = builder.compile()
res = app.invoke({"messages": [("user", "15 aur 27 jod kar batao")]})
print(res["messages"][-1].content)
```

### Checkpointing Memory (`MemorySaver` + `thread_id`)
```python
from langgraph.checkpoint.memory import MemorySaver

app = builder.compile(checkpointer=MemorySaver())

config = {"configurable": {"thread_id": "session_jayesh"}}
# Turn 1
app.invoke({"messages": [("user", "Mera naam Jayesh hai.")]}, config=config)
# Turn 2: Context is remembered automatically
res = app.invoke({"messages": [("user", "Mera naam kya hai?")]}, config=config)
print(res["messages"][-1].content)
```

### Node Retry Policy (`RetryPolicy`)
```python
from langgraph.types import RetryPolicy

policy = RetryPolicy(
    max_attempts=3,
    initial_interval=0.5,
    backoff_factor=2.0,
    retry_on=ConnectionError
)

builder.add_node("payment_node", process_payment, retry=policy)
```

---

## 12. MCP (Model Context Protocol)

### MCP Server (`FastMCP`)
```python
from mcp.server.fastmcp import FastMCP

server = FastMCP("KiranaStore")

# Executable Tool
@server.tool()
def calculate_bill(item: str, quantity: int) -> dict:
    """Calculates total bill for a store item."""
    prices = {"doodh": 30, "bread": 25, "biscuit": 10}
    total = prices.get(item, 0) * quantity
    return {"item": item, "total": total}

# Read-only Resource
@server.resource("store://policy")
def get_store_policy() -> str:
    """Returns store refund policies."""
    return "Returns accepted within 24 hours only with bill."

if __name__ == "__main__":
    server.run(transport="stdio")
```

### MCP Client with Dynamic Tool Discovery
```python
import asyncio
from mcp.client.stdio import stdio_client
from mcp.client.session import ClientSession
from langchain_mcp_adapters.tools import load_mcp_tools
from mcp import StdioServerParameters

server_params = StdioServerParameters(
    command="python",
    args=["mcp_learning/kirana_server.py"]
)

async def run_mcp_client():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            # Dynamic tool discovery
            tools = await load_mcp_tools(session)
            print("Found tools:", [t.name for t in tools])
            
            # Execute tool dynamically
            result = await tools[0].ainvoke({"item": "bread", "quantity": 2})
            print("Output:", result)

if __name__ == "__main__":
    asyncio.run(run_mcp_client())
```

---

## 13. Streamlit Chat UI

```python
import streamlit as st

st.title("AI Assistant")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Prior Messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Input Box
if prompt := st.chat_input("Apna sawal yahan likhein..."):
    # Render user query
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Assistant Thinking & Output
    with st.spinner("AI soch raha hai..."):
        ai_response = "Jawab yahan aayega."
        
    with st.chat_message("assistant"):
        st.markdown(ai_response)
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
```

---

## 14. PostgreSQL & pgvector (`psycopg` + `pgvector`)

### 1. Connection & Register Vector
```python
import os
import psycopg
from pgvector.psycopg import register_vector
from dotenv import load_dotenv

load_dotenv()

conn = psycopg.connect(os.getenv("DATABASE_URL"))
register_vector(conn)  # Enables Python list <-> pgvector conversion
```

### 2. Create Table with Vector Column
```python
with conn.cursor() as cur:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS food_items (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            price NUMERIC,
            is_veg BOOLEAN,
            embedding VECTOR(3072)
        );
    """)
conn.commit()
```

### 3. Insert Data with Vector
```python
# embedding_list is a standard Python list of floats, e.g. [0.012, -0.045, ...]
with conn.cursor() as cur:
    cur.execute(
        """
        INSERT INTO food_items (name, price, is_veg, embedding)
        VALUES (%s, %s, %s, %s);
        """,
        ("Paneer Butter Masala", 180, True, embedding_list)
    )
conn.commit()
```

### 4. Vector Search with Metadata Filter (Single Query)
```python
# <=> is Cosine Distance operator in pgvector (%s::vector explicitly casts Python list to vector)
query = """
    SELECT name, price, is_veg, embedding <=> %s::vector AS distance
    FROM food_items
    WHERE is_veg = %s AND price < %s
    ORDER BY distance ASC
    LIMIT 2;
"""

with conn.cursor() as cur:
    cur.execute(query, (query_embedding, True, 200))
    results = cur.fetchall()
    for row in results:
        print(f"Name: {row[0]}, Price: {row[1]}, Distance: {row[3]:.4f}")

conn.close()
```

---

## 15. Hybrid Search & RRF (Reciprocal Rank Fusion)

### 1. BM25 Keyword Search (`rank_bm25`)
```python
from rank_bm25 import BM25Okapi

corpus = ["Paneer Butter Masala", "Butter Chicken", "Dal Tadka", "Chicken Biryani"]
tokenized_corpus = [doc.lower().split() for doc in corpus]
bm25 = BM25Okapi(tokenized_corpus)

query = "spicy chicken"
tokenized_query = query.lower().split()
scores = bm25.get_scores(tokenized_query)

# Sort documents by BM25 score descending
bm25_results = sorted(zip(corpus, scores), key=lambda x: x[1], reverse=True)
bm25_ranked_docs = [doc for doc, score in bm25_results]
```

### 2. Reciprocal Rank Fusion (RRF Algorithm)
```python
def reciprocal_rank_fusion(bm25_ranked, vector_ranked, k=60):
    """Combines two ranked lists using RRF score formula: 1 / (k + rank)"""
    rrf_scores = {}

    for rank, doc in enumerate(bm25_ranked):
        rrf_scores[doc] = rrf_scores.get(doc, 0.0) + (1.0 / (k + rank + 1))

    for rank, doc in enumerate(vector_ranked):
        rrf_scores[doc] = rrf_scores.get(doc, 0.0) + (1.0 / (k + rank + 1))

    # Higher RRF score = Better overall rank
    return sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)
```

---

## 16. Testing & Structured Logging (`pytest`, `unittest.mock`, `logging`)

### 1. Structured Logging Setup
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s (line %(lineno)d): %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("ai_agent")

logger.info("Order placed successfully")
logger.warning("High latency detected on database")
logger.error("Payment failed")
```

### 2. Pytest Basics & Assertions
```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

### 3. Pytest Fixture (Isolated Test Data)
```python
import pytest

@pytest.fixture
def sample_user():
    return {"user_id": 101, "name": "Jayesh", "balance": 500}

def test_user_balance(sample_user):
    assert sample_user["balance"] == 500
```

### 4. Mocking LLM API Responses (`unittest.mock.MagicMock`)
```python
from unittest.mock import MagicMock

def call_ai(client, prompt: str) -> str:
    response = client.models.generate_content(model="gemini", contents=prompt)
    return response.text

def test_call_ai_with_mock():
    # Fake client without internet or token cost
    mock_client = MagicMock()
    mock_client.models.generate_content.return_value.text = "Fake AI Jawab"

    result = call_ai(mock_client, "Hello")
    assert result == "Fake AI Jawab"
    mock_client.models.generate_content.assert_called_once()
```

### 5. Mocking Exceptions / Failures (`side_effect`)
```python
def test_ai_failure_handling():
    mock_client = MagicMock()
    # Simulates instant server down error
    mock_client.models.generate_content.side_effect = ConnectionError("503 Service Unavailable")

    # Test error handling logic
    try:
        call_ai(mock_client, "Hello")
    except ConnectionError:
        pass  # Gracefully handled
```

