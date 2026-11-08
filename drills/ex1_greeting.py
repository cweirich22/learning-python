

def bin_label(aisle, shelf): # creates a function called bin_label which takes in two variables: aisle and shelf
    return f"{aisle}-{shelf:02}" # returns the f string which includes both the aisle and shelf along with the correct formatting to include the 0 for single digit shelves

print(bin_label("A", 3)) # uses bin_label function and prints what it returns
print(bin_label("B", 12)) # uses bin_label function and prints what it returns