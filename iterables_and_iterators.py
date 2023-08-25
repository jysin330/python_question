from itertools import combinations

if __name__=="__main__":
    length=int(input())
    str= list(input().split(" "))
    a=int(input())

list2 = list(combinations(str,a))
count=0

for tuple in list2:
    tuple=list(tuple)
    if "a" in tuple:
        count+=1
    else:
        count=count
result=count/len(list2)
print(f"{result:.4f}")
    