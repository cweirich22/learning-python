# run as: python drills/raise_example.py
def parse_qty(text): # creates a function called parse_qty with a parameter called text
    qty = int(text) # converts text to an integer and stores it in qty
    if qty < 0: # checks if qty is less than 0
        raise ValueError(f"negative qty: {qty}") # if True, raise a ValueError carrying this message (stops the function, no return)
    return qty # if False then return the qty

for raw in ["12", "-3", "ten"]: # loops through the list, putting each string in raw one at a time
    try: # try to run raw through parse_qty function
        q = parse_qty(raw) # q is equal to the return as long as no ValueError is raised
    except ValueError as e: # if a ValueError was raised in the try, catch it and store it in e
        print("rejected", raw, "->", e) # if ValueError is raised then print statement with raw and e
    else: # runs only if the try raised nothing
        print("accepted", q) # print string with q inside

# PREDICTIONS:
# accepted 12
# negative qty: -3
# rejected -3 -> negative qty: -3
# ValueError

# CORRECTION: only 3 lines print. raise doesn't print; the message only appears through print(e) in except
# line 2: This never prints as it sends the signal then prints later in the except ValueError as e:
# line 4: rejected ten -> invalid literal for int() with base 10: 'ten'