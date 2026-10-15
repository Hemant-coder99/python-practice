#Build a password-strength checker
import re
password=str(input())
if(len(password)>8 ):
    char=re.findall('[a-z]',password)
    CHAR=re.findall('[A-Z]',password)
    NUM=re.findall('[1-9]',password)
    UNI=re.findall('[@&%$*-]',password)
    print(len(char))
    print(len(CHAR))
    print(len(NUM))
    print(len(UNI))
    if(len(char)>=1 and len(CHAR)>=1 and len(NUM)>=1 and len(UNI)>=1):
        print('The strength is good')
    else:
        print("The password should cantain alphabate both upper and lower,number,symbol")    
else:
    print("Password should contain atleast 8 characters")