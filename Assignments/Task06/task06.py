def calculate_rate(fat, snf):
    rate = 30 + round((fat - 3.5) / 0.1) * 0.40
    rate += round((snf - 8.5) / 0.1) * 0.30
    return round(rate, 2)

def calculate_payment(litres, rate):
    return round(litres * rate, 2)

rate = calculate_rate(4.2, 8.7)
print("Rate:", format(rate, ".2f"))
print("Payment:", format(calculate_payment(8.5, rate), ".2f"))
