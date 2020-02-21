#Lab2A
#Bryce Daily
#Variables Used:
#num_records - number of records
#room - room name
#max - max room size
#attending - number of people atending
#w - place holder for the csv.reader
#over - how many people can't attend

import csv


num_records = 0


room = []   # creates an empty table (list) named room
max = []    # creates an empty table (list) named max
attending = [] # creates an empty table (list) named attending

with open("G:\DataFiles\lab2a.csv") as csvfile:
    w = csv.reader(csvfile)
    for record in w:
       room.append(record[0])           # appends the name to the room array (table)
       max.append(int(record[1]))       # appends the name to the max array (table)
       attending.append(int(record[2]))    # appends the name to the attending array (table)
       num_records = num_records + 1
print("Room                          Max              Attending              Over")
for index in range(0, num_records):             
    over = attending[index] - max[index]  
    
    if(max[index] < attending[index]):
        print("{:20}   {:10d}          {:10d}           {:10d}".format(room[index],max[index], attending[index], over))
print("Records Processed",num_records)
