ftemp = int(input("Please type in a temperature (F): "))

ctemp = (ftemp - 32) * 5/9

print(f"{ftemp} degrees Fahrenheit equals {ctemp} degrees Celsius")

if ctemp < 0:
    print("Brr! It's cold in here!")