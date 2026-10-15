#Armstrong number
num=int(input("enter the number"))
arm=0
while(num!=0):
    temp=num%10
    arm=arm+temp*temp
    num=num//10
print(arm)    

