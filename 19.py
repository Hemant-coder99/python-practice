#19. Calculate BMI
import pyttsx3

engine = pyttsx3.init(driverName='sapi5')

engine.say("enter weight in kg")
engine.runAndWait()

weight=float(input("enter weight in kg"))
engine.say("enter height in meter")
engine.runAndWait()
height=float(input("enter height in meter"))
BMI=weight/(height*height)
print(BMI)
if(BMI<18.5):
    engine.say("BSDK khana kha")
    
elif(18.5<=BMI<=24.9):
    engine.say("smart boy good")
    
elif(25<=BMI<=29.9):
    engine.say("elephant mutherfuker eat less")
    
else:
    engine.say("marega tu kha kha k marega tu")

engine.runAndWait()          