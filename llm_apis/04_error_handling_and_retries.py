from google import genai
from google.genai import types, errors
import time

client = genai.Client()
model_name = "gemini-flash-lite-latest"

reviews = [
    "khana achha tha par packaging kharab thi",
    "2 ghante late, khana bilkul thanda",
]

for review in reviews:
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=review,
                config=types.GenerateContentConfig(
                    system_instruction="Tum classifier ho. Sirf ek shabd do: positive, negative, mixed."
                ),
            )
            print(f"Success: {response.text.strip().lower()}")
            break
        except errors.ClientError as e:
            if e.code == 429:
                print("Rate limit 429 hit. Sleeping 20s...")
                time.sleep(20)
            else:
                print("Client error, code:", e.code)
                break
        except errors.ServerError as e:
            print(f"Server error {e.code}, retrying attempt {attempt + 1}...")
            time.sleep(5)
