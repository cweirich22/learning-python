# run as: python drills/low_stock_sql.py drills/stock_levels.csv
import sys # loads the sys module
import csv # loads the csv module
import sqlite3 # loads the sql module

def main(): # creates a function called main
    if len(sys.argv) != 2: # checks if sys.argv doesn't have exactly two arguments
        print("usage: python drills/low_stock_sql.py INPUT_CSV", file=sys.stderr) # prints string of the error reasoning to stderr
        sys.exit(2) # 2 = Not exactly one argument

    input_csv = sys.argv[1] # assigns the first argument to input_csv
    records = [] # assigns an empty list to records

    try:  # try opening the input_csv as f, create a reader and loop through each row, change on_hand an reorder_point values into integers thenm apprend the entire row to records list, if input_csv doesn't exist then FileNotFoundError
        with open(input_csv, newline="") as f: # opens the input_csv as f with original newline method
            reader = csv.DictReader(f) # ccreates a csv reader for f
            for row in reader: # loops through each row in reader
                records.append((row['sku'], row['bin'], int(row['on_hand']), int(row['reorder_point']))) # adds the values to records while also converting on_hand and reorder_point into an integer
    except FileNotFoundError: # if FileNotFoundError 
        print(f"{input_csv} file missing or doesn't exist.", file=sys.stderr) # prints f string with input_csv to stderr
        sys.exit(1) # 1 = Missing or not existing file

    conn = sqlite3.connect(":memory:") # opens a database only using RAM
    cur = conn.cursor() # the cursor sends SQL and holds the result

    cur.execute("CREATE TABLE inventory (sku TEXT, bin TEXT, on_hand INTEGER, reorder_point INTEGER)") # creates a table called inventory with th following columns and formats: sku TEXT, bin TEXT, on_hand INTEGER, reorder_point INTEGER
    cur.executemany("INSERT INTO inventory VALUES (?, ?, ?, ?)", records) # takes all the records and adds each row into the inventory table in the format (?, ?, ?, ?)
    conn.commit() # save the inserts

    cur.execute("SELECT sku, bin, on_hand, reorder_point FROM inventory WHERE on_hand < reorder_point ORDER BY on_hand, sku") # Goes into inventory and pulls the sku, bin, on_hand, reorder_point ifor the rows that on_hand is less than reorder_point and then sorts each row by on_hand and sku for tiebreakers

    print("SKU BIN ON_HAND REORDER_POINT") # prints the string
    clean_up = cur.fetchall() # gets everything in the inventory table and assigns it to clean_up
    for sku, bin_code, on_hand, reorder_point in clean_up: # loops through each row in clean_up, pulling all the sku, bin_code, on_hand, reorder_point
        print(sku, bin_code, on_hand, reorder_point) # prints each sku, bin_code, on_hand, reorder_point

    cur.execute("SELECT COUNT(*) FROM inventory") # counts all the rows in the inventory table
    counts = cur.fetchone()[0] # assigns the total count of rows in inventory to counts

    print(f"{len(clean_up)} of {counts} SKUs below reorder point.") # prints f string with length of clean_up and counts
    
    conn.close() # close the database
    sys.exit(0) # 0 = success

if __name__ == "__main__": # only allows main to run from ths script 
    main() # runs main function

# PREDICTIONS:
# python drills/low_stock_sql.py drills/stock_levels.csv
# $LASTEXITCODE
# SKU BIN ON_HAND REORDER_POINT
# SKU-4410,B1-03,0,8
# SKU-3301,B1-02,3,5
# SKU-1042,A3-04,10,15
# 3 of 5 SKUs below reorder point.
# 0

# python drills/low_stock_sql.py
# $LASTEXITCODE
# usage: python drills/low_stock_sql.py INPUT_CSV
# 2

# python drills/low_stock_sql.py drills/nope.csv
# $LASTEXITCODE
# drills/nope.csv file missing or doesn't exist.
# 1