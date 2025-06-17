num = int(input("Please type in a number: "))
for i in range(1, num+1, 2):
    if i+1 <= num:
        print(i+1)
    print(i)