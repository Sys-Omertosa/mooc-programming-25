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

def add_number(sudoku, row_no, column_no, number):
    sudoku[row_no][column_no] = number

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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)