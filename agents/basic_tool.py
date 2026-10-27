from google import genai
from google.genai import types

result = ""

def get_cricket_scores(team : str) -> str:
    
    """this function return cricket score"""
    return 100/2


c = genai.Client()

response = c.models.generate_content(
    model="gemini-flash-lite-latest",
    contents="india ka cricket score kya hai?",
    config=types.GenerateContentConfig(
        tools=[get_cricket_scores],
       
    )
    
)


print(response.text)




