import sys # loads the sys module which gives us argv, exit, stderr
import csv # loads the csv module
from label_parser_v4 import parse_label # loads parse_label function from label_parser_v4

def main(): # creates a function called main
    if len(sys.argv) != 3: # checks if sys.argv doesn't have exactly 3 items (script name + 2 args)
        print("usage: label_parser_cli.py INPUT_TXT OUTPUT_CSV", file=sys.stderr) # print usage: label_parser_cli.py INPUT_TXT OUTPUT_CSV through stderr
        sys.exit(2) # 2 = used wrong
    input_path = sys.argv[1] # assigns sys.argv index 1 to input_path
    output_path = sys.argv[2] # assigns sys.argv index 2 to output_path
    records = [] # assigns an empty list
    bad_lines = [] # assigns an empty list
    try: # try to open input_path then loop through the file to parse_label, if FileNotFound then jump to except
        with open(input_path) as f: # opens input_path as f
            for line_num, line in enumerate(f, start=1): # loops through each line_num and line in f and counts each line starting from 1
                try: # try to parse the line, if it raises ValueError, jump to except
                    result = parse_label(line) # assigns what parse_label(line) returns to result
                    records.append(result) # appends the result to the records list
                except ValueError: # if parse_label raises ValueError
                    bad_lines.append(f"line {line_num}: {line.strip()}") # append f string with line_num and line.strip() to bad_lines list
    except FileNotFoundError: # if the file doesn't exist, open() raises FileNotFoundError
        print(f"file not found: {input_path}", file=sys.stderr) # prints f string with input_path through stderr
        sys.exit(1) # 1 = file not found

    with open(output_path, "w", newline="") as out:  # creates or wipes output file using writemode and sets newline
        writer = csv.DictWriter(out, fieldnames=["sku", "qty", "po"])  # assigns a csv dictionary writer to out with fieldnames as sku, qty, and po
        writer.writeheader()  # writes the header with the fieldnames
        writer.writerows(records)  # writes a row for each dict in the records list

    for bad in bad_lines:  # loops through bad_lines
        print(bad, file=sys.stderr)  # prints the bad line using stderr

    print(f"Parsed {len(records)} labels, skipped {len(bad_lines)} bad lines.")  # Overall print statement using f string to relay the total records and bad lines

    if bad_lines:  # True if bad_lines has anything in it
        sys.exit(3)  # 3 = bad lines isn't empty
    sys.exit(0)  # 0 = no bad lines

if __name__ == "__main__": # if the code is run from this file then run main()
    main() 

# PREDICT these exit codes:
# 1. python drills/label_parser_cli.py
# 2. python drills/label_parser_cli.py drills/nope.txt drills/out.csv
# 3. python drills/label_parser_cli.py drills/labels_messy.txt drills/out.csv
# 4. What does line 31 print?
# 5. python drills/label_parser_cli.py drills/labels_clean.txt drills/out_clean.csv

# PREDICTIONS
# 1.
# usage: label_parser_cli.py INPUT_TXT OUTPUT_CSV
# 2

# 2.
# file not found: drills/nope.txt
# 1

# 3.
# Parsed 4 labels, skipped 3 bad lines.
# 3

# 4.
# line 4: SKU-77 | QTY: | PO-55015
# line 5: damaged pallet, no label
# line 7: SKU-5120 | QTY: 6 | PO-5501
# Parsed 4 labels, skipped 3 bad lines.

# 5.
# Parsed 4 labels, skipped 0 bad lines.
# 0