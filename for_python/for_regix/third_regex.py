
i = []

with open('abc.txt', 'r') as j:
	i.append((j.read().split()))
	print(i)
with open('new_abc.txt', 'w') as k:
	k.write(str(i))

