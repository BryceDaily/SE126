#Bryce Daily
#Lab5B


def replace():
    d = 0
    for index in range(0,size):
        if(dept[index] == "MIS"):
            a = email[index]
            b = a.replace(".com",".net")
            d += 1
            print(b)
    return d

import csv
import os

fNme = []
lNme = []
pNum = []
email = []
dept = []
pos = []

cont = "Y"


with open("G:\DataFiles\Lab5b.txt") as csvfile:
    w = csv.reader(csvfile)
    for record in w:
        fNme.append(record[0])
        lNme.append(record[1])
        pNum.append(record[2])
        email.append(record[3])
        dept.append(record[4])
        pos.append(record[5])

size = len(fNme)

print("\nThere were",replace(),"emails changed.")