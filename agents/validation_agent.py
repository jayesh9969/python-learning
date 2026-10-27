
from google import genai
from google.genai import types

def transfer_money(amount : int) -> str:
    """ye tool account se paise transfer karta hai"""

    if amount < 0:
        return "Error: Amount negative nahi ho sakta"

    else:
        return f"Success: {amount} transferred."



c = genai.Client()

chat = c.chats.create(
    model="gemini-flash-lite-latest",
    config=types.GenerateContentConfig(
        tools=[transfer_money]
    )
)

response = chat.send_message("Mere account se -5000 rupaye nikal lo")

print(response.text.strip())




