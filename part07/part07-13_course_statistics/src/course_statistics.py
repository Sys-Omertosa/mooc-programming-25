import json
import urllib.request

def retrieve_all():
    active_courses = []
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    course_data = json.loads(my_request.read())
    for course in course_data:
        if course["enabled"]:
            active_courses.append((course["fullName"], course["name"], course["year"], sum(course["exercises"])))
    return active_courses

def retrieve_course(course_name):
    stats_dict = {}
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses/" + course_name + "/stats")
    course_data = json.loads(my_request.read())
    stats_dict["weeks"] = len(course_data)
    stats_dict["students"] = max(course_week["students"] for course_week in course_data.values())
    stats_dict["hours"] = sum(course_week["hour_total"] for course_week in course_data.values())
    stats_dict["hours_average"] = stats_dict["hours"] // stats_dict["students"]
    stats_dict["exercises"] = sum(course_week["exercise_total"] for course_week in course_data.values())
    stats_dict["exercises_average"] = stats_dict["exercises"] // stats_dict["students"]
    return stats_dict

print(retrieve_course("docker2019"))