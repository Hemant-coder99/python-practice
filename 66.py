#Reverse string function
import time
start=time.perf_counter()
def reverStr(string):
    n=len(string)
    temp=""
    for i in range(n-1,-1,-1):
        temp=temp+string[i]
    print(temp)    
reverStr("hemant")
end=time.perf_counter()
print(end-start)
#using slicing for reverse
t1=time.perf_counter()
def reversSlicing(string):
    reverse=string[::-1]
    print(reverse)
reversSlicing("hemant")    
t2=time.perf_counter()
print(t2-t1)
#this time is just to check from loop and slicing which one is fast