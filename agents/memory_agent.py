from google import genai
from google.genai import types

c = genai.Client()

print("--- 1. Stateless (Ghajini) test ---")
c.models.generate_content(
    model="gemini-flash-lite-latest",
    contents="Mera naam Jayesh hai."
)

response = c.models.generate_content(
    model="gemini-flash-lite-latest",
    contents="mera naam kya hai"
)

print(response.text)


print("\n--- 2. Stateful (Chat Memory) test ---")

chat = c.chats.create(
    model="gemini-flash-lite-latest",

)

chat.send_message("Mera Naam Jayesh hai.")

response = chat.send_message("mera naam kya hai?")

print(response.text)

print(len(chat.get_history()))
