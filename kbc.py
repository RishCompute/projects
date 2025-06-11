questions=['1. What is the capital of Australia?',
           '2. Which planet is known as the "Evening Star"?',
           '3. What is the largest ocean on Earth?',
           '4. Who is known as the "Father of the Indian Constitution"?',
           '5. In which city was the first modern Olympic Games held? ']
options=['A. Canberra   B. Balmain  \nC. Bathurst   D. Geelong',
         'A. Mercury   B. Venus  \nC. Earth     D. Mars',
         'A.  Pacific Ocean   B. Indian Ocean  \nC. Atlantic         D. Arctic',
         'A. Dr. B.R. Ambedkar    B. Mahatma Gandhi  \nC. Jawaharlal Nehru     D. Madan Mohan Malviya',
         'A. Athens   B. Brazil  \nC. America  D. Australia']
while True:
 inp=input('Kya aap is khel ka aarambh karna chahte hai? \nHAA ya NAA me uttar dijiye.\n').upper()
 if inp=='HAA':
  print(questions[0], '💰=₹1000','\n',options[0],sep="")
  while True:
   ans1=input("Prashan ka uttar dijiye A/a,B/b,C/c ya D/d me dijiye \n").upper()
   if ans1=="A":
    print("Mahashya apne ₹1000 rupay ki 💰 dhan rashi prapt kar li hai ")
   #  sum=sum+1000
    print(questions[1], '💰=₹2000','\n',options[1],sep="")
    while True:
     ans2=input("Prashan ka uttar dijiye A/a,B/b,C/c ya D/d me dijiye \n").upper()
     if ans2=="A":
      print("Mahashya apne ₹2000 rupay ki 💰 dhan rashi prapt kar li hai ")

      print(questions[2], '💰=₹3000','\n',options[2],sep="")
      while True:
       ans3=input("Prashan ka uttar dijiye A/a,B/b,C/c ya D/d me dijiye \n").upper()
       if ans3=="A":
        print("Mahashya apne ₹3000 rupay ki 💰 dhan rashi prapt kar li hai ")

        print(questions[3], '💰=₹4000','\n',options[3],sep="")
        while True:
         ans4=input("Prashan ka uttar dijiye A/a,B/b,C/c ya D/d me dijiye \n").upper()
         if ans4=="A":
          print("Mahashya apne ₹4000 rupay ki 💰 dhan rashi prapt kar li hai ")

          print(questions[4], '💰=₹5000','\n',options[4],sep="")
          while True:
           ans5=input("Prashan ka uttar dijiye A/a,B/b,C/c ya D/d me dijiye \n").upper()
           if ans5=="A":
            print("Mahashya apne ₹5000 rupay ki 💰 dhan rashi prapt kar li hai ")
            print("Mubarak aap ₹15000 ki 💰 dhan rashi apne saath ghar le jaa rahe hai")
           elif ans5=="B"or ans5=="C"or ans5=="D":
            print("Mahashaya yeh uttar galat hai,shi uttar hai A ")
            print("Nirash na hoye app fir bhi ₹10000 ki 💰dhanrashi apne ghar lekar jaa rahe hai")
            exit()
           else:
              print('Kya apko type karna nhi aata!!🤬')

         elif ans4=="B"or ans4=="C"or ans4=="D":
          print("Mahashaya yeh uttar galat hai,shi uttar hai A ")
          print("Nirash na hoye app fir bhi ₹6000 ki 💰dhanrashi apne ghar lekar jaa rahe hai")
          exit()
         else:
          print('Kya apko type karna nhi aata!!🤬')















       elif ans3=="B"or ans3=="C"or ans3=="D":
        print("Mahashaya yeh uttar galat hai,shi uttar hai A ")
        print("Nirash na hoye app fir bhi ₹3000 ki 💰dhanrashi apne ghar lekar jaa rahe hai")
        exit()
       else:
         print('Kya apko type karna nhi aata!!🤬')















     elif ans2=="B"or ans2=="C"or ans2=="D":
      print("Mahashaya yeh uttar galat hai,shi uttar hai A ")
      print("Nirash na hoye app fir bhi ₹1000 ki 💰dhanrashi apne ghar lekar jaa rahe hai")
      exit()
     else:
      print('Kya apko type karna nhi aata!!🤬')













   elif ans1=="B"or ans1=="C"or ans1=="D":
    print("Mahashaya yeh uttar galat hai,shi uttar hai A ")
    print("Aapko khali haat ghar jana hoga")
    exit()
   else:
    print('Kya apko type karna nhi aata!!🤬')
 elif inp=='NAA':
  break
 else:
  print('Kya apko padhna nhi aata!!🤬')