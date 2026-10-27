from google import genai
from google.genai import types

def get_laptop_price(name : str) -> int:

    """this function returns laptop price"""

    return 100000

def get_discount(coupon : str) -> float:

    """this function returns coupon discount"""
    return 0.20


c = genai.Client()

chat = c.chats.create(
    model="gemini-flash-lite-latest",
    config=types.GenerateContentConfig(
        tools=[get_laptop_price, get_discount]
    )
)

response = chat.send_message(
    "Mera MacBook ka final price kya hoga agar main DIWALI50 coupon use karu?"
)

print(response.text)