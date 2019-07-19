import csv
mylist = []
revise = open('SampleCSVFile_119kb.csv', 'r')
reader_revise = csv.reader(revise)
for row in reader_revise:
    mylist.append(row)
    #print(row)
print(mylist[3][3])
