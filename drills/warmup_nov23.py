# run as: python drills/warmup_nov23.py PO-55012 receiving.csv
import os # loads the os module
import re # loads the re module
import subprocess # loads the subprocess module
import sys # loads the sys module

print(sys.argv[1]) # first argument which is PO-55012
print(len(sys.argv)) # counts the total length of the sys.arg
# PO-55012
# 3

m = re.search(r"SKU=(\S+)", "RCV PO=55012 SKU=SKU-3301 QTY=6") # uses regex pattern to search through the string then assigns the result to m
print(m.groups()) # prints the groups as a tuple
print(m.group(0)) # prints the entire matched text
print(m.group(1)) # prints the first capture group
# ('SKU-3301')
# SKU=SKU-3301
# SKU-3301
# CORRECTIONS:
# line 1: ('SKU-3301',) - Every tuple has a comma after the first item

stock = {"SKU-3301": 6} # assigns a dictionary with a single key: value pair
print(stock.get("SKU-0000", 0)) # prints the value but doess't add it to stock dictionary
print("SKU-0000" in stock) # checks if the string is a key inside stock
# {'SKU-0000': 0}
# None
# CORRECTIONS
# line 1: 0 - only prints the value to the key
# line 2: False - in makes this a Boolean since it checks if the key is inside stock

print(sorted(["12", "9", "105"])) # prints a sorted list
print(max(["12", "9", "105"])) # prints the max string in a list, this is a trap if you don't account for these being strings rather than integers
# [105, 12, 9]
# 9
# CORRECTIONS:
# line 1: ['105', '12', '9'] - the list contains strings which printing the list keeps them as strings. print remove quotations only when printing the string type

def total_cases(cases): # creates a function called total_cases with a parameter called cases
    return sum(cases) # returns the sum of all cases

def show_cases(cases): # creates a function called show_cases with a parameter called cases
    print(sum(cases)) # prints the sum of cases

a = total_cases([2, 3]) # stores the return of total_cases function
b = show_cases([2, 3]) # prints the sum(cases) but stores None inside b
print(a) # runs the total_cases function then prints the return of the function
print(b) # runs the show_cases function then runs the print inside the function then prints None after since the results wasn't returned in the function
# 5
# 5
# None

env = os.environ.copy() # creates a copy of the parents environment variables
env["WAREHOUSE"] = "LAL-1" # creates a key in the env then assigns a value to it. If the key already exists then it just assigns the new value
print("WAREHOUSE" in os.environ) # doesn't exist as this WAREHOUSE was added to the child environment
print(env["WAREHOUSE"]) # prints the value of WAREHOUSE
# None
# LAL-1
# CORRECTIONS:
# line 1: False - in makes this a Boolean since it checks if the key is in os.environ

r = subprocess.run([sys.executable, "-c", "import sys; sys.exit(2)"]) # runs Python and imports sys then pushes sys.exit(2)
print(r.returncode) # prints the returncode which was set to 2
# 2

try:  # try the block below; if a CalledProcessError happens, jump to except
    subprocess.run([sys.executable, "-c", "raise ValueError('bad qty')"], check=True)  # start a child Python that raises ValueError; the child has no except, so it crashes with exit code 1 and its traceback prints to the terminal (stderr isn't captured); check=True sees the non-zero 1 and raises CalledProcessError in MY script
    print("ok")  # skipped, because the line above raised before Python got here
    # ok
except subprocess.CalledProcessError as e:  # catch the error check=True raised and name it e
    print("caught", e.returncode)  # print "caught" and the child's exit code, which is 1
    # Nothing since check=True was in the subprocess.run line
# CORRECTION:
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# ValueError: bad qty
# caught 1

# What does exit code 0, 1, 2, 3 mean in the CLIs?
# 0 - Success
# 1 - Missing input file - FileNotFound
# 2 - Invalid usage
# 3 - Has bad lines 
