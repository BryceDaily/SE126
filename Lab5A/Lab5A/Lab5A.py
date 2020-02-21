#Bryce Daily
#Lab5A
#2/14/20
#Variables used:
#

import csv
import os

ip = []

with open("G:\DataFiles\Lab5a.txt") as csvfile:
    w = csv.reader(csvfile)
    for record in w:
        ip.append(record[0])

size = len(ip)

for i in range(0,size):
    if(ip[i] >= "128.0" and ip[i] <= "191.255"):
        print("{:15} Subnet mask is, 255.255.0.0".format(ip[i]))