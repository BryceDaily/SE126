#Bryce Daily
#Lab4A
#Variables used:
#num_records - Number of records
#rom - Counter for number of computers with over 8GBs of RAM
#ram - List
#csvfile - Place holder for the path to the file
#w - Place holder for csv.reader()
#record - Holds the list items 

import csv
rom = 0
ram = []
num_records = 0
with open("..\lab3a.csv") as csvfile:
    w = csv.reader(csvfile)
    for record in w:
        ram.append(int(record[3]))
        num_records = num_records + 1
    for index in range(0,num_records):
        if(ram[index] > 8):
            rom = rom + 1
    print("There are",rom,"computers with over 8GBs of RAM.")