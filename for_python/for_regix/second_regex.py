import os
way = r"/home/raunak/for_python/for_regix"
for i in (os.listdir(way)):
	j = (i[len(i)-3::])
	if j == 'txt':
		print(f"{i}, this is txt file.")
	else:
		print(f"{i}, this is not a text file.")	
