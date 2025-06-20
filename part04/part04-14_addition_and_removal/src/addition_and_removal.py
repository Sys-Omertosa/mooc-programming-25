my_list = []
i = 0
while True:
    print(f"The list is now {my_list}")
    choice = input("a(d)d, (r)emove or e(x)it: ")

    if choice == "x":
        print("Bye!")
        break

    if choice == "d":
        i += 1
        my_list.append(i)

    if choice == "r":
        my_list.pop()
        i -= 1