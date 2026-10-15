#Rotate a list
list1=[1,4,56,43,53,343,53,3434,434,4342]
list2=[]
n=len(list1)
for i in range(n):
    list2.append(list1[n-i-1])
print(list2)




