import os  # gives us os.environ, the current environment variables
import re  # regex module
import subprocess  # lets Python run other programs
import sys  # gives us argv and sys.executable

env = os.environ.copy()  # make a separate copy of ALL current env vars
env["REORDER_POINT"] = "30"  # change only the copy
r = subprocess.run([sys.executable, "-c", "import os; print(os.environ.get('REORDER_POINT'), 'PATH' in os.environ)"],
                   env=env, capture_output=True, text=True)  # child gets the full copy; capture its output as text
print(r.stdout.strip())  # what the child printed
print(os.environ.get("REORDER_POINT"))  # what the PARENT sees
# PREDICT (2 lines):
# 30
# 10
# In your own words: why does env=env keep PATH, but env={"REORDER_POINT": "30"} doesn't?
# env=env means we will be using the copy which has the changed REORDER_POINT while not using the env PATH whille use the default which is 10.
# CORRECTIONS:
# Parent line prints None: REORDER_POINT was only set in the env COPY, never in the parent's os.environ.
# .get() with no default returns None when the variable doesn't exist (there's no "10" default here).
# env=env keeps PATH because os.environ.copy() copied EVERY variable (PATH too), then we changed one.
# env={"REORDER_POINT": "30"} replaces the child's whole environment with just that one variable, so PATH is gone.

print(len(sys.argv))  # how many items are in argv
print(sys.argv[0])  # argv index 0
print(sys.argv[-1])  # the last item in argv
# PREDICT (3 lines):
# 4
# drills/warmup_nov18.py
# extra.txt

m = re.search(r"(BIN-[A-Z]\d) qty=(\d+)", "move BIN-C4 qty=7 to dock 2")  # find a bin and a quantity
print(m.groups())  # all captured groups at once
print(type(m.groups()))  # what kind of object that is
print(type(m.group(2)))  # what kind of object ONE group is
print(int(m.group(2)) + 1)  # convert, then add 1
# PREDICT (4 lines, and watch the brackets on line 1):
# [('BIN-C4'), ('7')]
# <class 'list'> <class 'tuple'>
# <class 'str'>
# 8
# CORRECTIONS:
# line one: ('BIN-C4', '7') - put into a single tuple, not multiple inside a list
# line two: <class 'tuple'> - all inside one tuple so the class is a tuple

# Write what exit code 0, 1, 2, 3 meain the the CLIs
# 0 = Success
# 1 = File doesn't exist
# 2 = Incorrect number of arguments
# 3 = Contains bad lines
# What does #LASTEXITCODE show after running label_parser_cli.py with bad lines? 3

def total_units(qtys):  # function that's given a list of quantities
    return sum(qtys)  # hand back the total
    print("done")  # a line after the return
x = total_units([4, 6])  # call it and save what comes back
print(x)  # show what was saved
print(total_units([1]) + 1)  # use the return value in math
# PREDICT every line that prints. Does "done" ever print? Why?
# 10
# 10
# 2
# done never prints because it is after return which ends the loop
# CORRECTIONS:
# line one & two are combined which prints one 10
# done isn't in a loob so it doesn't print because return finishes the function

r = subprocess.run([sys.executable, "-c", "import sys; sys.exit(0)"], check=True)  # child exits 0, check is on
print("ok", r.returncode)  # only runs if nothing was raised
# PREDICT: ok 0