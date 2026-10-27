from google import genai
from google.genai import types

def transfer_money(recipent: str, amount: int) -> str:
    """This tool transfers money from bank account"""

    if amount <= 500:
        return f"Success: Rs {amount} sent to {recipent} (Auto-approved)"

    if amount > 500:
        confirm = input(f"Do you want to send money to {recipent} Rs {amount} ? (yes/no): ")
        if confirm.lower() == "yes":
            return f"Success: Rs {amount} sent to {recipent} (Approved by user)"
        else:
            return f"Cancelled: Transfer of Rs {amount} to {recipent} was declined by user."


c = genai.Client()

chat = c.chats.create(
    model="gemini-flash-lite-latest",
    config=types.GenerateContentConfig(
        tools=[transfer_money]
    )
)

response = chat.send_message("Ramesh ko 2000 rupees bhej do")

print(response.text)

# response2 = chat.send_message("suresh ko 200 rupees bhej do")

# print(response2.text)

