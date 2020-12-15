import random as rnd

SIZE = 128

a = [[rnd.randint(0, 10) for i in range(SIZE)] for j in range(SIZE)]
b = [[rnd.randint(0, 10) for i in range(SIZE)] for j in range(SIZE)]

output = [[sum(x) for x in zip(a[i], b[i])] for i in range(len(a))]

print(output)
