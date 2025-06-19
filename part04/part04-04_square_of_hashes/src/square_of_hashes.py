def line(integer, string):
    if not string:
        print("*"*integer)
    else:
        print(string[0]*integer)

def square_of_hashes(size):
    for i in range(size):
        line(size, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
