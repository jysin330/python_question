if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

i =[a for a in range(0,x+1)]
j=[b for b in range(0,y+1)]
k=[c for c in range(0,z+1)]
# list=[]
# for list1 in i:
#     for list2 in j:
#         for list3 in k:
#             l=[list1,list2,list3]
#             list.append(l)
# print(list)
            
list=[[list1,list2,list3] for list1 in i for list2 in j for list3 in k]
print(list)
list1=[]
for l1 in list:
    sum=0
    for l in l1:
        sum+=l
    if sum!=n:
        list1.append(l1)
print(list1)
        
    

