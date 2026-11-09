def is_valid_sku(text): # creates a function called is_valid_sku that takes in the text parameter
    if text[:4] == "SKU-" and len(text) == 8 and text[4:].isdigit(): # checks that the prefix is SKU-, the length is 8, and the ending contains only digits
        return True # returns True
    else: # If not True then 
        return False # returns False 

print(is_valid_sku("SKU-0042")) # Prints the results of running the string through is_valid_sku function
print(is_valid_sku("SKU-1234"))
print(is_valid_sku("sku-0042"))
print(is_valid_sku("SKU-99"))
print(is_valid_sku("SKU-12345"))
print(is_valid_sku("SKU-00A2"))
print(is_valid_sku("ABC-0042"))
print(is_valid_sku(""))