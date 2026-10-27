import time
from google import genai
from google.genai import types

fake_server_calls = 0
attempt = 0
def get_server_data() -> str:
    """this tool takes data from bank server"""
    
    while attempt < 3:
        try:
            global fake_server_calls
            fake_server_calls += 1
            if fake_server_calls < 3:
                raise Exception("Server is down!")
    

            
            else:
                return "Data: Balance of the Bank is 50,000 ."

        except:
            time.sleep(2)
            attempt += 1

    return "Error: Server is down forever."


c = genai.Client()

chat = c.chats.create(
    model="gemini-flash-lite-latest",
    config=types.GenerateContentConfig(
        tools=[get_server_data]
    )
)

response = chat.send_message("Get my data from Bank Server")

print(response.text)

    