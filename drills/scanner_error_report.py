# Usage: python drills/scanner_error_report.py INPUT_LOG OUTPUT_CSV

import sys # loads the sys module
import csv # loads the csv module
import re # loads the regex module

ERROR_RE = re.compile(r"(SCN-\d+) ERROR (\w+)") # creates a regex pattern 

def parse_error_line(line): # creates a function called parse_error_line with a parameter called line
    m = ERROR_RE.search(line) # uses the ERROR_RE regex to search for a match in line then stores it in m
    if not m: # if m is no match found is True
        return None # returns None
    return m.group(1), m.group(2) # if m does have a match then return m capture group 1 and 2

def main(): # creates a function called main
    if len(sys.argv) != 3: # checks if sys.argv doesn't have exactly 3 items (script name + 2 args)
        print("usage: drills/scanner_error_report.py INPUT_LOG OUTPUT_CSV", file=sys.stderr) # print usage: drills/scanner_error_report.py INPUT_LOG OUTPUT_CSV through stderr
        sys.exit(2) # 2 = used wrong number of arguments
    input_path = sys.argv[1] # assigns sys.argv index 1 to input_path
    output_path = sys.argv[2] # assigns sys.argv index 2 to output_path
    scanner_counts = {} # assigns an empty dictionary
    error_counts = {} # assigns an empty dictionary
    try: # try to open input_path then loop through the file to parse_error_line, if FileNotFound then jump to except
        with open(input_path) as f: # opens input_path as f
            for line in f: # loops through each line in f
                result = parse_error_line(line) # (scanner, error) tuple, or None if not an ERROR line
                if result is None: # checks if result is equal to None
                    continue # if equal to None then continue by skipping through this loop
                scanner, error = result # assigns scanner to result[0] and error to result[1]
                error_counts[error] = error_counts.get(error, 0) + 1 # old count, or 0 if this key is new, plus 1
                scanner_counts[scanner] = scanner_counts.get(scanner, 0) + 1 # old count, or 0 if this key is new, plus 1
    except FileNotFoundError: # if the file doesn't exist, open() raises FileNotFoundError
        print(f"file not found: {input_path}", file=sys.stderr) # prints f string with input_path through stderr
        sys.exit(1) # 1 = file not found

    ranked_errors = sorted(error_counts.items(), key=lambda kv: kv[1], reverse=True) # `turn the dict into (error, count) pairs, sort them by the count (kv[1]), biggest first, and get back a list of tuples`.
    with open(output_path, "w", newline="") as out: # opens the output_path in write mode as out
        writer = csv.writer(out) # assigns a writer to out
        writer.writerow(["error", "count"]) # writes the header row with fieldnames error and count
        writer.writerows(ranked_errors) # writes each row with each line from ranked_errors

    total = sum(error_counts.values()) # adds all the values in error_counts then assigns it to total
    print(f"Found {total} errors across {len(scanner_counts)} scanners.") # prints f string that says the total and length of scanner_counts
    sys.exit(0) # 0 = success

if __name__ == "__main__": # makes sure that main is only run from this script
    main() # runs the main function

# PREDICTIONS:
# 1. python drills/scanner_error_report.py
# usage: drills/scanner_error_report.py INPUT_LOG OUTPUT_CSV
# 2
# 2. python drills/scanner_error_report.py drills/nope.log out.csv
# file not found: drills/nope.log
# 1
# 3a. python drills/scanner_error_report.py drills/scanner.log drills/scanner_errors.csv
# Found 8 errors across 3 scanners.
# 0
# 3b. Get-Content drills/scanner_errors.csv
# error, count
# NO_READ, 3
# JAM, 3
# TIMEOUT, 2

# CORRECTIONS:
# 3b. there is no spaces after the commas so it should be:
# error,count
# NO_READ,3
# JAM,3
# TIMEOUT,2