# run as: python drills/variance_ranking.py drills/cycle_report.csv NUMBER
import csv # loads the csv module
import sys # loads the sys module


def main(): # creates a function called main
    if len(sys.argv) != 3: # checks if the length of sys.argv isn't equal to 3
        print("usage: python drills/variance_ranking.py INPUT_CSV NUMBER", file=sys.stderr) # prints the usage error to sys.stderr
        sys.exit(2) # 2 = invalid usage
    input_csv = sys.argv[1] # assings the first argument as the input file
    number = sys.argv[2] # assigns the second argument as the number 
    try: # try to convert number to an integer, if able then check if n is negative and if it is then raise ValueError('negative number')
        n = int(number) # convert number to an integer then assign the result to n
        if n < 0: # check if n is a negative number
            raise ValueError('negative number') # if negative then raise ValueError('negative number')
    except ValueError: # if the number is negative or can't convert to an integer
        print(f"{number} is either not a whole number or is negative.", file=sys.stderr) # print f string with number to sys.stderr
        sys.exit(2) # 2 = Not a whole number or negative
    rankings = [] # assigns an empty list
    try: # try to open the input file wit Windows newliine format as f, create reader then read through each row and convert variance value to an integer, check if its not 0 then create a tuple with the bin, sku, and variance, then append to a list
        with open(input_csv, newline="") as f: # opens the input file with original line endings
            reader = csv.DictReader(f) # creates a csv reader for f
            for row in reader: # loops through each row in the reader
                v = int(row['variance']) # converts the value in vraiance key to an integer then assigns the result to v
                if v != 0: # checks if v doesn't equal 0
                    grouped = (row['bin'], row['sku'], v) # if yes then create a tuple with the key pairs vin, sku, and v
                    rankings.append(grouped) # append the tuple to rankings list
    except FileNotFoundError: # if input file is missing then except
        print(f"File ({input_csv}) doesn't exist or is missing.", file=sys.stderr) # prints f string with input_csv argument to sys.stderr
        sys.exit(1) # 1 = missing input file
    sorted_ranks = sorted(rankings, key=lambda r: (-abs(r[2]), r[0])) # sorts the rankings list from smallest to largest using the third item no matter the sign then use the first item for tie breakers
    rows_printed = 0 # assigns 0 to rows_printed
    for bin, sku, variance in sorted_ranks[:n]: # loops through n rows to pull each bin, sku, variance tuple 
        print(bin, sku, variance) # prints three values with spaces between them
        rows_printed += 1 # one id added to rows_printed for each loop
    print(f"Showed {rows_printed} of {len(sorted_ranks)} bins with variance.") # prints f string with rows_printed and the length of sorted_ranks
    sys.exit(0) # 0 = success

if __name__ == "__main__": # only runs main when running this script
    main() # runs the main function 

# Write the full stdout and $LASTEXITCODE

# python drills/variance_ranking.py drills/cycle_report.csv 2
# A3-04 SKU-1042 -2
# B1-01 SKU-0077 3
# Showed 2 of 3 bins with variance.
# 0
# python drills/variance_ranking.py drills/cycle_report.csv 10
# C2-07 SKU-5150 -7
# B1-01 SKU-0077 3
# A3-04 SKU-1042 -2
# Showed 3 of 3 bins with variance.
# 0
# python drills/variance_ranking.py drills/cycle_report.csv 0
# Showed 0 of 3 bins with variance.
# 0
# python drills/variance_ranking.py drills/cycle_report.csv abc
# ValueError('negative number')
# abc is either not a whole number or is negative.
# 2
# python drills/variance_ranking.py drills/nope.csv 2
# File drills/nope.csv doesn't exist or is missing.
# 1

# CORRECTIONS:
# python drills/variance_ranking.py drills/cycle_report.csv 2
# line one: C2-07 SKU-5150 -7 - order is backwards, it's largest to smallest witht eh sign disregarded

# python drills/variance_ranking.py drills/cycle_report.csv abc
# ValueError('negative number') doesn't print

# python drills/variance_ranking.py drills/nope.csv 2
# line one: File (drills/nope.csv) doesn't exist or is missing. - forgot the () inside the string