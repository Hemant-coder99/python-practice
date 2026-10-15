#palindrome string
string=str(input())
string.lower()
temp=""
n=len(string)

for i in range(n-1,-1,-1):
    temp=temp+string[i]
if string==temp:
    print("Entered string is palindrome")
else:
    print("try next word my bhai")    