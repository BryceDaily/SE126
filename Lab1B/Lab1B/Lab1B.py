#Lab1B
#Bryce Daily
#1/10/2020
#Variables used:
#mCap - Maximum Capacity -integer
#att - # of people attending -integer
#dif - difference of capcity and people attending
#cont - while loop continue
#
# # # # - - - - - - # # # # 
import os

cont ="Y"
while(cont == "Y"):
    mCap = int(input("Please enter the maximum capacity of the room. "))
    att = int(input("Please enter the number of people attending the meeting. "))

    dif = mCap - att
    
    if(dif>=0):
        print("The meeting can be held, there are,",dif,"spots available.")
    else:
        dif = dif * -1
        print(dif,"People need to be asked to leave.")
    cont = input("Do you want to check anymore rooms?(y/n)")
    cont = cont.upper()
    while(cont != "N") and (cont !="Y"):
        cont = input("Do you want to check anymore rooms?(y/n)")
        cont = cont.upper()