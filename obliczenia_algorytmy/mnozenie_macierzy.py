import random as rnd

SIZE = 8

a = [[rnd.randint(0, 10) for i in range(SIZE)] for j in range(SIZE)]
b = [[rnd.randint(0, 10) for i in range(SIZE)] for j in range(SIZE)]

output = [[0 for i in range(SIZE)] for j in range(SIZE)]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            output[i][j] += a[i][k] * b[k][j]

print(output)
