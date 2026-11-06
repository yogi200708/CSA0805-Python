# Q1: Lists and Slicing - Daily Rainfall
import random

readings = [round(random.uniform(0, 20), 1) for _ in range(365)]
weekly_totals = [sum(readings[i:i+7]) for i in range(0, len(readings), 7)]
print("Weekly totals:", weekly_totals)
print("Wettest week:", max(weekly_totals), "Week:", weekly_totals.index(max(weekly_totals))+1)
print("Driest week:", min(weekly_totals), "Week:", weekly_totals.index(min(weekly_totals))+1)

# 7-day moving average (running sum)
moving = []
if len(readings) >= 7:
    current = sum(readings[:7])
    moving.append(round(current/7, 2))
    for i in range(7, len(readings)):
        current += readings[i] - readings[i-7]
        moving.append(round(current/7, 2))
print("7-day moving averages:", moving)
print("Dry days (day numbers):", [i+1 for i, x in enumerate(readings) if x == 0])
print("readings[7:14]:", readings[7:14])
print("readings[-7:]:", readings[-7:])
print("readings[::7]:", readings[::7])
