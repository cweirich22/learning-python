# run as: python drills/warmup_nov20.py drills/cycle_counts.log drills/cycle_report.csv
import re # loads the re module
import subprocess # loads the subprocess module
import sys # loads the sys module

# A. check=True (yesterday's miss, so it gets drilled until it sticks)
r = subprocess.run([sys.executable, "-c", "import sys; sys.exit(3)"]) # run Python and exit 3
print(r.returncode) # prints the return code for r
print("after 1") # prints the string
try: # try to run a child using Python with exit code 3 
    subprocess.run([sys.executable, "-c", "import sys; sys.exit(3)"], check=True) # run Python and exit code 3 then checks the exit code
    print("inside try") # this print line is skipped
except subprocess.CalledProcessError: # CalledProcessError was raised
    print("caught it") # prints the string as long as the except was valid
print("after 2") # prints the string
# PREDICT (every line, in order):
# 3
# after 1
# caught it
# after 2

# B. .groups() (missed 3 days running, and it's on tomorrow's quiz)
m = re.search(r"BIN=(\S+)", "CC BIN=A3-04 SKU=SKU-1042") # creates a regex pattern then searches the string for a match then assigns the result to m
print(m.groups()) # prints the whole matched text
print(m.group(0)) # prints the entire pattern
print(m.group(1)) # prints capture group 1
# PREDICT (3 lines). Look very closely at the first one.
# ('A3-04')
# 'A3-04'
# IndexError
# CORRECTIONS: 
# line 1: ('A3-04',) - has a comma since this is a tuple
# line 2: BIN=A3-04 - group 0 is the entire pattern
# line 3: A3-04 - this is the first capture group

# C. Does .get() store anything?
counts = {} # assigns an empty dictionary to counts
print(counts.get("SKU-1042", 0) + 5) # gets 0 as the default (key missing, nothing stored) and prints 0 + 5
print(counts)  # prints the empty dictionary called counts
counts["SKU-1042"] = counts.get("SKU-1042", 0) + 5 # creates the key then sets the value to 0 is empty and then adds 5
print(counts) # prints the counts dictionary
# PREDICT (3 lines):
# None
# None
# {'SKU-1042': 5}
# CORRECTIONS:
# line 1: 5 - doesn't add the key and value but still prints the value of the key
# line 2: {} - still prints the empty dictionary rather than None even if it's empty

# D. None vs "" and what makes a tuple
def first_bin(line): # creates a function called first_bin with a parameter called line
    if "BIN=" not in line: # checks if the string is not inside line
        return None # if True then return None
    return line.split("BIN=")[1].split()[0] # If False then split line by "BIN=" then split any whitespace in index 0
print(first_bin("INFO scanner online")) # run the first_bin function on the string
print(first_bin("") is None) # runs the first_bin function on the string the boolean if the return is None
print(first_bin("") == "") # boolean to check if the return from first_bin function on the string is equal to ""
print(type(("A3-04"))) # prints the type
print(type(("A3-04",))) # prints the type
# PREDICT (5 lines):
# None
# True
# False
# <class 'tuple'>
# Error from the comma
# CORRECTIONS:
# line 4: <class 'str'> - "A3-04" is a string and the () is not part of the type
# line 5: <class 'tuple'> - the comma is what makes it a tuple

# E. return vs print
def total_units(qtys): # creates a function called total_units with a parameter called qtys
    print(sum(qtys)) # prints the sum of qtys
    return len(qtys) # returns the length of qtys
x = total_units([5, 3, 4]) # assigns the total_units function with the qtys to x
print(x) # prints x
# PREDICT (2 lines). Which line came from print and which came from return?
# 12 - this is the print
# 3 - this is the return

# F. argv
print(len(sys.argv)) # prints the length of sys.argv
print(sys.argv[0]) # prints the script 
print(sys.argv[-1]) # prints the last arg
# PREDICT (3 lines):
# 3
# drills/warmup_nov20.py
# drills/cycle_report.csv

# G. Written, no code (a Nov 16 miss): before calling subprocess.run(..., env=env),
# why is env = os.environ.copy(); env["REORDER_POINT"] = "5" better than
# env={"REORDER_POINT": "5"}, and better than os.environ["REORDER_POINT"] = "5"?
# ANSWER: This sets the environment to the copy which is the child rather than setting it to the parent. 
# CORRECTION:
# 1. `env={"REORDER_POINT": "5"}` gives the child only that one variable. Everything else is gone, including `PATH`, 
#    `SYSTEMROOT` and your user folders, so on Windows the child often can't even start Python or find files. It's like 
#    handing a new worker a single sticky note instead of the whole procedures binder.
# 2. `os.environ["REORDER_POINT"] = "5"` changes the parent's own environment. The child gets it, but so does 
#    every later subprocess in your script, and your own script now has that setting too. It's a side effect you didn't 
#    intend, like rewriting the master binder for one task.
# 3. `env = os.environ.copy(); env["REORDER_POINT"] = "5"` makes a copy of everything the parent has, adds one setting to 
#    the copy only, and gives that copy to the child. The child has everything it needs plus your setting, and the parent 
#    stays unchanged.