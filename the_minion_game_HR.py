# def isVowel(val):
#     if (val=="A" or val=="E" or val=="I" or val=="O" or val=="U"):
#         return "vow"
#     elif (val>=chr(65) and val<=chr(90)):
#         return "con"
    

# def minion_game(string):
#     # your code goes here
#     Kevincount=0
#     Stuartcount=0
#     allPossibleSubstring=[string[i:j] for i in range(len(string)) for j in range(i+1, len(string)+1)]
    
#     for substring in allPossibleSubstring:
       
#         if (isVowel(substring[0])=="vow" and substring.isupper() ):
#             Kevincount+=1
            
#         elif (isVowel(substring[0])=="con" and substring.isupper()):
#             Stuartcount+=1
        
#     print(Kevincount)  
#     print(Stuartcount)  
#     if Kevincount>Stuartcount:
#         print(f"Kevin {Kevincount}")
#     elif Stuartcount>Kevincount:
#         print(f"Stuart {Stuartcount}")
#     else:
#         print("Draw")
        

# if __name__ == '__main__':
#     s = input()
#     minion_game(s)


def minion_game(string):
    # your code goes here
    Stuart=0
    Kevin=0
    string=string.upper()
    vowels=['A','E','I','O','U']
		
    for i in range(len(string)):
        if string[i] not in vowels:
            Stuart+=(len(string)-i)
        else:
            Kevin+=(len(string)-i)
						
    if Stuart>Kevin:
        print('Stuart',Stuart)
    elif Stuart<Kevin:
        print("Kevin",Kevin)
    else:
        print("Draw")
            

if __name__ == '__main__':
    s = input()
    minion_game(s)