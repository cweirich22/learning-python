skus = ["A100", "B200", "C300", "D400"]
on_hand = [40, 3, 0, 12]

reorder_count = 0 # counter for SKUs that need reordering called reorder_count
total_units = 0 # running total for all untis on hand called total_untis
# loop through skus with enumerate to get the position and the sku
for i, sku in enumerate(skus):
    # get this sku's quantity from on_hand using the position
    sku_qty = on_hand[i]
    # add that quantity to the running total
    total_units += sku_qty
    # check if the quantity is under 5
    if sku_qty < 5:
        # print the REORDER line with an f-string
        print(f"REORDER {sku}: {sku_qty} on hand.")
        # add 1 to the reorder counter
        reorder_count += 1
# after the loop: print how many SKUs need reordering
print(f"SKUs that need to be reordered: {reorder_count}")
# after the loop: print the total units on hand
print(f"Total units on hand: {total_units}")

