
my_list = [1,2,3,4,5,'a','b','c','d']
print(my_list)
print (my_list[1:5])
print (my_list[1:])
print (my_list[::-1])
print (len(my_list))
my_list[2] = 'a'
print(my_list[2])
my_list += [2,4,6,'g']
my_list.append(5)

print(my_list)
my_list.remove('c')
my_list.pop()

my_list.pop(0)
print (my_list)
