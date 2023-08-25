if __name__ == '__main__':
    N = int(input())

list=[]
for i in range(1,N+1):
    command=input().split(" ")
    list.append(command)
obtlist=[]
for i in list:
    match i[0]:
        case "insert":
            obtlist.insert(int(i[1]),int(i[2]))
        case "print":
            print(obtlist)
        case "remove":
            obtlist.remove(int(i[1]))
        case "append":
            obtlist.append(int(i[1]))
        case "sort":
            obtlist.sort()
        case "pop":
            obtlist.pop()
        case "reverse":
            obtlist.reverse()
