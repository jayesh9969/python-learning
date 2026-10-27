from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.checkpoint.memory import MemorySaver

llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash")

def call_model(state: MessagesState) -> dict:
    response = llm.invoke(state["messages"])

    return {"messages": [response]}


builder = StateGraph(MessagesState)
builder.add_node("agent", call_model)

builder.add_edge(START, "agent")
builder.add_edge("agent", END)

app = builder.compile(checkpointer=MemorySaver())

print("--- Thread 1: user_jayesh ---")

config_jayesh = {"configurable": {"thread_id" : "user_jayesh"}}

print("Turn 1: Telling me...")

app.invoke({"messages": [("user", "mera naam Jayesh hai.")]}, config=config_jayesh)

print("Turn 2: Telling me...")

res2 = app.invoke({"messages": [("user", "Mera naam kya hai?")]}, config=config_jayesh)

print("AI Response:", res2["messages"][-1].content)

print("\n" + "="*50 + "\n")

print("--- Thread 2: user_stranger ---")

config_stranger = {"configurable": {"thread_id": "user_stranger"}}

res3 = app.invoke({"messages": [("user", "Mera naam kya hai?")]}, config=config_stranger)

print("AI Response:", res3["messages"][-1].content)


