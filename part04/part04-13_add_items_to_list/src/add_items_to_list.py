my_list = []
num_of_items = int(input("How many items: "))

for i in range(num_of_items):
    item = int(input(f"Item {i+1}: "))
    my_list.append(item)
print(my_list)