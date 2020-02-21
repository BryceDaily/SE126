#Bryce Daily
#Lab3B
#Variables used:
#type - list      
#numhdd - list
#year - List
#desk - total desktops
#lapt - total laptops
#deskCost - Total desktop cost
#laptCost - Total Laptop cost
#num_records - Number of records
#csvfile - Place holder for the path to the file
#w - Place holder for csv.reader()
#record - holds the list items 




import csv

# Variables -------------------------------
desk = 0
lapt = 0
deskCost = 0
laptCost = 0
num_records = 0

# Lists ---------------------------------------------------
type = []      
numhdd = []
year = []

# Main Code -------------------------------------------------------------
with open("..\lab3a.csv") as csvfile:
    w = csv.reader(csvfile)
    for record in w:
        num_records = num_records + 1
        type.append(record[0])              # Appeding type to record 0
        numhdd.append(int(record[5]))       # Appeding numhdd to record 5
        if(int(record[5]) == 1):
            year.append(int(record[7]))     # Appeding year to record 7

        elif(int(record[5]) == 2):
              year.append(int(record[8]))   # Appeding year to record 8

#   Processing the records
for index in range(0, num_records):
    if(year[int(index)] <= 18):         # Checking to see if the list items are less than 18
        if(type[index] == "D"):         # Checking to see if they are a Desktop
            desk = desk + 1             # Adding 1 to the total number of desktops
            deskCost = deskCost + 2000  # Adding 2000 to the total cost for the Desktops
               
        elif(type[index] == "L"):       # Checking to see if they are a Laptop
            lapt = lapt + 1             # Adding 1 to the total number of Laptops
            laptCost = laptCost + 1500  # Adding 1500 to the total cost for the Laptops

print(" ",desk,"Desktops need to be replaced for $",deskCost)
print(" ",lapt,"Laptops need to be replaced for $",laptCost)
print("  Number of Records Processed,",num_records)