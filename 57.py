#Find second largest number
n=int(input("Enter the number of element you want to enter in the list"))
listt=[]
for i in range(n):
    nu=int(input())
    listt.append(nu)
listt.sort(reverse=True)

max=listt[0]

for i in range(n):
    
    if(max!=listt[i]):
        print(F"This is the second highest element {listt[i]}")
        break