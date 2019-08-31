import requests
"""url = "https://github.com/saurjain108/Docker/blob/master/commands.txt"
pic = "https://www.tutorialspoint.com/python/images/logo.png"
r = requests.get(url)
q = requests.get(pic)
print(dir(r))
#print(help(r))
#print(r.text)
with open('aaa.png', 'wb') as ff:
    ff.write(q.content)"""

"""hh = requests.get('https://file-examples.com/wp-content/uploads/2017/11/file_example_MP3_700KB.mp3')
print(hh.headers)
with open('test.mp3','wb') as sss:
    sss.write(hh.content)"""
"""payload = {'page': '2', 'count': 25}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.text)
print(r.url)"""

"""payload = {'username': 'raunakjain', 'passwd': 'testingg'}
r = requests.post('https://httpbin.org/post', data=payload)
r_dict = r.json()
print(r_dict['form'])
print(r.url)"""

"""payload = {'username': 'raunakjain', 'passwd': 'testingg'}
r = requests.get('https://httpbin.org/basic-auth/raunakjain/testingg',auth=('raunakjain','testingg'))
print(r)"""

#delay
payload = {'username': 'raunakjain', 'passwd': 'testingg'}
r = requests.get('https://httpbin.org/delay/6', timeout=3)
print(r)
