# Use `reduce()`
import functools as fuk
num=[1,3,4,21,3,234,45,55,666]
reduced=fuk.reduce(lambda result,current : result+current,num)
reduced=fuk.reduce(lambda result,current : result/current,num)
print(reduced)