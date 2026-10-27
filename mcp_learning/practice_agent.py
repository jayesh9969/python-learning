
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client
from mcp import StdioServerParameters
import asyncio

server_params = StdioServerParameters(command="python", args=["mcp_learning/kirana_server.py"])

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()


            print("Session connected successfully!")


if __name__ == "__main__":
    asyncio.run(main())





