from google import genai
from google.genai import types

called_tool = None
called_args = None

def get_order_status(order_id: str) -> str:

    """Checks the delivery status of an order."""

    global called_tool, called_args

    called_tool = "get_order_status"
    called_args = order_id

    return f"Order {order_id} is out for delivery."


c = genai.Client()

chat = c.chats.create(
    model="gemini-flash-lite-latest",
    config=types.GenerateContentConfig(
        tools=[get_order_status]
    )
)

response = chat.send_message("Mera order 9988 kahan hai?")

print("AI Response:", response.text.strip())

print("\n--- Running Evaluation Tests ---")

assert called_tool == "get_order_status"

assert called_args == "9988"

assert "9988" in response.text or "delivery" in response.text.lower()

print("ALL 3 EVALUATION TESTS ARE PASSED!")