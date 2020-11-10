# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])
    return max_product

def max_pairwise_product_fast(numbers):
    index1 = 0
    for i in range(1,len(numbers)):
        if numbers[i] > numbers[index1]:
            index1 = i
    index2 = 0
    if index1 == 0:
        index2 = 1
    for i in range(1,len(numbers)):
        if index1 != i and numbers[i] > numbers[index2]:
            index2 = i
    return numbers[index1] * numbers[index2]



if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
