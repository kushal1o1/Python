b=input("Enter number between 2 and 8")
a=int(b)
print(a,b)
if a !="quit" :
    if  (a <=2 or a >=8 ):
      raise ValueError("The input number is not between 2 and 8")

   

else:
    print("You have entered the correct value.")
