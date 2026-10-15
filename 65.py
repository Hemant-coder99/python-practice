#Count vowels function
import re

def vowel(string):
    count=0
    for i in string:
            if(re.search('[aeiou]',i)):
                count=count+1
    print(count)
vowel("hemant") 

