# Task B1/B3: Simple chart and daily mean
import csv
from collections import defaultdict
import matplotlib.pyplot as plt

data = [
    ("Adyar", "2026-10-01", 48),
    ("Adyar", "2026-10-02", 52),
    ("Guindy", "2026-10-01", 95),
    ("Guindy", "2026-10-02", 121),
]

# Daily mean using Python dictionary
groups = defaultdict(list)
for station, day, pm25 in data:
    groups[(station, day)].append(pm25)

print("Daily means:")
for key, values in groups.items():
    print(key, sum(values) / len(values))

# Bar chart: station comparison
station_values = defaultdict(list)
for station, day, pm25 in data:
    station_values[station].append(pm25)

names = list(station_values.keys())
means = [sum(v) / len(v) for v in station_values.values()]
plt.bar(names, means)
plt.xlabel("Station")
plt.ylabel("Average PM2.5")
plt.title("Station-wise Average PM2.5")
plt.tight_layout()
plt.savefig("station_average.png")
plt.show()
