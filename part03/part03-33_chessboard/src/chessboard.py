def chessboard(length):
    if length == 1:
        print("1")
        return

    for i in range(length):
        for j in range(length):
            print("1", end="") if j % 2 == i % 2 else print("0", end="")
        print()

if __name__ == '__main__':
    chessboard(1)
    print()
    chessboard(6)