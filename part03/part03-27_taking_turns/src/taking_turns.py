num = int(input("Please type in a number: "))

for i in range(1, ((num+1)//2)+1):
    print(i)
    if num-i+1 != i:
        print(num-i+1)