# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0
    A = [0]*len(weights)
    # write your code here
    values, weights = zip(*sorted(zip(values, weights), key=lambda x: x[0]/x[1], reverse=True))
    values, weights = list(values), list(weights)
    for i in range(n):
        if capacity == 0:
            return value
        a = min(weights[i], capacity)
        value = value + a * values[i]/weights[i]
        weights[i] = weights[i] - a
        A[i] = A[i] + a
        capacity = capacity - a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
