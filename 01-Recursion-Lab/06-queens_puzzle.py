def set_queen(row, col, matrix, rows, columns, left_diagonals, right_diagonals):
    matrix[row][col] = '*'
    rows.add(row)
    columns.add(col)
    left_diagonals.add(row - col)
    right_diagonals.add(row + col)


def remove_queen(row, col, matrix, rows, columns, left_diagonals, right_diagonals):
    matrix[row][col] = '-'
    rows.remove(row)
    columns.remove(col)
    left_diagonals.remove(row - col)
    right_diagonals.remove(row + col)


def can_place_queen(row, col, rows, columns, left_diagonals, right_diagonals):
    if row in rows:
        return False
    if col in columns:
        return False
    if (row - col) in left_diagonals:
        return False
    if (row + col) in right_diagonals:
        return False
    return True


def print_board(matrix):
    for row in matrix:
        print(' '.join(row))
    print()


def put_queens(row, matrix, rows, columns, left_diagonals, right_diagonals):
    if row == 8:
        print_board(matrix)
        return

    for col in range(8):

        if can_place_queen(row, col, rows, columns, left_diagonals, right_diagonals):
            set_queen(row, col, matrix, rows, columns, left_diagonals, right_diagonals)
            put_queens(row + 1, matrix, rows, columns, left_diagonals, right_diagonals)
            remove_queen(row, col, matrix, rows, columns, left_diagonals, right_diagonals)


n = 8
matrix = []

[matrix.append(['-'] * n) for _ in range(n)]

put_queens(0, matrix, set(), set(), set(), set())
