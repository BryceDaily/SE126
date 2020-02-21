#Bryce Daily
#Lab4B
#1/31/20
#cont - continue
#rows - List
#aslA - List
#aslB - List
#aslC - List
#aslD - List
#rw - Which row the passenger would like to sit in
#se - Which seat the passenger would like to sit in
import os
def continues():
    cont = input("\t\t\t\tDo you want to continue?(y/n)")
    cont = cont.upper()

    while(cont != "N") and (cont != "Y"):
        cont = input("\t\t\t\tDo you want to continue?(y/n)")
        cont = cont.upper()
    return cont

def display():
    print("\t\t\t\t\t",rows[index],aslA[index],aslB[index],"\t",aslC[index],aslD[index])

def row():
    rw = int(input("\t\t\t\tWhich row would you like to sit in? "))
    return rw

def seat():
    se = input("\t\t\t\tWhich seat woud you like to sit in? ")
    se = se.upper()
    return se

def checker(se,rw,aslA,aslB,aslC,aslD):
    if(se == "A" and aslA[rw] == "X"):
        print("\t\t\t\tSorry that seat is taken please selec a different one.")
    elif(se == "B" and aslB[rw] == "X"):
        print("\t\t\t\tSorry that seat is taken please selec a different one.")
    elif(se == "C" and aslC[rw] == "X"):
        print("\t\t\t\tSorry that seat is taken please selec a different one.")
    elif(se == "D" and aslD[rw] == "X"):
        print("\t\t\t\tSorry that seat is taken please selec a different one.")

def assign(se):
    if(se == "A"):
        aslA[rw] = "X"
    elif(se == "B"):
        aslB[rw] = "X"
    elif(se == "C"):
        aslC[rw] = "X"
    elif(se == "D"):
        aslD[rw] = "X"


rows = ["",1,2,3,4,5,6,7]
aslA = ["","A","A","A","A","A","A","A"]
aslB = ["","B","B","B","B","B","B","B"]
aslC = ["","C","C","C","C","C","C","C"]
aslD = ["","D","D","D","D","D","D","D"]

cont = "Y"

while(cont == "Y"):
    for index in range (1,8):
        display()
    rw = row()
    se = seat()
    checker(se,rw,aslA,aslB,aslC,aslD)
    assign(se)
    
    
    for index in range (1,8):
        display()
    cont = continues()
    os.system("cls")