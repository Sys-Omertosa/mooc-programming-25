def squared(text : str, num : int):
    index = 0
    for i in range(num):
        for j in range(num):
            print(text[index], end="")
            index += 1
            index %= len(text)
        print()

if __name__ == '__main__':
    squared("ab", 3)
    print()
    squared("aybabtu", 5)