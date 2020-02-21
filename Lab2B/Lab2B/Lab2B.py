#Lab2B
#Bryce Daily
#Variables Used:
#num_records - number of records
#w - place holder for the csv.reader

def assignments():
    if(record[1] == "DL"):
        record[1] = "Dell"
    elif(record[1] == "GW"):
        record[1] = "Gateway"
    if(record[0] == "D"):
        record[0] = "Desktop"
    else:
        record[0] = "Laptop "

import csv

num_records = 0
print("Type       Brand      CPU        Ram      1st Disk  No HDD      2nd Disk     OS         Year")
with open("G:\DataFiles\lab2b-1.csv") as csvfile:
    w = csv.reader(csvfile)
    for record in w:
        assignments()
        if(int(record[5]) == 1):
            print("{:10} {:10} {:10} {:10} {:10} {:10}            {:10} {:10}".format(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]))
        else:
            print("{:10} {:10} {:10} {:10} {:10} {:10} {:10} {:10} {:10}".format(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8]))
        num_records = num_records + 1

print("Records Processed,",num_records)