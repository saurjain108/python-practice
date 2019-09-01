import csv
with open('pokemon_data.csv', 'r') as filee:
    aaa = csv.DictReader(filee)
    for i in aaa:
        print(i['Name'])
        
