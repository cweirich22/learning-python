# How many ERROR lines are there in total?
# 8
# Count per error type (JAM, NO_READ, TIMEOUT...)
# JAM: 3, NO_READ: 3, TIMEOUT: 2
# Count per scanner (SCN-01, SCN-02, SCN-03), errors only
# SCN-01: 3, SCN-02: 3, SCN-03: 2
# Which 3 lines get skipped as "not an error," and why? Watch the WARN line.
# lines 1, 7, and 13 as these are all info 
# CORRECTION: lines 1, 4, 7, 11, and 13


import re # loads the regex module

ERROR_RE = re.compile(r"(SCN-\d+) ERROR (\w+)") # creates a regex pattern which is assigned to ERROR_RE
scanner_counts = {} # creates an empty dictionary
desc_counts = {} # creates an empty dictionary
with open("drills/scanner.log", "r") as f: # opens drills/scanner.log in read mode as f
    for line in f: # loops through each line in f
        m = ERROR_RE.search(line) # uses ERROR_RE regex to search through line
        if not m: # if m doesn't find a match in the line
            continue # if not m is True so skip over this loop
        scanner = m.group(1) # scanner is assigned to capture m group 1
        scanner_counts[scanner] = scanner_counts.get(scanner, 0) + 1 # old count, or 0 if this key is new, plus 1
        # print(f"{scanner}: {scanner_counts}") # prints f string with scanner and scanner_counts
        desc = m.group(2) # desc is assigned to m capture group 2
        desc_counts[desc] = desc_counts.get(desc, 0) + 1 # old count, or 0 if this key is new, plus 1
        # print(f"{desc}: {desc_counts}") # prints f string with desc and desc_counts

# PREDICT PRINT IN LOOP (CHANGED THESE LINES TO COMMENTS)
# SCN-02: 1
# NO_READ: 1
# SCN-01: 1
# JAM: 1
# SCN-02: 2
# NO_READ: 2
# SCN-03: 1
# TIMEOUT: 1
# SCN-01: 2
# JAM: 2
# SCN-02: 3
# NO_READ: 3
# SCN-03: 2
# JAM: 3
# SCN-01: 3
# TIMEOUT: 2

# CORRECTION:
# SCN-02: {'SCN-02': 1}
# NO_READ: {'NO_READ': 1}
# SCN-01: {'SCN-02': 1, 'SCN-01': 1}
# # JAM: {'NO_READ': 1, 'JAM': 1}
# # SCN-02: {'SCN-02': 2, 'SCN-01': 1}
# NO_READ: {'NO_READ': 2, 'JAM': 1}
# SCN-03: {'SCN-02': 2, 'SCN-01': 1, 'SCN-03': 1}
# TIMEOUT: {'NO_READ': 2, 'JAM': 1, 'TIMEOUT': 1}
# SCN-01: {'SCN-02': 2, 'SCN-01': 2, 'SCN-03': 1}
# JAM: {'NO_READ': 2, 'JAM': 2, 'TIMEOUT': 1}
# SCN-02: {'SCN-02': 3, 'SCN-01': 2, 'SCN-03': 1}
# NO_READ: {'NO_READ': 3, 'JAM': 2, 'TIMEOUT': 1}
# SCN-03: {'SCN-02': 3, 'SCN-01': 2, 'SCN-03': 2}
# JAM: {'NO_READ': 3, 'JAM': 3, 'TIMEOUT': 1}
# SCN-01: {'SCN-02': 3, 'SCN-01': 3, 'SCN-03': 2}
# TIMEOUT: {'NO_READ': 3, 'JAM': 3, 'TIMEOUT': 2}

print(scanner_counts, desc_counts) # prints the two dictionaries scanner_counts and desc_counts
# PREDICT: {'SCN-02': 3, 'SCN-01': 3, 'SCN-03': 2} {'NO_READ': 3, 'JAM': 3, 'TIMEOUT': 2}

ranked_scanners = sorted(scanner_counts.items(), key=lambda kv: kv[1], reverse=True) # `turn the dict into (scanner, count) pairs, sort them by the count (kv[1]), biggest first, and get back a list of tuples`.
ranked_desc = sorted(desc_counts.items(), key=lambda kv: kv[1], reverse=True) # `turn the dict into (desc, count) pairs, sort them by the count (kv[1]), biggest first, and get back a list of tuples`.
print(ranked_scanners, ranked_desc) # prints the ranked_scanners and ranked_desc as sorted list of tuples
# PREDICT: [('SCN-02': 3), ('SCN-01': 3), ('SCN-03': 2)] [('NO_READ': 3), ('JAM': 3), ('TIMEOUT': 2)]
# CORRECTION: [('SCN-02', 3), ('SCN-01', 3), ('SCN-03', 2)] [('NO_READ', 3), ('JAM', 3), ('TIMEOUT', 2)]
print(ranked_scanners[0], ranked_desc[0]) # print the index 0 on both raned_scanners and ranked_desc
# PREDICT: ('SCN-02': 3) ('NO_READ': 3)
# CORRECTION: ('SCN-02', 3) ('NO_READ', 3)
print(type(ranked_scanners), type(ranked_scanners[0]), type(ranked_desc), type(ranked_desc[0])) # `.items()` makes the pairs, `sorted()` *always* returns a list, and each item in the list is one of those pair tuples.
# PREDICT: <class 'list'> <class 'tuple'> <class 'list'> <class 'tuple'>
 
for name, count in ranked_scanners: # loops through the name and count in ranked_scanners
    print(f"{name}: {count}") # prints f string of name and count for each instance in the for loop
# PREDICTION:
# SCN-02: 3
# SCN-01: 3
# SCN-03: 2

for name, count in ranked_desc: # loops through the name and count in ranked_desc
    print(f"{name}: {count}") # prints f string of name and count for each instance in the for loop
# PREDICTION:
# NO_READ: 3
# JAM: 3
# TIMEOUT: 2
