#Find the key with maximum value
marks = {
    "Ram": 78,
    "Sam": 92,
    "Hari": 65,
    "Gopal": 88
}
max=0
nam=''
for items,(key,value) in enumerate(marks.items()):
    if value>max or max==0:
        max=value
        nam=key
print(nam)    
    