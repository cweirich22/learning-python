# run as: python drills/dict_reader_demo.py
# (cycle_report.csv must exist first: python drills/cycle_count_report.py drills/cycle_counts.log drills/cycle_report.csv)
import csv # loads the csv module

with open("drills/cycle_report.csv", newline="") as f: # opens drills/cycle_report.csv as f with default mode and lets csv handle line endings 
    reader = csv.DictReader(f) # makes a DictReader that turns each CSV row into a dict, using the header row as keys
    rows = list(reader) # reads every row into a list of dicts

print(rows[0]) # prints the first dictionary inside rows
print(type(rows[0]["counted"])) # prints the type of the "counted" value in the first row

net = 0 # assigns 0 to net
off = 0 # assigns 0 to off
for row in rows: # loops through each row in rows
    v = int(row["variance"]) # converts the value inside variance to an integer for each row. (DictReader gives strings, so int() is needed for math)
    net = net + v # adds net and v and assigns the result to net
    off = off + abs(v) # adds the size of v (sign removed) to off

print("net:", net) # total variance with signs (overall over/short)
print("off:", off) # total units miscounted, ignoring sign

# PREDICTIONS:
# {'bin': 'A3-04', 'sku': 'SKU-1042', 'expected': '12', 'counted': '10', 'variance': '-2'}
# <class 'str'>
# net: -6
# off: 12

# QUESTIONS:
# TypeError since you can't add an integer to a string
# Shows the total mistakes happening 
# Adding to the second question: net can hide errors because overs and shorts cancel out. A net of -6 looks small, but 12 units were actually wrong. 
#                                An analyst uses `off` to judge count accuracy and decide which bins to recount, and uses `net` to see overall inventory 
#                                gain or loss.
