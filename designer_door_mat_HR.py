# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
if __name__ == '__main__':
    string = input().split()
  
x="-"
y=".|."
z=y
str="WELCOME"
n=int(string[0])
m=int(string[1])

for i in range(0,n):
    if(i<math.floor(n/2)):
       print(y.center(m,x))
       y=y+z+z
       
    elif(i==math.floor(n/2)):
        print(str.center(m,x))
     
    else:
         y=y[0:(len(y)-6)]
         print(y.center(m,x))
