#Replace spaces with hyphens
sentence=str(input())
sen=""
for i in sentence:
    if(i!=" "):
        sen=sen+i
    else:
        sen=sen+"-"
print(sen)
