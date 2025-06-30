student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

id_to_student = {}
with open(student_info) as student_file:
    next(student_file)
    for line in student_file:
        parts = line.split(";")
        id_to_student[int(parts[0])] = parts[1].strip() + " " + parts[2].strip()

id_to_exec_num = {}
with open(exercise_data) as exercise_file:
    next(exercise_file)
    for line in exercise_file:
        parts = line.split(";")
        id_to_exec_num[int(parts[0])] = sum(map(int, parts[1:]))

for student_id in id_to_student:
    print(f"{id_to_student[student_id]} {id_to_exec_num[student_id]}")