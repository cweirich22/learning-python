import csv
import os
import re
import sys
from collections import Counter

LINE_RE = re.compile(r"(\S+ \S+) (INFO|ERROR) \[(\w+)\] (.+)") # Takes all nonwhitespace characters for the date then a space and then all nonwhitespace characters for the time. Then it shows if its giving an ERROR or INFO. Then it gets the station in the brackets. Then gets all the characters after.
SCAN_RE = re.compile(r"Scanned (SKU-\d+) qty=(\d+)") # Gets the word Scanned then the SKU with the digits as this is changeable based on the SKU number. Then it gets the qty along with the corresponding number.

def parse_line(line):     # creates a function called parse_line that takes one line from the log file.
    # Why: one function = easy to test later
    match = LINE_RE.fullmatch(line.strip()) # line.strip() cuts the spaces and the \n off both ends ot the line. fullmatch checks whether the whole line fits the pattern from start to end. If it fits, match holds the result. If it doesn't, match is None.
    if not match: # If the line didn't fit, like the two junk lines, the function quits right away and gives back None, meaning "nothing is usable here."
        return None
    timestamp, level, station, message = match.groups() # match.group() gives back 4 captured pieces in order, like ("2026-10-27 08:01:12", "INFO", "PACK1", "Scanned SKU-1042 qty=5"). Then one line puts them into 4 variables at once. This is called unpacking.
    return {"timestamp": timestamp, "level": level, "station": station, "message": message} # This packs those 4 values into a dictionary, so other code can write row["level"] instead of trying to remember position numbers.

def build_reports(path): # creates a function called build_reports and takes in a path. This function will build the report.
    errors = Counter() # will keep count of all the errors
    sku_totals = Counter() # will keep count of all the sku totals
    skipped = 0 # starts a plain number counter at zero for bad lines. 
    with open(path) as f: # opens the file in the path as f
        for line in f: # goes through each line of the file
            row = parse_line(line) # parses the line using the parse_line function
            if row is None: # if the row gives back None then it gets skipped and is added to the skipped total
                skipped += 1 # this skip instance is added to the total
                continue # this will skip this instance and go to the next line of the file
            if row["level"] == "ERROR": # checks if the level in the row has ERROR
                errors[row["station"]] += 1 # if it does have ERROR then it adds 1 count to that station and keeps a totsl count
            scan = SCAN_RE.search(row["message"]) # uses search to to see if the pattern matches the message
            if scan: # this runs only if a scan was found, which skips messages like "Jam detected"
                sku, qty = scan.groups() # this unpacks the two captured groups, for example sku= "SKU-1042" and qty="5".
                sku_totals[sku] += int(qty) # int(qty) turns the text "5" into the number 5, and then it gets added to that SKU's running total. Wihtout int you get an Error.
    return errors, sku_totals, skipped # returns the values for all the errors, sku_totals, and skipped values.

def write_csv(path, fieldnames, rows): # takes in a file path then puts the fieldnames as the column names and rows which will be a list of dictionaries, one per row.
    with open(path, "w", newline="") as f: # opens the file in write mode which wipes the file and newline stops blanks rows from showing up on windows. 
        writer = csv.DictWriter(f, fieldnames=fieldnames) # DictWriter creates a writer that turns each dictionary into one csv row, and it uses fieldnames to set the column order.
        writer.writeheader() # writes the firs tline, sku, total_qty.
        writer.writerows(rows) # loops through the list and writes one line per dictionary.

def main(): # This defines the function that runs the whole script. It only starst when the __main__ guard at the bottom calls it.
    if len(sys.argv) != 2: # For python warehouse_log_report.py warehouse.log it's ["warehouse_log_report.py", "warehouse.log"], which is 2 items.
        print("Usage: python warehouse_log_report.py <logfile>", file=sys.stderr) # This shows how to run the script correctly. file=sys.stderr sends the message to the error output instea dof the normal output, so other tools can tell problems apart from real results.
        sys.exit(1) # This stops the script right away with exit code 1, which means "failed."
    log_path = sys.argv[1] # This grabs the second item, the file path you typed. Index 0 is the script's own name.
    if not os.path.exists(log_path): # If that file doesn't exist, the script says so and fails cleanly, so you don't get a messy crash inside open(). 
        print(f"Error: {log_path} not found", file=sys.stderr)
        sys.exit(1)
        
    errors, sku_totals, skipped = build_reports(log_path) # This runs build_reports on the log file. It returns 3 values, and unpacking puts each one in its own variable.
    out_dir = os.path.dirname(os.path.abspath(__file__)) # __file__ is this scripts path. abspath turns it into the full path. dirname cuts off the file name, so you're left with the folder, day5-logs. This is why the VSVs land next to the script no matter where you run it from.

    write_csv(os.path.join(out_dir, "error_report.csv"), # This calls the write_csv function. The first argument is the full path to the output file, built by joining the folder and the file name.
                ["station", "error_count"], # The second argument is the fieldnames, which are the column headers.
                [{"station": s, "error_count": c} for s, c in errors.most_common()]) # The third argument is the rows. This is a list comprehension. errors.most_common() gives pairs sorted from most errors to fewest, like [("PACK1", 2), ("DOCK3", 1), ...]. For each pair, s gets the station and c gets the count, and the comprehension builds one dictionary per row.
    write_csv(os.path.join(out_dir, "sku_totals.csv"),
                ["sku", "total_qty"],
                [{"sku": s, "total_qty": c} for s, c in sku_totals.most_common()])

    print(f"Done. Skipped {skipped} bad lines.")

if __name__ == "__main__":
    main()