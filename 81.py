#Find the longest word in a sentence
import re
sentence=str(input())
l=len(sentence)
lenn=0
max=0
word=""
maxWord=""
count=0
l=len(sentence)
for i in sentence:
    
    if(i!=" "  and i!="."):
        count=count+1                         
        word=word+i 
        print(word)
        print(count)
             
        
    else:
        if max< count:
            max=count
            
            maxWord=word
            
           
        word=""
        count=0    
            
print(maxWord)    




