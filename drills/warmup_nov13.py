import re  # load regex module

# REMEMBER: .groups() returns a TUPLE like ('SKU-88', '4'), not a list
# REMEMBER: .group(2) returns one STRING like '4'

# PREDICT: None - \b checks the character before B which is X
print(re.search(r"\bBIN-\d{2}\b", "XBIN-12"))      # Q1 \b weak spot
# PREDICT: None - Not sure if \b will allow :
print(re.search(r"\bBIN-\d{2}\b", "loc:BIN-12;"))  # Q2
m = re.search(r"(SKU-\d+) x(\d+)", "pick SKU-88 x4")  # Q3
# PREDICT: ['SKU-88', '4']
print(m.groups())          # Q3a what type?
# PREDICT: ['4'] - Does calling a single group still put the result into a list?
print(type(m.group(2)))    # Q3b
# PREDICT: SKU-1 SKU-2 SKU-3
print(re.sub(r"sku", "SKU", "sku-1 sku-2 Sku-3", re.IGNORECASE))  # Q4 the positional trap
# PREDICT: PO-55012
print(re.fullmatch(r"PO-\d{5}", "PO-55012 "))  # Q5 trailing space
# PREDICT: <Match: Object, span=(0,8), PO-55012>
print(re.search(r"PO-\d{5}", "PO-55012 "))     # Q6

def double_qty(q):   # Q7 return vs print
    q * 2
# PREDICT: 6
print(double_qty(3))

for n, line in enumerate(["SKU-1", "SKU-2"], start=1):  # Q8
    # PREDICT: 2, 1
    print(n, line)

try:                                   # Q9 your Qwiklabs bug
    open("<data/receiving.txt>")
except FileNotFoundError as e:
    # PREDICT: File
    print(type(e).__name__)

# CORRECTIONS
# Q1. correct
# Q2. <re.Match object; span=(4,10), match='BIN-12'> `:` and `;` aren't word characters, so there's a boundary on both sides of `BIN-12`
# Q3a. `('SKU-88', '4')`. The parentheses mean it's a tuple, not a list.
# Q3b. <class 'str'>. `.group(2)` returns one plain string, `'4'`, not inside a list. `type()` prints the class, not the value. Regex never gives you an int, so you still need `int()`
# Q4. SKU-1 SKU-2 Sku-3. The 4th positional argument is count, and `re.IGNORECASE` equals 2, so it replaced at most 2 matches with case still mattering. `Sku-3` doesn't match lowercase `sku`.
# Q5. None. `fullmatch` needs the whole string to match, and the trailing space isn't in the pattern.
# Q6. mostly correct. <re.Match object; span=(0, 8), match='PO-55012'>
# Q7. None. `q * 2` calculates 6 and throws it away, and with no `return` the function returns None.
# Q8. You get two lines, `1 SKU-1` then `2 SKU-2`. `enumerate` hands you a (number, item) pair on each loop, and `print(n, line)` puts a space between them.
# Q9. `FileNotFoundError`. `__name__` gives the full class name.

# Q4 FIX: flags= makes it case-insensitive and replaces all 3
print(re.sub(r"sku", "SKU", "sku-1 sku-2 Sku-3", flags=re.IGNORECASE))
# PREDICT: SKU-1 SKU-2 SKU-3

# Q7 FIX: return sends the value back to the caller
def double_qty_fixed(q):
    return q * 2
print(double_qty_fixed(3))
# PREDICT: 6
