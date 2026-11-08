def is_low(qty, threshold=10): # creates a function called is_low that takes in two variables: qty and threshold=10. Threshold can be changed manually.
    return qty < threshold # returns True or False depending on if qty < threshold

quantities = [4, 18, 9, 30] # list of numbers stored inside quantities
results = [] # empty list stored inside results
for qty in quantities: # loops through all the quantities in the list
    results.append(is_low(qty)) # appends the return of is_low by using a qty in quantities
print(results) # prints the results list