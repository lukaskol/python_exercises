a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

output = 0

for i in range(len(a)):
    output += a[i] * b[i]

print(output)