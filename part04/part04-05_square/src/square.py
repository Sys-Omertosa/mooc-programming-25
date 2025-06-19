def line(integer, string):
    if not string:
        print("*"*integer)
    else:
        print(string[0]*integer)

def square(size, character):
    for i in range(size):
        line(size, character)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")