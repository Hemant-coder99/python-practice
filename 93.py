#Find unique elements using sets
numbers = [4, 7, 2, 4, 9, 7, 3, 8, 2, 5, 9, 1, 6, 3]
seen=set()
dublicate=set()
unique=set()
for i in numbers:
    
    if i in seen:
        if i not in dublicate:
            dublicate.add(i)

    else:
        seen.add(i)    
for i in numbers:
    if i not in dublicate:
        unique.add(i)
print(unique)