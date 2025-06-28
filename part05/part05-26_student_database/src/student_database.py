def add_student(students, name):
    students[name] = {}

def add_course(students, name, course):
    if name in students and course[1] > 0:
        student_courses = students[name]
        course_name, grade = course
        if course_name in student_courses:
            if grade > student_courses[course_name]:
                student_courses[course_name] = grade
        else:
            student_courses[course_name] = grade

def no_of_courses(students, name):
    return len(students[name])

def average_grade(students, name):
    return sum(students[name].values()) / no_of_courses(students, name)

def print_student(students, name):
    print(f"{name}:", end="")
    if name not in students:
        print(" no such person in the database")
        return

    if not students[name]:
        print("\n no completed courses")
    else:
        course_dict = students[name]
        num_of_courses = no_of_courses(students, name)
        print()
        print(f" {num_of_courses} completed courses:")
        for course, grade in course_dict.items():
            print(f"  {course} {grade}")
        print(f" average grade {average_grade(students, name)}")

def summary(students):
    print(f"students {len(students)}")
    most_courses = [0, ""]
    best_average_grade = [0, ""]
    for name in students:
        num_of_courses = no_of_courses(students, name)
        if num_of_courses > most_courses[0]:
            most_courses[0] = num_of_courses
            most_courses[1] = name

        avg_grade = average_grade(students, name)
        if avg_grade > best_average_grade[0]:
            best_average_grade[0] = avg_grade
            best_average_grade[1] = name

    print(f"most courses completed {most_courses[0]} {most_courses[1]}")
    print(f"best average grade {best_average_grade[0]} {best_average_grade[1]}")

if __name__ == '__main__':
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)