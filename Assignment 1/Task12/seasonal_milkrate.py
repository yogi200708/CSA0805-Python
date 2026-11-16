from decimal import Decimal, ROUND_HALF_UP
def money(x):
    return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
def calculate_rate(fat, snf, month):
    if month in [4, 5, 6]:
        base = Decimal("32.00")
        fat_step_rate = Decimal("0.45")
    else:
        base = Decimal("30.00")
        fat_step_rate = Decimal("0.40")
    fat = Decimal(str(fat)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    snf = Decimal(str(snf)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    fat_steps = ((fat - Decimal("3.5")) / Decimal("0.1")).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    snf_steps = ((snf - Decimal("8.5")) / Decimal("0.1")).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    return money(base + fat_steps * fat_step_rate + snf_steps * Decimal("0.30"))
def calculate_ten_day_payment(litres, fat, snf, month):
    litres = Decimal(str(litres))
    rate = calculate_rate(fat, snf, month)
    milk_pay = money(litres * rate)
    bonus = Decimal("0.00")
    if litres > Decimal("500"):
        bonus = money(litres * Decimal("0.50"))
    return rate, milk_pay, bonus, money(milk_pay + bonus)
if __name__ == "__main__":
    rate, milk_pay, bonus, final_pay = calculate_ten_day_payment("520", "4.25", "8.65", 4)
    print("Rate per litre: Rs.", rate)
    print("Milk payment: Rs.", milk_pay)
    print("Bonus: Rs.", bonus)
    print("Final ten-day payment: Rs.", final_pay)
