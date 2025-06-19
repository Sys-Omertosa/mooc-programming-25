def line(integer, string):
    if not string:
        print("*"*integer)
    else:
        print(string[0]*integer)

def triangle(size):
    for i in range(1, size+1):
        line(i, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
