# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    value = [[0 for i in range(W+1)] for j in range(len(w))]
    result = 0
    for x in range(0, len(w)):
        for y in range(1, W+1):
            value[x][y] = value[x-1][y]
            if w[x] <= y:
                val = value[x-1][y-w[x]] + w[x]
                if value[x][y] < val:
                    value[x][y] = val
    return value[len(w)-1][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
