#del keyword 

#Used to delete object properties or object itself

class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("Apu")
print(s1) #It will show the location where the object stored 
print(s1.name) #Apu

del s1.name #name attribute deleted 
print(s1.name) #Now it will give an error because we deleted the name attribute

del s1 # s1 object deleted
print(s1)  #Now it will give an error because we deleted the s1 object




