import chromadb



fruits_dishes = [
    "pineapple juice - sweet and aromatic",
    "ice cream - cold and tasty available with diffrent flavours",
    "pasta - cheesy and buttery texture",
    "energy drink - for instant energy but also sweet",
    "samosa - spicy and fried"
    
    
    

]




query = "need something sweet"

client = chromadb.PersistentClient(path="chroma_test")


collection = client.get_or_create_collection(name="fruits_dishes")

id= [str(i) for i in range(len(fruits_dishes))]
meta = [{"cold" : True}, {"cold" : True}, {"cold" : False}, {"cold" : True}, {"cold" : False}]



        
collection.upsert(ids=id, documents=fruits_dishes, metadatas= meta)
    


res = collection.query(query_texts=[query], n_results=5, where={"cold" : True})


docs = res['documents'][0]
dist = res["distances"][0]


for m in range(len(docs)):
    print(f"{docs[m]} {dist[m] :.3f}")

# client.delete_collection(name="fruits_dishes")