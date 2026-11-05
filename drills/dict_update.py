stock = {"SKU-100": 25, "SKU-200": 44, "SKU-300": 12, "SKU-400": 3} # assigns a dictionary to stock
shipments = [("SKU-300", 11), ("SKU-100", 15), ("SKU-400", 3), ("SKU-200", 20)]

print("Before:", stock) # prints the Before stock dictionary
for sku, qty in shipments: # loops through each sku and qty inside shipments
    stock[sku] = stock.get(sku, 0) + qty # looks up the SKU in stock and returns its current qty, or `0` if the key is missing. Then adds the shipment and write the new total
print("After:", stock) # prints the After stock dictionary 