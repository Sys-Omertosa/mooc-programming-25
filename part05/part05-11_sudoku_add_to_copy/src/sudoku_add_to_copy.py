def print_sudoku(sudoku):
    grid_size = len(sudoku)
    block_size = grid_size ** 0.5
    for i in range(grid_size):
        for j in range(grid_size):
            num = sudoku[i][j]
            print("_ ", end="") if num == 0 else print(f"{num} ", end="")
            if (j+1) % block_size == 0 and (j+1) < grid_size:
                print(" ", end="")
        print()
        if (i+1) % block_size == 0 and (i+1) < grid_size:
            print()

def copy_and_add(sudoku, row_no, column_no, number):
    copy_sudoku = []
    for row in sudoku:
        copy_sudoku.append(row[:])
    copy_sudoku[row_no][column_no] = number
    return copy_sudoku

if __name__ == '__main__':
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)