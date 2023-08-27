def recursion(str):
    if str != '':
        li = list(str)
        i = str[0]
        if li.count(str[0]) > 1:
            string = str.replace(i, '')
            return i + recursion(string)
        else:
            string = str[1:]
            return i + recursion(string)
    else:
        return ''


def merge_the_tools(string, k):
    # your code goes here
    if k > 1:

        li = []
        a = 0
        for i in range(0, k):
            li.append(string[a:k+a])
            a += k

        for i in li:
            print(recursion(i))
    else:
        li = list(string)
        for i in li:
            print(i)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
