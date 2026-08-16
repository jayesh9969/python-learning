from google import genai

client = genai.Client()

response = client.models.generate_content(
    model = "gemini-flash-lite-latest",
    contents = "hey this is my first api call with python"
)

print(response.text)