def row_correct(sudoku, row_no):
    seen = set()
    for num in sudoku[row_no]:
        if num != 0:
            if not 1<=num<=9:
                return False
            if num in seen:
                return False
            seen.add(num)
    return True

def column_correct(sudoku, column_no):
    seen = set()
    for row in sudoku:
        pos = row[column_no]
        if pos != 0:
            if not 1<=pos<=9:
                return False
            if pos in seen:
                return False
            seen.add(pos)
    return True

def block_correct(sudoku, row_no, column_no):
    seen = set()
    for i in range(row_no, row_no+3):
        for j in range(column_no, column_no+3):
            num = sudoku[i][j]
            if num != 0:
                if not 1<=num<=9:
                    return False
                if num in seen:
                    return False
                seen.add(num)
    return True

def sudoku_grid_correct(sudoku):
    grid_size = len(sudoku)
    block_size = int(grid_size ** 0.5)

    for i in range(grid_size):
        if not row_correct(sudoku, i):
            return False
        if not column_correct(sudoku, i):
            return False

    for i in range(0, grid_size, block_size):
        for j in range(0, grid_size, block_size):
            if not block_correct(sudoku, i, j):
                return False

    return True

if __name__ == "__main__":
    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(row_correct(sudoku1, 0))
    print(row_correct(sudoku1, 1))
    print()
    print(column_correct(sudoku1, 0))
    print(column_correct(sudoku1, 1))
    print()
    print(block_correct(sudoku1, 0, 0))
    print(block_correct(sudoku1, 1, 2))
    print()
    print(sudoku_grid_correct(sudoku1))
    print(sudoku_grid_correct(sudoku2))