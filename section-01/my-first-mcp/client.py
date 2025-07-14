from mcp import ClientSession, StdioServerParameters, types 
from mcp.client.stdio  import stdio_client
import asyncio
import traceback

server_params = StdioServerParameters(
  command="uv",
  args=["run", "weather.py"], 
)

async def run():
  try:
    print("Starting stdio_client")
    async with stdio_client(server_params) as (read, write):
      async with ClientSession(read, write) as session:
        print("initializing session...")
        await session.initialize()
        
        print("listing tools...")
        tools = await session.list_tools()
        print("Available tools:", tools)
        
        print("Calling tool...")
        result = await session.call_tool("get_current_weather", arguments={"city": "seoul"})
        
        print("Tool result:", result)
  except Exception as e:
    print("An error occurred:")
    traceback.print_exc()
    
  
  if __name__ == "__main__":
    asyncio.run(run())
  