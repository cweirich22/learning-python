import csv

stock = {"SKU-100": 10, "SKU-200": 5, "SKU-300": 18, "SKU-400": 2, "SKU-500": 12}

def needs_pick(qty, threshold=10):
    return qty < threshold

def pick_qty(qty, target=20):
    if qty >= target:
        return 0
    else:
        return target - qty
    
def build_pick_list(stock, threshold=10, target=20):
    rows = []
    for sku, qty in stock.items():
        if needs_pick(qty):
            to_pick = pick_qty(qty)
            rows.append((sku, qty, to_pick))
    return rows

def main():
    rows = build_pick_list(stock)
    for sku, qty, to_pick in rows:
        print(f"{sku}: {qty} on hand, pick {to_pick}")
    with open("drills/pick_list.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["sku", "on_hand", "to_pick"])
        writer.writerows(rows)

if __name__ == "__main__":
    main()