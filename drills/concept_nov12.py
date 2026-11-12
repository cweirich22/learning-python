import re # loads the regex module
pattern = r"(PO-\d{5})" # regex pattern that has PO- followed by 5 digits
print(re.search(pattern, "PO-550123"))
# PREDICT: PO-55012
print(re.search(pattern + r"\b", "PO-550123"))
# PREDICT: PO-550123 
print(re.fullmatch(pattern, "PO-550123"))
# PREDICT: None
print(re.fullmatch(pattern, "  PO-55012 ".strip()))
# PREDICT: PO-55012
print(re.sub("qty", "QTY", "qty 3 Qty 4 qTy 5", re.IGNORECASE))
# PREDICT: QTY 3 Qty 4 qTy 5
print(re.sub("qty", "QTY", "qty 3 Qty 4 qTy 5", flags=re.IGNORECASE))
# PREDICT: QTY 3 QTY 4 QTY 5

# GRADING:
# Only one incorrect is the print(re.search(pattern + r"\b", "PO-550123")) while is None. \b asks if the next character is not a letter, digit, or underscore which 3 is.
# the first print is correct but missing some: <re.Match object; span=(0, 8), match='PO-55012'>. My predicted text was the .group() of that object.