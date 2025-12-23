from fastapi import FastAPI
from pydantic import BaseModel
from agent.agent import agent_chat

app = FastAPI(title="Agentic RAG API")

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat(payload: ChatRequest):
    result = await agent_chat(payload.query)
    return {"response": result}

@app.get("/")
async def health():
    return {"status": "ok"}
