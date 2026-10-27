import asyncio
from mcp.client.stdio import stdio_client
from mcp.client.session import ClientSession
from langchain_mcp_adapters.tools import load_mcp_tools
from mcp import StdioServerParameters

server_params = StdioServerParameters(command="python", args=["mcp_learning/kirana_server.py"])


async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()


            tools = await load_mcp_tools(session)

            print("Discovered MCP Tools:", [t.name for t in tools])


            result = await tools[0].ainvoke({"item": "doodh", "quantity": 4})


            print("Tool Execution Result:", result[0]["text"])

if __name__ == "__main__":
    asyncio.run(main())