#Find a missing number
numbers = [1, 2, 3, 5, 6, 7, 8, 9, 10]
num=[]
summ=sum(numbers)
n=len(numbers)
total=((n+1)*(n+2))/2


print("The missing number is ",total-summ)        