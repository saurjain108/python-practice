import re

name = open("names.txt", 'r')
data = name.read()
name.close()

print(re.search(r'[r]aunak',data))
print(re.search(r'[j]ain',data))

