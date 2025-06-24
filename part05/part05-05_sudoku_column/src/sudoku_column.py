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