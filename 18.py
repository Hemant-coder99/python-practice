#18. Calculate electricity bill
class ElectronicBill:
    def __init__(self,unit):
        self.unit=unit
    def billamount(self):
        if self.unit<=20:
            return self.unit*0+30
        elif self.unit<=30 and self.unit>20:
            return 20*0+(self.unit-20)*6.5+50
        elif self.unit<=50 and unit>30:
            return 20*0+10*6.5+(self.unit-30)*8+50
        elif self.unit<=100 and self.unit>50:
            return 20*0+10*6.5+20*8+(self.unit-50)*9.5+75
        elif self.unit<=250 and self.unit>100:
            return 20*0+10*6.5+20*8+50*9.5+(self.unit-100)*9.5+100
        else:
            return 20*0+10*6.5+20*8+50*9.5+150*9.5+(self.unit-250)*11+150
unit=int(input("Enter the unit"))        
bill=ElectronicBill(unit)
print(f"The bill amount is {bill.billamount()+bill.billamount()*0.13}")
        
        




        
            