listofqsn=["What is the highest mountain of the world","How many days are there in a leap year","This code is written in which language","what comes after sunday","complete the series: 2,4,6,8,","88+22=","101-1=","What comes once in tea and twice in coffee","Who is the father of Computer","How many planets are there in solar system"]
listofans=["mount everest","366","python","monday","10","110","100","e","charles babbage","7"]
i=0
amount=0
name=input("Enter your name")
print("Are u ready for KBC "+name+"\ty/n")
choice=input()
if choice=="y" :
    print("Okay let's start the game")
    x=True
    while  x==True :
        print (listofqsn[i])
        ans=input()
        Uans=ans.lower()
        if Uans==listofans[i] :
            amount+=100000
            print("correct answer \n")
            print("Congratulation "+name+" You have won RS.",amount)
            i+=1
            x=True
            if i==10 :
                print("congrats You answer all  qsn correctly")
                print("you won the KBC show ")
                break

        else :
            print("Sorry wrong answer.You lose")
            x=False
print("You have got ",amount)
print("ThankYou for Playing our game "+name)
