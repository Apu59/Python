#Object Oriented Programming(OOP) in Python

#Class is a blueprint or template for creating objects.

class Student :   #This is a class
    name = "Apu Sarker"  #Paramenter of class

s1 = Student()  #Object of class Student
print(s1.name) 


# __init__ function (construtor)

#All classes have a function called __init__(), which is always executed when the object is being initiated.

class Student2 :

    College_name = "xyz College"  #This is class attribute which is common for all object which will created by this class

    #This is default constructior and if we don't create this then python will create it automaticaly 
    def __init__(self) :
        pass

    #This is parameterized constructor, if any class have more than one constructor then which constructor match with object's parameter that one will be invoke
    def __init__(self, name, marks):  #self is the default parameter of init function
        self.name = name #This is call object attributes or instance 
        self.marks = marks  #This is call object attributes or instance
        print("Initiating the init function(constructor)") #This line will invoke first if any object is created with this class


s2 = Student2("Apu", 59)
print(s2.name, s2.marks) #Apu (Object attribute)
print(Student2.College_name) #xyz college (Class attribute)

s3 = Student2("Sarker", 95) 
print(s3.name, s2.marks) #Sarker
print(Student2.College_name) #xyz college (Class attribute)


#Class and Instance Atributes (Code are in Student2 object above)

#There are 2 types of attributes 1. Class attribites and 2. Object attributes or Instance.
# 1. Class attributes = Which attributes are common for all objects that will be class attributes. Ex:- College name
# 2. Object attributes = Which attributes are only for any specific object that will be object attribute or instance. Ex:- Name, Roll, Marks

#If any class attribute and object attribute is same then object attribute will invoke because object attributes gets higher precedence than class attributes.


