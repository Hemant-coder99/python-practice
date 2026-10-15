#Merge two lists
n=int(input("Enter the number of element in both the lists"))
list1=[]
list2=[]
for i in range(n):
    a=int(input("Enter the element of list1"))
    list1.append(a)
    b=int(input("Enter the element of list1"))
    list2.append(b)
list3=[]
for i in range(n):
    list3.append(list1[i])    
    list3.append(list2[i])    
list3.sort()
print(list3)    