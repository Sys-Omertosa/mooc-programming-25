def spruce(num : int):
    print("a spruce!")
    for i in range(1, num+1):
        print(" " * (num-i) + "*" * (2*i-1))
    print(" " * (num-1) + "*")

if __name__ == '__main__':
    spruce(3)
    print()
    spruce(5)
    spruce(6)