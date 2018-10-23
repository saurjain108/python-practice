import re
import os
way = "/root/python-practice/for_python"
python = []
text = []
other = []
for i in os.listdir(way):
	if re.match(r'.*py',i):
		python.append(i)
	elif re.match(r'.*txt',i):
		text.append(i)
	else:
		other.append(i)
print("******************************************************")
print(other)
print("******************************************************")
print(text)
print("******************************************************")
print(python)
print("******************************************************")

with open('pythonfile.txxt','w') as q:
	for j in python:
		q.write(j)


