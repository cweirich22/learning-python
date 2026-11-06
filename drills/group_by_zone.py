pairs = [("SKU-100", "A"), ("SKU-200", "B"), ("SKU-300", "A"), ("SKU-400", "B"), ("SKU-500", "A")] # list of tuples

zones = {} # assigns an empty dictionary to zones
for sku, zone in pairs: # loops through skuy and zone in pairs dictionary
    if zone not in zones: # checks if the zone is not in zones dictionary
        zones[zone] = [] # creates the key and sets its value to an empty list
    zones[zone].append(sku) # adds the SKU to the end of the list based on the matching key

print(zones) # prints the zones dictionary