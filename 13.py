#13. Find remainder without using %
a=int(input("Enter the number"))
b=int(input("Enter the number"))
class RemainderFinder:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def remainder(self):
        return self.a - (self.a // self.b) * self.b

re = RemainderFinder(a, b)
print("The remainder is", re.remainder())