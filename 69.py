#69. Use `map()`
#it is same as 68
listt=list(map(int,input().split()))
square=list(map(lambda a:a*a,listt))
print(square)