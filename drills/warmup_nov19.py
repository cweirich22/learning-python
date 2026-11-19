import os # loads the os module
import re # loads the re module
import subprocess # loads the subprocess module
import sys # loads the sys module

# A. .groups() (missed 3 days in a row, so it's on Saturday's quiz)
m = re.search(r"BIN=(\S+) SKU=(\S+)", "CC BIN=A3-04 SKU=SKU-1042 EXPECTED=12") # searches a string with the pattern and stores the match object in m
print(m.groups()) # prints the two groups matched inside the string
print(type(m.groups())) # prints the type which is always a tuple
print(m.group(2)) # prints the second capture group
# PREDICT (3 lines):
# ('A3-04', 'SKU-1042')
# <class 'tuple'>
# SKU-1042

# B. env vars (assume DOCK_DOOR_LIMIT is NOT set on your machine)
print(os.environ.get("DOCK_DOOR_LIMIT")) # print the key
print(os.environ.get("DOCK_DOOR_LIMIT", "4")) # assigns a value to the key
# PREDICT (2 lines):
# None
# 4

# C. None vs "" and what makes a tuple
def parse(line): # creates a function called parse which has a parameter called line
    if "ERROR" not in line: # checks if ERROR is not in the string
        return None # if ERROR not in then return None
    return line.split()[-1] # if ERROR is in the string then split the line by whitespace and return the last item 
print(parse("SCN-01 INFO startup")) # prints the return of parse on a string
print(parse("SCN-02 ERROR NO_READ")) # prints the return of parse on a string
print(parse("") == "") # gets the return of parse(line) then checks if its equal to the other string
print(type((""))) # prints what type a string is
print(type(("", None))) # prints a tuple which has a string and None
# PREDICT (5 lines):
# None
# NO_READ
# None
# <class 'str'>
# None

# CORRECTIONS:
# line 3: False since the return is None but then compared to ""
# line 5: <class 'tuple'> since ("", None) is a tuple with the comma

# D. continue vs break. Count your print lines carefully.
for qty in [5, 0, 3, -1, 8]: # loops through each qty in the list
    if qty == 0: # checks if qty is equal to 0
        continue # if True then skip to the next qty in the list
    if qty < 0: # checks if qty is less than 0
        break # if true then break out of the loop
    print("ok", qty) # prints ok qty if the qty is greater than 0
print("done") # prints done after the loop is complete
# PREDICT (every line, in order). How many lines print in total?
# ok 5
# ok 3
# done
# total lines printed: 3. total lines printed from the loop: 2

# E. Does .get store anything?
counts = {"NO_READ": 2} # assigns a dictionary
print(counts.get("JAM", 0)) # uses get to get the value of JAM but JAM isn't in the dictionary
print(counts) # prints the dictionary
counts["JAM"] = counts.get("JAM", 0) + 1 # adds JAM to the dictionary with a starting value of 0 if its currently blank, then adds one to the value
print(counts) # prints the updated dictionary
# PREDICT (3 lines):
# 0
# {'NO_READ': 2, 'JAM': 0}
# {'NO_READ': 2, 'JAM': 1}

# CORRECTIONS:
# line 2: {"NO_READ": 2} sicne .get() doesn't store anything

# F. return vs print
def bad_count(lines): # creates a function called bad_count with a parameter called lines
    print(len(lines)) # prints the length of lines
x = bad_count(["A3-04", "B1-01"]) # calls bad_count with a list and stores the return
print(x) # prints x
# PREDICT (2 lines). In your own words, why is the second line what it is?
# 2
# None
# Second line is None since the value wasn't returned inside the bad_count function

# G. argv and exit codes
print(len(sys.argv)) # prints the length of the sys.argv which is the script plus all the arguments
print(sys.argv[1]) # prints the second postion of sys.argv
# PREDICT (2 lines):
# 3
# drills/cycle_counts.log
# Write what exit codes 0, 1, 2, and 3 mean in your CLIs:
# 0 = Success
# 1 = File doesn't exist
# 2 = Invalid usage 
# 3 = Has bad lines
# Without running it: what happens on the next line, and does "after" print?
# silently sends exit code 3 and yes after prints 
# CORRECTION: raises CalledProcessError (check=True turns exit 3 into an error), so the script crashes and "after" does NOT print
r = subprocess.run([sys.executable, "-c", "import sys; sys.exit(3)"], check=True) # the child exits 3 beacuse its code says sys.sxit(3), check=True turns the 3 into a CalledProcessError
print("after") # never runs, because the line above crashes the script