import re

name = open("names.txt", 'r')
data = name.read()
name.close()

print(re.search(r'[r]aunak',data))
print(re.search(r'[j]ain',data))
print(re.search(r'\(\d{3}\) \d{3}-\d{4}',data))
print(re.search(r'\w+,\w+', data))
