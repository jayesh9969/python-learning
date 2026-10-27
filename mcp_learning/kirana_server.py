
try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    from mcp.server.mcpserver import MCPServer as FastMCP

import asyncio

server = FastMCP("KiranaStore")

@server.tool()

def calculate_bill(item: str, quantity: int) -> dict:

    """Kirana item ka total bill calculate karta hai."""

    prices = {"doodh": 30, "bread": 25, "biscuit": 10}

    total = prices[item] * quantity

    return {"item": item, "total": total, "status": "calculated"}


@server.resource("store://policy")

def get_store_policy() -> str:
    """Dukan ke niyam."""


    return "Udhari band hai! Returns within 24 hours only."


@server.resource("order://receipt/{order_id}")

def get_order_receipt(order_id: str) -> str:
    """Order reciept lene ke liye"""

    return f"Receipt for order #{order_id} Paid in full"


async def test_server():
    res = await server.call_tool("calculate_bill", {"item": "bread", "quantity": 3})
    print("Tool Output:", res[0].text)

    policy = await server.read_resource("store://policy")
    print("Policy:", policy[0].content)

    receipt = await server.read_resource("order://receipt/101")

    print("Order Receipt:", receipt[0].content)

if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        asyncio.run(test_server())
    else:
        server.run(transport="stdio")



