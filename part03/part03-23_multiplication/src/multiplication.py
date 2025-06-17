num = int(input("Please type in a number: "))
for i in range(1, num+1):
    for j in range(1, num+1):
        print(f"{i} x {j} = {i*j}")