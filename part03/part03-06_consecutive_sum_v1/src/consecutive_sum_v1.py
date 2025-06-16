limit = int(input("Limit: "))
sum = 0
adder = 1
while sum < limit:
    sum += adder
    adder += 1
print(sum)