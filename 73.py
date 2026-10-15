# Build a menu-driven program
import random as r
rn=r.randint(1,6)
print(rn)
print('This is for the motivation ')
print("For family related press 1" )
print("For financial related press 2") 
print("For study related press 3" )
print("For sleep related press 4")
choice=int(input())
def study(rn):
    if (rn==1):
        print("""Study now, so your future self doesn't have to introduce himself as 'still figuring things out.""")
    elif(rn==2):
        print("""Your books aren’t difficult. Your phone is just very persuasive.""")
    elif(rn==3): 
        print("""“You can either struggle for 3 hours studying or struggle for years explaining why you didn’t.”""")   
    elif(rn==4): 
        print("""“Dreams are free. The skills to achieve them are not.”""")   
    elif(rn==5): 
        print("""“Nobody cares about your potential until your potential starts paying bills.”""")   
    elif(rn==6): 
        print("""“Study like your Wi-Fi depends on your grades.”""")   
def sleep(rn):
    if (rn==1):
        print("""“Sleep is important. So is waking up. Unfortunately, you seem to support only half the system.”""")
    elif(rn==2):
        print("""Your bed has never paid your bills. Stop giving it overtime.""")
    elif(rn==3): 
        print("""Sleep early tonight. Tomorrow’s problems are already waiting for you.""")   
    elif(rn==4): 
        print("""5 more minutes is how 5 minutes becomes 2 hours.""")   
    elif(rn==5): 
        print("""Rest because you need it, not because your alarm has lost the will to fight you.""")   
    elif(rn==6): 
        print("""Your dreams are waiting. Literally. You’re asleep.""")   
def family(rn):
    if (rn==1):
        print("""One day, you’ll realize the people asking ‘Did you eat?’ were never annoying—they were your biggest supporters.""")
    elif(rn==2):
        print("""Make them proud quietly. Let your results make the noise.""")
    elif(rn==3): 
        print("""You’re building a future, but don’t forget the people who helped build you.""")   
    elif(rn==4): 
        print("""Success feels different when the people who believed in you are there to see it.""")   
    elif(rn==5): 
        print("""Call your family. Your phone has enough battery for scrolling; surely it has enough for them.""")   
    elif(rn==6): 
        print("""Don’t become successful so late that your family only gets to hear about it""")   
def financial(rn):
    if (rn==1):
        print("""Money doesn’t buy happiness, but being broke definitely buys stress.""")
    elif(rn==2):
        print("""Your future bank account is watching what you do with today’s money.""")
    elif(rn==3): 
        print("""Stop trying to look rich. Work until being financially stable becomes boring.""")   
    elif(rn==4): 
        print("""You don’t need another expensive distraction. You need another useful skill.""")   
    elif(rn==5): 
        print("""Being broke is temporary. Staying financially careless is a choice.""")   
    elif(rn==6): 
        print("""Build skills. Make money. Save money. Invest. Repeat. Flex later.""")

if(choice==1):
    family(rn)
elif(choice==2):
    financial(rn)    
elif(choice==3):
    study(rn)    
elif(choice==4):
    sleep(rn)  
else:
    print("bhai option bata choose garna kina jane baneko")      
