import csv
l = []

with open('SampleCSVFile_119kb.csv', 'r') as filee:
    aaa = csv.reader(filee)
    for i in aaa:
        l.append(i)
print(l)
with open('person.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(l)
csvFile.close()
