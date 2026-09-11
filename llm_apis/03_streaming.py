from google import genai
from google.genai import types

client = genai.Client()

for chunk in client.models.generate_content_stream(
    model="gemini-flash-lite-latest",
    contents="Ai seekhne ke liye ek insaan me kya kya qualities honi chahiye 10 lines me batao",
):

    print(chunk.text, end="", flush=True)


