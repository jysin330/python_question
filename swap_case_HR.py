def swap_case(s):
    results=list(s)
    string=''
    for i in results:
        if i.isupper():
            i=i.lower()
            string+=i
        elif i.islower():
            i=i.upper()
            string+=i
        else:
            string+=i
    return string
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
    