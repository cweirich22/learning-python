import subprocess   # lets Python start other programs
import sys          # sys.executable = the full path to the Python running this file
import os           

env = os.environ.copy() # makes a copy of this script's env-var dictionary
env["REORDER_POINT"] = "15" # sets REORDER_POINT in the copy only
child = subprocess.run([sys.executable, "-c", "import os; print(os.environ.get('REORDER_POINT'))"], capture_output=True, text=True, env=env) # start a child programand run this string using Python, save the output of the program, remove b prefix, and hands the copy to the child
print(repr(child.stdout)) #  shows what the child printed, with quotes and hidden characters
print(os.environ.get("REORDER_POINT")) # reads REORDER_POINT from the parent's own, unchanged dictionary

result = subprocess.run(                  # start a child program, wait for it to finish, save the receipt
    [sys.executable, "-c", "print('SKU-1042')"],   # the command as a list: this Python, run this code string
    capture_output=True,                  # keep what the child prints instead of showing it on screen
    text=True,                            # give the output back as a string, not bytes
)
print(result.returncode)      # the child's exit code
print(repr(result.stdout))    # what the child printed normally, repr shows quotes and hidden characters

result2 = subprocess.run([sys.executable, "-c", "import sys; sys.exit(3)"]) # start a child program and run this string using Python
print(result2.returncode) # the childs exit code

try:
    subprocess.run([sys.executable, "-c", "import sys; sys.exit(3)"], check=True) # raise CalledProcessError if the child exits with anything but 0
    print("child succeeded") # prints if there was no error
except subprocess.CalledProcessError as e: # catch that error and store the error object in e
    print("child failed with code", e.returncode) # prints a string with the returncode for e

try: # try this
    subprocess.run(["dir"]) # dir is built into cmd, not a real program file, so Windows can't find it
except FileNotFoundError: # if dir is not found
    print("dir is not a real program on Windows") # print statement if FileNotFoundError


# PREDICTIONS
# line 8: '15\n'
# line 9: None
# line 16: 0
# line 17: 'SKU-1042\n'
# line 20: 3
# line 24/26: child failed with code 3
# line 28-31: dir is not a real program on Windows

# NOTES
# Without `check=True`: the child exits with 3, and `subprocess.run` just hands you a receipt with `returncode` 3. Your script carries on as if nothing happened.
# With `check=True`: Python looks at the exit code. If it's anything other than 0, it raises `subprocess.CalledProcessError` right there, the same way a bad label raises `ValueError` in your parser.