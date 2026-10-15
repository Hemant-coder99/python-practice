#count word in string
import re
count=0
string=str(input()).lower()
for i in string:
    if(re.search("[a-z]",i)):
        count=1+count

print(count)
