# Sum of digits
num=int(input("enter the number"))
sum=0
while(num!=0):
    temp=num%10
    sum=sum+temp
    num=num//10
print(sum)    