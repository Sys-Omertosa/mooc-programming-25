def find_factorial(x):
    factorial = 1
    for i in range(x, 1, -1):
        factorial *= i
    return factorial

def factorials(n):
    return {i: find_factorial(i) for i in range(1, n+1)}