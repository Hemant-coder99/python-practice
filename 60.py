#Common elements in two lists
n1=int(input("enter the number of element in the list1"))
n2=int(input("enter the number of element in the list2"))
list1=[]
list2=[]
for i in range(n1):
    num=int(input())
    list1.append(num)
for i in range(n2):
    num=int(input())
    list2.append(num)  
list1.sort()
list2.sort()
repeated=[]
for i in list1:
    for j in list2:
        if(i==j):
            repeated.append(i)
unique=[]
for i in repeated:
    if i not in unique:
        unique.append(i)
                
print(unique)