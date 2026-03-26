#Abstraction 

#Hiding the implementation details of a class and only showing the essential feature to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.clutch = True
        print("Car started...")


car1 = Car()
car1.start()  #With calling this function we are just calling the function and we are hiding the features of the start() function. This is call Abstraction.



#Encapsulation

#Wraping data and functions into a single unit (object).
#If we are creating a class and we are declaring class attribute and object attribute these all are Encapsulation, because we are capsulating all in a class.

