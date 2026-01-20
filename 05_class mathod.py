class Person:
    name="annoymous" 
    
    # def changesName(self,name):
    #     # Person .name=name           
    #     self.__class__.name= "rahul" 

    @classmethod
    def changesName(cls,name):
        cls.name=name

p1=Person()
p1.changesName("rahul ")
print(p1.name)
print(Person.name)