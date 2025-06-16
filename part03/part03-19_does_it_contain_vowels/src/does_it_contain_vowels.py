string = input("Please type in a string: ").lower()
vowels = "aeo"

for char in vowels:
    if char in string:
        print(f"{char} found")
    else:
        print(f"{char} not found")