#Find the first non-repeating character
word=str(input("enter the word"))

dic={}

for i in word:
    if i in dic:
        dic[i]+=1
    else:    
        dic[i]=1
dic.sort()
print(dic)         
for i in dic.keys():
   
    if dic[i]==1:
        
        print("The first non repeated letter is ",i)
        break
                

    