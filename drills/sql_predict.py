# run as: python drills/sql_predict.py
import sqlite3 # loads the built-in sqlite module

conn = sqlite3.connect(":memory:") # opens a database only using RAM
cur = conn.cursor() # the cursor sends SQL and holds the result
cur.execute("CREATE TABLE receipts (po TEXT, sku TEXT, qty INTEGER)") # uses cursor to create a table called receipts with the columns po (text), sku (text), and qty (int)
cur.executemany("INSERT INTO receipts VALUES (?, ?, ?)", [ # inserts every tuple into the receipts table which will create three rows of values
    ("PO-55012", "SKU-1042", 12),
    ("PO-55012", "SKU-2210", 4),
    ("PO-55013", "SKU-1042", 8),
])
conn.commit() # saves the result to conn

cur.execute("SELECT qty FROM receipts WHERE sku = ?", ("SKU-1042",)) # finds the rows with the matching sku then grabs the qty for that row
print(cur.fetchall()) # prints a tuple with the qty for every row with the mtching sku

cur.execute("SELECT po, qty FROM receipts ORDER BY qty DESC") # grabs the po and qty from reach row in receipts in order of largest to smalled qty
print(cur.fetchall()[0]) # prints the po and qty in the first row which has the largest qty

cur.execute("SELECT sku FROM receipts WHERE qty > ?", (5,)) # grabs the sku from the rows that has a qty greater than 5
rows = cur.fetchall() # stores the result of the most recent call inside rows
print(len(rows)) # prints the length of rows which is two
print(rows[0][0]) # prints the first row along with the first value

cur.execute("SELECT qty FROM receipts WHERE po = ?", ("PO-99999",)) # grabs the qty of the rows with a po is equal to PO-99999
print(cur.fetchall()) # prints the result of the most recent cur.execute with returned None

cur.execute("SELECT COUNT(*) FROM receipts WHERE po = ?", ("PO-55012",)) # counts all the rows with a po matching PO-55012
print(cur.fetchone()) # prints the total count of rows that match the po which is 2

conn.close() # closes the script 

# PREDICT (every printed line in order):
# (8,), (12,)
# ('PO-55012',), ('PO-55013',), ('PO-55012',)
# 2
# PO-55012
# None
# 2