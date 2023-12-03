import random as r
print("\n")
print("👑welcome to   Snake🐍Gun🔫Water💦    game😎\n")
moves=["S","G","W"]
x=True
you=0
comp=0
draw=0
while(x):
    print("Enter your move\n S for 🐍\n g for 🔫 \n w for 💦 ")
    playermove=input().upper()

    if playermove in moves:
        cmpmove=r.choice("SWG")
        if playermove=="S" :
            if  cmpmove=="S":
                print(f"  YOU:     Computer:\n  🐍       🐍")
                print("DRAW")
                draw+=1
            elif cmpmove=="W":
                print(f"  YOU:     Computer:\n  🐍       💦")
                print("YOU WIN")
                you+=1
            else:
                print(f"  YOU:     Computer:\n  🐍       🔫")
                print("YOU LOOSE")
                comp+=1
        elif playermove=="W" :
            if  cmpmove=="S":
                print(f"  YOU:     Computer:\n  💦       🐍")
                print("YOU LOOSE")
                comp+=1
            elif cmpmove=="W":
                print(f"  YOU:     Computer:\n  💦       💦")
                print("DRAW")
                draw+=1
            else:
                print(f"  YOU:     Computer:\n  💦       🔫")
                print("YOU WIN")
                you+=1 
        else:
            if  cmpmove=="S":
                print(f"  YOU:     Computer:\n  🔫      🐍")
                print("YOU WIN")
                you+=1
            elif cmpmove=="W":
                print(f"  YOU:     Computer:\n  🔫       💦")
                print("YOU LOOSE")
                comp+=1
            else:
                print(f"  YOU:     Computer:\n  🔫       🔫")
                print("DRAW")
                draw+=1

            
    else:
        print("Invalid Move! Try Again.\n\n")
    print(f"YOU:{you}     COMPUTER:{comp}     DRAW:{draw}\n\n")
    print("Press e for exit\nPress Anyother key to Continue")
    exit = input().lower()
    if  exit == "e":
        x=False
    else:
        x=True

