import sys # loads the sys module which gives us argv, exit, stderr

def main(): # creates a function called main
    if len(sys.argv) != 3: # checks if length of sys.argv isn't equal to 3
        print("usage: check_stock.py SKU QTY", file=sys.stderr) # prints a string through stderr
        sys.exit(2) # 2 = used wrong
    sku = sys.argv[1] # assigns sku to sys.argv index 1
    qty = int(sys.argv[2]) # assigns qty to the integer of sys.argv index 2
    if qty < 10: # checks if qty is less than 10
        print(f"{sku}: LOW ({qty})") # prints f string saying sku LOW qty
        sys.exit(1) # 1 = stock is low
    print(f"{sku}: OK ({qty})") # prints f string sku OK qty
    sys.exit(0) # 0 = success

if __name__ == "__main__": # if the code is run from this file then run main()
    main()

# PREDICT these exit codes:
# python drills/check_stock.py SKU-1042 4
# python drills/check_stock.py SKU-1042 25
# python drills/check_stock.py

# PREDICTIONS
# SKU-1042: LOW (4)
# 1

# SKU-1042: OK (25)
# 0

# usage: check_stock.py SKU QTY
# 2