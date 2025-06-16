limit = int(input("Limit: "))
sum = 0
adder = 0
string = "The consecutive sum: "
while sum < limit:
    adder += 1
    sum += adder
    string += f"{adder} + "
print(string[:len(string)-3] + " = " + str(sum))