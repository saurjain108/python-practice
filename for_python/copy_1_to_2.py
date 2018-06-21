
a = open('aaa.txt', 'r')
#print(a.read().split())
#b= a.read()
b = open('bbb.txt', 'w')
for i in (a.read().split()):
#	print(i)
	b.write(i)
	b.write('\n')
#b.close()
#print('\n\n\n')
#b.open('bbb.txt','r')
#print(b.read())

