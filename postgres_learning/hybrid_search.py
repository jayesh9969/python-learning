



import numpy as np
from os import getenv
from google import genai
from rank_bm25 import BM25Okapi


catalog = [
    "iPhone 15 Pro Max 256GB",
    "iPhone 15 128GB",
    "Samsung Galaxy S24 Ultra",
    "Apple Smartphone Repair and Service Manual",
]


tokenized_catalog = [doc.lower().split() for doc in catalog]
bm25 = BM25Okapi(tokenized_catalog)

query = "iPhone 15 repair"

tokenized_query = query.lower().split()

scores = bm25.get_scores(tokenized_query)

bm25_results = sorted(zip(catalog, scores),
key=lambda x: x[1], reverse=True)


bm25_ranked_docs = [doc for doc, score in bm25_results]

print(bm25_ranked_docs)

client = genai.Client(api_key=getenv("GEMINI_API_KEY"))
res = client.models.embed_content(model="gemini-embedding-001", contents=query)

query_emb = res.embeddings[0].values

res2 = client.models.embed_content(model="gemini-embedding-001", contents=catalog)
item_emb = res2.embeddings[0].values

np.dot(query_emb, item_emb)

vector_scores = [np.dot(query_emb, e.values) for e in res2.embeddings]

vector_res = sorted(zip(catalog, vector_scores), key=lambda x: x[1], reverse=True)

vector_ranked_docs = [doc for doc, score in vector_res]

print("vector ranks:", vector_ranked_docs)

def reciprocal_rank_fusion(bm25_ranked_docs, vector_ranked_docs, k=60):
    """Combines two ranked lists using RRF score formula: 1 / (k + rank)"""

    rrf_scores = {}

    for rank, doc in enumerate(bm25_ranked_docs):
        rrf_scores[doc] = rrf_scores.get(doc, 0.0) + (1.0 / (k + rank + 1))  


    for rank, doc in enumerate(vector_ranked_docs):
        rrf_scores[doc] = rrf_scores.get(doc, 0.0) + (1.0 / (k + rank + 1))

    return sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)


print(reciprocal_rank_fusion(bm25_ranked_docs, vector_ranked_docs))