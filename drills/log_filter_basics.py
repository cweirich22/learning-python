import re

lines = [ # creates a list of strings which include the date, time, door, scan and sku.
    "2026-11-17 08:01 DOOR-3 SCAN OK SKU-100",
    "2026-11-17 08:02 DOOR-1 SCAN OK SKU-200",
    "2026-11-17 08:03 DOOR-3 SCAN OK SKU-300",
    "2026-11-17 08:04 DOOR-2 HEARTBEAT",
    "2026-11-17 08:05 DOOR-3 SCAN OK SKU-100",
    "2026-11-17 08:06 DOOR-1 SCAN OK SKU-400",
]

SCAN_RE = re.compile(r"(DOOR-\d+) SCAN OK") # creates a regex patter which is assigned to SCAN_RE

door_counts = {} # creates an empty dictionary 
for line in lines: # loops through each line in lines
    m = SCAN_RE.search(line) # searches each line using the regex pattern SCAN_RE
    if not m: # if m doesn't find a match in the line
        continue # moves on when theres no match
    door = m.group(1) # door is assigned to index 1 in m
    door_counts[door] = door_counts.get(door, 0) + 1 # sets the initial count to 0 for each door then adds one each time it appears

print(door_counts)
# PREDICT: {'DOOR-1': 2, 'DOOR-3': 3}

ranked = sorted(door_counts.items(), key=lambda kv: kv[1], reverse=True) # need help with this comment
print(ranked) # print the sorted dictionary called ranked
# PREDICT: {'DOOR-3': 3, 'DOOR-1': 2}
print(ranked[0]) # print index 0 of ranked
# PREDICT: 2
print(type(ranked), type(ranked[0])) # print the ranked type along with ranked type index 0
# PREDICT: <class 'dict'> <class 'int'>


