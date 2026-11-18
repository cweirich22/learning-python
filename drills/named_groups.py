import re  # regex module

CC_RE = re.compile(r"BIN=(?P<bin>[A-Z]\d-\d{2}) SKU=(?P<sku>SKU-\d{4}) COUNTED=(?P<counted>\d+)")  # creates regex pattern with three group with them named in order: bin, sku, counted
m = CC_RE.search("08:01:12 CC BIN=A3-04 SKU=SKU-1042 COUNTED=10")  # runs the regex pattern on the string 

print(m.group("bin"))  # prints the the first capture group
print(m.group(2))  # prints the second capture group
print(m.groups())  # prints every capture group
print(m.groupdict())  # prints a dictionary with the names as the keys and the text as the values
print(m.groupdict()["counted"] * 2)  # prints the dictionary with every key value pair and changes the counted string to 1010
print(CC_RE.search("08:03:55 CC BIN=A3-05 SKU=2210 COUNTED=40"))  # prints the entire string as long as theres a match with the search

# PREDICTIONS:
# A3-04
# SKU-1042
# ('A3-04', 'SKU-1042', '10')
# {'bin': 'A3-04', 'sku': 'SKU-1042', 'counted': '10'}
# {'counted': '1010'}
# BIN=A3-05 SKU=SKU-2210 COUNTED=40

# CORRECTIONS:
# block 5: print shows only the result of the value multiplied by two as a plain string so no dictionary or quotes
#          answer: 1010
# fix block 5 so it prints 20:
print(int(m.groupdict()["counted"]) * 2) # pulls the value from counted key then converts to an integer before multiplying it by 2
# block 6: SKU was missing SKU- so it wasn't a match. Even with a match the answer would be wrong, see in example below.
#          answer: None
# fix block 6 so it shows a Match:
print(CC_RE.search("08:03:55 CC BIN=A3-05 SKU=SKU-2210 COUNTED=40")) # searched through the string to check for a regex match
# answer for a match: <re.Match object; span=(12, 45), match='BIN=A3-05 SKU=SKU-2210 COUNTED=40'>