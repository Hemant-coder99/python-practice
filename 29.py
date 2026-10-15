import random 
x=random.randrange(100)
print(x)
print("Guess the number between 0 to 100")
while True:
    y=int(input())
    if x==y:
        print("Congratulations! You guessed the number.")
        break
    elif x>y:
        print("Your guess is low. Try again.")
    elif x<y:
        print("Your guess is high. Try again.")


    

