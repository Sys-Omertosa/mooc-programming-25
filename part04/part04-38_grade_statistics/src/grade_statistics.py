def take_user_input(exam_points_list : list[int], exercises_list : list[int]):
    while True:
        data = input("Exam points and exercises completed: ")
        if not data:
            return
        data = data.split()
        exam_points_list.append(int(data[0]))
        exercises_list.append(int(data[1]))

def determine_exercise_points(exercises_list : list[int]):
    for i in range(len(exercises_list)):
        exercises_list[i] //= 10

def determine_total_points(exam_points_list : list[int], exercises_list : list[int]) -> list[int]:
    return [exam_points + exercise_points for exam_points, exercise_points in zip(exam_points_list, exercises_list)]

# def determine_grades_list(total_points_list : list[int], exam_points_list : list[int]) -> list[int]:
#     return [0 if 0 <= total_points_list[i] <= 14 or exam_points_list[i] < 10
#             else 1 if 15 <= total_points_list[i] <= 17
#             else 2 if 18 <= total_points_list[i] <= 20
#             else 3 if 21 <= total_points_list[i] <= 23
#             else 4 if 24 <= total_points_list[i] <= 27
#             else 5
#             for i in range(len(total_points_list))]

def determine_grade_counts(total_points_list : list[int], exam_points_list : list[int]) -> list[int]:
    grade_counts = [0]*6
    for i in range(len(total_points_list)):
        if 0 <= total_points_list[i] <= 14 or exam_points_list[i] < 10: grade_counts[0] += 1
        elif 15 <= total_points_list[i] <= 17: grade_counts[1] += 1
        elif 18 <= total_points_list[i] <= 20: grade_counts[2] += 1
        elif 21 <= total_points_list[i] <= 23: grade_counts[3] += 1
        elif 24 <= total_points_list[i] <= 27: grade_counts[4] += 1
        else: grade_counts[5] += 1
    return grade_counts

def determine_statistics(total_points_list : list[int], grade_counts : list[int]):
    num_of_students = len(total_points_list)
    print("Statistics:")
    print(f"Points average: {sum(total_points_list)/num_of_students:.1f}")
    print(f"Pass percentage: {(sum(count for count in grade_counts[1:])/num_of_students)*100:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        print(f"{i}: " + "*" * grade_counts[i])

def main():
    exam_points_list = []
    exercises_list = []

    take_user_input(exam_points_list, exercises_list)
    determine_exercise_points(exercises_list)

    total_points_list = determine_total_points(exam_points_list, exercises_list)
    grade_counts = determine_grade_counts(total_points_list, exam_points_list)
    determine_statistics(total_points_list, grade_counts)

main()