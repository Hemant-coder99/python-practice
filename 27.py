#27. Find type of triangle
a,b,c=map(int,input("enter three side of the triangle").split())
if(a==b or a==c or b==c):
    print("this is a isosceles ")
elif(a==b==c):
    print("this is equilateral triangle") 
else:
    print("this triangle is scalene triangle")       