#Prime checker function
def prime(a):
    count=0
    for i in range(1,a+1):
        if(a%i==0):
            count=count+1
    if count==2:
        print("The given number is prime")
    else:
        print('The given number is not prime')            
prime(5)        