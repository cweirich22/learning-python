import re # loads the regex module

pos = ["PO-55012", "PO-550123", "XPO-55013", "PO-5501", "po-55014"] # list of PO strings assigned to pos

po_check_1 = [] # empty list called po_check_1
po_check_2 = [] # empty list called po_check_2
po_check_3 = [] # empty list called po_check_3

pattern_po = r"PO-\d{5}" # regex pattern that will check the POs
pattern_po2 = r"\bPO-\d{5}\b" # regex pattern that will check the POs with \b anchors to the start and end

for po in pos:  # loops through each po in pos
    po1 = re.search(pattern_po, po) # result of search using patten_po on po
    po2 = re.search(pattern_po2, po) # result of search using patten_po2 on po
    po3 = re.fullmatch(pattern_po, po, flags=re.IGNORECASE) # result of fullmatch using patten_po on po including the IGNORECASE flag
    po_check_1.append(po1) # appends the po1 result into po_check_1
    po_check_2.append(po2) # appends the po2 result into po_check_2
    po_check_3.append(po3) # appends the po3 result into po_check_3
 
print(po_check_1) # prints the po_check_1 list
print(po_check_2) # prints the po_check_2 list
print(po_check_3) # prints the po_check_3 list

# Predict the table:
# <re.Match object; span=(0, 8), match='PO-55012'>, <re.Match object; span=(0, 8), match='PO-55012'>, <re.Match object; span=(1, 9), match='PO-55013'>, None, None
# <re.Match object; span=(0, 8), match='PO-55012'>, None, None, None, None
# PO-55012, None, None, None, PO-55014

# OUTPUT:
# [<re.Match object; span=(0, 8), match='PO-55012'>, <re.Match object; span=(0, 8), match='PO-55012'>, <re.Match object; span=(1, 9), match='PO-55013'>, None, None]
# [<re.Match object; span=(0, 8), match='PO-55012'>, None, None, None, None]
# [<re.Match object; span=(0, 8), match='PO-55012'>, None, None, None, <re.Match object; span=(0, 8), match='po-55014'>]