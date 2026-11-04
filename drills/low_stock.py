qtys = [5, 12, 3, 30] # creates a list of integers

def totaling(numbers):
    total = 0
    for n in numbers:
        total += n
    print(f"The total is: {total}")

def largest(numbers):
    current = 0
    for n in numbers:
        if n >= current:
            current = n
    print(f"The largest number is: {current}")

totaling(qtys)
largest(qtys)

stock = {"SKU-1042": 20, "SKU-2001": 50} # creates a dictionary
stock["SKU-3000"] = 15 # adds a key and value to the dictionary
stock["SKU-1042"] += 10 # adds to to the value according to the key
for sku, qty in stock.items(): # loops through each sku and the qty pair in stock
    print(f"{sku}: {qty} units") # prints the sku and qty for the instance into a string using an f string

def low_stock(stock, limit): # creates a low_stock function using stock and a set limit
    low = [] # creates an empty list to store any sku's that are below qty limit
    for sku, qty in stock.items(): # loops through each pair in the dictionary 
        if qty < limit: # checks if the instance qty is below the limit
            low.append(sku) # if True then the sku is appended into the low list
    return low # returns the updated low list

print(low_stock(stock, 20)) # prints the low list based on the results of the low_stock function

text = "SKU-1042 qty=5"
parts = text.split(" ")
sku_num = int(parts[0].split("-")[1])
qty = int(parts[1].split("=")[1])
print(sku_num, qty)