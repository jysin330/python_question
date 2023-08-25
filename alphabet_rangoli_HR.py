def print_rangoli(size):
    # your code goes here
    
    i=size+(size-1)
    j=size+(size-1)*3
    x='-'
    y=size-1
    r=1
    str= "-"+chr(96+size)+"-"
    if(size>=1 and size<=26):
        for k in range(0,i):
            if(k<size-1):
                print(str.center(j,"-"))
                str= str[0:len(str)-r]+"-"+chr(96+y)+"-"+str[r:]
                y=y-1
                r+=2
            elif(k==size-1):
                str=str.strip("-")
                print(str)
            else:
                y+=1
                z=y+1
                word=chr(96+z)+"-"+chr(96+y)+"-"+chr(96+z)
                str=str.replace(word, f"{chr(96+z)}")
                print(str.center(j,"-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
