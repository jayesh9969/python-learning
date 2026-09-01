from fastapi import FastAPI
from google import genai
import chromadb
from pydantic import BaseModel

app = FastAPI()


college_rules = """entry in college starts from 11am.
students can leave the college at 5pm.
ragging is strictly not allowed and punishable by law.
if student have attendance below 75% that student is not eligible to sit in exams.
lunch time starts from 2:30pm to 3pm.
all the students must be well groomed hair and nails should be trimmed.
fighting and shouting in the premises will not be tolerated.
students needs to inform their class teacher before taking leaves.
if students didn't informed about taking leaves those students needs to call their parents without them students are not eligible to sit in their classes.
students can enter classes after parents teachers discussion is solved.
cheating and copying other students answers are not allowed if get caught student will be not allowed to sit in the exams for a year.
teachers are not allowed to abuse students physically or mentally and it is punishable by law"""

chunks = college_rules.split("\n")

class Question(BaseModel):
    query : str

class Answer(BaseModel):
    answer : str
    rules_used: list[str]



all_vectors = []
c = genai.Client()

client = chromadb.PersistentClient(path="chroma_rules_api")

collection = client.get_or_create_collection(name="college_rules")

if collection.count() == 0:
    r = c.models.embed_content(model="gemini-embedding-001", contents=chunks)
    for e in r.embeddings:
        all_vectors.append(e.values)

    id = [str(i) for i in range(len(chunks))]

    collection.add(ids=id, documents=chunks, embeddings=all_vectors)
    print("menu embeded")

else:
    print("already saved, skip")

@app.post("/poocho", response_model=Answer)
def question(body : Question):

    q = c.models.embed_content(model="gemini-embedding-001", contents=body.query)
    vectorq = q.embeddings[0].values

    res = collection.query(query_embeddings=[vectorq], n_results=8)

    rules = res["documents"][0]
    numbered_txt = ""

    for n, l in enumerate(rules, 1):
        numbered_txt = numbered_txt + f"{n} {l}\n"

    if res["distances"][0][0] > 0.8:
        return Answer(answer="it is not written in rules", rules_used=[])

    else:
        prompt = f"""chunks are given below: {numbered_txt} question: {body.query} in given chunks select 3 numbers which really give answer to the question. give only numbers, separated with comma 3,7,1 like this. do not write anythinng else"""
        response = c.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=prompt
        )

        nums = [int(v) for v in response.text.strip().split(",")]

        num_list = []

        for n in nums:
            s = rules[n - 1]
            num_list.append(s)

        num_text = ""
        for n, l in enumerate(num_list, 1):
            num_text = num_text + f"{n} {l}\n"


        n_prompt = f"""chunks are given below: {num_text} question: {body.query} give answer with citation [1] [2] . if the information is not available in the chunks say 'this info is not available yet'"""
        n_response = c.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=n_prompt
        )


            
            
        return Answer(answer=n_response.text.strip(), rules_used=num_list)        