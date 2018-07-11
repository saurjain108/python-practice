import re

pattern = r"Python"
sequence = "Python"
if re.match(pattern, sequence):
  print("Match is success!")
else: print("match is not success !")

# the '.' is used for any character except new line
a = re.search(r'Pyt..n', 'Python').group()
print(a)

#the '\w' is used for any single letter or digit or underscore	
b= re.search(r'P\wtho\w', 'Python').group()
print(b)

# the '\W' matches with the any character except the \w group
c = re.search(r'R\Wunak', 'R@unak').group()
print (c)

#the \s matches with single white space
d = re.search(r'hi\shello', 'hi hello').group()
print(d)

#the \S matches with single white space which is not part of \s
e = re.search(r'raun\Sk', 'raunak').group()
print(e)
 
