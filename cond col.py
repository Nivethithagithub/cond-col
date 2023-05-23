if df['ship_mode'] == "Same Day":
    df['surcharge'] = 0.2
elif df['ship_mode'] == "First Class":
    df['surcharge'] = 0.1
elif df['ship_mode'] == "Standard Class":
    df['surcharge'] = 0.05
else:
    df['surcharge'] = 0

df['total_cost'] = (df['sales'] - df['profit']) * (1 + df['surcharge'])
