# run as: python drills/warmup_nov24.py drills/stock_levels.csv 3
import re # leads the re module
import sqlite3 # loads the SQL module
import subprocess # loads the subprocess module
import sys # loads the sys module

print(sys.argv[1]) # prints the first argument
print(sys.argv[2] + "0") # prints the second argument with another string on the end
print(len(sys.argv)) # prints the length of sys.argv
# drills/stock_levels.csv
# 30
# 3

m = re.search(r"BIN=(\S+)", "MOVE SKU=SKU-4410 BIN=B1-03 QTY=8") # creates a regex pattern to search through the string then assigns the result to m
print(m.groups()) # prints all the groups into a tuple
print(m.group(0)) # prints the complete match
# ('B1-03',)
# BIN=B1-03

conn = sqlite3.connect(":memory:") # opens a database only using RAM
cur = conn.cursor() # the cursor sends the DQL and holds the result
cur.execute("CREATE TABLE stock (sku TEXT, on_hand INTEGER)") # creates a table called stock which has two columns 
cur.executemany("INSERT INTO stock VALUES (?, ?)", [("SKU-3301", 3), ("SKU-1042", 10), ("SKU-4410", 0)]) # insert the tuples into the table one row at a time in the exact format
conn.commit() # saves the inserts to conn

cur.execute("SELECT sku FROM stock WHERE on_hand < ? ORDER BY sku", (5,)) # Goes to the stock table then looks for each row where on_hand is less than 5 then pulls each sku in order of sku
print(cur.fetchall()) # prints a list of tuples of just the sku's
cur.execute("SELECT on_hand FROM stock WHERE sku = ?", ("SKU-9999",)) # Goes to the stock table then looks for each row that has a sku that matches SKU-9999 then pulls each on_hand in original order
print(cur.fetchone()) # prints the first on_hand with a match
cur.execute("SELECT on_hand FROM stock WHERE sku = ?", ("SKU-9999",)) # Goes to the stock table then looks for each row that has a sku that matches SKU-9999 then pulls each on_hand in original order
print(cur.fetchall()) # prints a list fo tuples with all the on_hand that match the sku
cur.execute("SELECT COUNT(*) FROM stock") # Counts all the rows in the stock table
print(cur.fetchone()) # prints the count
cur.execute("SELECT on_hand FROM stock ORDER BY on_hand DESC") # Goes to the stock table and orders all the rows by on_hand in descending order then pulls ythe on_hand
print(cur.fetchone()[0]) # prints the first row which is the largest
conn.close() # closes the database connection (and drops the :memory: DB) (any code below this still runs)
# [('SKU-3301'), ('SKU-4410')]
# None
# []
# 3
# (10,)

skus = ["SKU-3301", "SKU-1042"] # assigns a list of SKUs to skus
print("SKU-1042" in skus) # prints the Boolean True if the sku is in skus AND fALSE IF NOT
print(skus) # prints the skus list
# True
# ['SKU-3301', 'SKU-1042']

def check_qty(qty): # creates a function called check_qty with a parameter called qty
    try: # try to return the qty as long as qty is greater than or equal to 0, else raise ValueError(f"negative qty: {qty}") and move to the except which will return 0
        if qty < 0: # checks if qty is less than 0
            raise ValueError(f"negative qty: {qty}") # if True then raise ValueError with the f string message
        return qty # return qty if False
    except ValueError: # move to except if ValueError was raised
        return 0 # returns 0

result = check_qty(-4) # stores the return of check_qty(-4) inside result
print(result) # prints the return of result
# ValueError('negative qty: -4')
# 0 

try: # try running subprocess with Python and raising ValueError('bad')
    subprocess.run([sys.executable, "-c", "raise ValueError('bad')"], check=True, capture_output=True) #run subprocess through Python and raise ValueError
    print("ok") # only prints if no ValueError 
except subprocess.CalledProcessError as e: # if CalledProcessError then move to this except 
    print("caught", e.returncode) # prints caught and the return code which is 1
# caught 1
