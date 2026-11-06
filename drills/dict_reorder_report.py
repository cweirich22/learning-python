import csv

stock = {"SKU-100": 12, "SKU-200": 3, "SKU-300": 0, "SKU-400": 40} # assigns a dictionary called stock
reorder_point = {"SKU-100": 10, "SKU-200": 10, "SKU-300": 5, "SKU-400": 20} # assigns a dictionary called reorder_point

collect = [] # creates an empty list called collect

for sku, qty in stock.items(): # loops the sku and qty for all the items in the stock dicitonary
    point = reorder_point[sku] # pulls the reorder_point based on the sku in the loop
    if qty < point: # if statement to check if the qty is below the point
        order_qty = point * 2 - qty # calculates the qty to order for each sku
        collect.append([sku, qty, order_qty]) # appends the sku, qty, and order_qty to the collect list

with open("drills/reorder.csv", "w", newline="") as f: # opens the reorder.csv file as f in write mode
    writer = csv.writer(f) # creates a csv writer that formats rows and writes them to f
    writer.writerow(["sku", "stock", "order_qty"]) # writees the header to the file
    writer.writerows(collect) # writes all the data into the csv 

print(f"Need reorder: {len(collect)}") # prints the total SKU that need a reorder
