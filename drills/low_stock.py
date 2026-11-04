qtys = [5, 12, 3, 30] # creates a list of integers

def totaling(numbers): # creates a function called totaling and will take in a list called numbers
    total = 0 # stores a sum of the numbers starting at 0
    for n in numbers: # loops through each number in numbers
        total += n # adds each number to the running total
    print(f"The total is: {total}") # prints the total using an f string

def largest(numbers): # creates a function called largest and will take in a list called numbers
    current = numbers[0] # stores the highest number and starts with the first number in the list
    for n in numbers: # loops through each number in numbers
        if n >= current: # if statement to check if the number is greater than or equal to the biggest one so far
            current = n # if True then the current will now be equal to n
    print(f"The largest number is: {current}") # prints the current number using an f string

totaling(qtys) # calls the totaling function and passes in the qtys list
largest(qtys) # calls the largest function and passes in the qtys list

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

text = "SKU-1042 qty=5" # stroes a string in a avriable called text
parts = text.split(" ") # splits the string into a list based on a space
sku_num = int(parts[0].split("-")[1]) # splits the first position of the list based on the - and makes the second part an integer
qty = int(parts[1].split("=")[1]) # splits the second part of the list based on the = and makes the second part an integer
print(sku_num, qty) # prints the sku_num and qty