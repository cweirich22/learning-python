import os, sys # loads the os and sys modules

raw = os.environ.get("REORDER_POINT", "10") # read REORDER_POINT from env, default "10" if not set (always a str)
print(raw, type(raw)) # prints the value set on REDORDER_POINT with the str class

# PREDICTIONS
# when running: python drills/env_reorder.py
# 10 <class 'str'>
# when running: $env:REORDER_POINT="25", then python drills/env_reorder.py
# 10 <class 'str'>

# CORRECTION
# when running: $env:REORDER_POINT="25", then python drills/env_reorder.py
# 25 <class 'str'>
#     the env var doesn't overwrite the script. `.get("REORDER_POINT", "10")` 
#     means "use REORDER_POINT if it's set, otherwise fall back to the default 
#     `"10"`. Once you set it to 25 in PowerShell it existed, so the default 
#     never got used. It's still a `str` either way.

try: # try to convert raw into an integer, if ValueError print error through stderr and exit(2)
    reorder_point = int(raw) # converts raw to an integer
except ValueError: # if int(raw) raises a ValueError
    print(f"REORDER_POINT must be a whole number, got {raw!r}", file=sys.stderr) # print f string with raw in quotes and push it through stderr
    sys.exit(2) # ends the script here with code 2
print(reorder_point, type(reorder_point)) # prints raw as an integer and the type after converting

# PREDICTIONS
# running: $env:REORDER_POINT="25" and $LASTEXITCODE
# 25 <class 'str'>
# 25 <class 'int'>
# 0

# running: $env:REORDER_POINT="abc" and $LASTEXITCODE
# abc <class 'str'>
# REORDER_POINT must be a whole number, got 'abc'
# abc <class 'str'>
# 2

# running: Remove-Item Env:REORDER_POINT and $LASTEXITCODE
# 10 <class 'str'>
# 10 <class 'int'>
# 0

# CORRECTION:
# When setting the REORDER_POINT to abd this will skip the last print statement so the outcome should be:
# abc <class 'str'>
# REORDER_POINT must be a whole number, got 'abc'
# 2

stock = {"SKU-100": 4, "SKU-200": 25, "SKU-300": 12, "SKU-400": 10} # dictionary with skus and quantities 

for sku, qty in stock.items(): # loops through each sku and qty in stock
    if qty <= reorder_point: # checks if the qty is less than or equal to the reorder_point
        print(f"REORDER {sku}: {qty} on hand (reorder point {reorder_point})") # f string to print which SKUs are at or below the reorder_point

# PREDICTIONS
# With REORDER_POINT unset:
# 10 <class 'str'>
# 10 <class 'int'>
# REORDER SKU-100: 4 on hand (reorder point 10)
# REORDER SKU-400: 10 on hand (reorder point 10)

# With REORDER_POINT set to 12
# 
# 
# REORDER SKU-100: 4 on hand (reorder point 12)
# REORDER SKU-300: 12 on hand (reorder point 12)
# REORDER SKU-400: 10 on hand (reorder point 12)
