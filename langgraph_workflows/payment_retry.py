from langgraph.graph import StateGraph, START , END
from langgraph.types import RetryPolicy
from typing import TypedDict

class PayState(TypedDict):
    status: str


attempt = 0

def pay_node(state: PayState) -> dict:

    global attempt

    attempt+=1

    print(f"Attempt {attempt}")

    if attempt == 1:
        raise ConnectionError("Bank server busy...")

    if attempt == 2:
        print("Bank server connected!")

        return {"status": "final status: Payment of Rs 500 successful"}


policy = RetryPolicy(max_attempts=2, initial_interval=0.5, backoff_factor=2.0)

builder = StateGraph(PayState)

builder.add_node("pay", pay_node, retry=policy)

builder.add_edge(START, "pay")

builder.add_edge("pay", END)

app = builder.compile()

result = app.invoke({"status": ""})

print(result["status"])