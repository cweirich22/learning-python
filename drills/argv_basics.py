# Used python drills/argv_basics.py SKU-1042 12 "BIN A-03" in the Terminal

import sys

# PREDICT: ['drills/argv_basics.py', 'SKU-1042', '12', 'BIN A-03']
print(sys.argv) 
# PREDICT: 4
print(len(sys.argv))
# PREDICT: 'SKU-1042'
print(sys.argv[1])
# PREDICT: string
print(type(sys.argv[2]))


# CORRECTIONS
# 1. correct
# 2. correct
# 3. SKU-1042 - there's no quotes since print shows a strings text and quotes only appear in a whole list.
# 4. <class 'str'> - right type but not the correct format
