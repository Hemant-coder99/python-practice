#Check century year

while(True):
    year=int(input("Enter the year"))
    if(year%100==00):
        print("this is century year")
    else:
        print("this is not a century year")  
        break  