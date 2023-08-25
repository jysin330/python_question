from itertools import permutations

if __name__ == "__main__":
    a = input().split(" ")
    string = a[0]


an = list(permutations(string, int(a[1]))).sort()
for i in an:
    str = ''
    for j in i:
        str += j
    print(str)
    str = ""
