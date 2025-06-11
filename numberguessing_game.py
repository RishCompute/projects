import random
r=random.randint(1,100)
while True:
 a=input("Guess a number between 1 and 100 : ")
 if (a.isalpha()):
  print("Invalid Choice") 
 elif(int(a)>r):
        print("Too High")
 elif(int(a)<r):
        print("Too Low")
 else:
        print("Congratulations its",r)
        break    
 



