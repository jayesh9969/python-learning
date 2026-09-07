
from fastapi.responses import HTMLResponse
from google import genai
import chromadb
import json
from fastapi import FastAPI
from fastapi.responses import Response
from fastapi import Form
from twilio.twiml.messaging_response import MessagingResponse




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

    context_text = "\n\n".join(res["documents"][0]) if res.get("documents") else "no context found."

    prompt = f"""i have given you a list of documents: {context_text} give answer according to: {Body} if information is not available in the list say 'info not available' do not add additional information."""
    response = c.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=prompt
    )
    model_answer = response.text if response.text else "sorry, i couldn't generate an answer"
    resp = MessagingResponse()
    resp.message(model_answer)
    return Response(content=str(resp), media_type="application/xml")



    

    
