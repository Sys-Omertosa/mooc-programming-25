while True:
    num = int(input("Please type in a number: "))

    if num <= 0:
        print("Thanks and bye!")
        break

    factorial = 1
    for i in range(num, 1, -1):
        factorial *= i
    print(f"The factorial of the number {num} is {factorial}")