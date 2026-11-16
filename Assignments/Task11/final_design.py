from decimal import Decimal, ROUND_HALF_UP
def money(x):
    return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
def calculate_rate(fat, snf):
    fat_steps = ((fat - Decimal("3.5")) / Decimal("0.1")).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    snf_steps = ((snf - Decimal("8.5")) / Decimal("0.1")).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    return money(Decimal("30.00") + fat_steps * Decimal("0.40") + snf_steps * Decimal("0.30"))
rate = calculate_rate(Decimal("4.2"), Decimal("8.7"))
print("Recommended Decimal design")
print("Rate:", rate)
print("Payment:", money(Decimal("8.5") * rate))
