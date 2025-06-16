password = input("Password: ")
while True:
    repeat_password = input("Repeat password: ")

    if repeat_password == password:
        break

    print("They do not match!")

print("User account created!")