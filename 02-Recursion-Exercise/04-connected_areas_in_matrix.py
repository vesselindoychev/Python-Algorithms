def is_outside(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return True


def is_wall(row, col, matrix):
    if matrix[row][col] == '*':
        return True


def is_visited(row, col, matrix):
    if matrix[row][col] == 'v':
        return True


def explore_area(row, col, matrix, size):
    if is_outside(row, col, matrix):
        return
    if is_wall(row, col, matrix):
        return
    if is_visited(row, col, matrix):
        return

    matrix[row][col] = 'v'
    size.append(1)

    explore_area(row - 1, col, matrix, size)
    explore_area(row + 1, col, matrix, size)
    explore_area(row, col - 1, matrix, size)
    explore_area(row, col + 1, matrix, size)

    return sum(size)


rows = int(input())
cols = int(input())
matrix = []

for _ in range(rows):
    matrix.append(list(input()))

areas = []
for row in range(rows):
    for col in range(cols):
        size = explore_area(row, col, matrix, [])
        if size is not None:
            areas.append((row, col, size))

sorted_areas = sorted(areas, key=lambda x: ((x[2], -x[0], -x[1])), reverse=True)

print(f"Total areas found: {len(areas)}")
for index, area in enumerate(sorted_areas):
    print(f"Area #{index + 1} at ({area[0]}, {area[1]}), size: {area[2]}")
