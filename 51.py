#Count vowels in string
string=str(input())
count=0
string.lower()
for i in string:
    if(i=="a" or i=="e"or i=="i"or i=="o" or i=="u"):
        count=count+1
print(count)        