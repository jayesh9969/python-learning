from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class OrderState(TypedDict):
    order_id: int
    status: str
    rider: str


def cook_food(state: OrderState) -> dict:

    print(f"chef: Order {state['order_id']} ban raha hai...")

    

    return {"status": "food is ready"}
    pass

def assign_rider(state: OrderState) -> dict:
    print(f"System: Rider assign ho raha hai...")

    return {"rider": "Raju Delivery Partner", "status": "Out for delivery"}
    pass

builder = StateGraph(OrderState)

builder.add_node("cook", cook_food)
builder.add_node("delivery", assign_rider)
builder.add_edge(START,"cook")
builder.add_edge("cook","delivery")
builder.add_edge("delivery", END)




app = builder.compile()

initial_data = {"order_id": 9988, "status": "Order Placed", "rider": ""}

final_result = app.invoke(initial_data)

print("\n--- Aakhri Result ---")

print(final_result)