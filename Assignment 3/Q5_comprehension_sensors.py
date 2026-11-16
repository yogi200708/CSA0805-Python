# Q5: List Comprehension - Sensor Readings
temps = [1, 3, 9, 55, -60, 5, 7, 0, 25, 51]
valid = [t for t in temps if -50 <= t <= 50]
fahrenheit = [t * 9/5 + 32 for t in valid]
alarm_minutes = [minute for minute, t in enumerate(temps, start=1) if not 2 <= t <= 8]

# Loop + append alternative
valid_loop = []
for t in temps:
    if -50 <= t <= 50:
        valid_loop.append(t)

# map/filter alternative
valid_map_filter = list(filter(lambda t: -50 <= t <= 50, temps))
print("Valid Celsius:", valid)
print("Fahrenheit:", [round(x, 2) for x in fahrenheit])
print("Alarm minutes:", alarm_minutes)
print("Loop result:", valid_loop)
print("map/filter result:", valid_map_filter)
