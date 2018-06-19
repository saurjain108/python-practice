#first Method
a = open('abc.txt','r')
b = a.read()
c = b.split()

z =(input("please enter your name to check in list: \n"))

for i in c:
        if i == (z):
                print(f"{z},Yes you're in")
	#	break               
        else:
                print(f"{z}, Sorry! you're not in")
	#	break
