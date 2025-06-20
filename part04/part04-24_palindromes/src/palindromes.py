def palindromes(string : str) -> bool:
    return string == str(reversed(string))

while True:
    string = input("Please type in a palindrome: ")
    if palindromes(string):
        print(f"{string} is a palindrome!")
        break
    print("that wasn't a palindrome")
