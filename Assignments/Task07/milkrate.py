BASE_RATE = 30.00
BASE_FAT = 3.5
BASE_SNF = 8.5
FAT_STEP_RATE = 0.40
SNF_STEP_RATE = 0.30

def calculate_rate(fat, snf):
    fat_steps = round((fat - BASE_FAT) / 0.1)
    snf_steps = round((snf - BASE_SNF) / 0.1)
    return round(BASE_RATE + fat_steps * FAT_STEP_RATE + snf_steps * SNF_STEP_RATE, 2)

def calculate_payment(litres, fat, snf):
    rate = calculate_rate(fat, snf)
    return rate, round(litres * rate, 2)

if __name__ == "__main__":
    samples = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
    for litres, fat, snf in samples:
        rate, pay = calculate_payment(litres, fat, snf)
        print(f"{litres:>5} L  fat {fat:.1f}  snf {snf:.1f}  rate {rate:6.2f}  pay {pay:8.2f}")
