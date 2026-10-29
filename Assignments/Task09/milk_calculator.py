# Copy milkrate.py from Task07 into this folder before running.
from milkrate import calculate_payment
farmer_id = input("Farmer ID: ")
litres = float(input("Litres: "))
fat = float(input("Fat percentage: "))
snf = float(input("SNF percentage: "))
shift = input("Shift (morning/evening): ")
if litres < 0:
    print("Error: litres cannot be negative")
elif fat < 2.0 or fat > 7.0:
    print("Error: fat must be between 2.0 and 7.0")
else:
    rate, payment = calculate_payment(litres, fat, snf)
    print("\nPayment slip")
    print("Farmer ID:", farmer_id)
    print("Shift:", shift)
    print("Litres:", litres, "Fat:", fat, "SNF:", snf)
    print("Rate per litre: Rs.", format(rate, ".2f"))
    print("Payment: Rs.", format(payment, ".2f"))
