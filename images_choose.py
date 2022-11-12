import os
root_path="./image"
index=0
for idx,i in enumerate(os.listdir(root_path)):
    filename=os.path.join(root_path,i)
    
    if idx%6==0:continue
    os.remove(filename)