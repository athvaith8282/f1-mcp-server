"""
Run from the repository root:
    uv run examples/snippets/clients/streamable_basic.py
"""

import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main():
    # Connect to a streamable HTTP server
    async with streamablehttp_client("http://localhost:8000/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        # Create a session using the client streams
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            # List available tools
            tools = await session.list_tools()
            race_list_tool = tools.tools[1]
            print(f"Available tools: {[tool.name for tool in tools.tools]}")
            result = await session.call_tool(race_list_tool.name, arguments={
                'year': 2025
            })
            print("Tool result:", result)

if __name__ == "__main__":
    asyncio.run(main())
