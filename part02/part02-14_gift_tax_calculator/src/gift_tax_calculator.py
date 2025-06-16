value = int(input("Value of gift: "))

if value < 5000:
    tax = 0
elif 5000 <= value <= 25000:
    tax = 100 + 0.08*(value - 5000)
elif 25000 <= value <= 55000:
    tax = 1700 + 0.1*(value - 25000)
elif 55000 <= value <= 200000:
    tax = 4700 + 0.12*(value - 55000)
elif 200000 <= value <= 1000000:
    tax = 22100 + 0.15*(value - 200000)
else:
    tax = 142100 + 0.17*(value - 1000000)

if tax == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {tax}")