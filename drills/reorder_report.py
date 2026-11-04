skus = ["A100", "B200", "C300", "D400"]
on_hand = [40, 3, 0, 12]

reorder_count = 0 # counter for SKUs that need reordering called reorder_count
total_units = 0 # running total for all units on hand called total_units
for i, sku in enumerate(skus): # loops through skus, giving the position i and the sku name each time
    sku_qty = on_hand[i] # takes the sku position in the list and uses that same position to get the number in the on_hand list
    total_units += sku_qty # adds the sku_qty to the total_units to log the running total
    if sku_qty < 5: # checks if the sku_qty is less than 5
        print(f"REORDER {sku}: {sku_qty} on hand.") # if True then an f string is made to say what to REORDER and how many are currently on hand
        reorder_count += 1 # adds 1 to the reorder_count running total

print(f"SKUs that need to be reordered: {reorder_count}") # f string to print what the reorder_count is
print(f"Total units on hand: {total_units}") # f string to print out what the total units is

