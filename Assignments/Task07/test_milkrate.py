from milkrate import calculate_rate, calculate_payment
assert calculate_rate(3.5, 8.5) == 30.00
assert calculate_rate(4.2, 8.7) == 33.40
assert calculate_rate(3.1, 8.3) == 27.80
assert calculate_payment(10, 3.5, 8.5) == (30.00, 300.00)
print("All tests passed")
