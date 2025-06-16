while True:
    string = input("Please type in a string: ")

    if not string:
        break

    print("\n" + string)
    print("-" * len(string) + "\n")