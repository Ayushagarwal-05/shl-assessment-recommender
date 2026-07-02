from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from app.catalog import Catalog
from app.retrieval import Retriever
from app.agent import Agent

app = FastAPI(title="SHL Recommendation Agent")


catalog = Catalog()
retriever = Retriever(catalog)
agent = Agent(retriever)


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):
    messages = [
        {
            "role": m.role,
            "content": m.content
        }
        for m in request.messages
    ]

    return agent.chat(messages)