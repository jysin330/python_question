import os


this_file_path = os.path.abspath(__file__)
print(this_file_path)
BASE_DIR = os.path.dirname(this_file_path)
print(BASE_DIR)
# BASE_DIR2 = os.path.dirname(BASE_DIR)
# print(BASE_DIR2)
# BASE_DIR3 = os.path.dirname(BASE_DIR2)
# print(BASE_DIR3)
email_text = os.path.join("file_manager.txt")
# email_text = 'file_manager.txt'
# with open(email_text, 'w') as f:
#     f.write("hello world")
    
content =''    
with open(email_text, 'r') as f:
    content = f.read()
print(content.format(name= "jyoti"))
# content1= content.format(name= "jyoti")


# with open(email_text, 'w') as f:
#     f.write(content1)   
# print(content.format(name= "jyoti"))
    