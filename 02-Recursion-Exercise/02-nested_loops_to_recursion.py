def calc(n, vector, index):
    if index == len(vector):
        print(*vector, sep=' ')
        return
    for i in range(1, n + 1):
        vector[index] = i
        calc(n, vector, index + 1)


n = int(input())
vector = [None] * n

calc(n, vector, 0)
