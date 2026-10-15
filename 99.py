# Use `collections.defaultdict`
from collections import defaultdict
d=defaultdict(int)
for _ in range(5):
    key=input()
    d[key]+=1
print(d)