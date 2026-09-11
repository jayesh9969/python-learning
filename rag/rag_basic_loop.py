import chromadb
from google import genai
from google.genai import types


food_list = [
    "samosa - spicy and fried 30 rs",
    "coffee - hot and bitter  40 rs",
    "watermelon juice - cold and refreshing 70 rs",
    "mushroom soup - umami and comforting 120 rs"

]



query = "is mushroom soup jain?"



c = genai.Client()

all_vectors = []
client = chromadb.PersistentClient(path="chroma_food")

collection = client.get_or_create_collection(name="food_list")

if collection.count() == 0:
    r = c.models.embed_content(model="gemini-embedding-001", contents=food_list)
    for e in r.embeddings:
        all_vectors.append(e.values)

    id = [str(i) for i in range(len(food_list))]

    collection.add(ids=id, documents=food_list, embeddings=all_vectors)
    print("menu embed ho gaya")

else:
    print("pehle se saved hai, skip")

q = c.models.embed_content(model="gemini-embedding-001", contents=query)

vectorq = q.embeddings[0].values



res = collection.query(query_embeddings=[vectorq], n_results=4)

print(res["distances"], res["documents"])


if res["distances"][0][0] > 0.8:
    print("menu me iska jawab nahi hai")

# print(res["documents"])
else:
    prompt = f"""i have given you list give answer according to {query} if some information is not available in the list or data say i don't know and don't add any new additional information, you have permission to calculate"""
    response = c.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=res['documents'],
        
        config=types.GenerateContentConfig(
            system_instruction=prompt
        )

    )


    print(response.text.strip())

# client.delete_collection(name="food_list")






