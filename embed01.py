from google import genai
from google.genai import types
import numpy as np

menu = [
    "Chicken Chettinad - fiery South Indian curry",
    "Gulab Jamun - sweet dessert",
    "Dal Makhani - creamy mild lentils",
    "Andhra Chilli Fry - very hot",
]
query = "kuch teekha khana hai"

client = genai.Client()
scores = []

contents = [types.Content(parts=[types.Part.from_text(text=m)])for m in menu]
       
r = client.models.embed_content(model="gemini-embedding-2", contents=contents)

        
q = client.models.embed_content(model="gemini-embedding-2", contents=query)
vectorq = q.embeddings[0].values

for m in range(len(menu)):    
    vector = r.embeddings[m].values     
    score = np.dot(vectorq, vector)
            
    print(f"{score} {menu[m]}")
    scores.append(score)
position = np.argmax(scores)
    
print(menu[position])
    

    
    

    



    

