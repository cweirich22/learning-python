# run as: python drills/quiz_low_stock.py drills/inventory.csv REORDER_POINT
import csv # loads the csv module
import sys # loads the sys module

def main(): # creates a function called main
    if len(sys.argv) != 3: # checks if there is exact 2 arguments or not
        print("usage: drills/quiz_low_stock.py drills/inventory.csv REORDER_POINT", file=sys.stderr) # if not, then print the usage to stderr
        sys.exit(2) # 2 = Invalid usage 

    input_file = sys.argv[1] # assign the first argument to input_file

    try: # try to convert argument two to a integer then check if its a negative number, if not converted to ant or is negative then ValueError
        reorder_point = int(sys.argv[2]) # convert argument two to an integer
        if reorder_point < 0: # checks if reorder_point is a negative number
            raise ValueError("REORDER_POINT is either negative or not a whole number.") # raise ValueError if True with the error message
    except ValueError: # when ValueError is raised print the message along with exiting with code 2
        print("REORDER_POINT is either negative or not a whole number.", file=sys.stderr) # print string to stderr
        sys.exit(2) # 2 = REORDER_POINT is either negative or not a whole number

    records = [] # assigns an empty list to records
    total = 0 # assigns 0 to total
    try: # try to open the input file in read mode as f, assign a reader, loop through each row in the file and add 1 to the total, convert on_hand to an integer then check if that number is less than or equal to reorder_point and if True then append the row to records list
        with open(input_file, "r") as f: # open the input file in rea dmofe as f
            reader = csv.DictReader(f) # creates a dictreader for f
            for row in reader: # loops through each row in reader
                total += 1 # adds 1 to total for each row
                row["on_hand"] = int(row["on_hand"]) # converts the on_hand to an integer
                if row["on_hand"] <= reorder_point: # checks if the on_hand is less than or equal to reorder_point
                    records.append(row) # if True then append the row to the records list
    except FileNotFoundError: # except when FileNotFoundError is raised
        print("File is missing or doesn't exist.", file=sys.stderr) # print the string to stderr
        sys.exit(1) # 1 = File is missing or doesn't exist

    sorted_records = sorted(records, key=lambda row: (row["on_hand"], row["sku"])) # sort records based on on_hand and break ties with sku

    count = 0 # assigns 0 to count
    print("SKU ON_HAND") # prints the string
    for row in sorted_records: # loops through each row in sorted_records
        print(row["sku"], row["on_hand"]) # prints one string of sku and onhand for the row
        count += 1 # adds one to count
    print(f"{count} of {total} SKUs at or below reorder point {reorder_point}.") # prints a f string summary including count, total, reorder_point
    sys.exit(0) # 0 = success

if __name__ == "__main__": # only run main from this script
    main() # run main


# Predictions below each example:
# python drills/quiz_low_stock.py drills/inventory.csv 4
# $LASTEXITCODE
# SKU ON_HAND
# SKU-3301 0
# SKU-1042 4
# SKU-5005 4
# 3 of 5 SKUs at or below reorder point 4.
# 0

# python drills/quiz_low_stock.py drills/inventory.csv 100
# $LASTEXITCODE
# SKU ON_HAND
# SKU-3301 0
# SKU-1042 4
# SKU-5005 4
# SKU-4120 6
# SKU-2210 15
# 5 of 5 SKUs at or below reorder point 100.
# 0

# python drills/quiz_low_stock.py drills/inventory.csv -1
# $LASTEXITCODE
# REORDER_POINT is either negative or not a whole number.
# 2

# python drills/quiz_low_stock.py drills/inventory.csv
# $LASTEXITCODE
# usage: drills/quiz_low_stock.py drills/inventory.csv REORDER_POINT
# 2

# python drills/quiz_low_stock.py drills/missing.csv 4
# $LASTEXITCODE
# File is missing or doesn't exist.
# 1