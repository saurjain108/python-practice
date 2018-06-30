import os

way = r"/home/raunak/for_python"

for i in (os.listdir(way)):
	print(i)
for roots, dirs, files in os.walk(way):
	for file in files:
		print("file= %s" %file)
	for dir in dirs:
                print("directory =%s" %dir)	
#	for root in roots:
#               print(root)
