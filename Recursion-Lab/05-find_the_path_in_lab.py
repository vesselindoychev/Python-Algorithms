def is_outside(row, col, matrix):
    if row >= len(matrix) or col >= len(matrix) or row < 0 or col < 0:
        return True


def is_exit(row, col, matrix):
    if matrix[row][col] == 'e':
        return True


def is_wall(row, col, matrix):
    if matrix[row][col] == '*':
        return True


def find_path(row, col, matrix, direction, path):
    if is_outside(row, col, matrix):
        return

    if is_wall(row, col, matrix):
        return

    if matrix[row][col] == 'v':
        return

    path.append(direction)

    if is_exit(row, col, matrix):
        print(''.join(path))
        path.pop()
        return

    matrix[row][col] = 'v'

    find_path(row - 1, col, matrix, 'U', path)
    find_path(row + 1, col, matrix, 'D', path)
    find_path(row, col - 1, matrix, 'L', path)
    find_path(row, col + 1, matrix, 'R', path)

    matrix[row][col] = '-'

    path.pop()


rows = int(input())
cols = int(input())

matrix = []
path = []
for _ in range(rows):
    matrix.append(list(input()))

find_path(0, 0, matrix, '', [])
