def count_substring(string, sub_string):
   
    count=0
    i=0
    while(i<5):
       index=i
       i=string[i:].find(sub_string)
       print(i)
       count+=1
       i=i+1
       if(i==-1):
           count=0
           
        
       print(string[i:])
    
        
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    # print(count)