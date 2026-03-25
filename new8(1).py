#Methods for OOP in python

#Methods are functions that belongs to objects.

class Student :
    college_name = "ABC college"  #Class attribute

    def __init__(self, name, marks):  #Parameterized constructor
        self.name = name  #Object attribute
        self.marks = marks  #Object attribute
 
    def welcome(self):    #Method
        print("Welcome,", self.name)

    def get_marks(self): #Method
        return self.marks


s1 = Student("Apu Sarker", 59)
print(s1.name, s1.marks)
s1.welcome()   #Calling method
print(s1.get_marks()) #Calling method


 
