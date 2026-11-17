import re # loads the regex module

lines = [ # creates a list of strings which include the date, time, door, scan and sku.
    "2026-11-17 08:01 DOOR-3 SCAN OK SKU-100",
    "2026-11-17 08:02 DOOR-1 SCAN OK SKU-200",
    "2026-11-17 08:03 DOOR-3 SCAN OK SKU-300",
    "2026-11-17 08:04 DOOR-2 HEARTBEAT",
    "2026-11-17 08:05 DOOR-3 SCAN OK SKU-100",
    "2026-11-17 08:06 DOOR-1 SCAN OK SKU-400",
]

SCAN_RE = re.compile(r"(DOOR-\d+) SCAN OK") # creates a regex pattern which is assigned to SCAN_RE

door_counts = {} # creates an empty dictionary 
for line in lines: # loops through each line in lines
    m = SCAN_RE.search(line) # searches each line using the regex pattern SCAN_RE
    if not m: # if m doesn't find a match in the line
        continue # if not m is True so skip over this loop
    door = m.group(1) # door is assigned to capture group 1
    door_counts[door] = door_counts.get(door, 0) + 1 # old count, or 0 if this key is new, plus 1

print(door_counts)
# PREDICT: {'DOOR-1': 2, 'DOOR-3': 3}
# CORRECTION: {'DOOR-3': 3, 'DOOR-1': 2}
# EXPLANATION: DOOR-3 comes first in lines so that is added to the dictionary first.

ranked = sorted(door_counts.items(), key=lambda kv: kv[1], reverse=True) # `turn the dict into (door, count) pairs, sort them by the count (kv[1]), biggest first, and get back a list of tuples`.
print(ranked) # print the sorted list of tuples
# PREDICT: {'DOOR-3': 3, 'DOOR-1': 2}
# CORRECTION: [('DOOR-3', 3), ('DOOR-1', 2)]
# EXPLANATION: .items() puts every pair into a tuple which are all inside a single list
print(ranked[0]) # print index 0 of ranked
# PREDICT: 2
# CORRECTION: ('DOOR-3', 3)
# EXPLANATION: Index position was correct considering what the expectation was for ranked. Instead the output is the entire tuple
print(type(ranked), type(ranked[0])) # `.items()` makes the pairs, `sorted()` *always* returns a list, and each item in the list is one of those pair tuples.
# PREDICT: <class 'dict'> <class 'int'>
# CORRECTION: <class 'list'> <class 'tuple'>
# EXPLANATION: ranked was put into a list with .items() and when calling a specific index it calls on the tuple itself

