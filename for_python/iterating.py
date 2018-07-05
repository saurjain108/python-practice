import os
way = r"/home/raunak/for_python"
print (os.system('ls| grep -r aaa'))
#for i in (os.listdir(way)):
#	print(i)
#	if 'aaa' in open(i).read():
#		print(i)

if 'haha' in open('example.txt').read():
    print("true")

