from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition

def multiply(a: int, b: int) -> int:
    """Multiplies two numbers a and b."""

    print(f"Tool running: multiplying {a} * {b}...")

    return a * b


tools = [multiply]

llm = ChatGoogleGenerativeAI(model="gemini-flash-lite-latest").bind_tools(tools)

def call_model(state: MessagesState) -> dict:

    response = llm.invoke(state["messages"])

    return {"messages": [response]}


builder = StateGraph(MessagesState)

builder.add_node("agent", call_model)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "agent")

builder.add_conditional_edges("agent", tools_condition)

builder.add_edge("tools", "agent")

app = builder.compile()

print("--- Starting Agent Graph ---")

query = "Bhai 25 aur 40 ko multiply karke batao kitna hota hai?"

print("User Query:", query)

res = app.invoke({"messages": [("user", query)]})

print("\n--- Final Agent Answer ---")

print(res["messages"][-1].content)