b=input("Enter your name:")
import time
a=time.strftime("%H:%M:%S")
c=time.strftime("%I:%M:%S %p")
if("05:00:00"<=a<="12:00:00"): 
    print("Good Morning,",b,"its",c)
elif("12:00:00"<a<="17:00:00"):
    print("Good Afternoon,",b,"its",c)
elif("17:00:00"<a<="19:00:00"):
    print("Good Evening,",b,"its",c)
else:
    print("Good Night,",b,"its",c)