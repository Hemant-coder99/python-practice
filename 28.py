#Find roots of quadratic equation
import math
a,b,c=map(int,input("enter a ,b ,c of the quation").split())
tr=b*b-4*a*c
if tr< 0:
    print("mo real root")
else:    
    d=math.sqrt(tr)
    root1=(-b+d)/(2*a)
    root2=(-b-d)/(2*a)
    print(f"the roots are {root1} and {root2}")
