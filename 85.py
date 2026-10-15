#Check whether two strings are anagrams
st1=input("enter first string")
st2=input("enter second string")
list1=[]
list2=[]
for i in st1:
    list1.append(i)
for i in st2:
    list2.append(i)
list1.sort()
list2.sort()
print(list1)
print(list2)
if list1==list2:
    print("yes this two strings are anagrams")
else:
    print("NO")
