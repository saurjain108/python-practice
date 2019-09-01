
import csv
with open('SampleCSVFile_119kb.csv', 'r') as filee:
    aaa = csv.reader(filee)
    with open('newest.csv', 'w') as bbb:
        csv_writer = csv.writer(bbb)
        for i in aaa:
            csv_writer.writerow(i)
            
