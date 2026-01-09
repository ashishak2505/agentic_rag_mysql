from fastapi import FastAPI
from pydantic import BaseModel

from pipeline.run_pipeline import run_pipeline  # reuse existing logic

app = FastAPI(title="Federal Register RAG API")


class ChatRequest(BaseModel):
    query: str


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    answer = run_pipeline(request.query)
    return {"response": answer}
