from google import genai
from google.genai import types
import enum

class Mood(enum.Enum):
    POSITIVE = 'positive'
    NEGATIVE = 'negative'
    MIXED = 'mixed'

client = genai.Client()

reviews = [
    "khana achha tha par packaging kharab thi",
    "2 ghante late, khana bilkul thanda",
    "khana bahut tasty tha aur time par aaya",
]

print("Structured Output (Enums):")
for review in reviews:
    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=review,
        config=types.GenerateContentConfig(
            response_mime_type='text/x.enum',
            response_schema=Mood
        ),
    )
    print(f"Review: '{review}' -> Mood: {response.text.strip()}")
