from google import genai
from google.genai import types
import enum
from google.genai import errors
import time
import numpy as np

#a way to call model
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
#system instructions to answer control
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




# schema for total control we give options but model has to choose within one from options
# class Mood(enum.Enum):

#     POSITIVE = 'positive'
#     NEGATIVE = 'negative'
#     MIXED = 'mixed'

# for review in reviews:
#     response = client.models.generate_content(
#             model = "gemini-flash-lite-latest",
#             contents=review,
#             config=types.GenerateContentConfig(
#                 response_mime_type='text/x.enum',
#                 response_schema=Mood
#         ),
#     )

#     print(response.text)



       
# streaming to control answer delay so user dont need to wait for the answer long time       
# for chunk in client.models.generate_content_stream(
#     model = "gemini-flash-lite-latest",
#     contents="batao chai kaise banti hai",
# ):

#     print(chunk.text, end="", flush=True)

model1 = "gemini-flash-latest"
model2 = "gemini-flash-lite-latest"
model3 = "gemini-2.5-flash"
# for review in reviews:
#     for trying in range(3):
#         try:
#             response = client.models.generate_content(
#                 model=model2,
#                 contents=review,
#                 config=types.GenerateContentConfig(
#                     system_instruction="Tum classifier ho. Sirf ek shabd do: positive, negative, mixed."
#                 ),
            
#             )
#             print(response.text.strip().lower())
#             break
#         except errors.ClientError as e:
#             if e.code == 429:
#                 time.sleep(20)
#             # print("client error, code", e.code)

#             else:
#                 print("client error, code", e.code)
#                 break

#         except errors.ServerError as e:
            
#             time.sleep(5)
total = 0
est_total =0
for review in reviews:
    response = client.models.generate_content(
        model=model2,
        contents=review,
        config=types.GenerateContentConfig(
            system_instruction="Tum classifier ho. ek shabd do: positive, negative, mixed."
        )

    )
    ans = response.text.strip().lower()

            
    token_est = client.models.count_tokens(model=model2, contents=review).total_tokens

    # r_qn_tokens = response.usage_metadata.prompt_token_count
    # r_ans_tokens = response.usage_metadata.candidates_token_count

    r_total_tokens = response.usage_metadata.total_token_count
            
    print(f"{ans} tokens {r_total_tokens}")
    total = total + r_total_tokens
print(f"user ne total sab milake ke kharch kiye tokens = {total}  andaza tokens = {token_est}")




    

       




    


