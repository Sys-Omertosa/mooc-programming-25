from math import ceil

num_of_students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

num_of_groups = ceil(num_of_students / group_size)

print(f"Number of groups formed: {num_of_groups}")