import re # loads the regex module

pos = ["PO-55012", "PO-5501", "po-55013", "PO-550160", " PO-55014"] # list of pos
regex = r"PO-\d{5}" # regex pattern that starts PO- then 5 digits
for po in pos: # loops through each po in pos
    po = po.strip().upper() # strips the whitespace at the start and end then puts the word characters in uppercase
    print(po, bool(re.fullmatch(regex, po))) # boolean True/False if there is a fullmatch between the regex and po
    # PRECTIONS:
    # PO-55012 True
    # PO-5501 False
    # PO-55013 True
    # PO-550160 False
    # PO-55014 True

print(re.search(r"PO-\d{5}", "PO-550160")) # searches through the string starting with PO- then 5 digits, only needs part of the string to match
# PREDICTION: will show the Object and will show the indexing (0,8) PO-55016
print(re.fullmatch(r"PO-\d{5}", "PO-550160")) # searches for a fullmatch in the string with PO- and exactly 5 digits, fullmatch means the entire string must match
# PREDICTION: None
print(re.fullmatch(r"PO-\d{5}", "PO-55016")) # searches for a fullmatch in the string with PO- and exactly 5 digits, fullmatch means the entire string must match
# PREDICTION: PO-55016
print(bool(re.fullmatch(r"PO-\d{5}", "PO-55016"))) # boolean True/False if there is a fullmatch from the regex pattern to the string
# PREDICTION: True