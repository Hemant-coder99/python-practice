#Remove duplicates while preserving order
numbers = [4, 7, 2, 9, 4, 7, 3, 8, 2, 5, 9, 1, 6, 7, 3, 4]
updated=[]
dublicate=[]
for i in numbers:
    if i in updated:
        if i not in dublicate:
            dublicate.append(i)
    else:
        updated.append(i)        
print(updated)        
print(dublicate)        