#16. Find largest of three numbers
a=int(input())
b=int(input())
c=int(input())
if(a>b and a>c):
    print(f"{a} is greater")
elif(b>a and b>c):
    print(f"{b} is greater")
else:
    print(f"{c} is greater")