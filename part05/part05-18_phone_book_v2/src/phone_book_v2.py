def main():
    phonebook = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))
        if command == 3:
            print("quitting...")
            break

        name = input("name: ")
        if command == 1:
            if name in phonebook:
                for numbers in phonebook[name]:
                    print(numbers)
            else:
                print("no number")
        if command == 2:
            if name not in phonebook:
                phonebook[name] = []
            number = input("number: ")
            phonebook[name].append(number)
            print("ok!")

main()