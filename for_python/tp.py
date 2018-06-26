a = str(input("Enter a name: "))

with open('names.txt', 'r') as f:
	j = f.read().split()
	for i in j:
		if i == a:
			print(i)
	
