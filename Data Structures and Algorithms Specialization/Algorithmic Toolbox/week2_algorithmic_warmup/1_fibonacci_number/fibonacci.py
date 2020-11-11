# Uses python3
def calc_fib(n):
    fib_series = [0,1]
    for i in range(2,n+1):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series[n]

n = int(input())
print(calc_fib(n))
