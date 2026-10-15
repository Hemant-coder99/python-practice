#Merge two dictionaries
dict1 = {
    "name": "Alice",
    "age": 21,
    "city": "Pokhara"
}

dict2 = {
    "course": "Software Engineering",
    "age": 22,
    "country": "Nepal"
}
merged={}
for index,(key,value) in enumerate(dict1.items()):
    merged[key]=value
for index,(key,value) in enumerate(dict2.items()):
    merged[key]=value
print(merged)

    
