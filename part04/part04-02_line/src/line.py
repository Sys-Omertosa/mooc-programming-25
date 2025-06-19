def line(integer, string):
    if not string:
        print("*"*integer)
    else:
        print(string[0]*integer)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")