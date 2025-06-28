import string
import random
while True:
 main_ask=input('To encrypt the message press E/e or to decrypt press D/d\n').upper()

 if main_ask=="E":
  ask=input("Type your message:\n")
  result=[]
  for words in ask.split():
    if len(words)==1:
       result.append(words)

    elif len(words)==2:
        result.append(words[1]+words[0])
    
    elif len(words)>=3: 
     alpha=list(string.ascii_lowercase)+list(string.ascii_uppercase)
     result.append(random.choice(alpha)+random.choice(alpha)+random.choice(alpha)+words[1:len(words)]+words[0]+random.choice(alpha)+random.choice(alpha)+random.choice(alpha))
  print(' '.join(result)) 



 if main_ask=="D": 
  ask=input("Type your message:\n")
  result=[]
  for words in ask.split():
    if len(words)==1:
       result.append(words)

    elif len(words)==2:
        result.append(words[1]+words[0])
    
    else: 
     result.append(words[len(words)-4]+words[3:len(words)-4])
  print(' '.join(result))     
