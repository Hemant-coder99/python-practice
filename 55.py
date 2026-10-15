#Character frequency for each character i am doing

import re
string=str(input()).lower()
dic={}
listt=re.findall("[a-z]",string)
n=len(listt)

   
for i in range(n):
    t=listt[i]
    n=len(re.findall(t,string))
    dic[t]=n
print(dic)    
