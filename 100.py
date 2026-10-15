#Build a student record system using dictionaries
main = {
    101: {
        "Name": "Ram",
        "Marks": {
            "Math": 85,
            "Science": 90,
            "Social": 78
        }
    },
    102: {
        "Name": "Sita",
        "Marks": {
            "Math": 92,
            "Science": 88,
            "Social": 95
        }
    },
    103: {
        "Name": "Hari",
        "Marks": {
            "Math": 67,
            "Science": 72,
            "Social": 80
        }
    },
    104: {
        "Name": "Gita",
        "Marks": {
            "Math": 76,
            "Science": 84,
            "Social": 89
        }
    },
    105: {
        "Name": "Krishna",
        "Marks": {
            "Math": 95,
            "Science": 91,
            "Social": 87
        }
    }
}




def add():
    num=int(input("How many you want to add"))
    for i in range(num):
        Id_records={}
        Marks={}
        try:
            id=int(input("Enter the id of the student"))
            if id in main:
                print("This id already exist")  
                continue
        except ValueError:
            print("enter correct integer")
        name=input("Enter the student name")
        listt=["Math","Science","Social"]
        for subject in listt:
            
            while True:
                try:
                    mark=int(input(f"Enter the {subject} mark"))
                    if 0<= mark <=100:
                        Marks[subject]=mark
                        break
                        
                        

                    else:
                        print("enter value under 100")
                except ValueError  :
                    print("please enter the valid integer")      
            Id_records["Name"]=name
            Id_records["Marks"]=Marks
            main[id]=Id_records     
           
            
    print(main)             
def delete():
    id=int(input("Enter the id you want to delete"))
    if id in main:
        del main[id]
    else:
        print("No such id exist") 
    print(main)       

def view():
    print("These are the student registered")

    for index,(key,value) in enumerate(main.items()):
        print(key,end=" ")
        print(main[key]["Name"])
    print("Do you want continue viewing")  
    an1=input("Enter yes if you want to continue or no if not") 
    if an1.lower()=="yes":
        print("Do you want to view all record . ")
        an1=input("Enter yes if you want to continue or no if you want to view particular student detail")
        if an1.lower()=="yes":
            print(main)
        elif an1.lower()=="no":

            id=int(input("Enter the id of student ")) 
            print(main[id]) 
            
def update():
    
    t="yes" 
    while(t=="yes") :
        print("What you want to change subject name,marks")  
        ans=input("?") 
        if ans.lower()=="name":
            print("Enter the id of student whose name you want to change")
            id=int(input('Enter here'))
            main[id]["Name"]=input("Enter the name with which you want to change")
        elif ans.lower()=="marks" :
            print("Enter the id of student whose name you want to change")
            id=int(input('Enter here'))
            n=int(input('Enter how many mark you want to change their are 3 subject in total'))
            for _ in range(n):
                sub=input("enter the subject name").lower()
                mark=int(input("enter the updated mark"))
                main[id]["Marks"][sub]=mark
def averageTotal():

    
    for index,(key,value) in enumerate(main.items()):

        
        total=sum(value["Marks"].values())
        average=total/len(value["Marks"].values())
        print(f"the average and total of {value["Name"]} is {average} and {total}")
        if average>=t:
            t=average
            n=value["Name"]
    print(f"the topper is {n} with average of {t}")    
        
    
t=True
while t:
    try:
        task=str(input("enter what you want to do= add,update ,delete ,view or averageTotal"))
        if task.lower()=="add":
            add()
            
        elif task.lower()=="update":
            update() 
             
        elif task.lower()=="view":
            view()  
              
        elif task.lower()=="delete":
            delete() 
            

        elif task.lower()=="averageTotal":
            averageTotal() 
              
    except ValueError:
        print("enter correct")   
    t=False     
            



            
            
        
        
        
    




                  

         
          


