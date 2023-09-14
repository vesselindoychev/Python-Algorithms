def find_fibonacci(num):
    if num <= 1:
        return 1
    return find_fibonacci(num - 1) + find_fibonacci(num - 2)


num = int(input())
print(find_fibonacci(num))


def get_fibonacci(number):
    fib0 = 1
    fib1 = 1
    result = 0

    for i in range(number - 1):
        result = fib0 + fib1
        fib0, fib1 = fib1, result
    return result


number = int(input())
print(get_fibonacci(number))