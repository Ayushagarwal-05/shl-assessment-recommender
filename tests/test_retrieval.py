from app.catalog import Catalog
from app.retrieval import Retriever

catalog = Catalog()
retriever = Retriever(catalog)

results = retriever.search(
    "Java Developer personality assessment"
)

for r in results:
    print(r["name"])