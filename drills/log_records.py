import re # loads the re module
import csv # loads the csv module

SCAN_RE = re.compile(r"(?P<time>\d{2}:\d{2}) (?P<scanner>SCN-\d{2}) ERROR (?P<code>\w+)") # creates a regex pattern with three capture group in order: time, scanner, code

records = [] # creates an empty list
with open("drills/scanner.log", "r") as f: # opens a file in read mode as f
    for line in f: # loops through each line in f
        m = SCAN_RE.search(line) # uses SCAN_RE regex to search through the line
        if not m: # no match on this line (m is None)
            continue # skip to the next line; te loop keeps going
        records.append(m.groupdict()) # appends the dictionary in the for loop to records list

print(f"Records length is: {len(records)} with the first record being {records[0]}") # f string using length of records and records index 0
# PREDICT: Records length is: 8 with the first record being time: 08:02, scanner: SCN-02, code: NO_READ
# CORRECTION: Records length is: 8 with the first record being {'time': '08:02', 'scanner': 'SCN-02', 'code': 'NO_READ'}

with open("drills/scanner_records.csv", "w", newline="") as out: # oepns a csv in write mode as out
    writer = csv.DictWriter(out, fieldnames=["time", "scanner", "code"]) # creates a dictwriter for out with the fieldnames time, scanner, code
    writer.writeheader() # writes the fieldnames to the header
    writer.writerows(records) # writes one dictionary inside records to each row
# PREDICTION:
# time,scanner,code
# 08:02,SCN-02,NO_READ
# 08:03,SCN-01,JAM
# 08:06,SCN-02,NO_READ
# 08:08,SCN-03,TIMEOUT
# 08:11,SCN-01,JAM
# 08:12,SCN-02,NO_READ
# 08:14,SCN-03,JAM
# 08:17,SCN-01,TIMEOUT