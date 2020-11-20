# Uses python3

import math

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def MinAndMax(m, M, op, i, j):

    minimum = math.inf
    maximum = -math.inf

    for k in range(i, j):
        a = evalt(M[i][k], m[k + 1][j], op[k])
        b = evalt(m[i][k], m[k + 1][j], op[k])
        c = evalt(M[i][k], M[k + 1][j], op[k])
        d = evalt(m[i][k], M[k + 1][j], op[k])

        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)

    return minimum, maximum


def get_maximum_value(dataset):

    op = dataset[1:len(dataset):2]
    d = dataset[0:len(dataset) + 1:2]
    n = len(d)

    m = [[0 for i in range(n)] for j in range(n)]
    M = [[0 for i in range(n)] for j in range(n)
            ]
    for i in range(n):
        m[i][i] = int(d[i])
        M[i][i] = int(d[i])

    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(m, M, op, i, j)
            
    return M[0][n - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
