#Uses python3

import sys

def lcs2(a, b):
    #write your code here
    n = len(a)
    m = len(b)
    
    L = [[0 for x in range(m+1)] for y in range(n+1)]
    
    for i in range(n+1):
        for j in range(m+1):
            if (i == 0 or j == 0):
                L[i][j] = 0
            elif(a[i-1] == b[j-1]):
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1], L[i][j], L[i-1][j-1])
    
    return L[n][m]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
