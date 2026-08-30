import chromadb
from google import genai
from google.genai import types

college_rules = """entry in college starts from 11am.\n\nstudents can leave the college at 5pm.\n\nragging is strictly not allowed and punishable by law.\n\nif student have attendance below 75% that student is not eligible to sit in exams"""
chunks = college_rules.split("\n\n")


  

query = "when college starts and ends?"
c = genai.Client()

all_vectors = []
client = chromadb.PersistentClient(path="chroma_rules")

collection = client.get_or_create_collection(name="college_rules")

if collection.count() == 0:
    r = c.models.embed_content(model="gemini-embedding-001", contents=chunks)
    for e in r.embeddings:
        all_vectors.append(e.values)

    id = [str(i) for i in range(len(chunks))]

    collection.add(ids=id, documents=chunks, embeddings=all_vectors)
    print("menu embed ho gaya")

else:
    print("already saved, skip")

q = c.models.embed_content(model="gemini-embedding-001", contents=query)

vectorq = q.embeddings[0].values

res = collection.query(query_embeddings=[vectorq], n_results=4)

print(res["documents"],res["distances"])

rules = res["documents"][0]
# rules_text = "\n".join(rules)
rules_text = ""


for n, l in enumerate(rules, 1):
    rules_text = rules_text + f"[{n}] {l}\n"

    

if res["distances"][0][0] > 0.8:
    print("rules me iska jawab nahi hai")

else:
    prompt =f"""rules are given below: {rules_text}  question: {query} calculation is allowed, if information is not available in the rules say 'this info is not available yet', with every answer the number of rule should show like this [1] [2]"""
    response = c.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=prompt,

       

    )

    print(response.text.strip())



