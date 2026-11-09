stock = {"SKU-100": 15, "SKU-200": 45, "SKU-300": 12, "SKU-400": 21} # assigns a dictionary to stock which has SKUs as keys and Quantities as values

print(f"{'SKU':<10}{'QTY':>5}") # prints f string that starts with SKU and pads 'SKU' on the right with spaces to fill 10 characters then prints QTY and pads 'QTY' on the left with spaces to fill 5 characters
print("-"*15) # prints 15 -

for sku, qty in stock.items(): # loops through stock and pulls the sku and qty
    print(f"{sku:<10}{qty:>5}") # prints f string that starts with sku and pads 'SKU' on the right with spaces to fill 10 characters then prints qty and pads 'QTY' on the left with spaces to fill 5 characters

skus = list(stock.keys()) # assigns a list of the keys in the stock dictionary to skus
print(", ".join(skus)) # joins the skus into one string with ", " between each one, then prints it