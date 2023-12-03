import time
obj=time.strftime('%H:%M:%S')
print("Time is ",obj)
hr=int(time.strftime('%H'))

if( hr>=0 and hr<12):
    print("Good Morning")
elif(hr>=12 and hr<17):
    print("Good Afternoon")
else :
    print("Good Evening")