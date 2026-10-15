# Palindrome number
num=int(input("enter the number"))
temp=0
temp1=num
while(num!=0):
    dig=num%10
    temp=temp*10+dig
    num=num//10
if(temp1==temp):
    print("the given number is palindrome")
else:
    print("the given number is not a palindrome")    
