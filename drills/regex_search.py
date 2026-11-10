import re # loads Python's regular expression module

note = "Order PO-7781 arrived late" # assigns a string to note
regex = r"PO-\d+" # pattern: "PO-" followed by one or more digits (raw string so \d stays as-is)
match = re.search(regex, note) # finds the first match of the pattern in note; gives a match object or None
print(match) # shows the match object, including its span and matched text
print(match.group()) # prints only the characters from match
regex2 = r"PO-\d{5}" # pattern: "PO-" followed by exactly 5 digits
match2 = re.search(regex2, note) # assigns the result of searching for regex2 in note

if match2: # True if the search found a match; None counts as False
    print(match2.group()) # prints the matched PO text
else: # runs when match2 is None (no 5-digit PO)
    print("No 5-digit PO found") # if match2 has None then this prints