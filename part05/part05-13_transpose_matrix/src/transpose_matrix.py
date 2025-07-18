def transpose(matrix):
    size = len(matrix)
    for i in range(size-1):
        for j in range(i+1, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    transpose(matrix)
    for row in matrix:
        print(row)