#this is use for writting the conent of one file into anotheer filee

a = open('abc.txt','r')
# opened the file which we already have available in the sysyem

b = open('newwwwwwwwwwwwwwwwwwww_abc.txt', 'w')
#created a file in which we are going to write the data

b.write(a.read())
#read the data from a and write that in b

b.close()
#close the file

b= open(b.name, 'r+')
#open the file with "r+", which will allow to read and write in the file 

print(b.read())
#printing the content of the new file

