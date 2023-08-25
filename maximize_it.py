

if __name__ == "__main__":
    li = input().split(" ")
    list = [input().split(" ", 1) for i in range(int(li[0]))]

alllist = []

for i in list:
    alllist.append(i[1].split(" "))


# sum = 0
# for val in alllist:
#     i = 0
#     while (i < len(val)):
#         val[i] = int(val[i])
#         i += 1
#     sum += (max(val)*max(val))

# result = sum % int(li[1])
# func(alllist, 0)
# print(alllist)
# print(result)
