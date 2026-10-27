from typing import Literal
from google import genai
from google.genai import types


result = ""

def get_cricket_scores(team : str) -> str:
    
    """this function return cricket score"""
    return 100/2


c = genai.Client()

chat = c.chats.create(
    model="gemini-flash-lite-latest",
    config=types.GenerateContentConfig(
        tools=[get_cricket_scores]
    )
)

response = chat.send_message("india ka cricket score kya hai")

print(response.text.strip())



