#Find duplicates in a list
numbers = [4, 7, 2, 9, 4, 7, 3, 8, 2, 5, 9, 1, 6, 7, 3, 4]
seen=[]
dublicate=[]
for num in numbers:
    if num in seen:
        if num not in dublicate:
            dublicate.append(num)         
    else:
        seen.append(num)
print(dublicate)    

