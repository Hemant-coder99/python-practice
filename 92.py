#Find set union and intersection
list1 = [2, 4, 6, 8, 10, 12]
list2 = [6, 8, 10, 12, 14, 16]
union=[]
intersection=[]
for i in list1:
    if i in list2:
        intersection.append(i)
    else:
        union.append(i)  
for i in list2:
    if i not in union:
        union.append(i)         
print(intersection) 
print(union)
     
                