#Use `collections.Counter`
from collections import Counter
counts=Counter()
text = "python is easy and python is powerful and python is popular"
word=text.split()
counts=Counter(word)
print(counts)