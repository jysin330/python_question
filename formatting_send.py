from formatting import format_msg
from requests import get
# import sys

def send (name, website = None, verbose= False):
    if website != None:
        msg = format_msg(my_name=name, my_website=website)
        
    else:
        msg = format_msg(my_name = name)
        
    if verbose:
        print(name, website)
    r = get("https://httpbin.org/json")
    
    if r.status_code == 200:
        return r.json()
    else:
        return "there was an error"
    

if __name__ == "__main__":  
    # print(sys.argv)
    # name = 
    response= send("jyoti","cfe", verbose=True)

    print(response)

# print(r.json())
# print(r.status_code)