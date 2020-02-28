#Bryce Daily
#Lab6A

import os
def start_screen():     # Selection menu
    print("\t\t\t\t1. Purchase Tickets")
    print("\t\t\t\t2. Total Ticket Sales.")
    print("\t\t\t\t3. Seats that have been sold.")
    print("\t\t\t\t4. Seat Availability.")
    print("\t\t\t\t5. Exit!")
    se = int(input("\t\t\t\tPlease make a selection. "))
    

    while(se != 1) and (se != 2) and (se != 3) and (se != 4) and (se != 5):
        se = int(input("\t\t\t\tPlease make another selection "))
    if(se == 5):
        print("Exiting.")
    return se

def seat_cost(r):    # Calculates the cost of the tickets
    if(r >= 1 and r <=5):
        pr = 200
    elif(r >=6 and r <= 10):
        pr = 175
    else:
        pr = 150
   
    return pr

def display(r):   # Displays the seat map
    os.system("cls")
    print("    A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  ", end="")
    print("V  W  X  Y  Z  1  2  3  4")
    for line in range(1, 16):
        print("{:2}  ".format(line), end="")
        for pos in range(1, 31):
            print(r[line][pos]," ", end="")
        print()

def sales():
    global t_sold
    t_sold = t_sold + 1   # Counts the number of tickets sold
    return t_sold


def ticket_sale():
    ti = int(input("How many tickets would you like to purchase. "))  # Asks for how many tickets are being purchased
    return ti

def seat_num(s):      # Sets the seat letter to a number
    s = s.upper()
    if(s == "A"):
        num = 1
    elif(s == "B"):
        num = 2
    elif(s == "C"):
        num = 3
    elif(s == "D"):
        num = 4
    elif(s == "E"):
        num = 5
    elif(s == "F"):
        num = 6
    elif(s == "G"):
        num = 7
    elif(s == "H"):
        num = 8
    elif(s == "I"):
        num = 9
    elif(s == "J"):
        num = 10
    elif(s == "K"):
        num = 11
    elif(s == "L"):
        num = 12
    elif(s == "M"):
        num = 13
    elif(s == "N"):
        num = 14
    elif(s == "O"):
        num = 15
    elif(s == "P"):
        num = 16
    elif(s == "Q"):
        num = 17
    elif(s == "R"):
        num = 18
    elif(s == "S"):
        num = 19
    elif(s == "T"):
        num = 20
    elif(s == "U"):
        num = 21
    elif(s == "V"):
        num = 22
    elif(s == "W"):
        num = 23
    elif(s == "X"):
        num = 24
    elif(s == "Y"):
        num = 25
    elif(s == "Z"):
        num = 26
    elif(s == "1"):
        num = 27
    elif(s == "2"):
        num = 28
    elif(s == "3"):
        num = 29
    elif(s == "4"):
        num = 30
    return num

def seat_availability(r,t):
    display(r)
    for i in range(0,tick):
        t = t - 1
    print("There are,",t,"tickets available.")
    

def select_seat():
    s = input("Which Seat would you like to sit in? ")
    return s

def select_row():
    r = int(input("Which Row would you like to sit in? "))
    return r

# Main Code


a1 = ["","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
a2 = ["","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
a3 = ["","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
a4 = ["","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
a5 = ["","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
a6 = ["","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
a7 = ["","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
a8 = ["","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
a9 = ["","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
a10 = ["","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
a11 = ["","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
a12 = ["","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
a13 = ["","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
a14 = ["","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
a15 = ["","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
rows = []


t_sold = 0
sold_subtotal = 0
cont = 0
tot_tick = 450

rows.append([])
rows.append(a1)
rows.append(a2)
rows.append(a3)
rows.append(a4)
rows.append(a5)
rows.append(a6)
rows.append(a7)
rows.append(a8)
rows.append(a9)
rows.append(a10)
rows.append(a11)
rows.append(a12)
rows.append(a13)
rows.append(a14)
rows.append(a15)
taken_seats = []

while(cont != 5):
    display(rows)
    cont = start_screen()
    # Selection 1
    if(cont == 1):
        display(rows)
        
        tick = ticket_sale()
        for i in range(0,tick):
            row = select_row()
            seat = select_seat()
            
            seat_number = seat_num(seat)
            if(rows[row][seat_number] == "#"):
                rows[row][seat_number] = "S"
                
            price = seat_cost(row)
            taken_seats.append(row)
            taken_seats.append(seat)
            taken_seats.append(int(price))
            sold_subtotal = sold_subtotal + price
        print("Your subtotal is: $",sold_subtotal)
        input("Press Enter to continue.")
    # Selection 2
    if(cont == 2):
        for i in range(0,tick):
            tot = sales()
        print("There were",tot,"tickets sold.")
        input("Press Enter to continue.")
    # Selection 3
    if(cont == 3):
        for i in range (0,tick):
            print("Seat:",taken_seats[0+i*3],taken_seats[1+i*3],taken_seats[2+i*3])
        print("Total cost so far: $",sold_subtotal)
        input("Press Enter to continue.")
    # Selection 4
    if(cont == 4):
        seat_availability(rows,tot_tick)
        input("Press Enter to continue.")