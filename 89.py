#Flatten a nested list

numbers = [1, [2, 3], [4, 5]]
result=[]
# for i in numbers:
#     if type(i)==list:
#         for j in i:
#             result.append(j)
#     else:
#         result.append(i)        
# print(result)    
#alternative
for i in numbers:
    if isinstance(i,list):
        for j in i:
            result.append(j)
    else:
        result.append(i) 
print(result)