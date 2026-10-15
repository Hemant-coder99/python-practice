#Remove duplicate characters
import re
string=str(input()).lower()
listt=re.findall("[a-z]",string)
n=len(listt)
d={}
remove_key=[]
for i in range(n):
    t=listt[i]
    l=len(re.findall(t,string))
    d[t]=l
for index,(item,value) in enumerate(d.items()):
    print(item)
    print(value)
    
    if(value>1):
        remove_key.append(item)
for items in remove_key:
    del d[items]
result=""
for index,(item,value) in enumerate(d.items()):
    
    result=result+item
print(result)