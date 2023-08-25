def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    if (n%k==0):
        str=[string[i:i+k] for i in range(0, len(string), k)]
    i=0 
    new_str=[]
    while (i<len(str)):
        word=str[i]
        wr=""
        for s in range(0,len(word)):
            if(s+1<len(word)):
                if (word[s]==word[s+1]):
                    wr+=word[s]
                else:
                    wr=word[s]+word[s+1]
            else:
                wr+=word[s]
            
                    
                    
        new_str.append(wr)
        i+=1
    print(new_str)
       
                
            
            
            
            
        
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

