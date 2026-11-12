import re

# 1 return vs print
def total(a, b):
    print(a + b)
x = total(2, 3)
print(x)

# 2 list vs tuple
pallet = ("SKU-1042", 12)
pallet[1] = 13   
# PREDICT: pallet[1] will change the value from 12 to 13


# 3 backreferences
print(re.sub(r"(\d+)-(\d+)", r"\2-\1", "BIN 12-07"))
# PREDICT: prints BIN 07-12

# 4 lazy vs greedy
line = "SKU-12 | QTY 3 | PO-55013"
print(re.search(r"SKU-.+?\|", line).group())
# PREDICT: prints ('SKU-12 |')
print(re.search(r"SKU-.+\|", line).group())
# PREDICT: None as there is whitespace between the 12 and | which isn't in the regex pattern

# 5 \b word boundary
print(re.findall(r"\b\d{3}\b", "bin 101 1022 33 404"))
# PREDICT: 101 404

# 6 .groups() type
m = re.search(r"(\w+)-(\d+)", "PO-55013")
print(m.groups(), type(m.groups()))
# PREDICT: (('PO','55013'),(Object, Object))

# 7 strings are immutable
sku = "sku-1042"
sku.upper()
print(sku)
# PREDICT: sku-1042
sku = sku.upper()
print(sku)
# PREDICT: SKU-1042

# 8 dict lookups
stock = {"SKU-1042": 12}
print(stock.get("SKU-9999", 0))
# PREDICT: None
print(stock["SKU-9999"])   
# PREDICT: None - invalid there is no key

# GRADING:
# 1. Not answered but is 5, then None
# 2. TypeError. pallet is a tuple (parentheses), and cannot be changed.
# 3. Correct
# 4. greedy - . matches any character, including spaces. Greedy .+ gfoes as far as it can and still end on a |, so it takes the second pipe: SKU-12 | QTY 3 |
# 5. Correct numbers but the format is wrong: ['101', '404']
# 6. Half correct but heres the correct answer: ('PO', '55013') <class 'tuple'>
# 7. Correct
# 8. "SKU-9999" returns 0 not None and stock["SKU-9999"] raises KeyError which is why we use .get