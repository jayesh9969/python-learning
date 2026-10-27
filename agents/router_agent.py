from google import genai
from google.genai import types

c = genai.Client()

def handle_with_python(query: str) -> str:
    """This is a simple deterministic Python code (Zero AI tokens)."""

    return "[PYTHON ROUTE] Your Order #9988 wil be delivered on Tommarow Morning 10AM. (Execution: 0ms, Cost: $0)"



def handle_with_agent(query: str) -> str:
    """This is an agent route which handles complex complaints by using agent's analytical skills"""

    chat = c.chats.create(
        model="gemini-flash-lite-latest"
    )

    res = chat.send_message(f"Handle this Customer's complaint politely and with your Analytical skills: {query}")
    return f"[AI AGENT ROUTE] {res.text.strip()}"


def smart_router(query: str) -> str:

    if "track" in query or "order status" in query:
        return handle_with_python(query)

    else:
        return handle_with_agent(query)
        




q2 = "Mera track order status kya hai?"
print("User Query 2:", q2)
print(smart_router(q2))

print("\n" + "="*50 + "\n")

q1 = "Maine pizza mangwaya tha par wo poora thanda aur box dabha hua aaya hai, mujhe bohot gussa aa raha hai!"

print("User Query 1:", q1)
print(smart_router(q1))

