#print ("hello") 
#bubblesort

def bubblesort(my_list):
	for i in range(0,len(my_list)-1):
		for j in range(0,len(my_list)-1-i):
			if my_list[j] > my_list[j+1]:
				my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
	return my_list

my_list = [43,576,3,8,23,83,8,9,654,4,433,6565]

print(bubblesort(my_list))
