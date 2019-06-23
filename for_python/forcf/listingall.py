import os
import glob

path = r"/root/python-practice/for_python/forcf/file/*"
files=glob.glob(path)
a = open("test.txt", "w")
for file in files:     
    f=open(file, 'r')    
    a.write(f.read())       
    f.close()
a.close()

