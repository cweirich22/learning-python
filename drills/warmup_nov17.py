import subprocess  # lets Python run other programs
import sys  # gives us sys.executable, the path to the Python that's running
import os  # gives us os.environ
import re  # regex module

# A. check=True (yesterday's miss)
r = subprocess.run([sys.executable, "-c", "import sys; sys.exit(3)"])  # run a tiny child program that exits with code 3
print(r.returncode)  # show the child's exit code
# PREDICT: 3
# check=True turns a nonzero exit into a `CalledProcessError`, and without it the code just sits in `.returncode`

try:  # try the risky part
    subprocess.run([sys.executable, "-c", "import sys; sys.exit(3)"], check=True)  # same child, but check=True this time
    print("finished fine")  # only runs if nothing was raised
except subprocess.CalledProcessError as e:  # catch the error that check=True can raise
    print("caught", e.returncode)  # show the code stored on the error
# PREDICT: caught 3

# B. env copy (yesterday's miss)
env = os.environ.copy()  # make a separate copy of all current env vars
env["REORDER_POINT"] = "25"  # change only the copy
r = subprocess.run([sys.executable, "-c", "import os; print(os.environ.get('REORDER_POINT'), 'PATH' in os.environ)"],
                   env=env, capture_output=True, text=True)  # child gets the copy; capture its output as text
print(r.stdout.strip())  # what the child printed
print(os.environ.get("REORDER_POINT"))  # what the PARENT sees
# PREDICT both lines: '25' and '25'
# WRONG both lines: 25 True has no quotes and the path is in os.environ so its True. REORDER_POINT outside the child is None so the answer is None.
# Changing the copy leaves the parent's environment alone.
# `env={...}` throws away PATH and every other variable, and on Windows that can break the child.

# C. return vs print
def count_bad(lines):  # function that's given a list of lines
    print(len(lines))  # shows the length on screen
result = count_bad(["SKU-77", "no label"])  # call it and save what it hands back
print(result)  # show what was saved
# PREDICT both lines: 2 None
# Correct values predicted but they were put on the same line so wrong. First line it prints the prent in the function. Then a new line for printing the result.

# D. argv. Run `python drills/warmup_nov17.py receiving.txt out.csv` with the following lines at the bottom:
print(sys.argv[1])  # show argv index 1
print(len(sys.argv))  # how many items are in argv
# PREDICT: line one: receiving.txt line two: 2
# Corrections: line two is 3. There is index 0-2 which means the length is 3
# output: line two: 3

# E. Exit codes from memory
# Write what exit codes 0, 1, 2, and 3 mean
# 0 - Passed
# 1 - FileNotFoundError
# 2 - Incorrect Usage
# 3 - Forgot
# Corrections: 
# 3 - bad lines isn't empty


# F. .groups()
m = re.search(r"(SKU-\d{4}) x(\d+)", "pick SKU-1042 x12 bin A3")  # find a SKU and a quantity
print(m.groups())  # all captured groups at once
print(type(m.groups()))  # what kind of object that is
print(m.group(2) + 1)  # try to add 1 to the quantity
# PREDICT all three (one of them is a trap):
# ['SKU-1042', '12']
# <class 'str'>
# Can't add an integer to a string so incorrect type usage
# Corrections:
# 1 is a tuple so they use parentheses: ('SKU-1042', '12')
# 2 - <class 'tuple'> Every `.group(n)` is a string, but `.groups()` is a tuple of strings.
