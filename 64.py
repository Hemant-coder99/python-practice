#Recursive Fibonacci

def fibo(a):
    if(a==0 ):
        return 1
    elif(a==1):
        return 1
    
    else:
        result=fibo(a-1)+fibo(a-2)
        
        return result
      
      
print(fibo(6))       
