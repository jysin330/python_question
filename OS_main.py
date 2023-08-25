import os
if(not os.path.exists):
   os.mkdir("data")

for i in range(0,100):
    os.mkdir(f"data/day{i+1}")
    
