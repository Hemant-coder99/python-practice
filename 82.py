#Count uppercase and lowercase characters
import re
sentence=str(input())
Count=0
count=0
for i in sentence:
    if(re.search("[A-Z]",i)):
        Count=Count+1
    elif(re.search("[a-z]",i)):
        count=count+1
print("The number of upperCase is",Count)
print("The number of lowerCase is",count)