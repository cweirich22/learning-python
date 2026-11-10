import re # loads Python's regex module

note = "Pallets: 12, 40, 7 damaged: 2" # assigns a string to note

pallet_text = re.search(r"Pallets: (.+) damaged", note).group(1) # captures the text between "Pallets: " and " damaged" (the pallet numbers as one string)
damaged_text = re.search(r"damaged: (\d+)", note).group(1) # captures the digits after "damaged: " as a string
pallets = re.findall(r"\d+", pallet_text) # separates all the digits in the pallet_text string and puts them into a list called pallets
damaged = int(damaged_text) # result of converting damaged_text into an integer

pallet_counts = [int(p) for p in pallets] # loops through each string in pallets and converts the string into an integer and assigns the list to pallet_counts
record = {"pallets": pallet_counts, "damaged": damaged} # dictionary that has a pallet key with pallet_counts as values and a damaged key with damaged as the value

print(record) # prints the record dictionary
print(sum(record['pallets'])) # takes the 'pallets' key and totals all the values then prints it


