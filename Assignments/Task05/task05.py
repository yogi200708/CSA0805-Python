farmer_id = input("Farmer ID: ")
litres = float(input("Litres: "))
fat = float(input("Fat percentage: "))
snf = float(input("SNF percentage: "))
if litres < 0:
    print("Error: litres cannot be negative")
elif fat < 2.0 or fat > 7.0:
    print("Error: fat must be between 2.0 and 7.0")
else:
    print("Inputs accepted for farmer", farmer_id, "| Litres:", litres, "| Fat:", fat, "| SNF:", snf)
