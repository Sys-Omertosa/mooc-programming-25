from math import sqrt

while True:
    num = int(input("Please type in a number: "))

    if num == 0:
        print("Exiting...")
        break

    if num < 0:
        print("Invalid number")
        continue

    print(sqrt(num))