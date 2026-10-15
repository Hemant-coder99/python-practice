#4. Find area of rectangle
class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width    
rec=rectangle(4,5)
print(rec.area()) 