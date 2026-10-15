#reverse string
string=str(input())
temp=""
n=len(string)

for i in range(n-1,-1,-1):
    temp=temp+string[i]
print(temp)
