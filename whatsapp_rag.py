import os
import twilio
from twilio.rest import Client
from google import genai
import chromadb
import json
from fastapi import FastAPI
from fastapi import Form
from twilio.twiml.messaging_response import MessagingResponse
from fastapi.responses import Response






app = FastAPI()
with open("whatsapp_guide.json", "r", encoding="utf-8") as f:
    whasapp_ins = json.load(f)
    
    all_ids = list(whasapp_ins.keys())
    # print(all_ids)

    
    all_docs = []
    for steps in whasapp_ins.values():
        one_part = "\n".join(steps)
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

@app.post("/whatsapp")
def question(Body : str = Form(...)):
    q = c.models.embed_content(model="gemini-embedding-001", contents=Body)
    vectorq = q.embeddings[0].values

    res = collection.query(query_embeddings=[vectorq], n_results= 10)

    prompt = f"""i have given you a list {res["documents"]} give answer according to {Body} if information is not available in the list say 'info not available' do not add additional information. give 4 steps if {Body} is short"""
    response = c.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=prompt
    )
    resp = MessagingResponse()
    resp.message(response.text.strip())
    return Response(content=str(resp), media_type="application/xml") 

    























    

 




    
    





