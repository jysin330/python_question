from collections import Counter
from itertools import groupby


def integer(li):
    a = 0
    for i in li:
        li[a] = int(i)
        a += 1
    return li


if __name__ == "__main__":
    number_shoe = int(input())
    all_sizes = input().split(" ")
    all_sizes = integer(all_sizes)
    num_customers = int(input())
    size_and_price = []
    for i in range(0, num_customers):
        size_and_price.append(integer(input().split(" ")))
dict = dict(Counter(all_sizes))
# for k, g in groupby(size_and_price, lambda x: x[0]):
#     print(k, list(g))


# for a in dict:
    
    

