#22. Find grade from marks
class GradeMaker:
    def __init__(self,mark):
        self.mark=mark
    def gradeCon(self): 
        if(90<=self.mark<=100):
            print("your garde is A")
        elif(80<=self.mark<90):
            print("your garde is B")    
        elif(70<=self.mark<80):
            print("your garde is C")    
        elif(60<=self.mark<70):
            print("your garde is D")    
        elif(50<=self.mark<60):
            print("your garde is E")    
        elif(40<=self.mark<50):
            print("your garde is F") 
        else:
            print("With this marks you are expecting grade xiiiii")       
mark=int(input("ENTER YOUR VALIDE MARK"))
G=GradeMaker(mark)
G.gradeCon()