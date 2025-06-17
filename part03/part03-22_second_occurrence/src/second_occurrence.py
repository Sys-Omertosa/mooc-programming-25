str = input("Please type in a string: ")
substr = input("Please type in a substring: ")

if str.count(substr) > 1:
    index = str.find(substr)
    print(f"The second occurrence of the substring is at index {str.find(substr, index+len(substr))}.")
else:
    print("The substring does not occur twice in the string.")
