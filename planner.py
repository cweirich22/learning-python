def weeks_of_supply(on_hand, weekly_demand):
    if weekly_demand == 0:
        return None
    return on_hand / weekly_demand

def reorder_point(weekly_demand, lead_time_weeks, safety_stock):
    return weekly_demand * lead_time_weeks + safety_stock

print(weeks_of_supply(80, 20))
print(reorder_point(20, 2, 20))