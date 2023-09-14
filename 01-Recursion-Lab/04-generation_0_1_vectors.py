def gen_vec(index, vector):
    if index == len(vector):
        print(*vector, sep='')
        return
    for i in range(2):
        vector[index] = i
        gen_vec(index + 1, vector)


num = int(input())
vector = [0] * num

gen_vec(0, vector)
