import textwrap

def wrap(string, max_width):
    i=0
    num=max_width
    str=""
    strn=""
    while(i<len(string)):
        for i in range (i,max_width):
            str += string[i]
        i+=1
        max_width+=num
        
        if(max_width>len(string)):
            max_width=len(string)
        strn+=str+"\n"
        str=""
        
    return strn

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)