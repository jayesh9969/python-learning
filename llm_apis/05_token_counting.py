from google import genai
from google.genai import types

client = genai.Client()
model_name = "gemini-flash-lite-latest"

reviews = [
    "khana achha tha par packaging kharab thi",
    "2 ghante late, khana bilkul thanda",
    "khana bahut tasty tha aur time par aaya",
]

total_actual = 0
for review in reviews:
    # 1. Estimated tokens before API call
    est_tokens = client.models.count_tokens(model=model_name, contents=review).total_tokens

    # 2. Actual API call
    response = client.models.generate_content(
        model=model_name,
        contents=review,
        config=types.GenerateContentConfig(
            system_instruction="Tum classifier ho. ek shabd do: positive, negative, mixed."
        )
    )
    ans = response.text.strip().lower()

    # 3. Actual tokens used from usage metadata
    actual_tokens = response.usage_metadata.total_token_count
    total_actual += actual_tokens

    print(f"Review: '{review}' | Ans: {ans} | Estimated: {est_tokens} | Actual: {actual_tokens}")

print(f"\nKul kharch hue tokens: {total_actual}")
