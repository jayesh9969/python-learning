from google import genai
from google.genai import types

client = genai.Client()

# Pehla API Call
response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents="hey this is my first api call with python"
)
print("First call response:\n", response.text)

# Classifier using System Instruction
reviews = [
    "khana achha tha par packaging kharab thi",
    "2 ghante late, khana bilkul thanda",
    "khana bahut tasty tha aur time par aaya",
]

print("\nClassifier with System Instruction:")
for review in reviews:
    res = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=review,
        config=types.GenerateContentConfig(
            system_instruction="Tum classifier ho. Sirf ek shabd do: positive, negative, mixed."
        ),
    )
    print(f"Review: '{review}' -> {res.text.strip().lower()}")
