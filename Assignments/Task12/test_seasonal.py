from seasonal_milkrate import calculate_rate, calculate_ten_day_payment
print("April base rate:", calculate_rate("3.50", "8.50", 4))
print("July base rate:", calculate_rate("3.50", "8.50", 7))
print("500 litres:", calculate_ten_day_payment("500", "3.50", "8.50", 4))
print("520 litres:", calculate_ten_day_payment("520", "3.50", "8.50", 4))
