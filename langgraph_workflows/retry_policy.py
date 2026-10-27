from langgraph.graph import StateGraph, START, END
from langgraph.types import RetryPolicy
from typing import TypedDict

# 1. State Schema
class FlakyState(TypedDict):
    status: str

# Track karne ke liye ki function kitni baar call hua
attempt = 0

# 2. Node Function (Bina kisi loop ke — loop LangGraph khud chalayega!)
def flaky_node(state: FlakyState) -> dict:
    global attempt
    attempt += 1
    print(f"Attempt {attempt}")


    if attempt < 3:
        raise ConnectionError("Server glitch")
        


    else:
        return {"status": "Success: work done!"}


    # --- TODO 1: Logic yahan likho ---
    # Agar attempt < 3 hai, toh ConnectionError raise karo
    # Warna {"status": "Success: Kaam ho gaya!"} return karo



# 3. Retry Policy
# --- TODO 2: Policy define karo ---
# policy = RetryPolicy(max_attempts=3, initial_interval=0.5, backoff_factor=2.0)

policy = RetryPolicy(max_attempts=3, initial_interval=0.5, backoff_factor=2.0)

# 4. Graph Setup (Dhancha)
builder = StateGraph(FlakyState)

# --- TODO 3: Node add karo retry policy ke saath ---
# builder.add_node("flaky", flaky_node, retry=policy)

builder.add_node("flaky", flaky_node, retry=policy)

builder.add_edge(START, "flaky")
builder.add_edge("flaky", END)

app = builder.compile()

# 5. Run & Output
result = app.invoke({"status": ""})
print(result["status"])
