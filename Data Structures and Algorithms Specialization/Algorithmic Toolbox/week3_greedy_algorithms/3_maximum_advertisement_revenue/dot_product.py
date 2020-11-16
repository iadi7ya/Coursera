#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    
    res = 0
    #j, k = zip(*sorted(zip(a, b), key=lambda x: x[0]*x[1], reverse=True))
    #j, k = list(j), list(k)
    j = sorted(a)
    k = sorted(b)
    res = sum(x * y for x, y in zip(j, k))
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
