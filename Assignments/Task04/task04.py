fat = 4.2
snf = 8.7
fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)
rate = 30 + fat_steps * 0.40 + snf_steps * 0.30
print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate per litre: Rs.", format(rate, ".2f"))
