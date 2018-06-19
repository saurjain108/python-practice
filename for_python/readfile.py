#first Method
a = open('abc.txt','r')
b = a.read()
c = b.split()
for i in c:
	print(i)
	print(len(i))


#Second Method
words = open('abc.txt').read().split()
for j in words:
	print(j)
	print(len(j))
