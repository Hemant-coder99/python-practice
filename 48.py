#Find GCD
f1=int(input())
f2=int(input())
list1=[]
list2=[]
for i in range(1,f1+1):
    if(f1%i==0):
        list1.append(i)
for i in range(1,f2+1):
    if(f2%i==0):
        list2.append(i)
list1.sort(reverse=True)
list2.sort(reverse=True)

for i in range(0,len(list1)):
    t=False
    for j in range(0,len(list2)):
        if(list1[i]==list2[j]):
            t=True
            print(f"this {list1[i]} is the gcd of given  number")
            break 
    if(t) :
        break       
           

