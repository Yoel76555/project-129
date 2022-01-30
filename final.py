import csv
from email import header
bright_stars=[]
dwarf_stars=[]

with open("bright_stars.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        bright_stars.append(row)

with open("dwarf_stars.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dwarf_stars.append(row)

headers_1=bright_stars[0]
planet_data_1=bright_stars[1:]

headers_2=dwarf_stars[0]
planet_data_2=dwarf_stars[1:]

headers= headers_1+headers_2

planet_data=[]
for index, data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index]+planet_data_2[index])

with open("final.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)