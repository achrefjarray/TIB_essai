
# coding: utf-8

# In[ ]:


#Generate train.txt file for darknet yolov3 model training from directory of annotation files

from os import listdir

files = listdir("Annotations") #folder containing .txt annotation files

#Change above fields as required

f = open("train.txt", "w+")
for file in files:
        ending = file[:-4]
        f.write(ending+"\n") 
        

