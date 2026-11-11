import re  # loads the regex module

counts = {}  # empty dict to count SKUs
for sku in ["A1", "B2", "A1"]:  # loop over scanned SKUs
    counts[sku] = counts.get(sku, 0) + 1  # add 1, starting at 0 if new
print(counts)  # {"A1": 2, "B2": 1}

def total(qtys):  # adds up a list of quantities
    t = 0  # running total
    for q in qtys:  # each quantity
        t += q  # add it
    return t  # careful: where is this indented?
print(total([5, 10, 15]))  # Inititally will reset value of t so the last loop makes t = 15, fixed it so it will equal 30

print("SKU-1 , 5".split(","))  # ["SKU-1 ", " 5"] (look at the spaces)
print("SKU-1   5".split())  # ["SKU-1", "5"]

m = re.search(r"PO-(\d+)", "no po here")  # search for a PO number
print(m)  # Will crashg the code since theres no try/ except for the ValueError

def show(x):  # prints double x and returns nothing
    print(x * 2)  # prints
r = show(4)  # PREDICT what prints here
print(r)  # 8