from app.catalog import Catalog

catalog = Catalog()

print("Products:", len(catalog.get_all()))

java = catalog.find_by_name("Core Java (Advanced Level) (New)")
print(java["name"])

results = catalog.search("java")

print(len(results))

for r in results[:5]:
    print("-", r["name"])