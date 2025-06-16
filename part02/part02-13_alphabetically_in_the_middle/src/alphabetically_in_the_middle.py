letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

if letter2.lower() < letter1.lower() < letter3.lower() or letter3.lower() < letter1.lower() < letter2.lower():
    middle_letter = letter1
elif letter1.lower() < letter2.lower() < letter3.lower() or letter3.lower() < letter2.lower() < letter1.lower():
    middle_letter = letter2
else:
    middle_letter = letter3

print(f"The letter in the middle is {middle_letter}")