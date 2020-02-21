letter = ["K","B","X","M","O","Q","A"]
t = input("Enter a letter please.")
t = t.upper()
#found = 0
index = 0
#for index in range(0,7):
 #   if(t == letter[index]):
  #      print(t,"is record,",index,"in the list")
   #     found = 1
#if(found == 0):
 #   print("Not on List")

while(index <= 6 and letter[index] != t):
    index = index +1
if(index > 6):
    print("Record Not Found.")
else:
    print("Record is on the list")