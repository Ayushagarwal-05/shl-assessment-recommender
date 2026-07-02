from app.catalog import Catalog
from app.retrieval import Retriever
from app.agent import Agent

catalog = Catalog()
retriever = Retriever(catalog)
agent = Agent(retriever)

messages = [
    {
        "role": "user",
        "content": "Compare OPQ32r and Verify G+"
    }
]

response = agent.chat(messages)

from pprint import pprint
pprint(response)