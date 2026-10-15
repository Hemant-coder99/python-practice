#Find LCM
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
for i in range(1,len(list1)):
    t=False
    for j in range(1,len(list2)):
        if(list1[i]==list2[j]):
            t=True
            print(f"this {list1[i]} is the lcm of given  number")
            break 
        else:
            print(f"this 1 is the lcm of given  number")
            break
    if(t) :
        break  