string = input("Word: ")
space_length = 14 - len(string)//2
print("*"*30)
print("*" + " "*(space_length if len(string) % 2 == 0 else space_length - 1) + string + " "*space_length + "*")
print("*"*30)