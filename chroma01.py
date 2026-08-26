from google import genai
from google.genai import types
import chromadb as chr


menu = [
    "Chicken Chettinad - fiery South Indian curry",
    "Gulab Jamun - sweet dessert",
    "Dal Makhani - creamy mild lentils",
    "Andhra Chilli Fry - very hot",
]
query = "kuch meetha khana hai"


c = genai.Client()
all_vectors = []



client = chr.PersistentClient(path="chroma_data")



collection = client.get_or_create_collection(name="menu")
if collection.count() == 0: 
    r = c.models.embed_content(model="gemini-embedding-001", contents=menu)
    for e in r.embeddings:
        all_vectors.append(e.values)
    id = [str(i) for i in range(len(menu))]
    collection.add(ids=id, documents=menu, embeddings=all_vectors)
    print("menu embed ho gaya")
else:
    print("pahle se saved hai, skip")
q = c.models.embed_content(model="gemini-embedding-001", contents=query)
vectorq = q.embeddings[0].values
res = collection.query(query_embeddings=[vectorq], n_results=1)


print(res["documents"][0][0])

# client.delete_collection(name="menu")