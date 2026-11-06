from collections import Counter

scans = ["SKU-100", "SKU-200", "SKU-100", "SKU-300", "SKU-100",
    "SKU-200", "SKU-400", "SKU-100", "SKU-300", "SKU-200",] # creates a list called scans

counts = {}
for sku in scans: # loops through all the SKUs in scans list
    counts[sku] = counts.get(sku, 0) + 1 # gets the current count(or 0), then adds 1 and stores it
print(counts) # prints the new dictionary called counts

print(Counter(scans)) # uses a specialized dictionary made for counting
