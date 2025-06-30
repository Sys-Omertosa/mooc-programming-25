student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")

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

id_to_exm_pts = {}
with open(exam_points) as exam_points_file:
    next(exam_points_file)
    for line in exam_points_file:
        parts = line.split(";")
        id_to_exm_pts[int(parts[0])] = sum(map(int, parts[1:]))

id_to_tot_pts = {}
id_to_grade = {}
print("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")
for id in id_to_student:
    exec_pts = (id_to_exec_num[id] * 10 // 40)
    total_points = exec_pts + id_to_exm_pts[id]
    id_to_tot_pts[id] = total_points
    id_to_grade[id] = (
        0 if 0<=total_points<=14
        else 1 if 15 <= total_points <= 17
        else 2 if 18 <= total_points <= 20
        else 3 if 21 <= total_points <= 23
        else 4 if 24 <= total_points <= 27
        else 5
    )
    print(f"{id_to_student[id]:30}"
          f"{id_to_exec_num[id]:<10}"
          f"{exec_pts:<10}"
          f"{id_to_exm_pts[id]:<10}"
          f"{id_to_tot_pts[id]:<10}"
          f"{id_to_grade[id]:<10}"
    )