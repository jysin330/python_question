import os
folders=os.listdir("data")
# print(folders)
print(os.getcwd())
os.chdir("/Users/jyoti")
print(os.getcwd())
# for folder in folders:
#     print(os.listdir(f"data/{folder}"))