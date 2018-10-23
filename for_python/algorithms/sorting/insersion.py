#insersion sorting 
def insersion(l):
	for i in range(1,len(l)):
		for j in range(i-1,-1,-1):
			if l[j]>l[j+1]:
				l[j],l[j+1] = l[j+1],l[j]
			else:
				break

l = [21,43,2,6,323,75,4,8,5434,8,3434,7,5453,8,34,53,8432,43,8]
print(insersion(l))
		
 
