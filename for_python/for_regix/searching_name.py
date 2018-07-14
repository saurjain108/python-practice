import re
name = open("names.txt", 'r')
data = name.read()
name.close()
#print(data.replace('@teamtreehouse', '@gmail'))

"""print(re.search(r'[r]aunak',data))
print(re.search(r'[j]ain',data))
print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}',data)) # finding all contact numbers
print(re.findall(r'\w*, \w+', data))"""
#print(re.findall(r'[\w\d+.-]+@[\d\w.]+',data)) 
#print(re.findall(r'\b[trehous]{9}\b',data, re.IGNORECASE)) # finds all treehouse words
#print(re.findall(r'\b@[-\b\w.]*[^gov\t]+\b',data,re.IGNORECASE)) # ignores the gov 
#print(re.findall(r'\b[-\w]+,\s[-\w ]+[^\t\n]',data,re.X))# searching all names
line = re.compile(r'^(?P<name>[-\w ]*,\s[-\w ]+)\t(?P<email>[-\w\d.+]+@[-\w\d.]+)\t(?P<contact>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t(?P<job>[\w\s.]+,\s[\w\s.]+)\t?(?P<twitter>@[\w\d]+)?$',re.X|re.MULTILINE)
#print(line)
print(re.search(line, data).groupdict())
print(line.search(data).groupdict())
for match in line.finditer(data):
	print(match.group('name','email','contact'))
