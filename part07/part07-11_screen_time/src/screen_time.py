from collections import defaultdict
from datetime import datetime, timedelta

filename = input("Filename: ")
start_date = datetime.strptime(input("Starting date: "), "%d.%m.%Y")
formatted_start_date = start_date.strftime("%d.%m.%Y")
days = int(input("How many days: "))

print("Please type in screen time in minutes on each day (TV computer mobile):")
total_sum = 0
screen_times = defaultdict(str)
curr_day = ""
for i in range(days):
    curr_day = (start_date + timedelta(days=i)).strftime("%d.%m.%Y")
    daily_screen_time = input(f"Screen time {curr_day}: ")
    parts = daily_screen_time.split()
    total_sum += sum(map(int, parts))
    screen_times[curr_day] = "/".join(parts)

with open(filename, "w") as file:
    file.write(f"Time period: {formatted_start_date}-{curr_day}\n")
    file.write(f"Total minutes: {total_sum}\n")
    file.write(f"Average minutes: {total_sum/days}\n")
    for day in screen_times:
        file.write(f"{day}: {screen_times[day]}\n")