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