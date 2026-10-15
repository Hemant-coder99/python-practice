#Fibonacci series
first=0
second=1
n=int(input('enter the number'))
print(first)
print(second)

for i in range(n+1):
    next=first+second
    first=second
    second=next
    print(next)
   
     