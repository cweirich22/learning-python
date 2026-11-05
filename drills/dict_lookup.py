bins = {"A1": "SKU-100", "B1": "SKU-200", "C1": "SKU-300", "D1": "SKU-400"} # dictionary with four keys and four values

print(bins["C1"]) # prints the SKU as long as there is a macthing key to C1
print(bins.get("E1", "EMPTY")) # checks if E1 exists as a key in the bins dictionary, if not then EMPTY is printed
#print(bins["E1"]) # purposely raises a KeyError