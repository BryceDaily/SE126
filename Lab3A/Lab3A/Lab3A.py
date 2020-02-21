#Bryce Daily
#Lab3A
#Variables used:
#desk - total desktops
#lapt - total laptops
#deskCost - Total desktop cost
#laptCost - Total Laptop cost
#num_records - Number of records
#csvfile - Place holder for the path to the file
#w - Place holder for csv.reader()
#record - holds the list items 

import csv
desk = 0
lapt = 0
deskCost = 0
laptCost = 0
num_records = 0
with open("..\lab3a.csv") as csvfile:
    w = csv.reader(csvfile)
    for record in w:
        print(record)
        num_records = num_records + 1
        if(int(record[5]) == 1):
            if(int(record[7]) <= 17):
                if(record[0] == "D"):
                    desk = desk + 1
                    deskCost = deskCost + 2000
                elif(record[0] == "L"):
                    lapt = lapt + 1
                    laptCost = laptCost + 1500

        elif(int(record[5]) == 2):
            if(int(record[8]) <= 17):
                if(record[0] == "D"):
                    desk = desk + 1
                    deskCost = deskCost + 2000
                elif(record[0] == "L"):
                    lapt = lapt + 1
                    laptCost = laptCost + 1500

print(" ",desk,"Desktops need to be replaced for $",deskCost)
print(" ",lapt,"Laptops need to be replaced for $",laptCost)
