# run as: python drills/sort_keys.py
bins = [("B1-01", 3), ("A3-04", -2), ("C2-07", -7), ("A1-01", 3), ("A3-05", 0)]
print(sorted(bins)) # prints bins sorted starting with the first item and if theres a match between two first items then it sorts through the second item
print(sorted(bins, key=lambda b: b[1])) # prints bins sorted from smallest to largest based on the second item.ties keep original order
print(sorted(bins, key=lambda b: b[1], reverse=True)) # prints sorted bins from largest to smallest based on the second item. tie is left to the original order
print(sorted(bins, key=lambda b: (-abs(b[1]), b[0]))) # sorts by biggest miss first (size of the second item, sign ignored); ties broken by the first item A-Z 
print(sorted(bins, key=lambda b: abs(b[1]), reverse=True)) # prints bins sorted from largest to smallest based on second item. ties is left to the original order
print(bins) # prints the bins list

# PREDICTIONS:
# ('A1-01', 3), ('A3-04', -2), ('A3-05', 0), ('B1-01', 3), ('C2-07', -7)
# ('C2-07', -7), ('A3-04', -2), ('A3-05', 0), ('B1-01', 3), ('A1-01', 3)
# ('A1-01', 3), ('B1-01', 3), ('A3-05', 0), ('A3-04', -2), ('C2-07', -7)
# (0, 'A3-05'), (-2, 'A3-04'), (-3, 'A1-01'), (-3, 'B1-01'), (-7, 'C2-07')
# (3, 'B1-01'), (3, 'A1-01'), (0, 'A3-05'), (-2, 'A3-04'), (-7, 'C2-07')
# ('B1-01', 3), ('A3-04', -2), ('C2-07', -7), ('A1-01', 3), ('A3-05', 0)

# CORRECTIONS
# [('A1-01', 3), ('A3-04', -2), ('A3-05', 0), ('B1-01', 3), ('C2-07', -7)]
# [('C2-07', -7), ('A3-04', -2), ('A3-05', 0), ('B1-01', 3), ('A1-01', 3)]
# [('B1-01', 3), ('A1-01', 3), ('A3-05', 0), ('A3-04', -2), ('C2-07', -7)]
# [('C2-07', -7), ('A1-01', 3), ('B1-01', 3), ('A3-04', -2), ('A3-05', 0)]
# [('C2-07', -7), ('B1-01', 3), ('A1-01', 3), ('A3-04', -2), ('A3-05', 0)]
# [('B1-01', 3), ('A3-04', -2), ('C2-07', -7), ('A1-01', 3), ('A3-05', 0)]

# All lines are missing the list []. 
# Line 3 had incorrect order for A1-01 and B1-01 since they have the same item 2, they sort based on which comes first in the bins list.
# Lines 4 and 5 has the unchanged order of the tuple.
# Lines 4 and 5 differ on the tie: line 4's key includes the bin name, so A1-01 comes first; line 5's key is only the size, so the stable sort keeps B1-01 first

