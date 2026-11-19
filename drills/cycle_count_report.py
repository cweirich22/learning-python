import re # loads the re module
import csv # loads the csv module
import sys # loads the sys module

CC_RE = re.compile(r"^\S+ \S+ CC BIN=(?P<bin>[A-Z]\d-\d{2}) SKU=(?P<sku>SKU-\d{4}) EXPECTED=(?P<expected>\d+) COUNTED=(?P<counted>\d+)$") # regex pattern that has names for the capturing groups
# usage: python drills/cycle_count_report.py INPUT_LOG OUTPUT_CSV

def parse_count_line(line): # creates a function called parse_count_line with a parameter called line
    line = line.strip() # strips whitespace from the start and end of line 
    m = CC_RE.search(line) # uses CC_RE regex to search through line
    if not m: # if CC_RE finds no match in line
        return None # no match (m is None), so this isn't a valid count record
    d = m.groupdict() # one dict: group names are the keys, matched text (strings) is the values
    expected = int(d["expected"]) # converts the expected text into an integer
    counted = int(d["counted"]) # converts the counted text into an integer
    return { # return a record dict: bin/sku as strings, expected/counted as ints, plus variance = counted - expected
        "bin": d["bin"],
        "sku": d["sku"],
        "expected": expected,
        "counted": counted,
        "variance": counted - expected
    }

def main(): # creates a function called main
    if len(sys.argv) != 3: # checks if sys.argv has 3 arguments which includes the script name
        print("usage: python drills/cycle_count_report.py INPUT_LOG OUTPUT_CSV", file=sys.stderr) # print the correct format if sys.argv length doesnt equal 3
        sys.exit(2) # 2 = Incorrect usage
    input_path = sys.argv[1] # the first argument after the script name is the input log path
    output_path = sys.argv[2] # the second argument after the script name is the input log path
    records = [] # creates an empty list
    bad = 0 # creates a total counting starting from 0
    with_variance = 0 # creates a total count starting with 0
    try: # try to open input_path then loop through the file to see if the lines match " CC BIN=", FileNotFoundError comes from open() when the file is missing
        with open(input_path, "r") as f: # opens input_path in read mode as f
            for line_num, line in enumerate(f, start=1): # loops through the line_num and line in f along with a count for line_num which starts at 1
                if " CC BIN=" not in line: # checks if the string is not inside the line
                    continue # if not then move to the next line in the for loop
                rec = parse_count_line(line) # stores the result of parse_count_line(line)
                if rec is None: # check if rec is None
                    print(f"line {line_num}: bad count record: {line.strip()}", file=sys.stderr) # if rec is None then print the f string with line_num and line with the whitespace stripped from the start and end then push this through sys.stderr
                    bad += 1 # add 1 to the bad total count
                    continue # if None then skip to the next line in the for loop
                records.append(rec) # append rec for that line into the records list which will store a dictionary
                if rec["variance"] != 0: # checks if the variance is not equal to 0
                    with_variance += 1 # if not equal to zero then add 1 to the with_variance total count
    except FileNotFoundError: # if the file doesn't exist or is missing, raises FileNotFoundError
        print(f"File ({input_path}) doesn't exist or is missing.", file=sys.stderr) # prints f string with the input_path through sys.stderr
        sys.exit(1) # 1 = File doesn't exist or is missing

    with open(output_path, "w", newline="") as out: # opens the output_path in write mode which will create the file or wipe it clean with newline identifier as out
        writer = csv.DictWriter(out, fieldnames=["bin", "sku", "expected", "counted", "variance"]) # creates the csv DictWriter for out with the fieldnames
        writer.writeheader() # writes the fieldnames into the header
        writer.writerows(records) # writes each dictionary in the records list as a line into out

    print(f"Parsed {len(records)} counts, {with_variance} with variance, {bad} bad lines.") # overall summary that prints f string of length of records, with_variance, and bad
    if bad > 0: # if bad is greater than 0
        sys.exit(3) # 3 = Contains bad lines
    sys.exit(0) # 0 = Success

if __name__ == "__main__": # only run main when running this file
    main() # run the main function

# PREDICTIONS:
#    No args: stderr output and $LASTEXITCODE
# usage: python drills/cycle_count_report.py INPUT_LOG OUTPUT_CSV
# 2
#    drills/nope.log out.csv: stderr output and $LASTEXITCODE
# File (drills/nope.log) doesn't exist or is missing.
# 1
#    drills/cycle_counts.log drills/cycle_counts.csv: both stderr lines with their line numbers, the summary line, $LASTEXITCODE, and the full Get-Content drills/cycle_counts.csv
# line 5: bad count record: 2026-11-18 08:09:02 CC BIN=B1-02 SKU=SKU-3301 EXPECTED=24 COUNTED=
# line 9: bad count record: 2026-11-18 08:18:44 CC BIN=C2-08 SKU-9999 EXPECTED=10 COUNTED=10
# Parsed 5 counts, 3 with variance, 2 bad lines.
# 3
# bin,sku,expected,counted,variance
# A3-04,SKU-1042,12,10,-2
# A3-05,SKU-2210,40,40,0
# B1-01,SKU-0077,5,8,3
# B1-03,SKU-1042,6,6,0
# C2-07,SKU-5150,100,93,-7

