# import os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# files_dir = os.path.join(BASE_DIR, "images")

# # if  not os.path.exists(files_dir):
# #     print("this path is not valid")


# os.makedirs(files_dir, exist_ok=True)

# my_image= range(0,5)

# for x in my_image:
#     fname = f'img{x}.txt'
    
#     file_path = os.path.join(files_dir, fname)
    
#     if os.path.exists(file_path):
#         print(f'skipped')
#         continue
    
#     with open(file_path, "w") as f:
#         f.write(f"hello didi ,how are you {x}")



import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_name = os.path.join(BASE_DIR, "image1")

os.makedirs(file_name, exist_ok=True)

file_range = range(0,3)

for i in file_range:
    fname = f'image{i}.txt'
    fpath = os.path.join(file_name, fname)
    if os.path.exists(fpath):
        print("skipped")
        continue
    
    with open(fpath, 'w') as f:
        f.write(f"hey there everyone {i}")