
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product


def fun(list):

    for i, num in enumerate(list):
        list[i] = int(num)

    return list


if __name__ == "__main__":
    a = input().split(" ")
    b = input().split(" ")

a = fun(a)
b = fun(b)

num = list(product(a, b))
for i in num:
    print(i, end=", ")
