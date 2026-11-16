import os, subprocess, sys # loads os, subprocess, and sys modules

folder = os.path.dirname(os.path.abspath(__file__)) # grabs the directory name from the absolute file path of a file
SCRIPT = os.path.join(folder, "label_parser_cli.py") # creates a filepath by joining the folder directory with label_parser_cli.py
out_csv = os.path.join(folder, "out_check.csv") # builds a path string that points to out_check.csv in the drills folder

cases = [               # creates a list with tuples inside.
    ("no args", [], 2),
    ("missing file", [os.path.join(folder, "nope.txt"), out_csv], 1),
    ("messy file", [os.path.join(folder, "labels_messy.txt"), out_csv], 3),
    ("clean file", [os.path.join(folder, "labels_clean.txt"), out_csv], 0),
]

passed = 0 # sets the value of passed to 0

for desc, args, expected in cases: # loops through each desc, arrgs, expected pair in cases
    r = subprocess.run([sys.executable, SCRIPT, *args], capture_output=True, text=True) # uses Python to run the SCRIPT file and unpacks the list. The output is saved and the B prefix is removed
    if r.returncode == expected: # checks if the returncode for r is equal to expected
        print(f"PASS  {desc}: expected {expected}, got {r.returncode}") # f string with desc, expected, and r.returncode
        passed += 1 # adds 1 to passed running total
    else: # if r.returncode is not equal to expected
        print(f"FAIL  {desc}: expected {expected}, got {r.returncode}") # f string with desc, expected, and r.returncode

print(f"{passed}/{len(cases)} passed") # f string with passed and the length of cases

if passed != len(cases): # checks if passed total doesn't equal the length of cases
    sys.exit(1) # push exit code 1

# from the looks of it, each tuple has a string explaining the tuple, then the file with the path, then the exit code (returncode)

# TEST PRINTS
# print(len(cases)) # total number of tuples in the list
# print(cases[0]) # index 0 of cases

# PREDICTIONS
# line 29: 4
# line 30: ("no args", [], 2)
# PASS  no args: expected 2, got 2
# PASS  missing file: expected 1, got 1
# PASS  messy file: expected 3, got 3
# PASS  clean file: expected 0, got 0
# 4/4 passed

# CORRECTIONS
# line 17: ('no args', [], 2) - Python always shows strings inside a tuple or list with **single quotes**