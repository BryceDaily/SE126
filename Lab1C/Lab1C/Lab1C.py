#Lab1C
#Bryce Daily
#1/10/2020
#Variables used:
#mCap - Maximum Capacity -integer
#att - # of people attending -integer
#dif - difference of capcity and people attending
#cont - while loop continue
#capacity - function
#atendees - function
#people - number of people attending
#register - function
#continues - function
#difference - difference in number of people atteding and capacity
# # # # - - - - - - # # # # 

# Functions

def capacity():
    size = int(input("Please enter the maximum capacity of the room. "))
    return size

def atendees():
    people = int(input("Please enter the number of people attending the meeting. "))
    return people

def register(size,people):
    difference = mCap - att
    return difference

def continues():
    cont = input("Do you want to check anymore rooms?(y/n)")
    cont = cont.upper()
    while(cont != "N") and (cont !="Y"):
        cont = input("Do you want to check anymore rooms?(y/n)")
        cont = cont.upper()
    return cont

# Main Code

cont ="Y"
while(cont == "Y"):
    mCap = capacity()
    att = atendees()

    dif = register(mCap,att)
    
    if(dif>=0):
        print("The meeting can be held, there are,",dif,"spots available.")
    else:
        dif = dif * -1
        print(dif,"People need to be asked to leave.")
    cont = continues()