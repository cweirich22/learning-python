# run as: python drills/warmup_nov25.py drills/stock_levels.csv 3
import re # loads the re module
import sqlite3 # loads the sql module
import sys # loads the sys module

print(len(sys.argv)) # prints the length of sys.argv which is 3: script + two arguments
print(sys.argv[2] * 2) # prints second arument multiplied by two which the argument is a string so it equals 33
# PREDICT:
# 3
# 33

conn = sqlite3.connect(":memory:") # opens a database only using RAM
cur = conn.cursor() # the cursor sends SQL and holds the result
cur.execute("CREATE TABLE bins (bin TEXT, sku TEXT, qty INTEGER)") # uses cursor to create a table called bins with the columns bin(TEXT), sku(TEXT), qty(INTEGER)
cur.executemany( # adds a row for each tuple into the bins table
    "INSERT INTO bins VALUES (?, ?, ?)",
    [("A1-01", "SKU-1042", 5), ("A1-02", "SKU-2210", 0), ("B2-07", "SKU-1042", 9)],
)
print(cur.execute("SELECT COUNT(*) FROM bins WHERE sku = ?", ("SKU-1042",)).fetchone()) # fetches a count off all the rows that have a matching sku then prints the result as a 1-item tuple
print(cur.execute("SELECT bin FROM bins WHERE qty > 0 ORDER BY bin").fetchall()) # fetches all the rows where qty is greater than 0 and then orders them smallest to largest based on the bin then puts all the tuples into a list
conn.close() # closes the database connection (and drops the :memory: DB) 
# PREDICT:
# (2,)
# [('A1-01',), ('B2-07',)]


def check_qty(text): # creates a function called check_qty with a parameter called text
    try: # try to convert text into a int then assign it to qty, if ValueError then move to except and return bad, nif converted into an int then check if qty is negative
        qty = int(text) # convert text into int
    except ValueError: # if ValueError then return "bad"
        return "bad" # returns a string
    if qty < 0: # checks if qty is negative
        return "negative" # if negative then return the string
    return qty # if qty is integer and is 0 or greater than return qty

print(check_qty("12"))
print(check_qty("1.5"))
print(check_qty("-4"))
# PREDICT:
# 12
# bad
# negative

m = re.search(r"SKU-(\d{4})", "moved SKU-3301 to B2-07") # creates a regex pattern then searches the string for a match
print(m.groups()) # prints a list of the groups in m
print(m.group(1) + "0") # prints the first capture group with a string added to the end
# PREDICT:
# ['3301']
# '33010'
# CORRECTIONS:
# ('3301',) - groups are in a tuple which will always have a comma if theres only one item inside
# 33010 - prints a string so there is no quotes

def total_units(rows): # creates a function called total_units with a parameter called rows
    total = 0 # assigns 0 to total
    for row in rows: # loops through each row in rows
        total += row # adds row to totals

print(total_units([3, 4]))
# PREDICT:
# 7
# None
# CORRECTION:
# None - this is because the total was never returned

# EXPLAIN (in your own words):
# Q1: What type is every item in sys.argv, and how does that explain the second printed line?
# Every type is a string and the second argument is a number but since it's a string it will add the same string onto itself
# Q2: In subprocess.run(..., check=True), what does check=True do when the script exits with a nonzero code?
# forgot
# Answer: check=True makes subprocess,.run raise a CalledProcessError when the script exits with a nonzero code, instead of quietly handing you the code in returncode