from app.catalog import Catalog

catalog = Catalog()

for product in catalog.get_all():
    name = product["name"].lower()

    if "opq" in name:
        print(product["name"])