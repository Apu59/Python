#Private(like) attributes and method 

#Conceptual implementations in python 
#Private attributes and methods are meant to be used only within the class and are not accessible from outside the class

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  #Now the attribute is private, we can't access this outside of this class. To make any attribute private we just have to give __ infront of the attribute name.

    def reset_pass(self):
        print(self.__acc_pass) #We can access the private attribute from here because we are inside the class

    

acc1 = Account(11223459, "asdfg")
print(acc1.acc_no)
# print(acc1.acc_pass) #This will give error because the attribute is now private
acc1.reset_pass() #It will not give an error



class Person:
    __name = "anonymous"

    def __hello(self):  #Private method
        print("Hello!")

    def welcome(self):
        self.__hello() #Using private method from inside the class 


p1 = Person()
p1.welcome()
