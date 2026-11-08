def is_low(qty, threshold=10): # creates a functiion called is_low and has two variables: qty and threshold=10. Threshold will be equal to 10 unless the manually changed in the print statement
    if qty < threshold: # checks if qty is less than threshold
        return True # returns True if True
    else: # else for the other outcome
        return False # if False then returns False

print(is_low(50)) # prints the return from is_low function with a qty set to 50.
print(is_low(5)) # prints the return from is_low function with a qty set to 5.
print(is_low(15, 20)) # prints the return from is_low function with a qty set to 15 and threshold set to 20.
