import time
a = time.strftime('%H:%M:%S')
print(a)
a = int(time.strftime('%H'))
if(5<=a<12):
    print("good morning")
elif(12<=a<17):
    print("good afternoon")
elif(17<=a<19):
    print("good evening")
else: 
    print("good night")       
