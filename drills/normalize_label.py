import re # loads the regex module

def normalize(line): # creates a function called normalize with the parameter line
    line = line.strip() # strip spaces off the start and end
    line = re.sub(r"\s+", " ", line) # replaces every run of whitespace with a single whitespace
    line = re.sub(r"\s*\|\s*", " | ", line)  # any spaces + pipe + any spaces becomes exactly " | "
    return line.upper() # uppercase line and return it

print(normalize("  sku-2210|qty:3 |   po-55013 ")) # prints result of normalize("  sku-2210|qty:3 |   po-55013 ")

# call normalize on "  sku-2210|qty:3 |   po-55013 " and print the result
# PREDICTION: SKU-2210 | QTY:3 | PO-55013
# after strip: "sku-2210|qty:3 | po-55013"          WRONG: KEEPS THE EXTRA TWO SPACES AFTER THE SECOND |
# after first re.sub: "sku-2210 | qty:3 | po-55013"        WRONG: NO SPACES WERE ADDED AROUND THE FIRST |
# after second re.sub: adds a space on each side of the | if there isnt already a space
# after upper: SKU-2210 | QTY:3 | PO-55013