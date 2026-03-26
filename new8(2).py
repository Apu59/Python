#Static Methods

#Static Methods that don't use the self parameter (work at class level)

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    @staticmethod  #This will convert this function into a static method that don't need a self parameter to call and it will work now on class level. This is one kind of decorator
    def hello():
        print("Hello")


s1 = Student("Apu Sarker", 59)
s1.hello()  #This is not give an error because we convert the hello() function into a static method