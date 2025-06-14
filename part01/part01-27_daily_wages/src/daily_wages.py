hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
day = input("Day of the week: ")

daily_wage = hourly_wage*hours_worked

print(f"Daily wages: {daily_wage*2 if day == "Sunday" else daily_wage} euros")