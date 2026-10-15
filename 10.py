#10. Find average  numbers
list=list(map(int,input().split()))
sum=0
for i in range(len(list)):
    sum=list[i]+sum
    average=sum/len(list)
    print("The average of the given number is:",average)
    


