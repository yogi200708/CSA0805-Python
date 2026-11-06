# Q6: Nested Data - Railway Timetable
trains = {
    "12601": {"name": "Express A", "stops": [("Chennai", "08:00", "08:10"), ("Katpadi", "10:00", "10:05"), ("Bengaluru", "12:00", "12:10")], "days": {"Mon", "Wed", "Fri"}},
    "12602": {"name": "Express B", "stops": [("Chennai", "09:00", "09:10"), ("Katpadi", "11:00", "11:05"), ("Bengaluru", "13:00", "13:10")], "days": {"Tue", "Thu", "Sat"}},
    "12603": {"name": "Express C", "stops": [("Chennai", "10:00", "10:10"), ("Salem", "12:00", "12:05"), ("Coimbatore", "15:00", "15:10")], "days": {"Mon", "Tue", "Wed"}},
    "12604": {"name": "Express D", "stops": [("Chennai", "11:00", "11:10"), ("Katpadi", "13:00", "13:05"), ("Bengaluru", "15:00", "15:10")], "days": {"Sun", "Mon", "Tue"}},
    "12605": {"name": "Express E", "stops": [("Chennai", "12:00", "12:10"), ("Salem", "14:00", "14:05"), ("Coimbatore", "17:00", "17:10")], "days": {"Thu", "Fri", "Sat"}},
}

station, day = "Katpadi", "Mon"
found = []
for number, info in trains.items():
    if day in info["days"]:
        for stop_name, arrival, departure in info["stops"]:
            if stop_name == station:
                found.append((departure, number, info["name"]))
print("Trains at", station, "on", day, ":", sorted(found))

for number, info in trains.items():
    print(number, info["name"])
    for stop in info["stops"]:
        print(" ", stop)
