#Use dictionary comprehension
#{key:value for i in iteration}
listt=[23,34,3,4,3,3]
d={"hemant":55,"bahubali":100,"thor":99}
d1={i:d[i]*2 for i in d}
d2={x:x*2 for x in listt}
print(d2)
print(d1)