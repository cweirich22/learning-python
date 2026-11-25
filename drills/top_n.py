# run as: python drills/top_n.py
def top_n(counts, n): # creates a function called top_n with two parameters called counts and n
    if n < 0: # checks if n is less than 0
        raise ValueError(f"n must be 0 or more, got {n}") # if True then raise ValueError with f string: n
    ranked = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0])) # sort the items in counts based on the values negating the sign with tie breakers by the key with the order being smallest to greatest
    return ranked[:n] # returns a list first n tuples


if __name__ == "__main__": # only runs the indented code if the file is run directly
    picks = {"SKU-2210": 7, "SKU-1042": 12, "SKU-4410": 7, "SKU-3301": 3} # assigns a dictionary to picks
    print(top_n(picks, 2)) # prints the result of top_n with the two parameters
    print(top_n(picks, 3)) # prints the result of top_n with the two parameters
    print(top_n(picks, 10)) # prints the result of top_n with the two parameters
    print(top_n(picks, 0)) # prints the result of top_n with the two parameters

# PREDICT (all 4 printed lines):
# {'SKU-1042': 12, 'SKU-2210': 7}
# {'SKU-1042': 12, 'SKU-2210': 7, 'SKU-4410': 7}
# {'SKU-1042': 12, 'SKU-2210': 7, 'SKU-4410': 7, 'SKU-3301': 3}
# {'SKU-1042': 12}

# CORRECTIONS:
# When using items() this makes every pair from the dicitonary a tuple and puts them in a list. 
# [('SKU-1042', 12), ('SKU-2210', 7)]
# [('SKU-1042', 12), ('SKU-2210', 7), ('SKU-4410', 7)]
# [('SKU-1042', 12), ('SKU-2210', 7), ('SKU-4410', 7), ('SKU-3301', 3)]
# []
