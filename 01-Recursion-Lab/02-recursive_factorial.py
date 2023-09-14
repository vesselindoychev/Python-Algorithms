def calc_fact(num):
    if num == 0:
        return 1
    return num * calc_fact(num - 1)

num = int(input())

print(calc_fact(num))