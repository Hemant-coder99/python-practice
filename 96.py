#Sort a dictionary by value
marks = {
    "Alice": 78,
    "Bob": 92,
    "Charlie": 65,
    "David": 88,
    "Emma": 72,
    "Frank": 95
}
sorted_mark=dict(sorted(marks.items(),key=lambda items:items[1]))
print(sorted_mark)


        


