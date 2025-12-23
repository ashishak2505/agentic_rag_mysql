import asyncio
from agent import agent_chat

async def main():
    query = "Summarize executive orders about AI from January 2025."
    response = await agent_chat(query)
    print("\n========== AGENT RESPONSE ==========\n")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
