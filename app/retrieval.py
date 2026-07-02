import re

from rank_bm25 import BM25Okapi
from rapidfuzz import fuzz


class Retriever:
    def __init__(self, catalog):
        self.catalog = catalog
        self.products = catalog.get_all()

        self.documents = []

        for product in self.products:

            searchable_text = " ".join([
                product.get("name", ""),
                " ".join(product.get("keys", [])),
                " ".join(product.get("job_levels", [])),
                product.get("description", "")
            ]).lower()

            self.documents.append(
                re.findall(r"\w+", searchable_text)
            )

        self.bm25 = BM25Okapi(self.documents)

    def score_product(self, product, query, bm25_score):

        query = query.lower()

        name_score = fuzz.token_set_ratio(
            query,
            product.get("name", "").lower()
        )

        keys_score = fuzz.token_set_ratio(
            query,
            " ".join(product.get("keys", [])).lower()
        )

        level_score = fuzz.token_set_ratio(
            query,
            " ".join(product.get("job_levels", [])).lower()
        )

        desc_score = fuzz.partial_ratio(
            query,
            product.get("description", "").lower()
        )

        final_score = (
            bm25_score * 3.0 +
            name_score * 0.40 +
            keys_score * 0.30 +
            level_score * 0.10 +
            desc_score * 0.20
        )

        return final_score

    def search(self, query: str, top_k: int = 10):

        tokens = re.findall(r"\w+", query.lower())

        bm25_scores = self.bm25.get_scores(tokens)

        scored = []

        for product, bm25_score in zip(self.products, bm25_scores):

            score = self.score_product(
                product,
                query,
                bm25_score
            )

            scored.append((score, product))

        scored.sort(
            key=lambda x: x[0],
            reverse=True
        )

        unique = []
        seen = set()

        # Prefer assessments before reports
        assessments = []
        reports = []

        for score, product in scored:

            if product["name"] in seen:
                continue

            seen.add(product["name"])
            
            if "report" in product["name"].lower():
                reports.append(product)
            else:
                assessments.append(product)
            
        for product in assessments:
            unique.append(product)

            if len(unique) == top_k:
                return unique
            
        for product in reports:
            unique.append(product)

            if len(unique) == top_k:
                return unique
            
        return unique