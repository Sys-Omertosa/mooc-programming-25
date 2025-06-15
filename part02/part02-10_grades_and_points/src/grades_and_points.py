points = int(input("How many points [0-100]: "))

print("Grade: ", end="")

if points > 100 or points < 0:
    print("impossible!")
elif points >= 90:
    print("5")
elif points >= 80:
    print("4")
elif points >= 70:
    print("3")
elif points >= 60:
    print("2")
elif points >= 50:
    print("1")
else:
    print("fail")