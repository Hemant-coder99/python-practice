#21. Check leap year
year=int(input("Enter a year to check if it is a leap year or not: "))
if(year%400==0):
    print("This is leap year")
elif(year%100==0):
    print("This is not a leap year")
elif(year%4==0):
    print("This is leap year") 
else:
    print("This is not a leap year")           