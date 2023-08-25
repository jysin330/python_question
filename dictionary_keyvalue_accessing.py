dic={
    "name":"jyoti",
    "age":23,
    "eligible":True
}
print(dic["name"]) #throw an error if key is not found
print(dic.get("name")) #throw none if key is not found
print(dic.keys())
print(dic.values())
for key in dic.keys():
    print(dic[key])
    
print(dic.items())
for key, value in dic.items():
    print(f"the value of {key} is {value}")