import random as rnd

SIZE = 8

a = [[rnd.randint(0, 10) for i in range(SIZE)] for j in range(SIZE)]


def det(M):
    if len(M) == 1:
        return M[0][0]
    if len(M) == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]

    output = 0
    for i in range(len(M)):
        w = [row[:i] + row[i+1:] for row in (M[:0]+M[1:])]
        output += ((-1) ** i) * M[0][i] * det(w)
    return output


print(det(a))
