import random
import string
def randomletterfunc():
     letters = string.ascii_letters
     return random.choice(letters)
print("Hi ,buddy ")
print("Enter the message")
message=input()
ans=[]
messages=message.split()
print(" encryption or  decryption ? ")
print(f"Type e for encription and    d for decryption :")
choice=input()

if choice=='e':
     print('encrypting')
     for message in messages :
      if len(message)>3:
          # randomletter=random.choice("qwertyuiop")
          message=randomletterfunc()+randomletterfunc()+randomletterfunc()+message[1:]+message[0]+randomletterfunc()+randomletterfunc()+randomletterfunc()
          ans.append(message)
      else:
         message=message[::-1]
         ans.append(message)
         
else:
     print('decrypting')
     for message in messages :
        if len(message)>3:
          message=message[3:-3]
          x=len(message)
          first=message[x-1]
          remaining=message[0:-1]
          message=first+remaining
          ans.append(message)        
        else:
         message=message[::-1]
         ans.append(message)
ans=" ".join(ans)
print(ans)