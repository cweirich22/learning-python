def weeks_of_supply(on_hand, weekly_demand):
    if weekly_demand == 0:
        return None
    return on_hand / weekly_demand

def reorder_point(weekly_demand, lead_time_weeks, safety_stock):
    return weekly_demand * lead_time_weeks + safety_stock

print(weeks_of_supply(80, 20))
print(reorder_point(20, 2, 20))

on_hand = float(input("On-hand units: "))
weekly_demand = float(input("Weekly demand: "))
lead_time_days = float(input("Lead time in days: "))
buffer_weeks = float(input("Buffer weeks:"))

lead_time_weeks = lead_time_days / 7
safety_stock = weekly_demand * buffer_weeks
rop = reorder_point(weekly_demand, lead_time_weeks, safety_stock)
wos = weeks_of_supply(on_hand, weekly_demand)

print(f"Safety stock: {safety_stock}")
print(f"Reorder point: {rop}")
print(f"Weeks of supply: {wos}")

if wos is None:
    print("Status: cannot calculate (demand is 0)")
elif on_hand <= rop:
    print("Status: REORDER")
else:
    print("Status: OK")