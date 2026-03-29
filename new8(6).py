#Inheritance

#When one class(child/drived) drives the properties and method of another class(parent/base).

class Car:

    color = "Black"
    @staticmethod  #Class method
    def start():
        print("Car started.....")

    @staticmethod #Class method
    def stop():
        print("Car stoped.")


class ToyotaCar(Car):  #Inheritance (Single)
    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("Fortuner")
print(car1.name) #Fortuner
car1.start()  #Car started.....  #This is inheritated method
car1.stop() #Car stoped.         #This is inheritated method
print(car1.color) #Black         #This is inheritated method

car2 = ToyotaCar("Prius")
print(car2.name) #Prius
car2.start() #Car started.....   #This is inheritated method
car2.stop() #Car stoped.         #This is inheritated method


#Inheritance Types

# 1. Single Inheritance       # class1 > class2
# 2. Multi-level Inheritance  # class1 > class2 > class3 > class4 ......
# 3. Multiple Inheritance     


#Multiple Inheritance

class A:
    var1 = "This is class AThis is class A"

class B:
    var2 = "This is class B"

class C(A,B): #Multiple Inheritance
    var3 = "This is class C"


obj1 = C  #It can use class A, B and C all properties
print(obj1.var1)  #This is class A
print(obj1.var2)  #This is class B
print(obj1.var3)  #This is class C


