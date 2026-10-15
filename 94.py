#Build a word-frequency counter
text = "python is easy and python is powerful and python is popular"
dic={}
list1=[]
word=""

for i in range(len(text)):
    
    
    if text[i]!=" " or i==len(text)-1:
        word+=text[i]
        if i==len(text)-1:
            list1.append(word)
    
    else:
        list1.append(word)
        word=""
print(list1)        
for i in list1: 
    if i not in dic:
        dic[i]=1     
    else:
        dic[i]=dic[i]+1
# print(dic)        