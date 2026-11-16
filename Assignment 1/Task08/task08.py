print("Algorithm: read litres, fat and SNF; validate; calculate steps; calculate rate; calculate payment; display result.")
litres, fat, snf = 8.5, 4.2, 8.7
fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)
rate = 30 + fat_steps * 0.40 + snf_steps * 0.30
payment = litres * rate
print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate:", format(rate, ".2f"))
print("Payment:", format(payment, ".2f"))
