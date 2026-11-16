import os, re, sys                                   # tools: env vars, regex, command line
sys.argv = ["label_parser_cli.py", "labels_messy.txt", "out.csv"]  # fake what the command line would hand us
print(len(sys.argv))                                 # prints the length of sys.argv
print(sys.argv[2])                                   # prints index 2 of sys.argv
os.environ.pop("LABEL_OUT_DIR", None)                # make sure this var is NOT set
os.environ["REORDER_POINT"] = "20"                   # set an env var for this process
rp = os.environ.get("REORDER_POINT")                 # read it back
print(rp + rp)                                       # adds rp to rp which is two strings
print(os.environ.get("LABEL_OUT_DIR", "out"))        # D - not sure
pat = r"SKU-\d{4}"                                   # SKU pattern
print(bool(re.search(pat, "XSKU-1042")))             # True/ False if the pat is in the string
print(bool(re.fullmatch(pat, "XSKU-1042")))          # True/ False if the pat fullmatches the string
m = re.search(r"(SKU-\d{4}) qty=(\d+)", "SKU-1042 qty=12")  # two groups
print(m.groups())                                    # prints the groups (SKU-\d{4}) and (\d+)
print(type(m.group(2)))                              # prints the type for m group 2 (index 2)
def total(a, b):                                     # a function that...
    print(a + b)                                     # ...prints but doesn't return
x = total(3, 4)                                      # call it and store the result
print(x)                                             # prints x which uses the total function

# PREDICTIONS
# A. 4
# B. label_parser_cli.py
# C. 2020
# D. out
# E. True
# F. False
# G. ['SKU-1042'], ['12']
# H. <class=str>
# I. None

# CORRECTIONS
# A. 3
# B. out.csv
# G. ('SKU-1042', '12')
# H. <class 'str'>
# Ia. 7
# Ib. None

# EXPLANATIONS
# A. sys.arv is assigns a list with a length of 3
# B. the list starts with 0 then counts up to 2, so a total of 3 in the list. 2 index is out.csv.
# G. It's a tuple holding every group's string, in order.
# H. the type is string so we write <class 'str'>
# Ia. x is assinged with a function so it runs the function first then prints that output as long as the function has a print statement inside. 
# Ib. x is None because total() prints but never returns anything

# EXIT CODES in label_parser_cli.py
# 0 = clean file (parsed good labels with zero bad lines)
# 1 = FileNotFound
# 2 = used wrong: the wrong number of arguments, which is when the message prints
# 3 = bad lines is True (not empty)