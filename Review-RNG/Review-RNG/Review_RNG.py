#from random import*
import random

def rollDice():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    answer = d1 + d2 
    return answer 


for x in range(1,20,2):    #(x,y,s) s=step. how many it counts by
    print(" Game # " , x )
    sum = rollDice()
    #first roll
    if(sum == 7 or sum == 11):
        print("Winner!!! --- Game Over!!!")
    elif(sum == 2 or sum == 3 or sum == 12):
        print("Loser!!! --- Game Over !!!")
    else: 
        point = sum 
    #No winner or loser of first roll --- keep rolling until 7 or point 
        sum = rollDice()
        while(sum != point and sum != 7): 
         sum = rollDice() 
        if(sum == point): 
            print("Winner!!! --- Game Over!!!")
        else: 
            print("Loser!!! --- Game Over !!!")