import csv  # csv reading/writing
import re  # regex module

LINE_RE = re.compile(r"(?P<time>\d\d:\d\d) (?P<scanner>SCN-\d+) ERROR (?P<code>\w+)")  # regex pattern with three capture groups with each labeled in order: time, scanner, code
m = LINE_RE.search("2026-11-17 08:02 SCN-02 ERROR NO_READ")  # searched the string with the regex pattern
record = m.groupdict()  # puts each group into a single dictionary with the label as keys and the group itself as the value

with open("drills/one_record.csv", "w", newline="") as f:  # opens the file in write mode as f
    writer = csv.DictWriter(f, fieldnames=["time", "scanner", "code"])  # assigns a csv dictionary writer for f with fieldnames as time, scanner, and code
    writer.writeheader()  # write the fieldnames as the header
    writer.writerow(record)  # writes the values into a row

# PREDICT WHAT Get-Content drills/one_record.csv will show
# time,scanner,code
# '08:02','SCN-02','NO_READ'

# CORRECTION:
# time,scanner,code
# 08:02,SCN-02,NO_READ