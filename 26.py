#26. Check valid triangle
a,b,c=map(int,input('enter three side of the triangle').split())
if(a+b>c and a+c>b and c+b>a):
    print("This triangle is valid")
else:
    print("this triangle is not valid")    
