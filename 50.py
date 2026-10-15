#Find factors
n=int(input())
listt=[]
for i in range(1,n+1):
    if(n%i==0):
        listt.append(i)
print(listt)        