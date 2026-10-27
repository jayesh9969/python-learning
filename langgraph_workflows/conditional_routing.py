from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class QualityState(TypedDict):
    item_name: str
    rating: int
    final_status: str


def inspect_item(state: QualityState) -> dict:
    print(f"Inspector: {state['item_name']} check ho raha hai...")

    return {"rating": state["rating"]}


def pack_item(state: QualityState) -> dict:
    print(f"Packaging: Item pass ho gaya! Packing and shipping...")

    return {"final_status": "SHIPPED"}

    pass

def reject_item(state: QualityState) -> dict:
    print(f"QC Alert: Item fail ho gaya! Return to vendor...")

    return {"final_status": "REJECTED"}

    pass

def decide_qc_route(state: QualityState) -> str:
    if state["rating"] >= 7:
        return "pass"

    else:
        return "fail"
        pass


builder = StateGraph(QualityState)

builder.add_node("inspector", inspect_item)
builder.add_node("pack", pack_item)
builder.add_node("reject", reject_item)

builder.add_edge(START, "inspector")

builder.add_conditional_edges("inspector", decide_qc_route, {"pass": "pack", "fail": "reject"})

builder.add_edge("pack", END)
builder.add_edge("reject", END)

app = builder.compile()

print("--- Test1 (High Quality Item) ---")

res1 = app.invoke({"item_name": "Leather Jacket", "rating": 9, "final_status": ""})
print("Result 1 :", res1)

print("\n" + "="*40 + "\n")


print("--- Test 2 (Low Quality Item) ---")

res2 = app.invoke({"item_name": "Torn Shirt", "rating": 4, "final_status": ""})

print("Result 2:", res2)