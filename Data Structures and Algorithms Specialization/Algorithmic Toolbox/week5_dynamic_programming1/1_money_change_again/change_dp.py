# Uses python3
import sys
import math

def get_change(money):
    #write your code here
    MinNumCoins = [0] * (money + 1)
    coins = [1, 3, 4]
    for m in range(1, money + 1):
        MinNumCoins[m] = math.inf
        for coin in coins:
            if m >= coin:
                NumCoins = MinNumCoins[m - coin] + 1
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins
    return MinNumCoins[money]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
