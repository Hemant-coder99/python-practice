#Sort list without sort()
n=int(input("Enter the size of the list"))
listt=[]

for i in range(n):
    num=int(input())
    listt.append(num)
for i in range(n):
    for j in range(n-1):
        if(listt[j]>listt[j+1]):
            temp=listt[j]
            listt[j]=listt[j+1]
            listt[j+1]=temp
        
            
               
               
print(listt)           
