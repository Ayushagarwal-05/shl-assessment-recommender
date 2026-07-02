import json
from pathlib import Path
from typing import Any


class Catalog:
    def __init__(self, catalog_path: str = "data/catalog.json"):
        self.catalog_path = Path(catalog_path)

        with open(self.catalog_path, "r", encoding="utf-8") as f:
            self.products: list[dict[str, Any]] = json.load(f)

    def get_all(self) -> list[dict[str, Any]]:
        return self.products

    def find_by_name(self, name: str):
        name = name.lower()

        for product in self.products:
            if product["name"].lower() == name:
                return product

        return None

    def search(self, query: str):
        query = query.lower()

        results = []

        for product in self.products:
            text = " ".join([
                product.get("name", ""),
                product.get("description", ""),
                " ".join(product.get("keys", []))
            ]).lower()

            if query in text:
                results.append(product)

        return results