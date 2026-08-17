from google import genai
from google.genai import types
import enum

# client = genai.Client()

# response = client.models.generate_content(
#     model = "gemini-flash-lite-latest",
#     contents = "hey this is my first api call with python"
# )

# print(response.text)

reviews = [
    "khana achha tha par packaging kharab thi",
    "2 ghante late, khana bilkul thanda",
    "khana bahut tasty tha aur time par aaya",
]

client = genai.Client()
# for review in reviews:


#     response = client.models.generate_content(
#         model = "gemini-flash-lite-latest",
#         contents=review,
#         config=types.GenerateContentConfig(
#             system_instruction="Tum classifier ho. Sirf ek shabd do: positive, negative, mixed."
#         ),
#     )

#     answer = response.text.strip().lower()
#     print(answer)





class Mood(enum.Enum):

    POSITIVE = 'positive'
    NEGATIVE = 'negative'
    MIXED = 'mixed'

for review in reviews:
    response = client.models.generate_content(
            model = "gemini-flash-lite-latest",
            contents=review,
            config=types.GenerateContentConfig(
                response_mime_type='text/x.enum',
                response_schema=Mood
        ),
    )

    print(response.text)

       
        



