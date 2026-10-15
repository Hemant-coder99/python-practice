#20. Build a basic calculator (+, -, *, /)
class calculator:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def sum(self):
        return self.first+self.second
    def mul(self):
        return self.first*self.second
    def sub(self):
        return self.first-self.second
    def div(self):
        return self.first/self.second
    #use here error handling to complete this code
print('Enter two number')
first=float(input("enter first number"))
second=float(input("enter second number"))
cal=calculator(first,second)
command=str(input("what you want to do sum,mul,sub,div.Enter among them")) 
if(command.lower()=="sum"):
    print(cal.sum())
elif(command.lower()=="mul"):
    print(cal.mul())
elif(command.lower()=="sub"):
    print(cal.sub())
elif():
    print(cal.div())
    

