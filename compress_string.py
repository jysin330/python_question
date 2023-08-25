from itertools import groupby

# def func(n):
#     return n
if __name__=="__main__":
    string=input()
    
# for key, group in groupby(string, func):
for key, group in groupby(string, lambda x: x):
    print(f"({len(list(group))}, {key})", end=" ")
    
