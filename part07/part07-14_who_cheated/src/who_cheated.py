from collections import defaultdict
from datetime import datetime, timedelta
import csv


def format_data():
    cheaters = set()
    name_to_start_time = {}
    name_to_tasks = defaultdict(lambda: defaultdict(int))

    with open("start_times.csv") as file:
        for line in csv.reader(file, delimiter=";"):
            name_to_start_time[line[0]] = datetime.strptime(line[1], "%H:%M")

    with open("submissions.csv") as file:
        for line in csv.reader(file, delimiter=";"):
            name, task_num, task_points, end_time = line[0], int(line[1]), int(line[2]), datetime.strptime(line[3],"%H:%M")

            if end_time > name_to_start_time[name] + timedelta(hours=3):
                cheaters.add(name)
                continue

            name_to_tasks[name][task_num] = max(name_to_tasks[name][task_num], task_points)

    return cheaters, dict(name_to_tasks)


def cheaters():
    cheater_list, _ = format_data()
    return list(cheater_list)


def final_points():
    _, name_to_tasks = format_data()
    return {name : sum(name_to_tasks[name][task_num] for task_num in name_to_tasks[name]) for name in name_to_tasks}

print(cheaters())