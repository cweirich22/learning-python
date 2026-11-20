# run as: python drills/raise_basics.py
def check_bin(code): # creates a function called check_bin with a parameter called code
    if len(code) != 5: # checks if the length of code doesn't equal 5
        raise ValueError(f"bad bin length: {code}") # if True, raise a ValueError containing this message (stops the function and no return)
    return code.upper() # returns code with all letters in uppercase

def receive(po_qty, got): # creates a function called receive with two parameters called po_qty, got
    if got > po_qty: # checks if got is greater than po_qty
        raise ValueError(f"over-receipt: got {got}, PO says {po_qty}") # if True, raise a ValueError contianing this message (stops the function and no return)
    return po_qty - got # returns the value of po_qty minus got

print(check_bin("a3-04")) # prints the return of check_bin
try: # try to get a return from check_bin with the string and if there is a return then print the next string
    print(check_bin("A3-4")) # print the return of check_bin with the string if there is one
    print("after check_bin") # if there was a return then print this string
except ValueError as e: # if a ValueError was raised in the try, catch it and store it in e
    print("caught:", e) # prints a string with e which contains the message tied to ValueError in check_bin function
print(receive(10, 7)) # prints the return of the receive function as long as no ValueError is raised
try: # try to run the receive function with two values, if returned then store the return inside left, if ValueError then move to except
    left = receive(10, 12) # stores the return of receive function as long as no ValueError
except ValueError as e: # if a ValueError was raised in the try, catch it and store it in e
    print("caught:", e) # prints a string with e which contains the message tied to ValueError in receive function
else: # if no ValueError then left has the return of receive so print 
    print("left:", left) # prints string with left
try: # try to convert a string to an integer
    int("12.5") # tries to convert "12.5" to an integer (fails: not a whole number)
except ValueError: # if ValueError then print
    print("not a whole number") # print this if ValueError
print("done") # prints the string once complete
print(receive(5, 9)) # 9 > 5, so receive raises ValueError; there's no try, so the script crashes here
print("never?") # prints the string as the last line
# PREDICT (every line, in order, plus what happens on the last two lines):
# A3-04
# caught: bad bin length: A3-4
# 3
# caught: over-receipt: got 12, PO says 10
# not a whole number
# done
# ValueError - raises ValueError without the message then crashed the script
# Doesn't print

# CORRECTION:
# line 6: ValueError: over-receipt: got 9, PO says 5 - this also includes the traceback to stderr which is sent first. the message always travels with the exception

# PREDICT $LASTEXITCODE, and why:
# no idea what the exit code would be since this was an unsucceful run but doesn't match the 0-3 exit code we have used previously
# CORRECTION: 
# `$LASTEXITCODE` is 1. This was in yesterday's lesson: when an exception isn't caught, Python always exits with code 1. The 0–3 codes in your CLIs are ones you 
# chose and set with `sys.exit()`. A crash isn't your code choosing; it's Python's default.