x = int(input("Please enter an integer: "))
if x > 0 and x < 10:
	print("1 to 10")
elif  x > 10 and x < 20:
	print ("1 to 10")
else:
	print ("This number is larger than 20")


name = str(input("Enter you name: "))

if len(name)>=6:
	print("this is long name")
elif len(name)==5:
	print("the lenght is 5")
else:
	print("the name is short")

