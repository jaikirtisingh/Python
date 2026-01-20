class Employee:
     
    language="py" #this is class attribute
    salary=120000

    def __init__(self): # dender method automatically call karega 
       print("i am creating an object ")

    def getInfo(self):
     print(f"the language is {self.language}.the slary is{self.salary}")
    
    
    def greet(self):
       print("good morning ")

jai=Employee()
jai.name="Jai"
jai.language="javascrpts"  #this is an object  attribute
jai.getInfo()
jai.greet()

 