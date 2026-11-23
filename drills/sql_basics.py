import sqlite3 # loads the built-in module for SQLite databases

conn = sqlite3.connect(":memory:") # opens a datatbase using only RAM and closes when the script is done
cur = conn.cursor() # the cursor sends SQL and holds the result

cur.execute("CREATE TABLE inventory (sku TEXT, bin TEXT, on_hand INTEGER, reorder_point INTEGER)") # make an empty table with 4 typed columns

rows = [
    ("SKU-1042", "A3-04", 10, 15),
    ("SKU-2210", "A3-05", 40, 20),
    ("SKU-3301", "B1-02", 3, 5),
] # one tuple per row, in column order
cur.executemany("INSERT INTO inventory VALUES (?, ?, ?, ?)", rows) # insert every tuple; each ? is filled in order
conn.commit() # save the inserts

cur.execute("SELECT sku, on_hand FROM inventory WHERE on_hand < reorder_point ORDER BY on_hand") # low-stock rows, smallest on_hand first
for row in cur.fetchall(): # fetchall returns a list of tuples
    print(row) # print each row tuple

cur.execute("SELECT COUNT(*) FROM inventory") # ask how many rows are in the table
print(cur.fetchone()[0]) # fetchone gives a 1-item tuple; [0] pulls the number out

conn.close() # close the database

# OUTPUT:
# ('SKU-3301', 3)
# ('SKU-1042', 10)
# 3