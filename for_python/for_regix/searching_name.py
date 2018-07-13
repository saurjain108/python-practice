import re

name = open("names.txt", 'r')
data = name.read()
name.close()
#print(data.replace('@teamtreehouse', '@gmail'))

"""print(re.search(r'[r]aunak',data))
print(re.search(r'[j]ain',data))
print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}',data)) # finding all contact numbers
print(re.findall(r'\w*, \w+', data))"""
print(re.findall(r'[\w\d+.-]+@[\d\w.]+',data)) 
print(re.findall(r'\b[trehous]{9}\b',data, re.IGNORECASE)) # finds all treehouse words
print(re.findall(r'\b@[-\b\w.]*[^gov\t]+\b',data,re.IGNORECASE)) # ignores the gov 
