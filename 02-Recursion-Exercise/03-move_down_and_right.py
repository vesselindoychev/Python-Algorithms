def is_outside(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return True


def is_visited(row, col, matrix):
    if matrix[row][col] == 'v':
        return True


def is_exit(row, col, matrix):
    if matrix[row][col] == 'e':
        return True


def play(row, col, matrix, unique_paths):

    if is_outside(row, col, matrix):
        return

    if is_visited(row, col, matrix):
        return

    if is_exit(row, col, matrix):
        unique_paths.append(1)
        return

    matrix[row][col] = 'v'

    play(row + 1, col, matrix, unique_paths)
    play(row, col + 1, matrix, unique_paths)

    matrix[row][col] = '-'

    return sum(unique_paths)

row = int(input())
col = int(input())
matrix = []

for _ in range(row):
    matrix.append(['-'] * col)

matrix[row - 1][col - 1] = 'e'

print(play(0, 0, matrix, []))
