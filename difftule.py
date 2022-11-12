import os 
root_path="./images"
root_path_annotations="./Annotations"
# path_list=os.listdir(root_path)
path_list=[]
# path_annotations_list=os.listdir(root_path_annotations)
path_annotations_list=[]
# for 
for i in os.listdir(root_path):
    name,_=os.path.splitext(i)
    path_list.append(name)
for i in os.listdir(root_path_annotations):
    name,_=os.path.splitext(i)
    path_annotations_list.append(name)
# for i in path_annotations_list:
for i in path_list:
    if i not in path_annotations_list:print(i)
    # if i not in path_list:print(i)