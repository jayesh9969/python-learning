

from google import genai
import chromadb
import json















with open("whatsapp_guide.json", "r", encoding="utf-8") as f:
    whasapp_ins = json.load(f)
    
    all_ids = list(whasapp_ins.keys())
    # print(all_ids)

    
    all_docs = []
    for steps in whasapp_ins.values():
        one_part = "\n\n".join(steps)
        all_docs.append(one_part)




all_vectors = []




c = genai.Client()

client = chromadb.PersistentClient(path="chroma_whatsapp", settings=chromadb.Settings(allow_reset=True))

collection = client.get_or_create_collection(name="whatsapp_parts")
if collection.count() == 0:
    r = c.models.embed_content(model="gemini-embedding-001", contents=all_docs)
    for e in r.embeddings:
        all_vectors.append(e.values)
    collection.add(ids=all_ids, documents=all_docs, embeddings=all_vectors)
    print("menu embeded")
else:
    print("already emdeded, skip")

def ask_whatsapp_rag(user_query : str) ->str:
    q = c.models.embed_content(model="gemini-embedding-001", contents=user_query)
    vectorq = q.embeddings[0].values

    res = collection.query(query_embeddings=[vectorq], n_results= 10)

    context_text = res["documents"][0]

    prompt = f"""i have given you a list: {context_text} give answer according to: {user_query} if information is not available in the list say 'info not available' do not add additional information. convret these steps into marathi text"""
    response = c.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=prompt
    )
    return response.text



    




    

    
