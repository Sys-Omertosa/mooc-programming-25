str = input("Please type in a word: ")
char = input("Please type in a character: ")

while True:
    index = str.find(char)
    if index >= 0 and len(str[index:]) > 2:
        print(str[index:index+3])
        str = str[index+1:]
    else:
        break