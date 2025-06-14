times = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))

print(f"Average daily expenditure:\nDaily: {(groceries + (price*times))/7} euros\nWeekly: {groceries + (price*times)} euros")