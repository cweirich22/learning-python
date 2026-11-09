# make a dict called stock with 4 SKUs and their quantities
stock = {"SKU-100": 15, "SKU-200": 45, "SKU-300": 12, "SKU-400": 21}
# print a header row: "SKU" left-aligned in 10 spaces, "QTY" right-aligned in 5
print(f"{'SKU':<10}{'QTY':>5}")
# print a line of dashes 15 long (hint: "-" * 15)
print("-"*15)
# loop over stock.items() and print each sku left-aligned 10, qty right-aligned 5
for sku, qty in stock.items():
    print(f"{sku:<10}{qty:>5}")
# make a list of just the SKUs (hint: list(stock.keys()) or a loop with append)
skus = list(stock.keys())
# print them joined with ", " between each one
print(", ".join(skus))