import csv 

stock = {"SKU-100": 10, "SKU-200": 5, "SKU-300": 18, "SKU-400": 2, "SKU-500": 12} # assigns a dictionary to stock

def needs_pick(qty, threshold=10): # creates a function called needs_pick with two parameters: qty and threshold which holds a default value of 10
    return qty < threshold # Boolean that will return True or False based on if the qty is less than the threshold

def pick_qty(qty, target=20): # creates a function called pick_qty with two parameters: qty and target which holds a default value of 20
    if qty >= target: # if statement to check if the qty is greater than or equal to the target
        return 0 # if True then return 0
    else: # if the if statement is false
        return target - qty # returns the target minus the qty
    
def build_pick_list(stock, threshold=10, target=20): # creates a function called build_pick_list that takes in three parameters: stock, threshold with a default of 10, and target with a default of 20
    rows = [] # assigns an empty list to rows
    for sku, qty in stock.items(): # loops through sku and qty in stock disctionary
        if needs_pick(qty): # checks if needs_pick(qty) is True
            to_pick = pick_qty(qty, target) # calls pick_qty and stores the returned quntity in to_pick
            rows.append((sku, qty, to_pick)) # appends the sku, qty, and to_pick to the rows list as a tuple
    return rows # returns the rows list

def main(): # create a main fuction
    rows = build_pick_list(stock) # calls build_pick_list with stock and stores the returned list in rows
    for sku, qty, to_pick in rows: # unpacks each row's tuple into three variables
        print(f"{sku}: {qty} on hand, pick {to_pick}") # f string prints the sku, qty, and to_pick
    with open("drills/pick_list.csv", "w", newline="") as f: # opens pick_list.csv from the drills folder in write mode 
        writer = csv.writer(f) # creates a CSV writer that writes to f
        writer.writerow(["sku", "on_hand", "to_pick"]) # creates the header which has sku, on_hand, and _to_pick
        writer.writerows(rows) # writes all the rows from rows

if __name__ == "__main__": # checks whether this file is being run directly
    main() # calls main to run the report