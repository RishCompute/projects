import random
table=['r','p','s']
while True:
   while True:
     a=input("Rock paper and scissor (r/p/s)?  ").lower()
     if a in table:
       break
     else:
       print("Invalid Choice")
   k=random.choice(table)
   if a in table:
    print( "You chose:",a,"\nComputer chose:",k)
   if a=="r" and k=='s'or a=='s'and k=='p'or a=='p'and k=='r':
     print("You Won!!")
   elif a==k:
      print("Draw!!")
   else:
     print("You Lose!!")
   while True:
    ask=input("Wanna play again(y/n)? ").lower()
    if ask=='y':
     break
    elif ask=='n':
     exit()
    else:
      print("Invalid choice")     
   
   
      
     
     



 