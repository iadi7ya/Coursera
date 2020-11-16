# Uses python3
#import sys

def get_change(m):
    coins = m//10 + (m%10)//5 + (m%10)%5
    return coins

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
