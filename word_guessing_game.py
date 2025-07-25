
import random
easy_words = [
    "cat", "dog", "sun", "book", "car", "fish", "milk", "tree", "ball", "hat",
    "pen", "cup", "shoe", "rain", "star", "box", "bag", "bed", "door", "fan"
]

medium_words = [
    "pencil", "window", "garden", "planet", "jungle", "banana", "rocket", "castle", "silver", "monkey",
    "button", "shadow", "throat", "tunnel", "branch", "pillow", "drawer", "ladder", "packet", "closet"
]

hard_words = [
    "xylophone", "microscope", "labyrinth", "zephyr", "quarantine", "hierarchy", "dilemma", "paradox", "mnemonic", "opaque",
    "cryptic", "subtlety", "euphemism", "juxtapose", "reminisce", "oblivion", "zenith", "cacophony", "surreal", "aesthetic"
]

def entry():
    while True:
     try:
      print('---WORD GUESSING GAME---')
      level_choose()
     except TypeError:
        print('Try Again')

def level_choose():
    level_ask=input('Select the level:\nEasy(E/e):\nMedium(M/m):\nHard(H/h):\n').lower() 
    if level_ask=='h':
        print('Level Chosen:Hard')
        computer_choice=random.choice(hard_words)
    elif level_ask=='m':
        print('Level Chosen:Medium')
        computer_choice=random.choice(medium_words)
    elif level_ask=='e':
        print('Level Chosen:Easy')
        computer_choice=random.choice(easy_words)    
    else:
        print('\nWrong Selection\n')
        return
    game_start(computer_choice)

def game_start(computer_choice):

 while True:
   attempt=0
   game_start_ask=input('For starting the game press \'S/s\':\nTo return to main menu press \'R/r\':\n').lower()
   if game_start_ask=='s':
     print(f'It\'s a {len(computer_choice)} letter word:' )
     while True:
      main_word=input("Start guessing the word: ")
      matching_word=itersection(main_word,computer_choice)
      print(matching_word)
      if len(matching_word)==len(computer_choice):  
       attempt+=1
       if matching_word==computer_choice:
        if attempt==1:
         print(f'You won the game in {attempt} attempt(within limits) ')
         exit()
        else:
          print(f'You won the game in {attempt} attempt(within limits) ')
          exit()   
      else:
       attempt=attempt
   elif game_start_ask=='r' :
      break
   else:
      print('\nWrong Slection\n')
        
def itersection(main_word,computer_choice):
   l_ask=[i for i in main_word]
   l_word=[i for i in computer_choice]
   empty=[]
   if len(l_ask)==len(l_word):   
    for i in range(len(l_ask)):
      if l_ask[i]==l_word[i]:
         empty.append(l_ask[i])
      else:
         empty.append('_')
   else:
      print('Write letters within limits')
    
   return ''.join(empty)        
      
entry() 


