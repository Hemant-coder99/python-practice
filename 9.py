#9. Convert minutes into hours and minutes
class time_converter:
    def __init__(self,minute,hour):
        self.minute=minute
        self.hour=hour
    def minuteConverter(self):
        hour=self.minute/60
        print("minute in hour is:",hour)
    def hourConverter(self):
        minute=self.hour*60
        print("hour in minute is:",minute)

    
time=time_converter(90,5.6) 
time.minuteConverter()
time.hourConverter()

        