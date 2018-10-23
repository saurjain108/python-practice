import re
import os
way = "/root/python-practice/for_python"
a = []
txt = []
py = []
other = []
for i in os.listdir(way):
	a.append(i)

r = re.compile(".*py")
newlist = list(filter(r.match, a))
print(newlist)
print("*****************************************************************************************")
print(a)
