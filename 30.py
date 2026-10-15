#Rock Paper Scissors game
import random
a=random.randrange(3)
computerChoice=["scissor" ,"rock","paper"]
CC=computerChoice[a]
c=str(input("choose between rock , paper , scissor")).lower()

if( c=="rock" and CC == "paper") or ( c=="scissor" and CC=="rock") or (c=="paper" and CC=="scissor") :
    print(f"You loose . coumputer choice is {CC}")
elif(c==CC):
    print(f"game is draw .computer choice is {CC}")  
else:
    print(f"you win. computer choice is {CC}")      