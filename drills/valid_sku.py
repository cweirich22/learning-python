def is_valid_sku(text): # creates a function called is_valid_sku that takes in the text parameter
    text = text.strip() # strips the whitespace from the start and end
    return text[:4] == "SKU-" and len(text) == 8 and text[4:8].isdigit() # checks that the prefix is SKU-, the length is equal to 8, and the ending contains only digits        

if __name__ == "__main__":
    # Moved these print statements into the if statement so these are only run when this files code is ran. Importing this file will not run this code meaning we can just run is_valid_sku
    print(is_valid_sku("SKU-0042")) # True - Prints the results of running the string through is_valid_sku function
    print(is_valid_sku("SKU-1234")) # True
    print(is_valid_sku("sku-0042")) # False
    print(is_valid_sku("SKU-99")) # False
    print(is_valid_sku("SKU-12345")) # False
    print(is_valid_sku("SKU-00A2")) # False
    print(is_valid_sku("ABC-0042")) # False
    print(is_valid_sku("")) # False
    print(is_valid_sku(" SKU-0042 \n")) # True