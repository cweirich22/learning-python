import re #loads the regex module

note = "Pull from A12-3, then F07-1, skip G02-4, finish at C99-2" # strings with different bins
pattern = r"([A-F]\d{2})-(\d)" # regex pattern that looks for a uppercase letter A-F then two digits a dash and then one digit. group 1 is the aisle and group 2 is the slot

bins = re.findall(pattern, note) # findall with parameters pattern and note creates a list of tuples that are assigned to bins
for aisle, slot in bins: # loops through the aisle and slot pair inside bins
    print(f"Aisle {aisle}, slot {slot}") # f string with the aisle and slot

print(bins) # prints the list of tuples

# prediction: (['A12', '3'], ['F07', '1'], ['C99', '2']) 
# correction: parentheses and brackets are flipped. findall always returns a list on the outside, written with []. Each match inside is a tuple, written with ().