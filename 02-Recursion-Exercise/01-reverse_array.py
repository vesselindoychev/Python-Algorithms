def reverse_array(numbers, index, res):
    if index == len(numbers):
        return
    reverse_array(numbers, index + 1, res)
    res.append(numbers[index])
    return ' '.join(list(map(str, res)))


numbers = [int(x) for x in input().split()]

print(reverse_array(numbers, 0, []))
