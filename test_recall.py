from memory import recall_similar_incidents

results = recall_similar_incidents("checkout service throwing 500s, pool exhausted")

print("Found these related memories:")
for r in results.results:
    print("-", r.text)